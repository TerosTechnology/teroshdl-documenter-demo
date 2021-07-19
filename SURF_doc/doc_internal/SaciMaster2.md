# Entity: SaciMaster2

- **File**: SaciMaster2.vhd
## Diagram

![Diagram](SaciMaster2.svg "Diagram")
## Description

Title      : SACI Protocol: https://confluence.slac.stanford.edu/x/YYcRDQ
Company    : SLAC National Accelerator Laboratory
Description: New and improved version of the SaciMaster.
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name       | Type     | Value  | Description |
| ------------------ | -------- | ------ | ----------- |
| TPD_G              | time     | 1 ns   |             |
| SYS_CLK_PERIOD_G   | real     | 8.0e-9 |             |
| SACI_CLK_PERIOD_G  | real     | 1.0e-6 |             |
| SACI_CLK_FREERUN_G | boolean  | false  |             |
| SACI_NUM_CHIPS_G   | positive | 1      |             |
| SACI_RSP_BUSSED_G  | boolean  | false  |             |
## Ports

| Port name | Direction | Type                                                        | Description       |
| --------- | --------- | ----------------------------------------------------------- | ----------------- |
| sysClk    | in        | sl                                                          | Main clock        |
| sysRst    | in        | sl                                                          |                   |
| req       | in        | sl                                                          | Request interface |
| ack       | out       | sl                                                          |                   |
| fail      | out       | sl                                                          |                   |
| chip      | in        | slv(log2(SACI_NUM_CHIPS_G)-1 downto 0)                      |                   |
| op        | in        | sl                                                          |                   |
| cmd       | in        | slv(6 downto 0)                                             |                   |
| addr      | in        | slv(11 downto 0)                                            |                   |
| wrData    | in        | slv(31 downto 0)                                            |                   |
| rdData    | out       | slv(31 downto 0)                                            |                   |
| saciClk   | out       | sl                                                          | Serial interface  |
| saciSelL  | out       | slv(SACI_NUM_CHIPS_G-1 downto 0)                            |                   |
| saciCmd   | out       | sl                                                          |                   |
| saciRsp   | in        | slv(ite(SACI_RSP_BUSSED_G, 0, SACI_NUM_CHIPS_G-1) downto 0) |                   |
## Signals

| Name        | Type               | Description |
| ----------- | ------------------ | ----------- |
| r           | RegType            |             |
| rin         | RegType            |             |
| saciRspSync | slv(saciRsp'range) |             |
## Constants

| Name                    | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Description |
| ----------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| SACI_CLK_HALF_PERIOD_C  | integer |  integer(SACI_CLK_PERIOD_G / (2.0*SYS_CLK_PERIOD_G))-1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |             |
| SACI_CLK_COUNTER_SIZE_C | integer |  log2(SACI_CLK_HALF_PERIOD_C)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |             |
| REG_INIT_C              | RegType |  (       state          => IDLE_S,<br><span style="padding-left:20px">       shiftReg       => (others => '0'),<br><span style="padding-left:20px">       shiftCount     => (others => '0'),<br><span style="padding-left:20px">       clkCount       => (others => '0'),<br><span style="padding-left:20px">       saciClkRising  => '0',<br><span style="padding-left:20px">       saciClkFalling => '0',<br><span style="padding-left:20px">       ack            => '0',<br><span style="padding-left:20px">       fail           => '0',<br><span style="padding-left:20px">       rdData         => (others => '0'),<br><span style="padding-left:20px">       saciClk        => '0',<br><span style="padding-left:20px">       saciSelL       => (others => '1'),<br><span style="padding-left:20px">       saciCmd        => '0') |             |
## Types

| Name      | Type                                                                                                                                                                                                                                           | Description |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| StateType | (IDLE_S,<br><span style="padding-left:20px"> TX_S,<br><span style="padding-left:20px"> RX_START_S,<br><span style="padding-left:20px"> RX_HEADER_S,<br><span style="padding-left:20px"> RX_DATA_S,<br><span style="padding-left:20px"> ACK_S)  |             |
| RegType   |                                                                                                                                                                                                                                                |             |
## Processes
- comb: ( addr, chip, cmd, op, r, req, saciRspSync, sysRst, wrData )
**Description**
Main logic

- seq: ( sysClk )
