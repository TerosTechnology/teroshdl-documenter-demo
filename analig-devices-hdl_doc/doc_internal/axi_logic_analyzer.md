# Entity: axi_logic_analyzer

- **File**: axi_logic_analyzer.v
## Diagram

![Diagram](axi_logic_analyzer.svg "Diagram")
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

| Port name              | Direction | Type   | Description    |
| ---------------------- | --------- | ------ | -------------- |
| clk                    | input     |        |  interface     |
| clk_out                | output    |        |                |
| data_i                 | input     | [15:0] |                |
| data_o                 | output    | [15:0] |                |
| data_t                 | output    | [15:0] |                |
| trigger_i              | input     | [ 1:0] |                |
| adc_valid              | output    |        |                |
| adc_data               | output    | [15:0] |                |
| dac_data               | input     | [15:0] |                |
| dac_valid              | input     |        |                |
| dac_read               | output    |        |                |
| external_rate          | input     | [ 2:0] |                |
| external_valid         | input     |        |                |
| external_decimation_en | input     |        |                |
| trigger_in             | input     |        |                |
| trigger_out            | output    |        |                |
| trigger_out_adc        | output    |        |                |
| fifo_depth             | output    | [31:0] |                |
| s_axi_aclk             | input     |        |  axi interface |
| s_axi_aresetn          | input     |        |                |
| s_axi_awvalid          | input     |        |                |
| s_axi_awaddr           | input     | [ 6:0] |                |
| s_axi_awprot           | input     | [ 2:0] |                |
| s_axi_awready          | output    |        |                |
| s_axi_wvalid           | input     |        |                |
| s_axi_wdata            | input     | [31:0] |                |
| s_axi_wstrb            | input     | [ 3:0] |                |
| s_axi_wready           | output    |        |                |
| s_axi_bvalid           | output    |        |                |
| s_axi_bresp            | output    | [ 1:0] |                |
| s_axi_bready           | input     |        |                |
| s_axi_arvalid          | input     |        |                |
| s_axi_araddr           | input     | [ 6:0] |                |
| s_axi_arprot           | input     | [ 2:0] |                |
| s_axi_arready          | output    |        |                |
| s_axi_rvalid           | output    |        |                |
| s_axi_rdata            | output    | [31:0] |                |
| s_axi_rresp            | output    | [ 1:0] |                |
| s_axi_rready           | input     |        |                |
## Signals

