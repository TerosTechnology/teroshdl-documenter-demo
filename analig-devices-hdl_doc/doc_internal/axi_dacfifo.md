# Entity: axi_dacfifo

- **File**: axi_dacfifo.v
## Diagram

![Diagram](axi_dacfifo.svg "Diagram")
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
| DAC_DATA_WIDTH    |      | 64           |             |
| DMA_DATA_WIDTH    |      | 64           |             |
| AXI_DATA_WIDTH    |      | 512          |             |
| AXI_SIZE          |      | 2            |             |
| AXI_LENGTH        |      | 15           |             |
| AXI_ADDRESS       |      | 32'h00000000 |             |
| AXI_ADDRESS_LIMIT |      | 32'hffffffff |             |
## Ports

| Port name     | Direction | Type                     | Description                 |
| ------------- | --------- | ------------------------ | --------------------------- |
| dma_clk       | input     |                          |  dma interface (AXI Stream) |
| dma_rst       | input     |                          |                             |
| dma_valid     | input     |                          |                             |
| dma_data      | input     | [(DMA_DATA_WIDTH-1):0]   |                             |
| dma_ready     | output    |                          |                             |
| dma_xfer_req  | input     |                          |                             |
| dma_xfer_last | input     |                          |                             |
| dac_clk       | input     |                          |  dac interface              |
| dac_rst       | input     |                          |                             |
| dac_valid     | input     |                          |                             |
| dac_data      | output    | [(DAC_DATA_WIDTH-1):0]   |                             |
| dac_dunf      | output    |                          |                             |
| dac_xfer_out  | output    |                          |                             |
| bypass        | input     |                          |                             |
| axi_clk       | input     |                          |  axi interface              |
| axi_resetn    | input     |                          |                             |
| axi_awvalid   | output    |                          |                             |
| axi_awid      | output    | [ 3:0]                   |                             |
| axi_awburst   | output    | [ 1:0]                   |                             |
| axi_awlock    | output    |                          |                             |
| axi_awcache   | output    | [ 3:0]                   |                             |
| axi_awprot    | output    | [ 2:0]                   |                             |
| axi_awqos     | output    | [ 3:0]                   |                             |
| axi_awlen     | output    | [ 7:0]                   |                             |
| axi_awsize    | output    | [ 2:0]                   |                             |
| axi_awaddr    | output    | [ 31:0]                  |                             |
| axi_awready   | input     |                          |                             |
| axi_wvalid    | output    |                          |                             |
| axi_wdata     | output    | [(AXI_DATA_WIDTH-1):0]   |                             |
| axi_wstrb     | output    | [(AXI_DATA_WIDTH/8-1):0] |                             |
| axi_wlast     | output    |                          |                             |
| axi_wready    | input     |                          |                             |
| axi_bvalid    | input     |                          |                             |
| axi_bid       | input     | [ 3:0]                   |                             |
| axi_bresp     | input     | [ 1:0]                   |                             |
| axi_bready    | output    |                          |                             |
| axi_arvalid   | output    |                          |                             |
| axi_arid      | output    | [ 3:0]                   |                             |
| axi_arburst   | output    | [ 1:0]                   |                             |
| axi_arlock    | output    |                          |                             |
| axi_arcache   | output    | [ 3:0]                   |                             |
| axi_arprot    | output    | [ 2:0]                   |                             |
| axi_arqos     | output    | [ 3:0]                   |                             |
| axi_arlen     | output    | [ 7:0]                   |                             |
| axi_arsize    | output    | [ 2:0]                   |                             |
| axi_araddr    | output    | [ 31:0]                  |                             |
| axi_arready   | input     |                          |                             |
| axi_rvalid    | input     |                          |                             |
| axi_rid       | input     | [ 3:0]                   |                             |
| axi_rresp     | input     | [ 1:0]                   |                             |
| axi_rlast     | input     |                          |                             |
| axi_rdata     | input     | [(AXI_DATA_WIDTH-1):0]   |                             |
| axi_rready    | output    |                          |                             |
## Signals

| Name                | Type                        | Description |
| ------------------- | --------------------------- | ----------- |
| dma_bypass_m1       | reg                         |             |
| dma_bypass          | reg                         |             |
| dac_bypass_m1       | reg                         |             |
| dac_bypass          | reg                         |             |
| dac_xfer_out_m1     | reg                         |             |
| dac_xfer_out_bypass | reg                         |             |
| axi_xfer_req_s      | wire                        |             |
| axi_last_addr_s     | wire [31:0]                 |             |
| axi_last_beats_s    | wire [ 7:0]                 |             |
| dma_last_beats_s    | wire [ 3:0]                 |             |
| dac_data_fifo_s     | wire [(DAC_DATA_WIDTH-1):0] |             |
| dac_data_bypass_s   | wire [(DAC_DATA_WIDTH-1):0] |             |
| dac_xfer_fifo_out_s | wire                        |             |
| dac_dunf_fifo_s     | wire                        |             |
| dac_dunf_bypass_s   | wire                        |             |
| dma_ready_wr_s      | wire                        |             |
## Constants

| Name        | Type | Value     | Description |
| ----------- | ---- | --------- | ----------- |
| FIFO_BYPASS |      | undefined |             |
## Instantiations

- i_wr: axi_dacfifo_wr
- i_rd: axi_dacfifo_rd
