# Entity: AxiStreamDmaV2WriteMux

## Diagram

![Diagram](AxiStreamDmaV2WriteMux.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: This MUX is used to make sure that the write descriptor is sent
             after the data is sent. Else the descriptor can get to the
             software driver before the data received
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name   | Type          | Value | Description |
| -------------- | ------------- | ----- | ----------- |
| TPD_G          | time          | 1 ns  |             |
| AXI_CONFIG_G   | AxiConfigType |       |             |
| AXI_READY_EN_G | boolean       | false |             |
## Ports

| Port name       | Direction | Type               | Description               |
| --------------- | --------- | ------------------ | ------------------------- |
| axiClk          | in        | sl                 | Clock and reset           |
| axiRst          | in        | sl                 |                           |
| dataWriteMaster | in        | AxiWriteMasterType | DMA Data Write Path       |
| dataWriteSlave  | out       | AxiWriteSlaveType  |                           |
| dataWriteCtrl   | out       | AxiCtrlType        |                           |
| descWriteMaster | in        | AxiWriteMasterType | DMA Descriptor Write Path |
| descWriteSlave  | out       | AxiWriteSlaveType  |                           |
| mAxiWriteMaster | out       | AxiWriteMasterType | MUX Write Path            |
| mAxiWriteSlave  | in        | AxiWriteSlaveType  |                           |
| mAxiWriteCtrl   | in        | AxiCtrlType        |                           |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Description |
| ---------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| REG_INIT_C | RegType |  (       pause      => '0',<br><span style="padding-left:20px">       armed      => '0',<br><span style="padding-left:20px">       descSlave  => AXI_WRITE_SLAVE_INIT_C,<br><span style="padding-left:20px">       dataSlave  => AXI_WRITE_SLAVE_INIT_C,<br><span style="padding-left:20px">       descriptor => AXI_WRITE_MASTER_INIT_C,<br><span style="padding-left:20px">       master     => AXI_WRITE_MASTER_INIT_C,<br><span style="padding-left:20px">       state      => ADDR_S) |             |
## Types

| Name      | Type                                                                                               | Description |
| --------- | -------------------------------------------------------------------------------------------------- | ----------- |
| StateType | ( ADDR_S,<br><span style="padding-left:20px"> DATA_S,<br><span style="padding-left:20px"> DESC_S)  |             |
| RegType   |                                                                                                    |             |
## Processes
- comb: ( axiRst, dataWriteMaster, descWriteMaster, mAxiWriteCtrl,
                   mAxiWriteSlave, r )
- seq: ( axiClk )
