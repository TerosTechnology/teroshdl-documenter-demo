# Entity: AxiXcf128Reg

## Diagram

![Diagram](AxiXcf128Reg.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: AXI-Lite Register Access
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name   | Type | Value    | Description |
| -------------- | ---- | -------- | ----------- |
| TPD_G          | time | 1 ns     |             |
| AXI_CLK_FREQ_G | real | 200.0E+6 |             |
## Ports

| Port name      | Direction | Type                   | Description                 |
| -------------- | --------- | ---------------------- | --------------------------- |
| axiReadMaster  | in        | AxiLiteReadMasterType  | AXI-Lite Register Interface |
| axiReadSlave   | out       | AxiLiteReadSlaveType   |                             |
| axiWriteMaster | in        | AxiLiteWriteMasterType |                             |
| axiWriteSlave  | out       | AxiLiteWriteSlaveType  |                             |
| status         | in        | AxiXcf128StatusType    | Register Inputs/Outputs     |
| config         | out       | AxiXcf128ConfigType    |                             |
| axiClk         | in        | sl                     | Global Signals              |
| axiRst         | in        | sl                     |                             |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Description |
| ---------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| MAX_CNT_C  | natural |  (getTimeRatio(AXI_CLK_FREQ_G,<br><span style="padding-left:20px"> 10.0E+6))-1                                                                                                                                                                                                                                                                                                                                                                                  |             |
| REG_INIT_C | RegType |  (       (others => '0'),<br><span style="padding-left:20px">       (others => (others => '0')),<br><span style="padding-left:20px">       '0',<br><span style="padding-left:20px">       0,<br><span style="padding-left:20px">       AXI_XCF128_CONFIG_INIT_C,<br><span style="padding-left:20px">       IDLE_S,<br><span style="padding-left:20px">       AXI_LITE_READ_SLAVE_INIT_C,<br><span style="padding-left:20px">       AXI_LITE_WRITE_SLAVE_INIT_C) |             |
## Types

| Name      | Type                                                                                                                                                                                                                                                   | Description |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| stateType | ( IDLE_S,<br><span style="padding-left:20px"> CMD_LOW_S,<br><span style="padding-left:20px"> CMD_HIGH_S,<br><span style="padding-left:20px"> WAIT_S,<br><span style="padding-left:20px"> DATA_LOW_S,<br><span style="padding-left:20px"> DATA_HIGH_S)  |             |
| RegType   |                                                                                                                                                                                                                                                        |             |
## Processes
- comb: ( axiReadMaster, axiRst, axiWriteMaster, r, status )
- seq: ( axiClk )
