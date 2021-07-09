# Entity: axi_ad9122

## Diagram

![Diagram](axi_ad9122.svg "Diagram")
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

| Generic name            | Type | Value                | Description |
| ----------------------- | ---- | -------------------- | ----------- |
| ID                      |      | 0                    |             |
| FPGA_TECHNOLOGY         |      | 0                    |             |
| FPGA_FAMILY             |      | 0                    |             |
| SPEED_GRADE             |      | 0                    |             |
| DEV_PACKAGE             |      | 0                    |             |
| SERDES_OR_DDR_N         |      | 1                    |             |
| MMCM_OR_BUFIO_N         |      | 1                    |             |
| MMCM_CLKIN_PERIOD       |      | 1.667                |             |
| MMCM_VCO_DIV            |      | 2                    |             |
| MMCM_VCO_MUL            |      | 4                    |             |
| MMCM_CLK0_DIV           |      | 2                    |             |
| MMCM_CLK1_DIV           |      | 8                    |             |
| DAC_DATAPATH_DISABLE    |      | 0                    |             |
| DAC_DDS_TYPE            |      | 1                    |             |
| DAC_DDS_CORDIC_DW       |      | 20                   |             |
| DAC_DDS_CORDIC_PHASE_DW |      | 18                   |             |
| IO_DELAY_GROUP          |      | "dev_if_delay_group" |             |
## Ports

| Port name       | Direction | Type   | Description   |
| --------------- | --------- | ------ | ------------- |
| dac_clk_in_p    | input     |        | dac interface |
| dac_clk_in_n    | input     |        |               |
| dac_clk_out_p   | output    |        |               |
| dac_clk_out_n   | output    |        |               |
| dac_frame_out_p | output    |        |               |
| dac_frame_out_n | output    |        |               |
| dac_data_out_p  | output    | [15:0] |               |
| dac_data_out_n  | output    | [15:0] |               |
| dac_sync_out    | output    |        | master/slave  |
| dac_sync_in     | input     |        |               |
| dac_div_clk     | output    |        | dma interface |
| dac_valid_0     | output    |        |               |
| dac_enable_0    | output    |        |               |
| dac_ddata_0     | input     | [63:0] |               |
| dac_valid_1     | output    |        |               |
| dac_enable_1    | output    |        |               |
| dac_ddata_1     | input     | [63:0] |               |
| dac_dunf        | input     |        |               |
| s_axi_aclk      | input     |        | axi interface |
| s_axi_aresetn   | input     |        |               |
| s_axi_awvalid   | input     |        |               |
| s_axi_awaddr    | input     | [15:0] |               |
| s_axi_awready   | output    |        |               |
| s_axi_wvalid    | input     |        |               |
| s_axi_wdata     | input     | [31:0] |               |
| s_axi_wstrb     | input     | [ 3:0] |               |
| s_axi_wready    | output    |        |               |
| s_axi_bvalid    | output    |        |               |
| s_axi_bresp     | output    | [ 1:0] |               |
| s_axi_bready    | input     |        |               |
| s_axi_arvalid   | input     |        |               |
| s_axi_araddr    | input     | [15:0] |               |
| s_axi_arready   | output    |        |               |
| s_axi_rvalid    | output    |        |               |
| s_axi_rdata     | output    | [31:0] |               |
| s_axi_rresp     | output    | [ 1:0] |               |
| s_axi_rready    | input     |        |               |
| s_axi_awprot    | input     | [ 2:0] |               |
| s_axi_arprot    | input     | [ 2:0] |               |
## Signals

| Name            | Type        | Description                 |
| --------------- | ----------- | --------------------------- |
| dac_rst         | wire        | internal clocks and resets  |
| mmcm_rst        | wire        |                             |
| up_clk          | wire        |                             |
| up_rstn         | wire        |                             |
| dac_frame_i0_s  | wire        | internal signals            |
| dac_data_i0_s   | wire [15:0] |                             |
| dac_frame_i1_s  | wire        |                             |
| dac_data_i1_s   | wire [15:0] |                             |
| dac_frame_i2_s  | wire        |                             |
| dac_data_i2_s   | wire [15:0] |                             |
| dac_frame_i3_s  | wire        |                             |
| dac_data_i3_s   | wire [15:0] |                             |
| dac_frame_q0_s  | wire        |                             |
| dac_data_q0_s   | wire [15:0] |                             |
| dac_frame_q1_s  | wire        |                             |
| dac_data_q1_s   | wire [15:0] |                             |
| dac_frame_q2_s  | wire        |                             |
| dac_data_q2_s   | wire [15:0] |                             |
| dac_frame_q3_s  | wire        |                             |
| dac_data_q3_s   | wire [15:0] |                             |
| dac_status_s    | wire        |                             |
| up_drp_sel_s    | wire        |                             |
| up_drp_wr_s     | wire        |                             |
| up_drp_addr_s   | wire [11:0] |                             |
| up_drp_wdata_s  | wire [31:0] |                             |
| up_drp_rdata_s  | wire [31:0] |                             |
| up_drp_ready_s  | wire        |                             |
| up_drp_locked_s | wire        |                             |
| up_wreq_s       | wire        |                             |
| up_waddr_s      | wire [13:0] |                             |
| up_wdata_s      | wire [31:0] |                             |
| up_wack_s       | wire        |                             |
| up_rreq_s       | wire        |                             |
| up_raddr_s      | wire [13:0] |                             |
| up_rdata_s      | wire [31:0] |                             |
| up_rack_s       | wire        |                             |
## Instantiations

- i_if: axi_ad9122_if
**Description**
device interface

- i_core: axi_ad9122_core
**Description**
core

- i_up_axi: up_axi
**Description**
up bus interface

