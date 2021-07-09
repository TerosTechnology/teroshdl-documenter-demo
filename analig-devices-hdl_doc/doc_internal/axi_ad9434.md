# Entity: axi_ad9434

## Diagram

![Diagram](axi_ad9434.svg "Diagram")
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

| Generic name    | Type | Value                | Description |
| --------------- | ---- | -------------------- | ----------- |
| ID              |      | 0                    |             |
| FPGA_TECHNOLOGY |      | 0                    |             |
| FPGA_FAMILY     |      | 0                    |             |
| SPEED_GRADE     |      | 0                    |             |
| DEV_PACKAGE     |      | 0                    |             |
| IO_DELAY_GROUP  |      | "dev_if_delay_group" |             |
## Ports

| Port name     | Direction | Type   | Description        |
| ------------- | --------- | ------ | ------------------ |
| adc_clk_in_p  | input     |        | physical interface |
| adc_clk_in_n  | input     |        |                    |
| adc_data_in_p | input     | [11:0] |                    |
| adc_data_in_n | input     | [11:0] |                    |
| adc_or_in_p   | input     |        |                    |
| adc_or_in_n   | input     |        |                    |
| delay_clk     | input     |        | delay interface    |
| adc_clk       | output    |        | dma interface      |
| adc_enable    | output    |        |                    |
| adc_valid     | output    |        |                    |
| adc_data      | output    | [63:0] |                    |
| adc_dovf      | input     |        |                    |
| s_axi_aclk    | input     |        | axi interface      |
| s_axi_aresetn | input     |        |                    |
| s_axi_awvalid | input     |        |                    |
| s_axi_awaddr  | input     | [15:0] |                    |
| s_axi_awready | output    |        |                    |
| s_axi_wvalid  | input     |        |                    |
| s_axi_wdata   | input     | [31:0] |                    |
| s_axi_wstrb   | input     | [ 3:0] |                    |
| s_axi_wready  | output    |        |                    |
| s_axi_bvalid  | output    |        |                    |
| s_axi_bresp   | output    | [ 1:0] |                    |
| s_axi_bready  | input     |        |                    |
| s_axi_arvalid | input     |        |                    |
| s_axi_araddr  | input     | [15:0] |                    |
| s_axi_arready | output    |        |                    |
| s_axi_rvalid  | output    |        |                    |
| s_axi_rresp   | output    | [ 1:0] |                    |
| s_axi_rdata   | output    | [31:0] |                    |
| s_axi_rready  | input     |        |                    |
| s_axi_awprot  | input     | [ 2:0] |                    |
| s_axi_arprot  | input     | [ 2:0] |                    |
## Signals

| Name               | Type        | Description               |
| ------------------ | ----------- | ------------------------- |
| adc_rst            | wire        | internal clocks & resets  |
| up_rstn            | wire        |                           |
| mmcm_rst           | wire        |                           |
| up_clk             | wire        |                           |
| up_wreq_s          | wire        | internal signals          |
| up_rreq_s          | wire        |                           |
| up_waddr_s         | wire [13:0] |                           |
| up_raddr_s         | wire [13:0] |                           |
| up_wdata_s         | wire [31:0] |                           |
| up_rdata_s         | wire [31:0] |                           |
| up_wack_s          | wire        |                           |
| up_rack_s          | wire        |                           |
| up_status_pn_err_s | wire [ 1:0] |                           |
| up_status_pn_oos_s | wire [ 1:0] |                           |
| up_status_or_s     | wire [ 1:0] |                           |
| adc_status_s       | wire        |                           |
| up_dld_s           | wire [12:0] |                           |
| up_dwdata_s        | wire [64:0] |                           |
| up_drdata_s        | wire [64:0] |                           |
| delay_clk_s        | wire        |                           |
| delay_rst          | wire        |                           |
| delay_locked_s     | wire        |                           |
| up_drp_sel_s       | wire        |                           |
| up_drp_wr_s        | wire        |                           |
| up_drp_addr_s      | wire [11:0] |                           |
| up_drp_wdata_s     | wire [31:0] |                           |
| up_drp_rdata_s     | wire [31:0] |                           |
| up_drp_ready_s     | wire        |                           |
| up_drp_locked_s    | wire        |                           |
| adc_data_if_s      | wire [47:0] |                           |
| adc_or_if_s        | wire        |                           |
## Instantiations

- i_if: axi_ad9434_if
- i_core: axi_ad9434_core
**Description**
common processor control

- i_up_axi: up_axi
**Description**
up bus interface

