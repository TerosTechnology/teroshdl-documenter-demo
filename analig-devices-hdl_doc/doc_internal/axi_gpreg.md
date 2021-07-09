# Entity: axi_gpreg

## Diagram

![Diagram](axi_gpreg.svg "Diagram")
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

| Generic name    | Type    | Value | Description |
| --------------- | ------- | ----- | ----------- |
| ID              | integer | 0     |             |
| NUM_OF_IO       | integer | 8     |             |
| NUM_OF_CLK_MONS | integer | 8     |             |
| BUF_ENABLE_0    | integer | 1     |             |
| BUF_ENABLE_1    | integer | 1     |             |
| BUF_ENABLE_2    | integer | 1     |             |
| BUF_ENABLE_3    | integer | 1     |             |
| BUF_ENABLE_4    | integer | 1     |             |
| BUF_ENABLE_5    | integer | 1     |             |
| BUF_ENABLE_6    | integer | 1     |             |
| BUF_ENABLE_7    | integer | 1     |             |
## Ports

| Port name     | Direction | Type    | Description    |
| ------------- | --------- | ------- | -------------- |
| up_gp_ioenb_0 | output    | [ 31:0] | io             |
| up_gp_out_0   | output    | [ 31:0] |                |
| up_gp_in_0    | input     | [ 31:0] |                |
| up_gp_ioenb_1 | output    | [ 31:0] |                |
| up_gp_out_1   | output    | [ 31:0] |                |
| up_gp_in_1    | input     | [ 31:0] |                |
| up_gp_ioenb_2 | output    | [ 31:0] |                |
| up_gp_out_2   | output    | [ 31:0] |                |
| up_gp_in_2    | input     | [ 31:0] |                |
| up_gp_ioenb_3 | output    | [ 31:0] |                |
| up_gp_out_3   | output    | [ 31:0] |                |
| up_gp_in_3    | input     | [ 31:0] |                |
| up_gp_ioenb_4 | output    | [ 31:0] |                |
| up_gp_out_4   | output    | [ 31:0] |                |
| up_gp_in_4    | input     | [ 31:0] |                |
| up_gp_ioenb_5 | output    | [ 31:0] |                |
| up_gp_out_5   | output    | [ 31:0] |                |
| up_gp_in_5    | input     | [ 31:0] |                |
| up_gp_ioenb_6 | output    | [ 31:0] |                |
| up_gp_out_6   | output    | [ 31:0] |                |
| up_gp_in_6    | input     | [ 31:0] |                |
| up_gp_ioenb_7 | output    | [ 31:0] |                |
| up_gp_out_7   | output    | [ 31:0] |                |
| up_gp_in_7    | input     | [ 31:0] |                |
| d_clk_0       | input     |         | clock monitors |
| d_clk_1       | input     |         |                |
| d_clk_2       | input     |         |                |
| d_clk_3       | input     |         |                |
| d_clk_4       | input     |         |                |
| d_clk_5       | input     |         |                |
| d_clk_6       | input     |         |                |
| d_clk_7       | input     |         |                |
| s_axi_aclk    | input     |         | axi interface  |
| s_axi_aresetn | input     |         |                |
| s_axi_awvalid | input     |         |                |
| s_axi_awaddr  | input     | [ 15:0] |                |
| s_axi_awready | output    |         |                |
| s_axi_wvalid  | input     |         |                |
| s_axi_wdata   | input     | [ 31:0] |                |
| s_axi_wstrb   | input     | [  3:0] |                |
| s_axi_wready  | output    |         |                |
| s_axi_bvalid  | output    |         |                |
| s_axi_bresp   | output    | [  1:0] |                |
| s_axi_bready  | input     |         |                |
| s_axi_arvalid | input     |         |                |
| s_axi_araddr  | input     | [ 15:0] |                |
| s_axi_arready | output    |         |                |
| s_axi_rvalid  | output    |         |                |
| s_axi_rdata   | output    | [ 31:0] |                |
| s_axi_rresp   | output    | [  1:0] |                |
| s_axi_rready  | input     |         |                |
| s_axi_awprot  | input     | [ 2:0]  |                |
| s_axi_arprot  | input     | [ 2:0]  |                |
## Signals

| Name          | Type            | Description       |
| ------------- | --------------- | ----------------- |
| up_rack_d     | reg             |                   |
| up_rdata_d    | reg     [ 31:0] |                   |
| up_wack       | reg             |                   |
| up_scratch    | reg     [ 31:0] |                   |
| up_rack       | reg             |                   |
| up_rdata      | reg     [ 31:0] |                   |
| up_rstn       | wire            | internal signals  |
| up_clk        | wire            |                   |
| up_wreq       | wire            |                   |
| up_waddr      | wire [ 13:0]    |                   |
| up_wdata      | wire [ 31:0]    |                   |
| up_rreq       | wire            |                   |
| up_raddr      | wire [ 13:0]    |                   |
| up_wreq_s     | wire            |                   |
| up_rreq_s     | wire            |                   |
| up_gp_ioenb_s | wire [ 31:0]    |                   |
| up_gp_out_s   | wire [ 31:0]    |                   |
| up_gp_in_s    | wire [ 31:0]    |                   |
| d_clk_s       | wire [  7:0]    |                   |
| up_wack_s     | wire [ 16:0]    |                   |
| up_rack_s     | wire [ 16:0]    |                   |
| up_rdata_s    | wire [ 31:0]    |                   |
## Constants

| Name          | Type    | Value        | Description |
| ------------- | ------- | ------------ | ----------- |
| PCORE_VERSION | [31:0]  | 32'h00040063 | version     |
| BUF_ENABLE    | integer | 'd0          |             |
## Processes
- unnamed: ( @(posedge up_clk or negedge up_rstn) )
**Description**
up signals

- unnamed: ( @(negedge up_rstn or posedge up_clk) )
**Description**
processor write interface

- unnamed: ( @(negedge up_rstn or posedge up_clk) )
**Description**
processor read interface

## Instantiations

- i_up_axi: up_axi