| Name                    | Type           | Description                    |
| ----------------------- | -------------- | ------------------------------ |
| data_r                  | reg     [15:0] |  internal registers            |
| trigger_m1              | reg     [ 1:0] |                                |
| downsampler_counter_la  | reg     [31:0] |                                |
| upsampler_counter_pg    | reg     [31:0] |                                |
| sample_valid_la         | reg            |                                |
| io_selection            | reg     [15:0] | 1 - input, 0 - output          |
| delay_counter           | reg     [31:0] |                                |
| triggered               | reg            |                                |
| up_triggered            | reg            |                                |
| up_triggered_d1         | reg            |                                |
| up_triggered_d2         | reg            |                                |
| up_triggered_set        | reg            |                                |
| up_triggered_reset      | reg            |                                |
| up_triggered_reset_d1   | reg            |                                |
| up_triggered_reset_d2   | reg            |                                |
| streaming_on            | reg            |                                |
| trigger_i_m1            | reg    [ 1:0]  |                                |
| trigger_i_m2            | reg    [ 1:0]  |                                |
| trigger_i_m3            | reg    [ 1:0]  |                                |
| trigger_adc_m1          | reg            |                                |
| trigger_adc_m2          | reg            |                                |
| trigger_la_m2           | reg            |                                |
| pg_trigered             | reg            |                                |
| any_edge_trigger        | reg    [ 1:0]  |                                |
| rise_edge_trigger       | reg    [ 1:0]  |                                |
| fall_edge_trigger       | reg    [ 1:0]  |                                |
| high_level_trigger      | reg    [ 1:0]  |                                |
| low_level_trigger       | reg    [ 1:0]  |                                |
| trigger_holdoff_counter | reg    [31:0]  |                                |
| adc_data_delay          | reg    [ 3:0]  |                                |
| data_fixed_delay        | reg    [16:0]  |                                |
| data_dynamic_delay      | reg    [15:0]  |                                |
| up_clk                  | wire           |  internal signals              |
| up_rstn                 | wire           |                                |
| up_waddr                | wire [ 4:0]    |                                |
| up_wdata                | wire [31:0]    |                                |
| up_wack                 | wire           |                                |
| up_wreq                 | wire           |                                |
| up_rack                 | wire           |                                |
| up_rdata                | wire [31:0]    |                                |
| up_rreq                 | wire           |                                |
| up_raddr                | wire [ 4:0]    |                                |
| reset                   | wire           |                                |
| divider_counter_la      | wire [31:0]    |                                |
| divider_counter_pg      | wire [31:0]    |                                |
| edge_detect_enable      | wire [17:0]    |                                |
| rise_edge_enable        | wire [17:0]    |                                |
| fall_edge_enable        | wire [17:0]    |                                |
| low_level_enable        | wire [17:0]    |                                |
| high_level_enable       | wire [17:0]    |                                |
| trigger_logic           | wire [ 6:0]    | 0-OR,1-AND                     |
| clock_select            | wire           |                                |
| overwrite_enable        | wire [15:0]    |                                |
| overwrite_data          | wire [15:0]    |                                |
| io_selection_s          | wire [15:0]    | 1 - input, 0 - output          |
| od_pp_n                 | wire [15:0]    | 0 - push/pull, 1 - open drain  |
| trigger_out_s           | wire           |                                |
| trigger_delay           | wire [31:0]    |                                |
| trigger_out_delayed     | wire           |                                |
| pg_trigger_config       | wire [19:0]    |                                |
| pg_en_trigger_pins      | wire [ 1:0]    |                                |
| pg_en_trigger_adc       | wire           |                                |
| pg_en_trigger_la        | wire           |                                |
| pg_low_level            | wire [ 1:0]    |                                |
| pg_high_level           | wire [ 1:0]    |                                |
| pg_any_edge             | wire [ 1:0]    |                                |
| pg_rise_edge            | wire [ 1:0]    |                                |
| pg_fall_edge            | wire [ 1:0]    |                                |
| trigger_holdoff         | wire [31:0]    |                                |
| trigger_out_holdoff     | wire           |                                |
| streaming               | wire           |                                |
| in_data_delay           | wire [ 3:0]    |                                |
| up_data_delay           | wire [ 3:0]    |                                |
| master_delay_ctrl       | wire           |                                |
| data_delay_control      | wire [ 9:0]    |                                |
| adc_data_mn             | wire [15:0]    |                                |
## Processes
- unnamed: ( @(posedge clk_out) )
  - **Type:** always
- unnamed: ( @(posedge clk_out) )
  - **Type:** always
- unnamed: ( @(posedge up_clk) )
  - **Type:** always
- unnamed: ( @(posedge clk_out) )
  - **Type:** always
**Description**
 adc path 'rate delay' given by axi_adc_decimate 
- unnamed: ( @(posedge clk_out) )
  - **Type:** always
- unnamed: ( @(posedge clk_out) )
  - **Type:** always
- unnamed: ( @(posedge clk_out) )
  - **Type:** always
**Description**
 downsampler logic analyzer 
- unnamed: ( @(posedge clk) )
  - **Type:** always
**Description**
 sync 
- unnamed: ( @(posedge clk) )
  - **Type:** always
- unnamed: ( @(posedge clk_out) )
  - **Type:** always
**Description**
 upsampler pattern generator 
- unnamed: ( @(posedge clk_out) )
  - **Type:** always
- unnamed: ( @(posedge clk) )
  - **Type:** always
## Instantiations

- BUFGMUX_CTRL_inst: BUFGMUX_CTRL
- i_trigger: axi_logic_analyzer_trigger
- i_registers: axi_logic_analyzer_reg
- i_up_axi: up_axi
**Description**
 axi interface

