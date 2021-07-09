# Entity: I2cRegMaster

## Diagram

![Diagram](I2cRegMaster.svg "Diagram")
## Description

File       : I2cRegMaster.vhd
Company    : SLAC National Accelerator Laboratory
Description:
  PRESCALE_G = (clk_freq / (5 * i2c_freq)) - 1
  FILTER_G = (min_pulse_time / clk_period) + 1
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name         | Type                      | Value | Description |
| -------------------- | ------------------------- | ----- | ----------- |
| TPD_G                | time                      | 1 ns  |             |
| OUTPUT_EN_POLARITY_G | integer range 0 to 1      | 0     |             |
| FILTER_G             | integer range 2 to 512    | 8     |             |
| PRESCALE_G           | integer range 0 to 655535 | 62    |             |
## Ports

| Port name | Direction | Type                | Description |
| --------- | --------- | ------------------- | ----------- |
| clk       | in        | sl                  |             |
| srst      | in        | sl                  |             |
| arst      | in        | sl                  |             |
| regIn     | in        | I2cRegMasterInType  |             |
| regOut    | out       | I2cRegMasterOutType |             |
| i2ci      | in        | i2c_in_type         |             |
| i2co      | out       | i2c_out_type        |             |
## Signals

| Name         | Type             | Description |
| ------------ | ---------------- | ----------- |
| r            | RegType          |             |
| rin          | RegType          |             |
| i2cMasterIn  | I2cMasterInType  |             |
| i2cMasterOut | I2cMasterOutType |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Description |
| ---------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       state          => WAIT_REQ_S,<br><span style="padding-left:20px">       byteCount      => (others => '0'),<br><span style="padding-left:20px">       regOut         => (          regAck      => '0',<br><span style="padding-left:20px">          regFail     => '0',<br><span style="padding-left:20px">          regFailCode => (others => '0'),<br><span style="padding-left:20px">          regRdData   => (others => '0')),<br><span style="padding-left:20px">       i2cMasterIn    => (          enable      => '0',<br><span style="padding-left:20px">          prescale    => (others => '0'),<br><span style="padding-left:20px">          filter      => (others => '0'),<br><span style="padding-left:20px">          txnReq      => '0',<br><span style="padding-left:20px">          stop        => '0',<br><span style="padding-left:20px">          op          => '0',<br><span style="padding-left:20px">          busReq      => '0',<br><span style="padding-left:20px">          addr        => (others => '0'),<br><span style="padding-left:20px">          tenbit      => '0',<br><span style="padding-left:20px">          wrValid     => '0',<br><span style="padding-left:20px">          wrData      => (others => '0'),<br><span style="padding-left:20px">          rdAck       => '0')) |             |
## Types

| Name      | Type                                                                                                                                                                                                                                                                                              | Description |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| StateType | ( WAIT_REQ_S,<br><span style="padding-left:20px"> ADDR_S,<br><span style="padding-left:20px"> WRITE_S,<br><span style="padding-left:20px"> READ_TXN_S,<br><span style="padding-left:20px"> READ_S,<br><span style="padding-left:20px"> BUS_ACK_S,<br><span style="padding-left:20px"> REG_ACK_S)  |             |
| RegType   |                                                                                                                                                                                                                                                                                                   |             |
## Functions
- getIndex <font id="function_arguments">( endianness : sl;<br><span style="padding-left:20px"> byteCount  : unsigned;<br><span style="padding-left:20px"> totalBytes : unsigned) </font> <font id="function_return">return integer </font>
## Processes
- comb: ( regIn, i2cMasterOut, r, srst )
- seq: ( clk, arst )
## Instantiations

- i2cMaster_1: surf.I2cMaster
