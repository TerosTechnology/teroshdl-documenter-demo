# Entity: axi_logic_analyzer_reg

## Diagram

![Diagram](axi_logic_analyzer_reg.svg "Diagram")
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

| Port name          | Direction | Type   | Description   |
| ------------------ | --------- | ------ | ------------- |
| clk                | input     |        |               |
| reset              | output    |        |               |
| divider_counter_la | output    | [31:0] |               |
| divider_counter_pg | output    | [31:0] |               |
| io_selection       | output    | [15:0] |               |
| edge_detect_enable | output    | [17:0] |               |
| rise_edge_enable   | output    | [17:0] |               |
| fall_edge_enable   | output    | [17:0] |               |
| low_level_enable   | output    | [17:0] |               |
| high_level_enable  | output    | [17:0] |               |
| fifo_depth         | output    | [31:0] |               |
| trigger_delay      | output    | [31:0] |               |
| trigger_logic      | output    | [ 6:0] |               |
| clock_select       | output    |        |               |
| overwrite_enable   | output    | [15:0] |               |
| overwrite_data     | output    | [15:0] |               |
| input_data         | input     | [15:0] |               |
| od_pp_n            | output    | [15:0] |               |
| trigger_holdoff    | output    | [31:0] |               |
| pg_trigger_config  | output    | [19:0] |               |
| triggered          | input     |        |               |
| streaming          | output    |        |               |
| data_delay_control | output    | [ 9:0] |               |
| up_rstn            | input     |        | bus interface |
| up_clk             | input     |        |               |
| up_wreq            | input     |        |               |
| up_waddr           | input     | [ 4:0] |               |
| up_wdata           | input     | [31:0] |               |
| up_wack            | output    |        |               |
| up_rreq            | input     |        |               |
| up_raddr           | input     | [ 4:0] |               |
| up_rdata           | output    | [31:0] |               |
| up_rack            | output    |        |               |
## Signals

| Name                  | Type           | Description         |
| --------------------- | -------------- | ------------------- |
| up_version            | reg     [31:0] | internal registers  |
| up_scratch            | reg     [31:0] |                     |
| up_divider_counter_la | reg     [31:0] |                     |
| up_divider_counter_pg | reg     [31:0] |                     |
| up_io_selection       | reg     [15:0] |                     |
| up_edge_detect_enable | reg     [17:0] |                     |
| up_rise_edge_enable   | reg     [17:0] |                     |
| up_fall_edge_enable   | reg     [17:0] |                     |
| up_low_level_enable   | reg     [17:0] |                     |
| up_high_level_enable  | reg     [17:0] |                     |
| up_fifo_depth         | reg     [31:0] |                     |
| up_trigger_delay      | reg     [31:0] |                     |
| up_trigger_logic      | reg     [ 6:0] |                     |
| up_clock_select       | reg            |                     |
| up_overwrite_enable   | reg     [15:0] |                     |
| up_overwrite_data     | reg     [15:0] |                     |
| up_od_pp_n            | reg     [15:0] |                     |
| up_trigger_holdoff    | reg     [31:0] |                     |
| up_pg_trigger_config  | reg     [19:0] |                     |
| up_triggered          | reg            |                     |
| up_streaming          | reg            |                     |
| up_data_delay_control | reg     [ 9:0] |                     |
| up_input_data         | wire [15:0]    |                     |
## Processes
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
**Description**
processor read interface

## Instantiations

- i_core_rst_reg: ad_rst
- i_xfer_cntrl: up_xfer_cntrl
- i_xfer_status: up_xfer_status
**Description**
10

