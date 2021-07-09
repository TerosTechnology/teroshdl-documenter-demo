# Entity: AxiI2cEepromCore

## Diagram

![Diagram](AxiI2cEepromCore.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: AXI-Lite Read/ModifyWrite for standard EEPROM Module
Supported Devices:
   24AA01F/24LC01F/24FC01F    (1kb:   ADDR_WIDTH_G = 7)
   24AA02F/24LC02F/24FC02F    (2kb:   ADDR_WIDTH_G = 8)
   24AA04F/24LC04F/24FC04F    (4kb:   ADDR_WIDTH_G = 9)
   24AA08F/24LC08F/24FC08F    (8kb:   ADDR_WIDTH_G = 10)
   24AA16F/24LC16F/24FC16F    (16kb:  ADDR_WIDTH_G = 11)
   24AA32F/24LC32F/24FC32F    (32kb:  ADDR_WIDTH_G = 12)
   24AA64F/24LC64F/24FC64F    (64kb:  ADDR_WIDTH_G = 13)
   24AA128F/24LC128F/24FC128F (128kb: ADDR_WIDTH_G = 14)
   24AA256F/24LC256F/24FC256F (256kb: ADDR_WIDTH_G = 15)
   24AA512F/24LC512F/24FC512F (512kb: ADDR_WIDTH_G = 16)
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name    | Type            | Value     | Description      |
| --------------- | --------------- | --------- | ---------------- |
| TPD_G           | time            | 1 ns      |                  |
| ADDR_WIDTH_G    | positive        | 16        |                  |
| POLL_TIMEOUT_G  | positive        | 16        |                  |
| I2C_ADDR_G      | slv(6 downto 0) | "1010000" |                  |
| I2C_SCL_FREQ_G  | real            | 100.0E+3  | units of Hz      |
| I2C_MIN_PULSE_G | real            | 100.0E-9  | units of seconds |
| AXI_CLK_FREQ_G  | real            | 156.25E+6 |                  |
## Ports

| Port name       | Direction | Type                   | Description                 |
| --------------- | --------- | ---------------------- | --------------------------- |
| i2ci            | in        | i2c_in_type            | I2C Ports                   |
| i2co            | out       | i2c_out_type           |                             |
| axilReadMaster  | in        | AxiLiteReadMasterType  | AXI-Lite Register Interface |
| axilReadSlave   | out       | AxiLiteReadSlaveType   |                             |
| axilWriteMaster | in        | AxiLiteWriteMasterType |                             |
| axilWriteSlave  | out       | AxiLiteWriteSlaveType  |                             |
| axilClk         | in        | sl                     | Clocks and Resets           |
| axilRst         | in        | sl                     |                             |
## Signals

| Name   | Type                | Description |
| ------ | ------------------- | ----------- |
| r      | RegType             |             |
| rin    | RegType             |             |
| regOut | I2cRegMasterOutType |             |
## Constants

| Name                        | Type               | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Description  |
| --------------------------- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| I2C_SCL_5xFREQ_C            | real               |  5.0 * I2C_SCL_FREQ_G                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |              |
| PRESCALE_C                  | natural            |  (getTimeRatio(AXI_CLK_FREQ_G,<br><span style="padding-left:20px"> I2C_SCL_5xFREQ_C)) - 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |              |
| FILTER_C                    | natural            |  natural(AXI_CLK_FREQ_G * I2C_MIN_PULSE_G) + 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |              |
| ADDR_SIZE_C                 | slv(1 downto 0)    |  toSlv(wordCount(ADDR_WIDTH_G,<br><span style="padding-left:20px"> 8) - 1,<br><span style="padding-left:20px"> 2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |              |
| DATA_SIZE_C                 | slv(1 downto 0)    |  toSlv(wordCount(32,<br><span style="padding-left:20px"> 8) - 1,<br><span style="padding-left:20px"> 2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |              |
| I2C_ADDR_C                  | slv(9 downto 0)    |  ("000" & I2C_ADDR_G)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |              |
| TIMEOUT_C                   | natural            |  (getTimeRatio(AXI_CLK_FREQ_G,<br><span style="padding-left:20px"> 200.0)) - 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 5 ms timeout |
| MY_I2C_REG_MASTER_IN_INIT_C | I2cRegMasterInType |  (       i2cAddr     => I2C_ADDR_C,<br><span style="padding-left:20px">       tenbit      => '0',<br><span style="padding-left:20px">       regAddr     => (others => '0'),<br><span style="padding-left:20px">       regWrData   => (others => '0'),<br><span style="padding-left:20px">       regOp       => '0',<br><span style="padding-left:20px">               -- 1 for write,<br><span style="padding-left:20px"> 0 for read       regAddrSkip => '0',<br><span style="padding-left:20px">       regAddrSize => ADDR_SIZE_C,<br><span style="padding-left:20px">       regDataSize => DATA_SIZE_C,<br><span style="padding-left:20px">       regReq      => '0',<br><span style="padding-left:20px">       busReq      => '0',<br><span style="padding-left:20px">       endianness  => '1',<br><span style="padding-left:20px">               -- Big endian       repeatStart => '0') |              |
| REG_INIT_C                  | RegType            |  (       timer          => 0,<br><span style="padding-left:20px">       RnW            => '0',<br><span style="padding-left:20px">       axilReadSlave  => AXI_LITE_READ_SLAVE_INIT_C,<br><span style="padding-left:20px">       axilWriteSlave => AXI_LITE_WRITE_SLAVE_INIT_C,<br><span style="padding-left:20px">       regIn          => MY_I2C_REG_MASTER_IN_INIT_C,<br><span style="padding-left:20px">       state          => IDLE_S)                                                                                                                                                                                                                                                                                                                                                                                                                                                   |              |
## Types

| Name      | Type                                                                                                                                                                                                                                                                                                        | Description |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> READ_ACK_S,<br><span style="padding-left:20px"> READ_DONE_S,<br><span style="padding-left:20px"> WRITE_REQ_S,<br><span style="padding-left:20px"> WRITE_ACK_S,<br><span style="padding-left:20px"> WRITE_DONE_S,<br><span style="padding-left:20px"> WAIT_S)  |             |
| RegType   |                                                                                                                                                                                                                                                                                                             |             |
## Processes
- comb: ( axilReadMaster, axilRst, axilWriteMaster, r, regOut )
- seq: ( axilClk )
## Instantiations

- U_I2cRegMaster: surf.I2cRegMaster
