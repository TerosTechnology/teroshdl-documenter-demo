# Entity: axi_ad9671

- **File**: axi_ad9671.v
## Diagram

![Diagram](axi_ad9671.svg "Diagram")
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

| Generic name    | Type | Value | Description |
| --------------- | ---- | ----- | ----------- |
| ID              |      | 0     |             |
| FPGA_TECHNOLOGY |      | 0     |             |
| FPGA_FAMILY     |      | 0     |             |
| SPEED_GRADE     |      | 0     |             |
| DEV_PACKAGE     |      | 0     |             |
| QUAD_OR_DUAL_N  |      | 1     |             |
## Ports

| Port name     | Direction | Type                       | Description                               |
| ------------- | --------- | -------------------------- | ----------------------------------------- |
| rx_clk        | input     |                            |  jesd interface rx_clk is (line-rate/40)  |
| rx_sof        | input     | [ 3:0]                     |                                           |
| rx_valid      | input     |                            |                                           |
| rx_data       | input     | [(64*QUAD_OR_DUAL_N)+63:0] |                                           |
| rx_ready      | output    |                            |                                           |
| adc_clk       | output    |                            |  dma interface                            |
| adc_valid     | output    | [ 7:0]                     |                                           |
| adc_enable    | output    | [ 7:0]                     |                                           |
| adc_data      | output    | [127:0]                    |                                           |
| adc_dovf      | input     |                            |                                           |
| adc_sync_in   | input     |                            |                                           |
| adc_sync_out  | output    |                            |                                           |
| adc_raddr_in  | input     | [ 3:0]                     |                                           |
| adc_raddr_out | output    | [ 3:0]                     |                                           |
| s_axi_aclk    | input     |                            |  axi interface                            |
| s_axi_aresetn | input     |                            |                                           |
| s_axi_awvalid | input     |                            |                                           |
| s_axi_awaddr  | input     | [ 15:0]                    |                                           |
| s_axi_awprot  | input     | [ 2:0]                     |                                           |
| s_axi_awready | output    |                            |                                           |
| s_axi_wvalid  | input     |                            |                                           |
| s_axi_wdata   | input     | [ 31:0]                    |                                           |
| s_axi_wstrb   | input     | [ 3:0]                     |                                           |
| s_axi_wready  | output    |                            |                                           |
| s_axi_bvalid  | output    |                            |                                           |
| s_axi_bresp   | output    | [ 1:0]                     |                                           |
| s_axi_bready  | input     |                            |                                           |
| s_axi_arvalid | input     |                            |                                           |
| s_axi_araddr  | input     | [ 15:0]                    |                                           |
| s_axi_arprot  | input     | [ 2:0]                     |                                           |
| s_axi_arready | output    |                            |                                           |
| s_axi_rvalid  | output    |                            |                                           |
| s_axi_rresp   | output    | [ 1:0]                     |                                           |
| s_axi_rdata   | output    | [ 31:0]                    |                                           |
| s_axi_rready  | input     |                            |                                           |
## Signals

| Name              | Type            | Description                |
| ----------------- | --------------- | -------------------------- |
| up_status_pn_err  | reg             |  internal registers        |
| up_status_pn_oos  | reg             |                            |
| up_status_or      | reg             |                            |
| up_rdata          | reg     [ 31:0] |                            |
| up_rack           | reg             |                            |
| up_wack           | reg             |                            |
| adc_rst           | wire            |  internal clocks & resets  |
| up_rstn           | wire            |                            |
| up_clk            | wire            |                            |
| adc_status_s      | wire            |  internal signals          |
| adc_sync_status_s | wire            |                            |
| adc_valid_s       | wire            |                            |
| adc_data_s        | wire [ 15:0]    |                            |
| adc_or_s          | wire [  7:0]    |                            |
| up_adc_pn_err_s   | wire [  7:0]    |                            |
| up_adc_pn_oos_s   | wire [  7:0]    |                            |
| up_adc_or_s       | wire [  7:0]    |                            |
| up_wreq_s         | wire            |                            |
| up_waddr_s        | wire [ 13:0]    |                            |
| up_wdata_s        | wire [ 31:0]    |                            |
| up_rreq_s         | wire            |                            |
| up_raddr_s        | wire [ 13:0]    |                            |
| up_rdata_s        | wire [ 31:0]    |                            |
| up_rack_s         | wire            |                            |
| up_wack_s         | wire            |                            |
| adc_start_code    | wire [ 31:0]    |                            |
| adc_sync          | wire            |                            |
## Processes
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
</br>**Description**
 processor read interface 
## Instantiations

- i_if: axi_ad9671_if
</br>**Description**
 main (device interface)

- i_up_adc_common: up_adc_common
</br>**Description**
 common processor control

- i_up_axi: up_axi
</br>**Description**
 up bus interface

