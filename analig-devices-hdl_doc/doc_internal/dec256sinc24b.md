# Entity: dec256sinc24b

## Diagram

![Diagram](dec256sinc24b.svg "Diagram")
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

| Port name  | Direction | Type   | Description                        |
| ---------- | --------- | ------ | ---------------------------------- |
| reset_i    | input     |        |                                    |
| mclkout_i  | input     |        |                                    |
| mdata_i    | input     |        |                                    |
| data_rdy_o | output    |        | signals when new data is available |
| data_o     | output    | [15:0] | outputs filtered data              |
## Signals

| Name       | Type       | Description |
| ---------- | ---------- | ----------- |
| ip_data1   | reg [23:0] |             |
| acc1       | reg [23:0] |             |
| acc2       | reg [23:0] |             |
| acc3       | reg [23:0] |             |
| acc3_d1    | reg [23:0] |             |
| acc3_d2    | reg [23:0] |             |
| diff1      | reg [23:0] |             |
| diff2      | reg [23:0] |             |
| diff3      | reg [23:0] |             |
| diff1_d    | reg [23:0] |             |
| diff2_d    | reg [23:0] |             |
| word_count | reg [7:0]  |             |
| word_clk   | reg        |             |
## Processes
- unnamed: ( @(mdata_i) )
**Description**
Perform the Sinc ACTION */

- unnamed: ( @(negedge mclkout_i or posedge reset_i) )
- unnamed: ( @(posedge mclkout_i or posedge reset_i ) )
- unnamed: ( @(word_count) )
- unnamed: ( @(posedge word_clk or posedge reset_i) )
- unnamed: ( @(posedge word_clk) )
**Description**
Clock the Sinc output into an output register
    Clocking Sinc Output into an Output Register
WORD_CLK = output word rate */

