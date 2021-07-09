# Entity: axi_adc_decimate

## Diagram

![Diagram](axi_adc_decimate.svg "Diagram")
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

| Port name           | Direction | Type   | Description   |
| ------------------- | --------- | ------ | ------------- |
| adc_clk             | input     |        |               |
| adc_rst             | input     |        |               |
| adc_data_a          | input     | [15:0] |               |
| adc_data_b          | input     | [15:0] |               |
| adc_valid_a         | input     |        |               |
| adc_valid_b         | input     |        |               |
| adc_dec_data_a      | output    | [15:0] |               |
| adc_dec_data_b      | output    | [15:0] |               |
| adc_dec_valid_a     | output    |        |               |
| adc_dec_valid_b     | output    |        |               |
| adc_data_rate       | output    | [ 2:0] |               |
| adc_oversampling_en | output    |        |               |
| s_axi_aclk          | input     |        | axi interface |
| s_axi_aresetn       | input     |        |               |
| s_axi_awvalid       | input     |        |               |
| s_axi_awaddr        | input     | [ 6:0] |               |
| s_axi_awprot        | input     | [ 2:0] |               |
| s_axi_awready       | output    |        |               |
| s_axi_wvalid        | input     |        |               |
| s_axi_wdata         | input     | [31:0] |               |
| s_axi_wstrb         | input     | [ 3:0] |               |
| s_axi_wready        | output    |        |               |
| s_axi_bvalid        | output    |        |               |
| s_axi_bresp         | output    | [ 1:0] |               |
| s_axi_bready        | input     |        |               |
| s_axi_arvalid       | input     |        |               |
| s_axi_araddr        | input     | [ 6:0] |               |
| s_axi_arprot        | input     | [ 2:0] |               |
| s_axi_arready       | output    |        |               |
| s_axi_rvalid        | output    |        |               |
| s_axi_rdata         | output    | [31:0] |               |
| s_axi_rresp         | output    | [ 1:0] |               |
| s_axi_rready        | input     |        |               |
## Signals

| Name                         | Type        | Description       |
| ---------------------------- | ----------- | ----------------- |
| up_clk                       | wire        | internal signals  |
| up_rstn                      | wire        |                   |
| up_waddr                     | wire [ 4:0] |                   |
| up_wdata                     | wire [31:0] |                   |
| up_wack                      | wire        |                   |
| up_wreq                      | wire        |                   |
| up_rack                      | wire        |                   |
| up_rdata                     | wire [31:0] |                   |
| up_rreq                      | wire        |                   |
| up_raddr                     | wire [ 4:0] |                   |
| decimation_ratio             | wire [31:0] |                   |
| filter_mask                  | wire [ 2:0] |                   |
| adc_correction_enable_a      | wire        |                   |
| adc_correction_enable_b      | wire        |                   |
| adc_correction_coefficient_a | wire [15:0] |                   |
| adc_correction_coefficient_b | wire [15:0] |                   |
## Instantiations

- axi_adc_decimate_filter: axi_adc_decimate_filter
- axi_adc_decimate_reg: axi_adc_decimate_reg
- i_up_axi: up_axi
