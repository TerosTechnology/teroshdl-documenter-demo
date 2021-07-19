# Entity: SsiIbFrameFilter

- **File**: SsiIbFrameFilter.vhd
## Diagram

![Diagram](SsiIbFrameFilter.svg "Diagram")
## Description

Title      : SSI Protocol: https://confluence.slac.stanford.edu/x/0oyfD
Company    : SLAC National Accelerator Laboratory
Description: Inbound AXI Stream FIFO SSI Filter ....
             Tags frames with EOFE on double SOFs
             Drops frames that are missing SOF frame marker
             Tags frames with EOFE on change in TDEST during move
             Generates the overflow FIFO signal for user logic
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name     | Type                | Value | Description |
| ---------------- | ------------------- | ----- | ----------- |
| TPD_G            | time                | 1 ns  |             |
| SLAVE_READY_EN_G | boolean             | true  |             |
| AXIS_CONFIG_G    | AxiStreamConfigType |       |             |
## Ports

| Port name      | Direction | Type                | Description                                  |
| -------------- | --------- | ------------------- | -------------------------------------------- |
| sAxisMaster    | in        | AxiStreamMasterType | Slave Interface (User Application Interface) |
| sAxisSlave     | out       | AxiStreamSlaveType  |                                              |
| sAxisCtrl      | out       | AxiStreamCtrlType   |                                              |
| sAxisDropWord  | out       | sl                  | Word dropped status output                   |
| sAxisDropFrame | out       | sl                  | Frame dropped status output                  |
| mAxisMaster    | out       | AxiStreamMasterType | Master Interface (AXIS FIFO Write Interface) |
| mAxisSlave     | in        | AxiStreamSlaveType  |                                              |
| mAxisCtrl      | in        | AxiStreamCtrlType   |                                              |
| axisClk        | in        | sl                  | Clock and Reset                              |
| axisRst        | in        | sl                  |                                              |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name          | Type               | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Description |
| ------------- | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| SLAVE_INIT_C  | AxiStreamSlaveType |  ite(SLAVE_READY_EN_G,<br><span style="padding-left:20px"> AXI_STREAM_SLAVE_INIT_C,<br><span style="padding-left:20px"> AXI_STREAM_SLAVE_FORCE_C)                                                                                                                                                                                                                                                                                                                    |             |
| CHECK_TDEST_C | boolean            |  AXIS_CONFIG_G.TDEST_BITS_C > 0                                                                                                                                                                                                                                                                                                                                                                                                                                      |             |
| TDEST_BITS_C  | natural            |  ite(CHECK_TDEST_C,<br><span style="padding-left:20px"> AXIS_CONFIG_G.TDEST_BITS_C,<br><span style="padding-left:20px"> 1)                                                                                                                                                                                                                                                                                                                                           |             |
| REG_INIT_C    | RegType            |  (       overflow     => '0',<br><span style="padding-left:20px">       wordDropped  => '0',<br><span style="padding-left:20px">       frameDropped => '0',<br><span style="padding-left:20px">       tDest        => (others => '0'),<br><span style="padding-left:20px">       master       => AXI_STREAM_MASTER_INIT_C,<br><span style="padding-left:20px">       slave        => SLAVE_INIT_C,<br><span style="padding-left:20px">       state        => IDLE_S) |             |
## Types

| Name      | Type                                                                                                                                                     | Description |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> BLOWOFF_S,<br><span style="padding-left:20px"> MOVE_S,<br><span style="padding-left:20px"> INSERT_EOFE_S)  |             |
| RegType   |                                                                                                                                                          |             |
## Processes
- comb: ( axisRst, mAxisCtrl, mAxisSlave, r, sAxisMaster )
- seq: ( axisClk )
