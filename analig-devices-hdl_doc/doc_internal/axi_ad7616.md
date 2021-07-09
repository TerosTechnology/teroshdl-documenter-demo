# Entity: axi_ad7616

## Diagram

![Diagram](axi_ad7616.svg "Diagram")
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

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| ID           |      | 0     |             |
| IF_TYPE      |      | 1     |             |
## Ports

| Port name     | Direction | Type   | Description                |
| ------------- | --------- | ------ | -------------------------- |
| rx_sclk       | output    |        | physical data interface    |
| rx_cs_n       | output    |        |                            |
| rx_sdo        | output    |        |                            |
| rx_sdi        | input     | [ 1:0] |                            |
| rx_db_o       | output    | [15:0] |                            |
| rx_db_i       | input     | [15:0] |                            |
| rx_db_t       | output    |        |                            |
| rx_rd_n       | output    |        |                            |
| rx_wr_n       | output    |        |                            |
| rx_cnvst      | output    |        | physical control interface |
| rx_busy       | input     |        |                            |
| s_axi_aclk    | input     |        | AXI Slave Memory Map       |
| s_axi_aresetn | input     |        |                            |
| s_axi_awvalid | input     |        |                            |
| s_axi_awaddr  | input     | [15:0] |                            |
| s_axi_awprot  | input     | [ 2:0] |                            |
| s_axi_awready | output    |        |                            |
| s_axi_wvalid  | input     |        |                            |
| s_axi_wdata   | input     | [31:0] |                            |
| s_axi_wstrb   | input     | [ 3:0] |                            |
| s_axi_wready  | output    |        |                            |
| s_axi_bvalid  | output    |        |                            |
| s_axi_bresp   | output    | [ 1:0] |                            |
| s_axi_bready  | input     |        |                            |
| s_axi_arvalid | input     |        |                            |
| s_axi_araddr  | input     | [15:0] |                            |
| s_axi_arprot  | input     | [ 2:0] |                            |
| s_axi_arready | output    |        |                            |
| s_axi_rvalid  | output    |        |                            |
| s_axi_rresp   | output    | [ 1:0] |                            |
| s_axi_rdata   | output    | [31:0] |                            |
| s_axi_rready  | input     |        |                            |
| adc_valid     | output    |        | Write FIFO interface       |
| adc_data      | output    | [15:0] |                            |
| adc_sync      | output    |        |                            |
| irq           | output    |        |                            |
## Signals

| Name              | Type           | Description         |
| ----------------- | -------------- | ------------------- |
| up_wack           | reg            | internal registers  |
| up_rack           | reg            |                     |
| up_rdata          | reg     [31:0] |                     |
| up_clk            | wire           | internal signals    |
| up_rstn           | wire           |                     |
| up_rst            | wire           |                     |
| up_rreq_s         | wire           |                     |
| up_raddr_s        | wire [13:0]    |                     |
| up_wreq_s         | wire           |                     |
| up_waddr_s        | wire [13:0]    |                     |
| up_wdata_s        | wire [31:0]    |                     |
| up_wack_if_s      | wire           |                     |
| up_rack_if_s      | wire           |                     |
| up_rdata_if_s     | wire [31:0]    |                     |
| up_wack_cntrl_s   | wire           |                     |
| up_rack_cntrl_s   | wire           |                     |
| up_rdata_cntrl_s  | wire [31:0]    |                     |
| trigger_s         | wire           |                     |
| rd_req_s          | wire           |                     |
| wr_req_s          | wire           |                     |
| wr_data_s         | wire [15:0]    |                     |
| rd_data_s         | wire [15:0]    |                     |
| rd_valid_s        | wire           |                     |
| burst_length_s    | wire [ 4:0]    |                     |
| m_axis_ready_s    | wire           |                     |
| m_axis_valid_s    | wire           |                     |
| m_axis_data_s     | wire [15:0]    |                     |
| m_axis_xfer_req_s | wire           |                     |
## Constants

| Name       | Type | Value | Description |
| ---------- | ---- | ----- | ----------- |
| NUM_OF_SDI |      | 2     |             |
| SERIAL     |      | 0     |             |
| PARALLEL   |      | 1     |             |
| NEG_EDGE   |      | 1     |             |
## Processes
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
**Description**
processor read interface

## Instantiations

- i_ad7616_control: axi_ad7616_control
- i_up_axi: up_axi
**Description**
up bus interface

