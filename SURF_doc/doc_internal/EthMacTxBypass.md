# Entity: EthMacTxBypass

- **File**: EthMacTxBypass.vhd
## Diagram

![Diagram](EthMacTxBypass.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description:
Mux stage to allow high priority bypass traffic to override primary path
traffic.
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| TPD_G        | time    | 1 ns  |             |
| BYP_EN_G     | boolean | false |             |
## Ports

| Port name   | Direction | Type                | Description              |
| ----------- | --------- | ------------------- | ------------------------ |
| ethClk      | in        | sl                  | Clock and Reset          |
| ethRst      | in        | sl                  |                          |
| sPrimMaster | in        | AxiStreamMasterType | Incoming primary traffic |
| sPrimSlave  | out       | AxiStreamSlaveType  |                          |
| sBypMaster  | in        | AxiStreamMasterType | Incoming bypass traffic  |
| sBypSlave   | out       | AxiStreamSlaveType  |                          |
| mAxisMaster | out       | AxiStreamMasterType | Outgoing data to MAC     |
| mAxisSlave  | in        | AxiStreamSlaveType  |                          |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                  | Description |
| ---------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       mAxisMaster => AXI_STREAM_MASTER_INIT_C,<br><span style="padding-left:20px">       sPrimSlave  => AXI_STREAM_SLAVE_INIT_C,<br><span style="padding-left:20px">       sBypSlave   => AXI_STREAM_SLAVE_INIT_C,<br><span style="padding-left:20px">       state       => IDLE_S) |             |
## Types

| Name      | Type                                                                                              | Description |
| --------- | ------------------------------------------------------------------------------------------------- | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> PRIM_S,<br><span style="padding-left:20px"> BYP_S)  |             |
| RegType   |                                                                                                   |             |
