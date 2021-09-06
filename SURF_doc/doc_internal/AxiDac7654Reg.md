# Entity: AxiDac7654Reg

- **File**: AxiDac7654Reg.vhd
## Diagram

![Diagram](AxiDac7654Reg.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: AXI-Lite Register Access Module
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

| Generic name       | Type                  | Value | Description |
| ------------------ | --------------------- | ----- | ----------- |
| TPD_G              | time                  | 1 ns  |             |
| STATUS_CNT_WIDTH_G | natural range 1 to 32 | 32    |             |
## Ports

| Port name      | Direction | Type                   | Description                                 |
| -------------- | --------- | ---------------------- | ------------------------------------------- |
| axiClk         | in        | sl                     | AXI-Lite Register Interface (axiClk domain) |
| axiRst         | in        | sl                     |                                             |
| axiReadMaster  | in        | AxiLiteReadMasterType  |                                             |
| axiReadSlave   | out       | AxiLiteReadSlaveType   |                                             |
| axiWriteMaster | in        | AxiLiteWriteMasterType |                                             |
| axiWriteSlave  | out       | AxiLiteWriteSlaveType  |                                             |
| status         | in        | AxiDac7654StatusType   | Register Inputs/Outputs (axiClk domain)     |
| config         | out       | AxiDac7654ConfigType   |                                             |
## Signals

| Name   | Type                 | Description |
| ------ | -------------------- | ----------- |
| r      | RegType              |             |
| rin    | RegType              |             |
| syncIn | AxiDac7654StatusType |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                              | Description |
| ---------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       AXI_DAC7654_CONFIG_INIT_C,<br><span style="padding-left:20px">       IDLE_S,<br><span style="padding-left:20px">       AXI_LITE_READ_SLAVE_INIT_C,<br><span style="padding-left:20px">       AXI_LITE_WRITE_SLAVE_INIT_C) |             |
## Types

| Name      | Type                                                                                             | Description |
| --------- | ------------------------------------------------------------------------------------------------ | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> REQ_S,<br><span style="padding-left:20px"> ACK_S)  |             |
| RegType   |                                                                                                  |             |
## Processes
- comb: ( axiReadMaster, axiRst, axiWriteMaster, r, syncIn )
- seq: ( axiClk )
