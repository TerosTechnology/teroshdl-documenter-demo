# Entity: AxiLiteRespTimer

## Diagram

![Diagram](AxiLiteRespTimer.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: Writing to this module sets a timer for a deleyed write response
             Read transaction are not supported and will respond with error
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| TPD_G        | time | 1 ns  |             |
## Ports

| Port name       | Direction | Type                   | Description              |
| --------------- | --------- | ---------------------- | ------------------------ |
| axilClk         | in        | sl                     | Slave AXI-Lite Interface |
| axilRst         | in        | sl                     |                          |
| axilReadMaster  | in        | AxiLiteReadMasterType  |                          |
| axilReadSlave   | out       | AxiLiteReadSlaveType   |                          |
| axilWriteMaster | in        | AxiLiteWriteMasterType |                          |
| axilWriteSlave  | out       | AxiLiteWriteSlaveType  |                          |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                            | Description |
| ---------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| REG_INIT_C | RegType |  (       timer          => (others => '0'),<br><span style="padding-left:20px">       axilWriteSlave => AXI_LITE_WRITE_SLAVE_INIT_C,<br><span style="padding-left:20px">       axilReadSlave  => AXI_LITE_READ_SLAVE_INIT_C,<br><span style="padding-left:20px">       state          => IDLE_S) |             |
## Types

| Name      | Type                                                    | Description |
| --------- | ------------------------------------------------------- | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> TIMER_S)  |             |
| RegType   |                                                         |             |
## Processes
- comb: ( axilReadMaster, axilRst, axilWriteMaster, r )
- seq: ( axilClk )
