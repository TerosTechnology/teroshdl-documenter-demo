# Entity: axi_hdmi_tx

## Diagram

![Diagram](axi_hdmi_tx.svg "Diagram")
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

| Generic name     | Type | Value    | Description |
| ---------------- | ---- | -------- | ----------- |
| ID               |      | 0        |             |
| CR_CB_N          |      | 0        |             |
| FPGA_TECHNOLOGY  |      | 0        |             |
| INTERFACE        |      | "16_BIT" |             |
| OUT_CLK_POLARITY |      | 0        |             |
## Ports

| Port name         | Direction | Type   | Description      |
| ----------------- | --------- | ------ | ---------------- |
| hdmi_clk          | input     |        | hdmi interface   |
| hdmi_out_clk      | output    |        |                  |
| hdmi_16_hsync     | output    |        | 16-bit interface |
| hdmi_16_vsync     | output    |        |                  |
| hdmi_16_data_e    | output    |        |                  |
| hdmi_16_data      | output    | [15:0] |                  |
| hdmi_16_es_data   | output    | [15:0] |                  |
| hdmi_24_hsync     | output    |        | 24-bit interface |
| hdmi_24_vsync     | output    |        |                  |
| hdmi_24_data_e    | output    |        |                  |
| hdmi_24_data      | output    | [23:0] |                  |
| hdmi_36_hsync     | output    |        | 36-bit interface |
| hdmi_36_vsync     | output    |        |                  |
| hdmi_36_data_e    | output    |        |                  |
| hdmi_36_data      | output    | [35:0] |                  |
| vdma_clk          | input     |        | vdma interface   |
| vdma_end_of_frame | input     |        |                  |
| vdma_valid        | input     |        |                  |
| vdma_data         | input     | [63:0] |                  |
| vdma_ready        | output    |        |                  |
| s_axi_aclk        | input     |        | axi interface    |
| s_axi_aresetn     | input     |        |                  |
| s_axi_awvalid     | input     |        |                  |
| s_axi_awaddr      | input     | [15:0] |                  |
| s_axi_awprot      | input     | [ 2:0] |                  |
| s_axi_awready     | output    |        |                  |
| s_axi_wvalid      | input     |        |                  |
| s_axi_wdata       | input     | [31:0] |                  |
| s_axi_wstrb       | input     | [ 3:0] |                  |
| s_axi_wready      | output    |        |                  |
| s_axi_bvalid      | output    |        |                  |
| s_axi_bresp       | output    | [ 1:0] |                  |
| s_axi_bready      | input     |        |                  |
| s_axi_arvalid     | input     |        |                  |
| s_axi_araddr      | input     | [15:0] |                  |
| s_axi_arprot      | input     | [ 2:0] |                  |
| s_axi_arready     | output    |        |                  |
| s_axi_rvalid      | output    |        |                  |
| s_axi_rresp       | output    | [ 1:0] |                  |
| s_axi_rdata       | output    | [31:0] |                  |
| s_axi_rready      | input     |        |                  |
## Signals

| Name                 | Type        | Description       |
| -------------------- | ----------- | ----------------- |
| up_rstn              | wire        | reset and clocks  |
| up_clk               | wire        |                   |
| hdmi_rst             | wire        |                   |
| vdma_rst             | wire        |                   |
| up_wreq_s            | wire        | internal signals  |
| up_waddr_s           | wire [13:0] |                   |
| up_wdata_s           | wire [31:0] |                   |
| up_wack_s            | wire        |                   |
| up_rreq_s            | wire        |                   |
| up_raddr_s           | wire [13:0] |                   |
| up_rdata_s           | wire [31:0] |                   |
| up_rack_s            | wire        |                   |
| hdmi_csc_bypass_s    | wire        |                   |
| hdmi_ss_bypass_s     | wire        |                   |
| hdmi_srcsel_s        | wire [ 1:0] |                   |
| hdmi_const_rgb_s     | wire [23:0] |                   |
| hdmi_hl_active_s     | wire [15:0] |                   |
| hdmi_hl_width_s      | wire [15:0] |                   |
| hdmi_hs_width_s      | wire [15:0] |                   |
| hdmi_he_max_s        | wire [15:0] |                   |
| hdmi_he_min_s        | wire [15:0] |                   |
| hdmi_vf_active_s     | wire [15:0] |                   |
| hdmi_vf_width_s      | wire [15:0] |                   |
| hdmi_vs_width_s      | wire [15:0] |                   |
| hdmi_ve_max_s        | wire [15:0] |                   |
| hdmi_ve_min_s        | wire [15:0] |                   |
| hdmi_clip_max_s      | wire [23:0] |                   |
| hdmi_clip_min_s      | wire [23:0] |                   |
| hdmi_fs_toggle_s     | wire        |                   |
| hdmi_raddr_g_s       | wire [ 8:0] |                   |
| hdmi_tpm_oos_s       | wire        |                   |
| hdmi_status_s        | wire        |                   |
| vdma_wr_s            | wire        |                   |
| vdma_waddr_s         | wire [ 8:0] |                   |
| vdma_wdata_s         | wire [47:0] |                   |
| vdma_fs_ret_toggle_s | wire        |                   |
| vdma_fs_waddr_s      | wire [ 8:0] |                   |
| vdma_ovf_s           | wire        |                   |
| vdma_unf_s           | wire        |                   |
| vdma_tpm_oos_s       | wire        |                   |
## Constants

| Name              | Type | Value     | Description                                               |
| ----------------- | ---- | --------- | --------------------------------------------------------- |
| EMBEDDED_SYNC     |      | undefined | 0 = Launch on rising edge, 1 = Launch on falling edge */  |
| XILINX_7SERIES    |      | 1         |                                                           |
| XILINX_ULTRASCALE |      | 2         |                                                           |
| INTEL_5SERIES     |      | 101       |                                                           |
## Instantiations

- i_up_axi: up_axi
**Description**
axi interface

- i_up: up_hdmi_tx
**Description**
processor interface

- i_vdma: axi_hdmi_tx_vdma
**Description**
vdma interface

- i_tx_core: axi_hdmi_tx_core
**Description**
hdmi interface

