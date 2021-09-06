# Entity: fir_decim

- **File**: fir_decim.v
## Diagram

![Diagram](fir_decim.svg "Diagram")
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

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| USE_DSP48E   |      | 1     |             |
## Ports

| Port name  | Direction | Type          | Description |
| ---------- | --------- | ------------- | ----------- |
| clk        | input     |               |             |
| clk_enable | input     |               |             |
| reset      | input     |               |             |
| filter_in  | input     | signed [11:0] |             |
| filter_out | output    | [25:0]        |             |
| ce_out     | output    |               |             |
## Signals

| Name      | Type              | Description                                                                                                                                                                                                                        |
| --------- | ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| active    | reg               |  We know that clk_enable is asserted at most every 5th clock cycle and the  output is decimated by two. So we have 10 clock cycles to compute the  result. That's plenty of time considering that there are only 6  coefficients.  |
| active_d1 | reg               |                                                                                                                                                                                                                                    |
| active_d2 | reg               |                                                                                                                                                                                                                                    |
| count     | reg [1:0]         |                                                                                                                                                                                                                                    |
| phase     | reg               |                                                                                                                                                                                                                                    |
| ready     | reg               |                                                                                                                                                                                                                                    |
| storage0  | reg [3:0]         |                                                                                                                                                                                                                                    |
| storage1  | reg [3:0]         |                                                                                                                                                                                                                                    |
| data0     | reg signed [11:0] |                                                                                                                                                                                                                                    |
| data1     | reg signed [11:0] |                                                                                                                                                                                                                                    |
| coeff     | reg signed [11:0] |                                                                                                                                                                                                                                    |
| sum       | wire [25:0]       |                                                                                                                                                                                                                                    |
| j         | integer           |                                                                                                                                                                                                                                    |
## Constants

| Name          | Type          | Value            | Description  |
| ------------- | ------------- | ---------------- | ------------ |
| coeffphase1_1 | signed [11:0] | 12'b000011010101 | sfix12_En11  |
| coeffphase1_2 | signed [11:0] | 12'b011011110010 | sfix12_En11  |
| coeffphase1_3 | signed [11:0] | 12'b110000111110 | sfix12_En11  |
## Processes
- unnamed: ( @(posedge clk) )
  - **Type:** always
- unnamed: ( @(posedge clk) )
  - **Type:** always
- unnamed: ( @(posedge clk) )
  - **Type:** always
- unnamed: ( @(posedge clk) )
  - **Type:** always
- unnamed: ( @(*) )
  - **Type:** always
- unnamed: ( @(posedge clk) )
  - **Type:** always
- unnamed: ( @(posedge clk) )
  - **Type:** always
## State machines

![Diagram_state_machine_0]( stm_fir_decim_00.svg "Diagram")