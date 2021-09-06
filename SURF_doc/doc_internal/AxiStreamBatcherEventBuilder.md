# Entity: AxiStreamBatcherEventBuilder

- **File**: AxiStreamBatcherEventBuilder.vhd
## Diagram

![Diagram](AxiStreamBatcherEventBuilder.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Title      : AxiStream BatcherV1 Protocol: https://confluence.slac.stanford.edu/x/th1SDg
-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: Wrapper on AxiStreamBatcher for multi-AXI stream event building
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

| Generic name         | Type                 | Value             | Description                                                                                                                                                       |
| -------------------- | -------------------- | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TPD_G                | time                 | 1 ns              |                                                                                                                                                                   |
| NUM_SLAVES_G         | positive             | 2                 | Number of Inbound AXIS stream SLAVES                                                                                                                              |
| MODE_G               | string               | "INDEXED"         | In INDEXED mode, the output TDEST is set based on the selected slave index In ROUTED mode, TDEST is set according to the TDEST_ROUTES_G table                     |
| TDEST_ROUTES_G       | Slv8Array            | (0 => "--------") | In ROUTED mode, an array mapping how TDEST should be assigned for each slave port Each TDEST bit can be set to '0', '1' or '-' for passthrough from slave TDEST.  |
| TDEST_LOW_G          | integer range 0 to 7 | 0                 | In INDEXED mode, assign slave index to TDEST at this bit offset                                                                                                   |
| TRANS_TDEST_G        | slv(7 downto 0)      | x"FF"             | Set the TDEST to detect for transition frame                                                                                                                      |
| AXIS_CONFIG_G        | AxiStreamConfigType  |                   |                                                                                                                                                                   |
| INPUT_PIPE_STAGES_G  | natural              | 0                 |                                                                                                                                                                   |
| OUTPUT_PIPE_STAGES_G | natural              | 0                 |                                                                                                                                                                   |
## Ports

| Port name       | Direction | Type                                          | Description        |
| --------------- | --------- | --------------------------------------------- | ------------------ |
| axisClk         | in        | sl                                            | Clock and Reset    |
| axisRst         | in        | sl                                            |                    |
| blowoffExt      | in        | sl                                            | Misc               |
| axilReadMaster  | in        | AxiLiteReadMasterType                         | AXI-Lite Interface |
| axilReadSlave   | out       | AxiLiteReadSlaveType                          |                    |
| axilWriteMaster | in        | AxiLiteWriteMasterType                        |                    |
| axilWriteSlave  | out       | AxiLiteWriteSlaveType                         |                    |
| sAxisMasters    | in        | AxiStreamMasterArray(NUM_SLAVES_G-1 downto 0) | AXIS Interfaces    |
| sAxisSlaves     | out       | AxiStreamSlaveArray(NUM_SLAVES_G-1 downto 0)  |                    |
| mAxisMaster     | out       | AxiStreamMasterType                           |                    |
| mAxisSlave      | in        | AxiStreamSlaveType                            |                    |
## Signals

| Name            | Type                                          | Description |
| --------------- | --------------------------------------------- | ----------- |
| r               | RegType                                       |             |
| rin             | RegType                                       |             |
| sAxisMastersTmp | AxiStreamMasterArray(NUM_SLAVES_G-1 downto 0) |             |
| rxMasters       | AxiStreamMasterArray(NUM_SLAVES_G-1 downto 0) |             |
| rxSlaves        | AxiStreamSlaveArray(NUM_SLAVES_G-1 downto 0)  |             |
| txMaster        | AxiStreamMasterType                           |             |
| txSlave         | AxiStreamSlaveType                            |             |
| batcherIdle     | sl                                            |             |
| timeoutEvent    | sl                                            |             |
| axisReset       | sl                                            |             |
## Constants

| Name        | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Description |
| ----------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| DEST_SIZE_C | integer |  bitSize(NUM_SLAVES_G-1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |             |
| REG_INIT_C  | RegType |  (       softRst        => '0',<br><span style="padding-left:20px">       hardRst        => '0',<br><span style="padding-left:20px">       blowoffReg     => '0',<br><span style="padding-left:20px">       blowoff        => '0',<br><span style="padding-left:20px">       timerRst       => '0',<br><span style="padding-left:20px">       cntRst         => '0',<br><span style="padding-left:20px">       ready          => '0',<br><span style="padding-left:20px">       maxSubFrames   => toSlv(NUM_SLAVES_G,<br><span style="padding-left:20px"> 16),<br><span style="padding-left:20px">       timer          => (others => '0'),<br><span style="padding-left:20px">       timeout        => (others => '0'),<br><span style="padding-left:20px">       bypass         => (others => '0'),<br><span style="padding-left:20px">       dataCnt        => (others => (others => '0')),<br><span style="padding-left:20px">       nullCnt        => (others => (others => '0')),<br><span style="padding-left:20px">       transCnt       => (others => '0'),<br><span style="padding-left:20px">       timeoutDropCnt => (others => (others => '0')),<br><span style="padding-left:20px">       accept         => (others => '0'),<br><span style="padding-left:20px">       nullDet        => (others => '0'),<br><span style="padding-left:20px">       transDet       => (others => '0'),<br><span style="padding-left:20px">       timeoutDet     => (others => '0'),<br><span style="padding-left:20px">       index          => 0,<br><span style="padding-left:20px">       axilReadSlave  => AXI_LITE_READ_SLAVE_INIT_C,<br><span style="padding-left:20px">       axilWriteSlave => AXI_LITE_WRITE_SLAVE_INIT_C,<br><span style="padding-left:20px">       rxSlaves       => (others => AXI_STREAM_SLAVE_INIT_C),<br><span style="padding-left:20px">       txMaster       => AXI_STREAM_MASTER_INIT_C,<br><span style="padding-left:20px">       state          => IDLE_S) |             |
## Types

| Name      | Type                                                   | Description |
| --------- | ------------------------------------------------------ | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> MOVE_S)  |             |
| RegType   |                                                        |             |
## Processes
- TDEST_REMAP: ( sAxisMasters )
- comb: ( axilReadMaster, axilWriteMaster, axisRst, batcherIdle,
                   blowoffExt, r, rxMasters, timeoutEvent, txSlave )
**Description**
 greater than or equal to (a >= b) 
- seq: ( axisClk )
## Instantiations

- U_DspComparator: surf.DspComparator
- U_AxiStreamBatcher: surf.AxiStreamBatcher
**Description**
----------------
 AxiStreamBatcher
----------------

