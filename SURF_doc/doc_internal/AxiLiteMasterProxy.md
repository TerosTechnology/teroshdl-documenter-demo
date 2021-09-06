# Entity: AxiLiteMasterProxy

- **File**: AxiLiteMasterProxy.vhd
## Diagram

![Diagram](AxiLiteMasterProxy.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: A Proxy module for sending transactions on an AXI-Lite bus.

 Usefull for situations with long transactions times, such as when the
 AXI-Lite bus is bridged to I2C. In this case, the AXI-Lite bus Master
 could be locked out for some time while waiting for the I2C transaction to
 complete. This module allows the transaction to be kicked off and then the
 response to be polled for later.
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

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| TPD_G        | time | 1 ns  |             |
## Ports

| Port name       | Direction | Type                   | Description                 |
| --------------- | --------- | ---------------------- | --------------------------- |
| axiClk          | in        | sl                     | Clocks and Resets           |
| axiRst          | in        | sl                     |                             |
| sAxiReadMaster  | in        | AxiLiteReadMasterType  | AXI-Lite Register Interface |
| sAxiReadSlave   | out       | AxiLiteReadSlaveType   |                             |
| sAxiWriteMaster | in        | AxiLiteWriteMasterType |                             |
| sAxiWriteSlave  | out       | AxiLiteWriteSlaveType  |                             |
| mAxiReadMaster  | out       | AxiLiteReadMasterType  | AXI-Lite Register Interface |
| mAxiReadSlave   | in        | AxiLiteReadSlaveType   |                             |
| mAxiWriteMaster | out       | AxiLiteWriteMasterType |                             |
| mAxiWriteSlave  | in        | AxiLiteWriteSlaveType  |                             |
## Signals

| Name | Type           | Description |
| ---- | -------------- | ----------- |
| r    | RegType        |             |
| rin  | RegType        |             |
| ack  | AxiLiteAckType |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Description |
| ---------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       sAxiWriteSlave  => AXI_LITE_WRITE_SLAVE_INIT_C,<br><span style="padding-left:20px">       sAxiReadSlave   => AXI_LITE_READ_SLAVE_INIT_C,<br><span style="padding-left:20px">       req             => AXI_LITE_REQ_INIT_C,<br><span style="padding-left:20px">       state           => READY_S,<br><span style="padding-left:20px">       rnw             => '0',<br><span style="padding-left:20px">       done            => '1',<br><span style="padding-left:20px">       resp            => "00",<br><span style="padding-left:20px">       addr            => (others=>'0'),<br><span style="padding-left:20px">       data            => (others=>'0') ) |             |
## Types

| Name      | Type                                                    | Description |
| --------- | ------------------------------------------------------- | ----------- |
| StateType | ( READY_S,<br><span style="padding-left:20px"> ACK_S )  |             |
| RegType   |                                                         |             |
## Processes
- comb: ( ack, axiRst, r, sAxiReadMaster, sAxiWriteMaster )
- seq: ( axiClk )
## Instantiations

- U_AxiLiteMaster: surf.AxiLiteMaster
