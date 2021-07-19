# Entity: AxiLiteToIpBus

- **File**: AxiLiteToIpBus.vhd
## Diagram

![Diagram](AxiLiteToIpBus.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: AXI-Lite to IP Bus Bridge
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
| clk             | in        | sl                     | Clock and Reset          |
| rst             | in        | sl                     |                          |
| axilReadMaster  | in        | AxiLiteReadMasterType  | AXI-Lite Slave Interface |
| axilReadSlave   | out       | AxiLiteReadSlaveType   |                          |
| axilWriteMaster | in        | AxiLiteWriteMasterType |                          |
| axilWriteSlave  | out       | AxiLiteWriteSlaveType  |                          |
| ipbRdata        | in        | slv(31 downto 0)       | IP Bus Master Interface  |
| ipbAck          | in        | sl                     |                          |
| ipbErr          | in        | sl                     |                          |
| ipbAddr         | out       | slv(31 downto 0)       |                          |
| ipbWdata        | out       | slv(31 downto 0)       |                          |
| ipbStrobe       | out       | sl                     |                          |
| ipbWrite        | out       | sl                     |                          |
## Signals

| Name | Type           | Description |
| ---- | -------------- | ----------- |
| r    | RegType        |             |
| rin  | RegType        |             |
| req  | AxiLiteReqType |             |
| ack  | AxiLiteAckType |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                                                                                             | Description |
| ---------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       ipbAddr   => (others => '0'),<br><span style="padding-left:20px">       ipbWdata  => (others => '0'),<br><span style="padding-left:20px">       ipbStrobe => '0',<br><span style="padding-left:20px">       ipbWrite  => '0',<br><span style="padding-left:20px">       ack       => AXI_LITE_ACK_INIT_C,<br><span style="padding-left:20px">       state     => IDLE_S) |             |
## Types

| Name      | Type                                                   | Description |
| --------- | ------------------------------------------------------ | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> WAIT_S)  |             |
| RegType   |                                                        |             |
## Processes
- comb: ( ipbAck, ipbErr, ipbRdata, r, req, rst )
- seq: ( clk )
## Instantiations

- U_AxiLiteSlave: surf.AxiLiteSlave
