# Entity: speed_detector

- **File**: speed_detector.v
## Diagram

![Diagram](speed_detector.svg "Diagram")
## Description

 ***************************************************************************
 ***************************************************************************
 Copyright 2014 - 2017 (c) Analog Devices, Inc. All rights reserved.

 In this HDL repository, there are many different and unique modules, consisting
 of various HDL (Verilog or VHDL) components. The individual modules are
 developed independently, and may be accompanied by separate and unique license
 terms.

 The user should read each of these license terms, and understand the
 freedoms and responsibilities that he or she has by using this source/core.

 This core is distributed in the hope that it will be useful, but WITHOUT ANY
 WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
 A PARTICULAR PURPOSE.

 Redistribution and use of source or resulting binaries, with or without modification
 of this file, are permitted under one of the following two license terms:

   1. The GNU General Public License version 2 as published by the
      Free Software Foundation, which can be found in the top level directory
      of this repository (LICENSE_GPL2), and also online at:
      <https://www.gnu.org/licenses/old-licenses/gpl-2.0.html>

 OR

   2. An ADI specific BSD license, which can be found in the top level directory
      of this repository (LICENSE_ADIBSD), and also on-line at:
      https://github.com/analogdevicesinc/hdl/blob/master/LICENSE_ADIBSD
      This will allow to generate bit files and not release the source code,
      as long as it attaches to an ADI device.

 ***************************************************************************
 ***************************************************************************

## Generics

| Generic name     | Type | Value | Description                           |
| ---------------- | ---- | ----- | ------------------------------------- |
| AVERAGE_WINDOW   |      | 32    |  Averages data on the latest samples  |
| LOG_2_AW         |      | 5     |  Average window is 2 ^ LOG_2_AW       |
| SAMPLE_CLK_DECIM |      | 10000 |                                       |
## Ports

| Port name       | Direction | Type   | Description                           |
| --------------- | --------- | ------ | ------------------------------------- |
| clk_i           | input     |        |                                       |
| rst_i           | input     |        |                                       |
| position_i      | input     | [ 2:0] | position as determined by the sensors |
| new_speed_o     | output    |        | signals a new speed has been computed |
| current_speed_o | output    | [31:0] | data bus with the current speed       |
| speed_o         | output    | [31:0] | data bus with the mediated speed      |
## Signals

| Name                | Type       | Description                                                                                                                                                                                                                                   |
| ------------------- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| position_old        | reg [ 2:0] | ------------------------------------------------------------------------------ ----------- Registers Declarations ------------------------------------------- ------------------------------------------------------------------------------  |
| avg_register        | reg [63:0] |                                                                                                                                                                                                                                               |
| avg_register_stable | reg [63:0] |                                                                                                                                                                                                                                               |
| cnt_period          | reg [31:0] |                                                                                                                                                                                                                                               |
| decimation          | reg [31:0] | register used to divide by ten the speed                                                                                                                                                                                                      |
| cnt_period_old      | reg [31:0] |                                                                                                                                                                                                                                               |
| fifo                | reg [31:0] | 32 bit wide RAM                                                                                                                                                                                                                               |
| write_addr          | reg [AW:0] |                                                                                                                                                                                                                                               |
| read_addr           | reg [AW:0] |                                                                                                                                                                                                                                               |
| sample_clk_div      | reg [31:0] |                                                                                                                                                                                                                                               |
| state               | reg [ 7:0] |                                                                                                                                                                                                                                               |
| next_state          | reg [ 7:0] |                                                                                                                                                                                                                                               |
## Constants

| Name            | Type | Value        | Description                                                                                                                                                                                                                                   |
| --------------- | ---- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AW              |      | LOG_2_AW - 1 | ------------------------------------------------------------------------------ ----------- Local Parameters ------------------------------------------------- ------------------------------------------------------------------------------  |
| MAX_SPEED_CNT   |      | 32'h10000    |                                                                                                                                                                                                                                               |
| RESET           |      | 8'b00000001  | State machine                                                                                                                                                                                                                                 |
| INIT            |      | 8'b00000010  |                                                                                                                                                                                                                                               |
| CHANGE_POSITION |      | 8'b00000100  |                                                                                                                                                                                                                                               |
| ADD_COUNTER     |      | 8'b00001000  |                                                                                                                                                                                                                                               |
| SUBSTRACT_MEM   |      | 8'b00010000  |                                                                                                                                                                                                                                               |
| UPDATE_MEM      |      | 8'b00100000  |                                                                                                                                                                                                                                               |
| IDLE            |      | 8'b10000000  |                                                                                                                                                                                                                                               |
## Processes
- unnamed: ( @(posedge clk_i) )
  - **Type:** always
</br>**Description**
------------------------------------------------------------------------------ ----------- Assign/Always Blocks --------------------------------------------- ------------------------------------------------------------------------------  Count ticks per position 
- unnamed: ( @(posedge clk_i) )
  - **Type:** always
- unnamed: ( @* )
  - **Type:** always
- unnamed: ( @(posedge clk_i) )
  - **Type:** always
- unnamed: ( @(posedge clk_i) )
  - **Type:** always
</br>**Description**
 Stable sampling frequency of the motor speed 
