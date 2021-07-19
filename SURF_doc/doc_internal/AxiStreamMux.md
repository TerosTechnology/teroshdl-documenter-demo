# Entity: AxiStreamMux

- **File**: AxiStreamMux.vhd
## Diagram

![Diagram](AxiStreamMux.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description:
Block to connect multiple incoming AXI streams into a single encoded
outbound stream. The destination field is updated accordingly.
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name         | Type                    | Value             | Description                                                                                                                                                                                                            |
| -------------------- | ----------------------- | ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TPD_G                | time                    | 1 ns              |                                                                                                                                                                                                                        |
| PIPE_STAGES_G        | integer range 0 to 16   | 0                 |                                                                                                                                                                                                                        |
| NUM_SLAVES_G         | integer range 1 to 256  | 4                 |                                                                                                                                                                                                                        |
| MODE_G               | string                  | "INDEXED"         | Note: Planning to rename "MODE_G" to "TDEST_MODE_G" in a future MAJOR release of SURF                                                                                                                                  |
| TDEST_ROUTES_G       | Slv8Array               | (0 => "--------") | In ROUTED mode, an array mapping how TDEST should be assigned for each slave port Each TDEST bit can be set to '0', '1' or '-' for passthrough from slave TDEST.                                                       |
| TID_MODE_G           | string                  | "PASSTHROUGH"     | In INDEXED mode, the output TID is set based on the selected slave index In ROUTED mode, TID is set according to the TID_ROUTES_G table In PASSTHROUGH mode, TID is passed through from the slave untouched (default)  |
| TID_ROUTES_G         | Slv8Array               | (0 => "--------") | In ROUTED mode, an array mapping how TID should be assigned for each slave port                                                                                                                                        |
| TDEST_LOW_G          | integer range 0 to 7    | 0                 | In INDEXED mode, assign slave index to TDEST at this bit offset                                                                                                                                                        |
| ILEAVE_EN_G          | boolean                 | false             | Set to true if interleaving dests                                                                                                                                                                                      |
| ILEAVE_ON_NOTVALID_G | boolean                 | false             | Rearbitrate when tValid drops on selected channel, ignored when ILEAVE_EN_G=false                                                                                                                                      |
| ILEAVE_REARB_G       | natural range 0 to 4095 | 0                 | Max number of transactions between arbitrations, 0 = unlimited, ignored when ILEAVE_EN_G=false                                                                                                                         |
| REARB_DELAY_G        | boolean                 | true              | One cycle gap in stream between during re-arbitration. Set true for better timing, false for higher throughput.                                                                                                        |
| FORCED_REARB_HOLD_G  | boolean                 | false             | Block selected slave txns arriving on same cycle as rearbitrate or disableSel from going through, creating 1 cycle gap. This might be needed logically but decreases throughput.                                       |
## Ports

| Port name    | Direction | Type                                          | Description     |
| ------------ | --------- | --------------------------------------------- | --------------- |
| axisClk      | in        | sl                                            | Clock and reset |
| axisRst      | in        | sl                                            |                 |
| disableSel   | in        | slv(NUM_SLAVES_G-1 downto 0)                  | Slaves          |
| rearbitrate  | in        | sl                                            |                 |
| ileaveRearb  | in        | slv(11 downto 0)                              |                 |
| sAxisMasters | in        | AxiStreamMasterArray(NUM_SLAVES_G-1 downto 0) |                 |
| sAxisSlaves  | out       | AxiStreamSlaveArray(NUM_SLAVES_G-1 downto 0)  |                 |
| mAxisMaster  | out       | AxiStreamMasterType                           | Master          |
| mAxisSlave   | in        | AxiStreamSlaveType                            |                 |
## Signals

| Name            | Type                                          | Description |
| --------------- | --------------------------------------------- | ----------- |
| r               | RegType                                       |             |
| rin             | RegType                                       |             |
| sAxisMastersTmp | AxiStreamMasterArray(NUM_SLAVES_G-1 downto 0) |             |
| pipeAxisMaster  | AxiStreamMasterType                           |             |
| pipeAxisSlave   | AxiStreamSlaveType                            |             |
## Constants

| Name        | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Description |
| ----------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| DEST_SIZE_C | integer |  bitSize(NUM_SLAVES_G-1)                                                                                                                                                                                                                                                                                                                                                                                                                                             |             |
| ARB_BITS_C  | integer |  2**DEST_SIZE_C                                                                                                                                                                                                                                                                                                                                                                                                                                                      |             |
| REG_INIT_C  | RegType |  (       acks   => (others => '0'),<br><span style="padding-left:20px">       ackNum => toSlv(NUM_SLAVES_G-1,<br><span style="padding-left:20px"> DEST_SIZE_C),<br><span style="padding-left:20px">       valid  => '0',<br><span style="padding-left:20px">       arbCnt => (others => '0'),<br><span style="padding-left:20px">       slaves => (others => AXI_STREAM_SLAVE_INIT_C),<br><span style="padding-left:20px">       master => AXI_STREAM_MASTER_INIT_C) |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- ROUTE_TABLE_REMAP: ( sAxisMasters )
**Description**
Override TDESTS and TIDs according to the routing tables

- comb: ( axisRst, disableSel, ileaveRearb, pipeAxisSlave, r, rearbitrate, sAxisMastersTmp )
- seq: ( axisClk )
## Instantiations

- AxiStreamPipeline_1: surf.AxiStreamPipeline
**Description**
Optional output pipeline registers to ease timing

