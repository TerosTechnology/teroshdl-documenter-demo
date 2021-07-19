# Entity: ClinkData

- **File**: ClinkData.vhd
## Diagram

![Diagram](ClinkData.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description:
CameraLink data de-serializer.
Wrapper for ClinkDeSerial when used as dedicated data channel.
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type   | Value     | Description |
| ------------ | ------ | --------- | ----------- |
| TPD_G        | time   | 1 ns      |             |
| XIL_DEVICE_G | string | "7SERIES" |             |
## Ports

| Port name       | Direction | Type                   | Description                                       |
| --------------- | --------- | ---------------------- | ------------------------------------------------- |
| cblHalfP        | inout     | slv(4 downto 0)        |  8, 10, 11, 12,  9                                |
| cblHalfM        | inout     | slv(4 downto 0)        | 21, 23, 24, 25, 22                                |
| dlyClk          | in        | sl                     | Delay clock, 200Mhz                               |
| dlyRst          | in        | sl                     |                                                   |
| sysClk          | in        | sl                     | System clock and reset, must be 100Mhz or greater |
| sysRst          | in        | sl                     |                                                   |
| linkConfig      | in        | ClLinkConfigType       | Status and config                                 |
| linkStatus      | out       | ClLinkStatusType       |                                                   |
| parData         | out       | slv(27 downto 0)       | Data output                                       |
| parValid        | out       | sl                     |                                                   |
| parReady        | in        | sl                     |                                                   |
| axilReadMaster  | in        | AxiLiteReadMasterType  | AXI-Lite Interface                                |
| axilReadSlave   | out       | AxiLiteReadSlaveType   |                                                   |
| axilWriteMaster | in        | AxiLiteWriteMasterType |                                                   |
| axilWriteSlave  | out       | AxiLiteWriteSlaveType  |                                                   |
## Signals

| Name     | Type             | Description |
| -------- | ---------------- | ----------- |
| r        | RegType          |             |
| rin      | RegType          |             |
| rstFsm   | sl               |             |
| clinkClk | sl               |             |
| clinkRst | sl               |             |
| intData  | slv(27 downto 0) |             |
| parClock | slv(6 downto 0)  |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Description |
| ---------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       state   => RESET_S,<br><span style="padding-left:20px">       lastClk => (others => '0'),<br><span style="padding-left:20px">       delay   => toSlv(10,<br><span style="padding-left:20px">5),<br><span style="padding-left:20px">       delayLd => '0',<br><span style="padding-left:20px">       bitSlip => '0',<br><span style="padding-left:20px">       count   => 99,<br><span style="padding-left:20px">       status  => CL_LINK_STATUS_INIT_C) |             |
## Types

| Name      | Type                                                                                                                                                                                                                                                                                                                                           | Description                                                                                      |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| LinkState | (RESET_S,<br><span style="padding-left:20px"> WAIT_C_S,<br><span style="padding-left:20px"> SHIFT_C_S,<br><span style="padding-left:20px"> CHECK_C_S,<br><span style="padding-left:20px"> LOAD_C_S,<br><span style="padding-left:20px"> SHIFT_D_S,<br><span style="padding-left:20px"> CHECK_D_S,<br><span style="padding-left:20px"> DONE_S)  |                                                                                                  |
| RegType   |                                                                                                                                                                                                                                                                                                                                                | Each delay tap = 1/(32 * 2 * 200Mhz) = 78psInput rate = 85Mhz * 7 = 595Mhz = 1.68nS = 21.55 taps |
## Processes
- comb: ( clinkRst, parClock, r, rstFsm )
**Description**
State Machine

- seq: ( clinkClk )
**Description**
sync logic

## Instantiations

- U_DataShift: surf.ClinkDataShift
- U_RstSync: surf.RstSync
- U_DataFifo: surf.Fifo
**Description**
Output FIFO and status

- U_Locked: surf.Synchronizer
- U_Delay: surf.SynchronizerVector
- U_ShiftCnt: surf.SynchronizerVector
