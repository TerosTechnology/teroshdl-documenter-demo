# Entity: axi_dac_interpolate

## Diagram

![Diagram](axi_dac_interpolate.svg "Diagram")
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

| Generic name       | Type | Value | Description |
| ------------------ | ---- | ----- | ----------- |
| CORRECTION_DISABLE |      | 1     |             |
## Ports

| Port name        | Direction | Type   | Description   |
| ---------------- | --------- | ------ | ------------- |
| dac_clk          | input     |        |               |
| dac_rst          | input     |        |               |
| dac_data_a       | input     | [15:0] |               |
| dac_data_b       | input     | [15:0] |               |
| dac_valid_a      | input     |        |               |
| dac_valid_b      | input     |        |               |
| dma_valid_a      | input     |        |               |
| dma_valid_b      | input     |        |               |
| dma_ready_a      | output    |        |               |
| dma_ready_b      | output    |        |               |
| dac_enable_a     | input     |        |               |
| dac_enable_b     | input     |        |               |
| dac_int_data_a   | output    | [15:0] |               |
| dac_int_data_b   | output    | [15:0] |               |
| dac_valid_out_a  | output    |        |               |
| dac_valid_out_b  | output    |        |               |
| hold_last_sample | output    |        |               |
| underflow        | output    |        |               |
| trigger_i        | input     | [ 1:0] |               |
| trigger_adc      | input     |        |               |
| trigger_la       | input     |        |               |
| s_axi_aclk       | input     |        | axi interface |
| s_axi_aresetn    | input     |        |               |
| s_axi_awvalid    | input     |        |               |
| s_axi_awaddr     | input     | [ 6:0] |               |
| s_axi_awprot     | input     | [ 2:0] |               |
| s_axi_awready    | output    |        |               |
| s_axi_wvalid     | input     |        |               |
| s_axi_wdata      | input     | [31:0] |               |
| s_axi_wstrb      | input     | [ 3:0] |               |
| s_axi_wready     | output    |        |               |
| s_axi_bvalid     | output    |        |               |
| s_axi_bresp      | output    | [ 1:0] |               |
| s_axi_bready     | input     |        |               |
| s_axi_arvalid    | input     |        |               |
| s_axi_araddr     | input     | [ 6:0] |               |
| s_axi_arprot     | input     | [ 2:0] |               |
| s_axi_arready    | output    |        |               |
| s_axi_rvalid     | output    |        |               |
| s_axi_rdata      | output    | [31:0] |               |
| s_axi_rresp      | output    | [ 1:0] |               |
| s_axi_rready     | input     |        |               |
## Signals

| Name                         | Type          | Description       |
| ---------------------------- | ------------- | ----------------- |
| trigger_i_m1                 | reg    [ 1:0] |                   |
| trigger_i_m2                 | reg    [ 1:0] |                   |
| trigger_i_m3                 | reg    [ 1:0] |                   |
| trigger_adc_m1               | reg           |                   |
| trigger_adc_m2               | reg           |                   |
| trigger_adc_m3               | reg           |                   |
| trigger_la_m1                | reg           |                   |
| trigger_la_m2                | reg           |                   |
| trigger_la_m3                | reg           |                   |
| any_edge_trigger             | reg    [ 1:0] |                   |
| rise_edge_trigger            | reg    [ 1:0] |                   |
| fall_edge_trigger            | reg    [ 1:0] |                   |
| high_level_trigger           | reg    [ 1:0] |                   |
| low_level_trigger            | reg    [ 1:0] |                   |
| up_clk                       | wire          | internal signals  |
| up_rstn                      | wire          |                   |
| up_waddr                     | wire [ 4:0]   |                   |
| up_wdata                     | wire [31:0]   |                   |
| up_wack                      | wire          |                   |
| up_wreq                      | wire          |                   |
| up_rack                      | wire          |                   |
| up_rdata                     | wire [31:0]   |                   |
| up_rreq                      | wire          |                   |
| up_raddr                     | wire [ 4:0]   |                   |
| interpolation_ratio_a        | wire [31:0]   |                   |
| interpolation_ratio_b        | wire [31:0]   |                   |
| filter_mask_a                | wire [ 2:0]   |                   |
| filter_mask_b                | wire [ 2:0]   |                   |
| dma_transfer_suspend         | wire          |                   |
| start_sync_channels          | wire          |                   |
| dac_correction_enable_a      | wire          |                   |
| dac_correction_enable_b      | wire          |                   |
| dac_correction_coefficient_a | wire [15:0]   |                   |
| dac_correction_coefficient_b | wire [15:0]   |                   |
| trigger_config               | wire [19:0]   |                   |
| en_start_trigger             | wire          |                   |
| en_stop_trigger              | wire          |                   |
| en_trigger_pins              | wire [ 1:0]   |                   |
| en_trigger_adc               | wire          |                   |
| en_trigger_la                | wire          |                   |
| low_level                    | wire [ 1:0]   |                   |
| high_level                   | wire [ 1:0]   |                   |
| any_edge                     | wire [ 1:0]   |                   |
| rise_edge                    | wire [ 1:0]   |                   |
| fall_edge                    | wire [ 1:0]   |                   |
| trigger_active               | wire          |                   |
| trigger                      | wire          |                   |
| ext_trigger                  | wire          |                   |
| underflow_a                  | wire          |                   |
| underflow_b                  | wire          |                   |
| lsample_hold_config          | wire [ 1:0]   |                   |
| sync_stop_channels           | wire          |                   |
## Processes
- unnamed: ( @(posedge dac_clk) )
**Description**
sync

- unnamed: ( @(posedge dac_clk) )
## Instantiations

- i_filter_a: axi_dac_interpolate_filter
- i_filter_b: axi_dac_interpolate_filter
- axi_dac_interpolate_reg_inst: axi_dac_interpolate_reg
- i_up_axi: up_axi
