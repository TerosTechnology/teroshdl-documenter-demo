# Entity: cordic_demod

- **File**: cordic_demod.v
## Diagram

![Diagram](cordic_demod.svg "Diagram")
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

| Port name    | Direction | Type   | Description |
| ------------ | --------- | ------ | ----------- |
| clk          | input     |        |             |
| resetn       | input     |        |             |
| s_axis_valid | input     |        |             |
| s_axis_ready | output    |        |             |
| s_axis_data  | input     | [63:0] |             |
| m_axis_valid | output    |        |             |
| m_axis_ready | input     |        |             |
| m_axis_data  | output    | [63:0] |             |
## Signals

| Name          | Type       | Description |
| ------------- | ---------- | ----------- |
| step_counter  | reg [4:0]  |             |
| shift_counter | reg [4:0]  |             |
| phase         | reg [30:0] |             |
| state         | reg [2:0]  |             |
| i             | reg [32:0] |             |
| q             | reg [32:0] |             |
| i_shift       | reg [32:0] |             |
| q_shift       | reg [32:0] |             |
| angle         | reg [31:0] |             |
## Constants

| Name             | Type | Value | Description |
| ---------------- | ---- | ----- | ----------- |
| STATE_IDLE       |      | 0     |             |
| STATE_SHIFT_LOAD |      | 1     |             |
| STATE_SHIFT      |      | 2     |             |
| STATE_ADD        |      | 3     |             |
| STATE_DONE       |      | 4     |             |
## Processes
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
## State machines

![Diagram_state_machine_0]( stm_cordic_demod_00.svg "Diagram")