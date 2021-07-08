# Entity: AxiLiteMaster

## Diagram

![Diagram](AxiLiteMaster.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: AXI-Lite Master module controlled via REQ/ACK interface
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type | Value | Description     |
| ------------ | ---- | ----- | --------------- |
| TPD_G        | time | 1 ns  | General Config  |
## Ports

| Port name       | Direction | Type                   | Description |
| --------------- | --------- | ---------------------- | ----------- |
| axilClk         | in        | sl                     |             |
| axilRst         | in        | sl                     |             |
| req             | in        | AxiLiteReqType         |             |
| ack             | out       | AxiLiteAckType         |             |
| axilWriteMaster | out       | AxiLiteWriteMasterType |             |
| axilWriteSlave  | in        | AxiLiteWriteSlaveType  |             |
| axilReadMaster  | out       | AxiLiteReadMasterType  |             |
| axilReadSlave   | in        | AxiLiteReadSlaveType   |             |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                           | Description |
| ---------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       ack              =>  AXI_LITE_ACK_INIT_C,<br><span style="padding-left:20px">       state            => S_IDLE_C,<br><span style="padding-left:20px">       axilWriteMaster => AXI_LITE_WRITE_MASTER_INIT_C,<br><span style="padding-left:20px">       axilReadMaster  => AXI_LITE_READ_MASTER_INIT_C) |             |
## Types

| Name      | Type                                                                                                                                                                                                          | Description |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| StateType | (S_IDLE_C,<br><span style="padding-left:20px"> S_WRITE_C,<br><span style="padding-left:20px"> S_WRITE_AXI_C,<br><span style="padding-left:20px"> S_READ_C,<br><span style="padding-left:20px"> S_READ_AXI_C)  |             |
| RegType   |                                                                                                                                                                                                               |             |
## Processes
- comb: ( axilRst, axilReadSlave, axilWriteSlave, r, req )
- seq: ( axilClk )
