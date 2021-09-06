# Entity: axi_xcvrlb

- **File**: axi_xcvrlb.v
## Diagram

![Diagram](axi_xcvrlb.svg "Diagram")
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

| Generic name   | Type    | Value | Description  |
| -------------- | ------- | ----- | ------------ |
| CPLL_FBDIV     | integer | 1     |  parameters  |
| CPLL_FBDIV_4_5 | integer | 5     |              |
| NUM_OF_LANES   |         | 1     |              |
| XCVR_TYPE      | integer | 2     |              |
## Ports

| Port name     | Direction | Type                 | Description            |
| ------------- | --------- | -------------------- | ---------------------- |
| ref_clk       | input     |                      |  transceiver interface |
| rx_p          | input     | [(NUM_OF_LANES-1):0] |                        |
| rx_n          | input     | [(NUM_OF_LANES-1):0] |                        |
| tx_p          | output    | [(NUM_OF_LANES-1):0] |                        |
| tx_n          | output    | [(NUM_OF_LANES-1):0] |                        |
| s_axi_aclk    | input     |                      |  axi interface         |
| s_axi_aresetn | input     |                      |                        |
| s_axi_awvalid | input     |                      |                        |
| s_axi_awaddr  | input     | [15:0]               |                        |
| s_axi_awprot  | input     | [ 2:0]               |                        |
| s_axi_awready | output    |                      |                        |
| s_axi_wvalid  | input     |                      |                        |
| s_axi_wdata   | input     | [31:0]               |                        |
| s_axi_wstrb   | input     | [ 3:0]               |                        |
| s_axi_wready  | output    |                      |                        |
| s_axi_bvalid  | output    |                      |                        |
| s_axi_bresp   | output    | [ 1:0]               |                        |
| s_axi_bready  | input     |                      |                        |
| s_axi_arvalid | input     |                      |                        |
| s_axi_araddr  | input     | [15:0]               |                        |
| s_axi_arprot  | input     | [ 2:0]               |                        |
| s_axi_arready | output    |                      |                        |
| s_axi_rvalid  | output    |                      |                        |
| s_axi_rresp   | output    | [ 1:0]               |                        |
| s_axi_rdata   | output    | [31:0]               |                        |
| s_axi_rready  | input     |                      |                        |
## Signals

| Name            | Type           | Description          |
| --------------- | -------------- | -------------------- |
| up_wack         | reg            |  internal registers  |
| up_scratch      | reg     [31:0] |                      |
| up_resetn       | reg            |                      |
| up_status       | reg     [31:0] |                      |
| up_pll_locked   | reg     [31:0] |                      |
| up_rack         | reg            |                      |
| up_rdata        | reg     [31:0] |                      |
| up_rstn         | wire           |  internal signals    |
| up_clk          | wire           |                      |
| up_wreq_s       | wire           |                      |
| up_waddr_s      | wire [ 7:0]    |                      |
| up_wdata_s      | wire [31:0]    |                      |
| up_rreq_s       | wire           |                      |
| up_raddr_s      | wire [ 7:0]    |                      |
| up_status_s     | wire [31:0]    |                      |
| up_pll_locked_s | wire [31:0]    |                      |
## Constants

| Name    | Type   | Value        | Description  |
| ------- | ------ | ------------ | ------------ |
| VERSION | [31:0] | 32'h00100161 |  parameters  |
## Processes
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
</br>**Description**
 register access 
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
## Instantiations

- i_axi: up_axi
