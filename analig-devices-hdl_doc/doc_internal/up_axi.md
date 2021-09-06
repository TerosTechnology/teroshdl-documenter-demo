# Entity: up_axi

- **File**: up_axi.v
## Diagram

![Diagram](up_axi.svg "Diagram")
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

| Generic name      | Type | Value | Description |
| ----------------- | ---- | ----- | ----------- |
| AXI_ADDRESS_WIDTH |      | 16    |             |
## Ports

| Port name      | Direction | Type                      | Description       |
| -------------- | --------- | ------------------------- | ----------------- |
| up_rstn        | input     |                           |  reset and clocks |
| up_clk         | input     |                           |                   |
| up_axi_awvalid | input     |                           |  axi4 interface   |
| up_axi_awaddr  | input     | [(AXI_ADDRESS_WIDTH-1):0] |                   |
| up_axi_awready | output    |                           |                   |
| up_axi_wvalid  | input     |                           |                   |
| up_axi_wdata   | input     | [31:0]                    |                   |
| up_axi_wstrb   | input     | [ 3:0]                    |                   |
| up_axi_wready  | output    |                           |                   |
| up_axi_bvalid  | output    |                           |                   |
| up_axi_bresp   | output    | [ 1:0]                    |                   |
| up_axi_bready  | input     |                           |                   |
| up_axi_arvalid | input     |                           |                   |
| up_axi_araddr  | input     | [(AXI_ADDRESS_WIDTH-1):0] |                   |
| up_axi_arready | output    |                           |                   |
| up_axi_rvalid  | output    |                           |                   |
| up_axi_rresp   | output    | [ 1:0]                    |                   |
| up_axi_rdata   | output    | [31:0]                    |                   |
| up_axi_rready  | input     |                           |                   |
| up_wreq        | output    |                           |  pcore interface  |
| up_waddr       | output    | [(AXI_ADDRESS_WIDTH-3):0] |                   |
| up_wdata       | output    | [31:0]                    |                   |
| up_wack        | input     |                           |                   |
| up_rreq        | output    |                           |                   |
| up_raddr       | output    | [(AXI_ADDRESS_WIDTH-3):0] |                   |
| up_rdata       | input     | [31:0]                    |                   |
| up_rack        | input     |                           |                   |
## Signals

| Name               | Type                              | Description          |
| ------------------ | --------------------------------- | -------------------- |
| up_axi_awready_int | reg                               |  internal registers  |
| up_axi_wready_int  | reg                               |                      |
| up_axi_bvalid_int  | reg                               |                      |
| up_wack_d          | reg                               |                      |
| up_wsel            | reg                               |                      |
| up_wreq_int        | reg                               |                      |
| up_waddr_int       | reg     [(AXI_ADDRESS_WIDTH-3):0] |                      |
| up_wdata_int       | reg     [31:0]                    |                      |
| up_wcount          | reg     [ 4:0]                    |                      |
| up_axi_arready_int | reg                               |                      |
| up_axi_rvalid_int  | reg                               |                      |
| up_axi_rdata_int   | reg     [31:0]                    |                      |
| up_rack_d          | reg                               |                      |
| up_rdata_d         | reg     [31:0]                    |                      |
| up_rsel            | reg                               |                      |
| up_rreq_int        | reg                               |                      |
| up_raddr_int       | reg     [(AXI_ADDRESS_WIDTH-3):0] |                      |
| up_rcount          | reg     [ 4:0]                    |                      |
| up_wack_s          | wire                              |  internal signals    |
| up_rack_s          | wire                              |                      |
| up_rdata_s         | wire [31:0]                       |                      |
## Processes
- unnamed: ( @(posedge up_clk) )
  - **Type:** always
- unnamed: ( @(posedge up_clk) )
  - **Type:** always
- unnamed: ( @(posedge up_clk) )
  - **Type:** always
- unnamed: ( @(posedge up_clk) )
  - **Type:** always
