# Entity: AxiStreamRepeater

- **File**: AxiStreamRepeater.vhd
## Diagram

![Diagram](AxiStreamRepeater.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description:
 Block to connect a single incoming AXI stream to multiple outgoing AXI
 streams
-----------------------------------------------------------------------------
 This file is part of 'SLAC Firmware Standard Library'.
 It is subject to the license terms in the LICENSE.txt file found in the
 top-level directory of this distribution and at:
    https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
 No part of 'SLAC Firmware Standard Library', including this file,
 may be copied, modified, propagated, or distributed except according to
 the terms contained in the LICENSE.txt file.
-----------------------------------------------------------------------------
## Generics

| Generic name         | Type     | Value | Description                                                                                                        |
| -------------------- | -------- | ----- | ------------------------------------------------------------------------------------------------------------------ |
| TPD_G                | time     | 1 ns  |                                                                                                                    |
| NUM_MASTERS_G        | positive | 2     |                                                                                                                    |
| INCR_AXIS_ID_G       | boolean  | false |  true = overwrites the TID with a counter that increments after each TLAST (help with frame alignment down stream) |
| INPUT_PIPE_STAGES_G  | natural  | 0     |                                                                                                                    |
| OUTPUT_PIPE_STAGES_G | natural  | 0     |                                                                                                                    |
## Ports

| Port name    | Direction | Type                                           | Description     |
| ------------ | --------- | ---------------------------------------------- | --------------- |
| axisClk      | in        | sl                                             | Clock and reset |
| axisRst      | in        | sl                                             |                 |
| sAxisMaster  | in        | AxiStreamMasterType                            | Slave           |
| sAxisSlave   | out       | AxiStreamSlaveType                             |                 |
| mAxisMasters | out       | AxiStreamMasterArray(NUM_MASTERS_G-1 downto 0) | Masters         |
| mAxisSlaves  | in        | AxiStreamSlaveArray(NUM_MASTERS_G-1 downto 0)  |                 |
## Signals

| Name              | Type                                           | Description |
| ----------------- | ---------------------------------------------- | ----------- |
| r                 | RegType                                        |             |
| rin               | RegType                                        |             |
| inputAxisMaster   | AxiStreamMasterType                            |             |
| inputAxisSlave    | AxiStreamSlaveType                             |             |
| outputAxisMasters | AxiStreamMasterArray(NUM_MASTERS_G-1 downto 0) |             |
| outputAxisSlaves  | AxiStreamSlaveArray(NUM_MASTERS_G-1 downto 0)  |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                         | Description |
| ---------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       tId     => (others => '0'),<br><span style="padding-left:20px">       slave   => AXI_STREAM_SLAVE_INIT_C,<br><span style="padding-left:20px">       masters => (others => AXI_STREAM_MASTER_INIT_C)) |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( axisRst, inputAxisMaster, outputAxisSlaves, r )
- seq: ( axisClk )
## Instantiations

- U_Input: surf.AxiStreamPipeline
