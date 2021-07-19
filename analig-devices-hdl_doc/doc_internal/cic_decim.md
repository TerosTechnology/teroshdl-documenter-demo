# Entity: cic_decim

- **File**: cic_decim.v
## Diagram

![Diagram](cic_decim.svg "Diagram")
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

| Port name     | Direction | Type   | Description |
| ------------- | --------- | ------ | ----------- |
| clk           | input     |        |             |
| clk_enable    | input     |        |             |
| filter_enable | input     | [4:0]  |             |
| reset         | input     |        |             |
| filter_in     | input     | [11:0] |             |
| rate_sel      | input     | [2:0]  |             |
| filter_out    | output    | [11:0] |             |
| ce_out        | output    |        |             |
## Signals

| Name               | Type                  | Description |
| ------------------ | --------------------- | ----------- |
| filter_input_stage | reg [11:0]            |             |
| data_stage         | wire [DATA_WIDTH-1:0] |             |
| data_final_stage   | wire [DATA_WIDTH-1:0] |             |
| counter            | reg [16:0]            |             |
| ce_comb            | reg                   |             |
| ce_out_reg         | reg                   |             |
| data_out           | reg [11:0]            |             |
| rate               | reg [15:0]            |             |
| enable             | wire [4:0]            |             |
| counter_in         | wire [15:0]           |             |
## Constants

| Name       | Type | Value | Description |
| ---------- | ---- | ----- | ----------- |
| NUM_STAGES |      | 6     |             |
| DATA_WIDTH |      | 106   |             |
## Processes
- unnamed: ( @(*) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
## Instantiations

- i_comb0: cic_comb
- i_comb1: cic_comb
