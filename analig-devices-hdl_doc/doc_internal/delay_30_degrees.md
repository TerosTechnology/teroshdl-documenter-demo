# Entity: delay_30_degrees

## Diagram

![Diagram](delay_30_degrees.svg "Diagram")
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
 
## Ports

| Port name  | Direction | Type   | Description                      |
| ---------- | --------- | ------ | -------------------------------- |
| clk_i      | input     |        |                                  |
| rst_i      | input     |        |                                  |
| offset_i   | input     | [31:0] | offset register                  |
| position_i | input     | [2:0]  | input position                   |
| position_o | output    | [2:0]  | delayed with 30 degrees position |
## Signals

| Name          | Type       | Description                                                    |
| ------------- | ---------- | -------------------------------------------------------------- |
| state         | reg [5:0]  | current state                                                  |
| next_state    | reg [5:0]  | next state                                                     |
| position_old  | reg [2:0]  | saves the latest position                                      |
| speed_count   | reg [31:0] | counts the current speed of rotation                           |
| speed_divider | reg [31:0] | divides the speed of rotation by 2, correspoding to 30 degrees |
| delay_count   | reg [31:0] | Applied the delay to the input signal                          |
## Constants

| Name             | Type | Value       | Description |
| ---------------- | ---- | ----------- | ----------- |
| MAX_SPEED_COUNT  |      | 32'h1000000 |             |
| RESET            |      | 6'b000001   |             |
| INIT             |      | 6'b000010   |             |
| CHANGE_POSITION  |      | 6'b000100   |             |
| DELAY_30_DEGREES |      | 6'b001000   |             |
| APPLY_CHANGE     |      | 6'b010000   |             |
| IDLE             |      | 6'b100000   |             |
## Processes
- unnamed: ( @* )
**Description**
State transitions

- unnamed: ( @(posedge clk_i) )
- unnamed: ( @ (posedge clk_i) )
