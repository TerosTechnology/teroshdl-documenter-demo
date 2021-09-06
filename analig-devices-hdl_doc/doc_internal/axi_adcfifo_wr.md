# Entity: axi_adcfifo_wr

- **File**: axi_adcfifo_wr.v
## Diagram

![Diagram](axi_adcfifo_wr.svg "Diagram")
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

| Generic name      | Type | Value        | Description |
| ----------------- | ---- | ------------ | ----------- |
| AXI_DATA_WIDTH    |      | 512          |             |
| AXI_SIZE          |      | 2            |             |
| AXI_LENGTH        |      | 16           |             |
| AXI_ADDRESS       |      | 32'h00000000 |             |
| AXI_ADDRESS_LIMIT |      | 32'h00000000 |             |
## Ports

| Port name    | Direction | Type                 | Description                  |
| ------------ | --------- | -------------------- | ---------------------------- |
| dma_xfer_req | input     |                      |  request and synchronization |
| axi_rd_req   | output    |                      |  read interface              |
| axi_rd_addr  | output    | [ 31:0]              |                              |
| adc_rst      | input     |                      |  fifo interface              |
| adc_clk      | input     |                      |                              |
| adc_wr       | input     |                      |                              |
| adc_wdata    | input     | [AXI_DATA_WIDTH-1:0] |                              |
| axi_clk      | input     |                      |  axi interface               |
| axi_resetn   | input     |                      |                              |
| axi_awvalid  | output    |                      |                              |
| axi_awid     | output    | [ 3:0]               |                              |
| axi_awburst  | output    | [ 1:0]               |                              |
| axi_awlock   | output    |                      |                              |
| axi_awcache  | output    | [ 3:0]               |                              |
| axi_awprot   | output    | [ 2:0]               |                              |
| axi_awqos    | output    | [ 3:0]               |                              |
| axi_awuser   | output    | [ 3:0]               |                              |
| axi_awlen    | output    | [ 7:0]               |                              |
| axi_awsize   | output    | [ 2:0]               |                              |
| axi_awaddr   | output    | [ 31:0]              |                              |
| axi_awready  | input     |                      |                              |
| axi_wvalid   | output    |                      |                              |
| axi_wdata    | output    | [AXI_DATA_WIDTH-1:0] |                              |
| axi_wstrb    | output    | [AXI_BYTE_WIDTH-1:0] |                              |
| axi_wlast    | output    |                      |                              |
| axi_wuser    | output    | [ 3:0]               |                              |
| axi_wready   | input     |                      |                              |
| axi_bvalid   | input     |                      |                              |
| axi_bid      | input     | [ 3:0]               |                              |
| axi_bresp    | input     | [ 1:0]               |                              |
| axi_buser    | input     | [ 3:0]               |                              |
| axi_bready   | output    |                      |                              |
| axi_dwovf    | output    |                      |  axi status                  |
| axi_dwunf    | output    |                      |                              |
| axi_werror   | output    |                      |                              |
## Signals

| Name             | Type                         | Description          |
| ---------------- | ---------------------------- | -------------------- |
| adc_xfer_req_m   | reg     [  2:0]              |  internal registers  |
| adc_xfer_init    | reg                          |                      |
| adc_xfer_limit   | reg                          |                      |
| adc_xfer_enable  | reg                          |                      |
| adc_xfer_addr    | reg     [ 31:0]              |                      |
| adc_waddr        | reg     [  7:0]              |                      |
| adc_waddr_g      | reg     [  7:0]              |                      |
| adc_rel_enable   | reg                          |                      |
| adc_rel_toggle   | reg                          |                      |
| adc_rel_waddr    | reg     [  7:0]              |                      |
| axi_rel_toggle_m | reg     [  2:0]              |                      |
| axi_rel_waddr    | reg     [  7:0]              |                      |
| axi_waddr_m1     | reg     [  7:0]              |                      |
| axi_waddr_m2     | reg     [  7:0]              |                      |
| axi_waddr        | reg     [  7:0]              |                      |
| axi_addr_diff    | reg     [  7:0]              |                      |
| axi_almost_full  | reg                          |                      |
| axi_almost_empty | reg                          |                      |
| axi_xfer_req_m   | reg     [  2:0]              |                      |
| axi_xfer_init    | reg                          |                      |
| axi_raddr        | reg     [  7:0]              |                      |
| axi_rd           | reg                          |                      |
| axi_rlast        | reg                          |                      |
| axi_rd_d         | reg                          |                      |
| axi_rlast_d      | reg                          |                      |
| axi_rdata_d      | reg     [AXI_DATA_WIDTH-1:0] |                      |
| axi_reset        | reg                          |                      |
| axi_rel_toggle_s | wire                         |  internal signals    |
| axi_addr_diff_s  | wire [  8:0]                 |                      |
| axi_wready_s     | wire                         |                      |
| axi_rd_s         | wire                         |                      |
| axi_req_s        | wire                         |                      |
| axi_rlast_s      | wire                         |                      |
| axi_rdata_s      | wire [AXI_DATA_WIDTH-1:0]    |                      |
## Constants

| Name             | Type | Value                       | Description |
| ---------------- | ---- | --------------------------- | ----------- |
| AXI_BYTE_WIDTH   |      | AXI_DATA_WIDTH/8            |             |
| AXI_AWINCR       |      | AXI_LENGTH * AXI_BYTE_WIDTH |             |
| BUF_THRESHOLD_LO |      | 8'd6                        |             |
| BUF_THRESHOLD_HI |      | 8'd250                      |             |
## Functions
- b2g <font id="function_arguments">()</font> <font id="function_return">return ([7:0])</font>
**Description**
 binary to grey conversion

- g2b <font id="function_arguments">()</font> <font id="function_return">return ([7:0])</font>
**Description**
 grey to binary conversion

## Processes
- unnamed: ( @(posedge adc_clk) )
  - **Type:** always
**Description**
 fifo interface 
- unnamed: ( @(posedge axi_clk or negedge axi_resetn) )
  - **Type:** always
- unnamed: ( @(posedge axi_clk or negedge axi_resetn) )
  - **Type:** always
- unnamed: ( @(posedge axi_clk or negedge axi_resetn) )
  - **Type:** always
**Description**
 transfer request is required to keep things in sync 
- unnamed: ( @(posedge axi_clk or negedge axi_resetn) )
  - **Type:** always
- unnamed: ( @(posedge axi_clk or negedge axi_resetn) )
  - **Type:** always
**Description**
 send read request for every burst about to be completed 
- unnamed: ( @(posedge axi_clk or negedge axi_resetn) )
  - **Type:** always
- unnamed: ( @(posedge axi_clk or negedge axi_resetn) )
  - **Type:** always
- unnamed: ( @(posedge axi_clk or negedge axi_resetn) )
  - **Type:** always
**Description**
 fifo needs a reset 
## Instantiations

- i_axis_inf: ad_axis_inf_rx
**Description**
 interface handler

- i_mem: ad_mem
**Description**
 buffer

