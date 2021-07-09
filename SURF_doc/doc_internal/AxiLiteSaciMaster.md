# Entity: AxiLiteSaciMaster

## Diagram

![Diagram](AxiLiteSaciMaster.svg "Diagram")
## Description

Title      : SACI Protocol: https://confluence.slac.stanford.edu/x/YYcRDQ
Company    : SLAC National Accelerator Laboratory
Description: New and improved version of the AxiLiteSaciMaster.
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name       | Type                  | Value  | Description         |
| ------------------ | --------------------- | ------ | ------------------- |
| TPD_G              | time                  | 1 ns   |                     |
| AXIL_CLK_PERIOD_G  | real                  | 8.0e-9 | In units of seconds |
| AXIL_TIMEOUT_G     | real                  | 1.0E-3 | In units of seconds |
| SACI_CLK_PERIOD_G  | real                  | 1.0e-6 | In units of seconds |
| SACI_CLK_FREERUN_G | boolean               | false  |                     |
| SACI_NUM_CHIPS_G   | positive range 1 to 4 | 1      |                     |
| SACI_RSP_BUSSED_G  | boolean               | false  |                     |
## Ports

| Port name       | Direction | Type                                                        | Description                   |
| --------------- | --------- | ----------------------------------------------------------- | ----------------------------- |
| saciClk         | out       | sl                                                          | SACI interface                |
| saciCmd         | out       | sl                                                          |                               |
| saciSelL        | out       | slv(SACI_NUM_CHIPS_G-1 downto 0)                            |                               |
| saciRsp         | in        | slv(ite(SACI_RSP_BUSSED_G, 0, SACI_NUM_CHIPS_G-1) downto 0) |                               |
| saciBusReq      | out       | sl                                                          | Optional SACI bus arbitration |
| saciBusGr       | in        | sl                                                          |                               |
| axilClk         | in        | sl                                                          | AXI-Lite Register Interface   |
| axilRst         | in        | sl                                                          |                               |
| axilReadMaster  | in        | AxiLiteReadMasterType                                       |                               |
| axilReadSlave   | out       | AxiLiteReadSlaveType                                        |                               |
| axilWriteMaster | in        | AxiLiteWriteMasterType                                      |                               |
| axilWriteSlave  | out       | AxiLiteWriteSlaveType                                       |                               |
## Signals

| Name   | Type             | Description |
| ------ | ---------------- | ----------- |
| r      | RegType          |             |
| rin    | RegType          |             |
| ack    | sl               |             |
| fail   | sl               |             |
| rdData | slv(31 downto 0) |             |
## Constants

| Name        | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Description |
| ----------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| CHIP_BITS_C | integer |  log2(SACI_NUM_CHIPS_G)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |             |
| TIMEOUT_C   | integer |  integer(AXIL_TIMEOUT_G/AXIL_CLK_PERIOD_G)-1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |             |
| REG_INIT_C  | RegType |  (       state          => IDLE_S,<br><span style="padding-left:20px">       saciBusReq     => '0',<br><span style="padding-left:20px">       saciRst        => '1',<br><span style="padding-left:20px">       req            => '0',<br><span style="padding-left:20px">       chip           => (others => '0'),<br><span style="padding-left:20px">       op             => '0',<br><span style="padding-left:20px">       cmd            => (others => '0'),<br><span style="padding-left:20px">       addr           => (others => '0'),<br><span style="padding-left:20px">       wrData         => (others => '0'),<br><span style="padding-left:20px">       timer          => 0,<br><span style="padding-left:20px">       axilReadSlave  => AXI_LITE_READ_SLAVE_INIT_C,<br><span style="padding-left:20px">       axilWriteSlave => AXI_LITE_WRITE_SLAVE_INIT_C) |             |
## Types

| Name      | Type                                                                                                       | Description |
| --------- | ---------------------------------------------------------------------------------------------------------- | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> SACI_REQ_S,<br><span style="padding-left:20px"> SACI_ACK_S)  |             |
| RegType   |                                                                                                            |             |
## Processes
- comb: ( ack, axilReadMaster, axilRst, axilWriteMaster, fail, r, rdData, saciBusGr )
**Description**
[in]

- seq: ( axilClk )
## Instantiations

- U_SaciMaster2_1: surf.SaciMaster2
