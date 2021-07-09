# Entity: util_dec256sinc24b

## Diagram

![Diagram](util_dec256sinc24b.svg "Diagram")
## Description

***************************************************************************
 ***************************************************************************
 Copyright 2014 - 2017 (c) Analog Devices, Inc. All rights reserved.
 In this HDL repository, there are many different and unique modules, consisting
 of various HDL (Verilog or VHDL) components. The individual modules are
 developed independently, and may be accompanied by separate and unique license
 terms.
 The user should read each of these license terms, and understand the
 freedoms and responsabilities that he or she has by using this source/core.
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

| Port name | Direction | Type   | Description                  |
| --------- | --------- | ------ | ---------------------------- |
| clk       | input     |        | used to clk filter */        |
| reset     | input     |        | used to reset filter */      |
| data_in   | input     |        | input data to be filtered */ |
| data_out  | output    | [15:0] | filtered output */           |
| data_en   | output    |        |                              |
| dec_rate  | input     | [15:0] |                              |
## Signals

| Name       | Type        | Description                           |
| ---------- | ----------- | ------------------------------------- |
| data_int   | reg [36:0]  | Data is read on positive clk edge */  |
| acc1       | reg [36:0]  |                                       |
| acc2       | reg [36:0]  |                                       |
| acc3       | reg [36:0]  |                                       |
| acc3_d     | reg [36:0]  |                                       |
| diff1_d    | reg [36:0]  |                                       |
| diff2_d    | reg [36:0]  |                                       |
| word_count | reg [15:0]  |                                       |
| word_en    | reg         |                                       |
| enable     | reg         |                                       |
| acc1_s     | wire [36:0] |                                       |
| acc2_s     | wire [36:0] |                                       |
| acc3_s     | wire [36:0] |                                       |
| diff1_s    | wire [36:0] |                                       |
| diff2_s    | wire [36:0] |                                       |
| diff3_s    | wire [36:0] |                                       |
## Processes
- unnamed: ( @(data_in) )
**Description**
Perform the Sinc action */

- unnamed: ( @(negedge clk) )
**Description**
Accumulator (Integrator) Perform the accumulation (IIR) at the speed of
   * the modulator. Z = one sample delay MCLKOUT = modulators conversion
   * bit rate */

- unnamed: ( @(posedge clk) )
**Description**
decimation stage (MCLKOUT/WORD_CLK) */

- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
**Description**
Differentiator (including decimation stage)
   * Perform the differentiation stage (FIR) at a lower speed.
   * Z = one sample delay WORD_EN = output word rate */

- unnamed: ( @(posedge clk) )
**Description**
Clock the Sinc output into an output register
   * WORD_EN = output word rate */

- unnamed: ( @(posedge clk) )
**Description**
Synchronize Data Output */

