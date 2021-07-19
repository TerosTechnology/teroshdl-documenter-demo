# Entity: IpBusToAxiLite

- **File**: IpBusToAxiLite.vhd
## Diagram

![Diagram](IpBusToAxiLite.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: IP Bus to AXI-Lite Bridge
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

| Port name       | Direction | Type                   | Description               |
| --------------- | --------- | ---------------------- | ------------------------- |
| clk             | in        | sl                     | Clock and Reset           |
| rst             | in        | sl                     |                           |
| ipbAddr         | in        | slv(31 downto 0)       | IP Bus Slave Interface    |
| ipbWdata        | in        | slv(31 downto 0)       |                           |
| ipbStrobe       | in        | sl                     |                           |
| ipbWrite        | in        | sl                     |                           |
| ipbRdata        | out       | slv(31 downto 0)       |                           |
| ipbAck          | out       | sl                     |                           |
| ipbErr          | out       | sl                     |                           |
| axilReadMaster  | out       | AxiLiteReadMasterType  | AXI-Lite Master Interface |
| axilReadSlave   | in        | AxiLiteReadSlaveType   |                           |
| axilWriteMaster | out       | AxiLiteWriteMasterType |                           |
| axilWriteSlave  | in        | AxiLiteWriteSlaveType  |                           |
## Signals

| Name | Type           | Description |
| ---- | -------------- | ----------- |
| r    | RegType        |             |
| rin  | RegType        |             |
| ack  | AxiLiteAckType |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                | Description |
| ---------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       ipbRdata => (others => '0'),<br><span style="padding-left:20px">       ipbAck   => '0',<br><span style="padding-left:20px">       ipbErr   => '0',<br><span style="padding-left:20px">       req      => AXI_LITE_REQ_INIT_C,<br><span style="padding-left:20px">       state    => IDLE_S) |             |
## Types

| Name      | Type                                                   | Description |
| --------- | ------------------------------------------------------ | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> WAIT_S)  |             |
| RegType   |                                                        |             |
## Processes
- comb: ( ack, ipbAddr, ipbStrobe, ipbWdata, ipbWrite, r, rst )
- seq: ( clk )
## Instantiations

- U_AxiLiteMaster: surf.AxiLiteMaster
