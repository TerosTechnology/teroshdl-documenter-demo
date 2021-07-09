# Entity: I2cRegSlave

## Diagram

![Diagram](I2cRegSlave.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: Implements an I2C slave attached to a generic RAM interface.
Protocol is simple: Address of configurable size, followed by data of
configurable size.
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name         | Type                    | Value | Description                       |
| -------------------- | ----------------------- | ----- | --------------------------------- |
| TPD_G                | time                    | 1 ns  |                                   |
| TENBIT_G             | integer range 0 to 1    | 0     | Generics passed down to I2cSlave  |
| I2C_ADDR_G           | integer range 0 to 1023 | 0     |                                   |
| OUTPUT_EN_POLARITY_G | integer range 0 to 1    | 0     |                                   |
| FILTER_G             | integer range 2 to 512  | 4     |                                   |
| ADDR_SIZE_G          | natural                 | 2     | in bytes                          |
| DATA_SIZE_G          | positive                | 1     | in bytes                          |
| ENDIANNESS_G         | integer range 0 to 1    | 0     |                                   |
## Ports

| Port name | Direction | Type                            | Description             |
| --------- | --------- | ------------------------------- | ----------------------- |
| sRst      | in        | sl                              |                         |
| aRst      | in        | sl                              |                         |
| clk       | in        | sl                              |                         |
| addr      | out       | slv((8*ADDR_SIZE_G)-1 downto 0) | Front End Ram Interface |
| wrEn      | out       | sl                              |                         |
| wrData    | out       | slv((8*DATA_SIZE_G)-1 downto 0) |                         |
| rdEn      | out       | sl                              |                         |
| rdData    | in        | slv((8*DATA_SIZE_G)-1 downto 0) |                         |
| i2ci      | in        | i2c_in_type                     | I2C Signals             |
| i2co      | out       | i2c_out_type                    |                         |
## Signals

| Name        | Type            | Description   |
| ----------- | --------------- | ------------- |
| r           | RegType         |               |
| rin         | RegType         |               |
| i2cSlaveOut | I2cSlaveOutType | From i2cSlave |
| i2cSlaveIn  | I2cSlaveInType  | To I2cSlave   |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Description |
| ---------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       state      => IDLE_S,<br><span style="padding-left:20px">       byteCnt    => (others => '0'),<br><span style="padding-left:20px">       addr       => (others => '0'),<br><span style="padding-left:20px">       wrEn       => '0',<br><span style="padding-left:20px">       wrData     => (others => '0'),<br><span style="padding-left:20px">       rdEn       => '0',<br><span style="padding-left:20px">       i2cSlaveIn => I2C_SLAVE_IN_INIT_C) |             |
## Types

| Name      | Type                                                                                                                                                     | Description |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| StateType | (IDLE_S,<br><span style="padding-left:20px"> ADDR_S,<br><span style="padding-left:20px"> WRITE_DATA_S,<br><span style="padding-left:20px"> READ_DATA_S)  |             |
| RegType   |                                                                                                                                                          |             |
## Functions
- getIndex <font id="function_arguments">( byteCount  : unsigned;<br><span style="padding-left:20px"> totalBytes : positive) </font> <font id="function_return">return integer </font>
## Processes
- comb: ( rdData, r, i2cSlaveOut, sRst )
- seq: ( clk, aRst )
## Instantiations

- I2cSlave_1: surf.I2cSlave
