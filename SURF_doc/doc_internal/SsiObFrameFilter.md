# Entity: SsiObFrameFilter

- **File**: SsiObFrameFilter.vhd
## Diagram

![Diagram](SsiObFrameFilter.svg "Diagram")
## Description

Title      : SSI Protocol: https://confluence.slac.stanford.edu/x/0oyfD
Company    : SLAC National Accelerator Laboratory
Description: Outbound AXI Stream FIFO SSI Filter ....
             Tags frames with EOFE on double SOFs
             Drops frames that are EOFE frame marker when VALID_THOLD_G = 0
             Tags frames with EOFE on change in TDEST during move
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name  | Type                | Value | Description |
| ------------- | ------------------- | ----- | ----------- |
| TPD_G         | time                | 1 ns  |             |
| VALID_THOLD_G | natural             | 1     |             |
| PIPE_STAGES_G | natural             | 1     |             |
| AXIS_CONFIG_G | AxiStreamConfigType |       |             |
## Ports

| Port name      | Direction | Type                | Description                           |
| -------------- | --------- | ------------------- | ------------------------------------- |
| sAxisMaster    | in        | AxiStreamMasterType | Slave Port (AXIS FIFO Read Interface) |
| sTLastTUser    | in        | slv(7 downto 0)     |                                       |
| sAxisSlave     | out       | AxiStreamSlaveType  |                                       |
| mAxisMaster    | out       | AxiStreamMasterType | Master Port                           |
| mAxisSlave     | in        | AxiStreamSlaveType  |                                       |
| mAxisDropWord  | out       | sl                  | Word dropped status output            |
| mAxisDropFrame | out       | sl                  | Frame dropped status output           |
| axisClk        | in        | sl                  | Clock and Reset                       |
| axisRst        | in        | sl                  |                                       |
## Signals

| Name       | Type                | Description |
| ---------- | ------------------- | ----------- |
| r          | RegType             |             |
| rin        | RegType             |             |
| axisMaster | AxiStreamMasterType |             |
| axisSlave  | AxiStreamSlaveType  |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Description |
| ---------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| REG_INIT_C | RegType |  (       sof          => '0',<br><span style="padding-left:20px">       eofe         => '0',<br><span style="padding-left:20px">       wordDropped  => '0',<br><span style="padding-left:20px">       frameDropped => '0',<br><span style="padding-left:20px">       tDest        => x"00",<br><span style="padding-left:20px">       master       => AXI_STREAM_MASTER_INIT_C,<br><span style="padding-left:20px">       slave        => AXI_STREAM_SLAVE_INIT_C,<br><span style="padding-left:20px">       state        => IDLE_S) |             |
## Types

| Name      | Type                                                                                                  | Description |
| --------- | ----------------------------------------------------------------------------------------------------- | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> BLOWOFF_S,<br><span style="padding-left:20px"> MOVE_S)  |             |
| RegType   |                                                                                                       |             |
## Processes
- comb: ( axisRst, axisSlave, r, sAxisMaster, sTLastTUser )
- seq: ( axisClk )
## Instantiations

- U_Pipe: surf.AxiStreamPipeline
