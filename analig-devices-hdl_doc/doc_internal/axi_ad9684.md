# Entity: axi_ad9684

## Diagram

![Diagram](axi_ad9684.svg "Diagram")
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
| OR_STATUS       |      | 1                    |             |
## Ports

| Port name     | Direction | Type   | Description               |
| ------------- | --------- | ------ | ------------------------- |
| adc_clk_in_p  | input     |        | device interface ports    |
| adc_clk_in_n  | input     |        |                           |
| adc_data_in_p | input     | [13:0] |                           |
| adc_data_in_n | input     | [13:0] |                           |
| adc_data_or_p | input     |        |                           |
| adc_data_or_n | input     |        |                           |
| adc_clk       | output    |        | dma interface ports       |
| adc_rst       | output    |        |                           |
| adc_valid_0   | output    |        |                           |
| adc_enable_0  | output    |        |                           |
| adc_data_0    | output    | [31:0] |                           |
| adc_valid_1   | output    |        |                           |
| adc_enable_1  | output    |        |                           |
| adc_data_1    | output    | [31:0] |                           |
| adc_dovf      | input     |        |                           |
| delay_clk     | input     |        | delay clock ports         |
| s_axi_aclk    | input     |        | axi slave interface ports |
| s_axi_aresetn | input     |        |                           |
| s_axi_awvalid | input     |        |                           |
| s_axi_awaddr  | input     | [15:0] |                           |
| s_axi_awprot  | input     | [ 2:0] |                           |
| s_axi_awready | output    |        |                           |
| s_axi_wvalid  | input     |        |                           |
| s_axi_wdata   | input     | [31:0] |                           |
| s_axi_wstrb   | input     | [ 3:0] |                           |
| s_axi_wready  | output    |        |                           |
| s_axi_bvalid  | output    |        |                           |
| s_axi_bresp   | output    | [ 1:0] |                           |
| s_axi_bready  | input     |        |                           |
| s_axi_arvalid | input     |        |                           |
| s_axi_araddr  | input     | [15:0] |                           |
| s_axi_arprot  | input     | [ 2:0] |                           |
| s_axi_arready | output    |        |                           |
| s_axi_rvalid  | output    |        |                           |
| s_axi_rresp   | output    | [ 1:0] |                           |
| s_axi_rdata   | output    | [31:0] |                           |
| s_axi_rready  | input     |        |                           |
## Signals

| Name               | Type           | Description               |
| ------------------ | -------------- | ------------------------- |
| up_wack            | reg            | internal registers        |
| up_rdata           | reg     [31:0] |                           |
| up_rack            | reg            |                           |
| up_clk             | wire           | internal clocks & resets  |
| up_rstn            | wire           |                           |
| delay_rst          | wire           |                           |
| adc_rawdata_s      | wire [55:0]    | internal signals          |
| adc_rawdata_0_s    | wire [27:0]    |                           |
| adc_rawdata_1_s    | wire [27:0]    |                           |
| adc_or_0_s         | wire           |                           |
| adc_or_1_s         | wire           |                           |
| adc_status_s       | wire           |                           |
| adc_or_s           | wire           |                           |
| up_dld_s           | wire [14:0]    |                           |
| up_dwdata_s        | wire [74:0]    |                           |
| up_drdata_s        | wire [74:0]    |                           |
| delay_locked_s     | wire           |                           |
| up_status_pn_err_s | wire           |                           |
| up_status_pn_oos_s | wire           |                           |
| up_status_or_s     | wire           |                           |
| up_adc_pn_err_s    | wire [ 1:0]    |                           |
| up_adc_pn_oos_s    | wire [ 1:0]    |                           |
| up_adc_or_s        | wire [ 1:0]    |                           |
| up_rreq_s          | wire           |                           |
| up_raddr_s         | wire [13:0]    |                           |
| up_rdata_s         | wire [31:0]    |                           |
| up_rack_s          | wire           |                           |
| up_wack_s          | wire           |                           |
| up_wreq_s          | wire           |                           |
| up_waddr_s         | wire [13:0]    |                           |
| up_wdata_s         | wire [31:0]    |                           |
| up_drp_sel_s       | wire           |                           |
| up_drp_wr_s        | wire           |                           |
| up_drp_addr_s      | wire [11:0]    |                           |
| up_drp_wdata_s     | wire [31:0]    |                           |
| up_drp_rdata_s     | wire [31:0]    |                           |
| up_drp_ready_s     | wire           |                           |
| up_drp_locked_s    | wire           |                           |
| rst_s              | wire           |                           |
## Processes
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
**Description**
processor read interface

## Instantiations

- i_ad9684_if: axi_ad9684_if
**Description**
device interface instance

- i_up_adc_common: up_adc_common
- i_channel_0: axi_ad9684_channel
**Description**
adc channel 0 instance

- i_channel_1: axi_ad9684_channel
**Description**
adc channel 1 instance

- i_delay_cntrl: up_delay_cntrl
**Description**
adc delay control instance

- i_up_axi: up_axi
**Description**
uP bus interface instance

