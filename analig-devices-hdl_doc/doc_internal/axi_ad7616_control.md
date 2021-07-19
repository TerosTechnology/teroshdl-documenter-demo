# Entity: axi_ad7616_control

- **File**: axi_ad7616_control.v
## Diagram

![Diagram](axi_ad7616_control.svg "Diagram")
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
| ID           |      | 0     |             |
| IF_TYPE      |      | 0     |             |
## Ports

| Port name       | Direction | Type   | Description     |
| --------------- | --------- | ------ | --------------- |
| cnvst           | output    |        | control signals |
| busy            | input     |        |                 |
| up_read_data    | input     | [15:0] |                 |
| up_read_valid   | input     |        |                 |
| up_write_data   | output    | [15:0] |                 |
| up_read_req     | output    |        |                 |
| up_write_req    | output    |        |                 |
| up_burst_length | output    | [ 4:0] |                 |
| end_of_conv     | output    |        |                 |
| up_rstn         | input     |        | bus interface   |
| up_clk          | input     |        |                 |
| up_wreq         | input     |        |                 |
| up_waddr        | input     | [13:0] |                 |
| up_wdata        | input     | [31:0] |                 |
| up_wack         | output    |        |                 |
| up_rreq         | input     |        |                 |
| up_raddr        | input     | [13:0] |                 |
| up_rdata        | output    | [31:0] |                 |
| up_rack         | output    |        |                 |
## Signals

| Name            | Type           | Description       |
| --------------- | -------------- | ----------------- |
| up_scratch      | reg     [31:0] | internal signals  |
| up_resetn       | reg            |                   |
| up_cnvst_en     | reg            |                   |
| up_conv_rate    | reg     [31:0] |                   |
| cnvst_counter   | reg     [31:0] |                   |
| pulse_counter   | reg     [ 3:0] |                   |
| cnvst_buf       | reg            |                   |
| cnvst_pulse     | reg            |                   |
| chsel_ff        | reg     [ 2:0] |                   |
| up_rst          | wire           |                   |
| up_rack_s       | wire           |                   |
| up_read_data_s  | wire [31:0]    |                   |
| up_read_valid_s | wire           |                   |
## Constants

| Name          | Type | Value      | Description |
| ------------- | ---- | ---------- | ----------- |
| PCORE_VERSION |      | 'h00001002 |             |
| POS_EDGE      |      | 0          |             |
| NEG_EDGE      |      | 1          |             |
| SERIAL        |      | 0          |             |
| PARALLEL      |      | 1          |             |
## Processes
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
**Description**
processor write interface

- unnamed: ( @(negedge up_rstn or posedge up_clk) )
- unnamed: ( @(posedge up_clk) )
**Description**
convertion start generator
NOTE: + The minimum convertion cycle is 1 us
+ The rate of the cnvst must be defined in a way,
to not lose any data. cnvst_rate >= t_conversion + t_aquisition
See the AD7616 datasheet for more information.

- unnamed: ( @(cnvst_counter, up_conv_rate) )
- unnamed: ( @(posedge up_clk) )
## Instantiations

- i_ad_edge_detect: ad_edge_detect
