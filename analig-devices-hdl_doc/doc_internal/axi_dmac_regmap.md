# Entity: axi_dmac_regmap

- **File**: axi_dmac_regmap.v
## Diagram

![Diagram](axi_dmac_regmap.svg "Diagram")
## Description

***************************************************************************
 ***************************************************************************
 Copyright 2014 - 2018 (c) Analog Devices, Inc. All rights reserved.
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

| Generic name              | Type | Value | Description |
| ------------------------- | ---- | ----- | ----------- |
| ID                        |      | 0     |             |
| DISABLE_DEBUG_REGISTERS   |      | 0     |             |
| BYTES_PER_BEAT_WIDTH_DEST |      | 1     |             |
| BYTES_PER_BEAT_WIDTH_SRC  |      | 1     |             |
| BYTES_PER_BURST_WIDTH     |      | 7     |             |
| DMA_TYPE_DEST             |      | 0     |             |
| DMA_TYPE_SRC              |      | 2     |             |
| DMA_AXI_ADDR_WIDTH        |      | 32    |             |
| DMA_LENGTH_WIDTH          |      | 24    |             |
| DMA_LENGTH_ALIGN          |      | 3     |             |
| DMA_CYCLIC                |      | 0     |             |
| HAS_DEST_ADDR             |      | 1     |             |
| HAS_SRC_ADDR              |      | 1     |             |
| DMA_2D_TRANSFER           |      | 0     |             |
| SYNC_TRANSFER_START       |      | 0     |             |
## Ports

| Port name                      | Direction | Type                                             | Description            |
| ------------------------------ | --------- | ------------------------------------------------ | ---------------------- |
| s_axi_aclk                     | input     |                                                  | Slave AXI interface    |
| s_axi_aresetn                  | input     |                                                  |                        |
| s_axi_awvalid                  | input     |                                                  |                        |
| s_axi_awready                  | output    |                                                  |                        |
| s_axi_awaddr                   | input     | [10:0]                                           |                        |
| s_axi_awprot                   | input     | [2:0]                                            |                        |
| s_axi_wvalid                   | input     |                                                  |                        |
| s_axi_wready                   | output    |                                                  |                        |
| s_axi_wdata                    | input     | [31:0]                                           |                        |
| s_axi_wstrb                    | input     | [3:0]                                            |                        |
| s_axi_bvalid                   | output    |                                                  |                        |
| s_axi_bready                   | input     |                                                  |                        |
| s_axi_bresp                    | output    | [1:0]                                            |                        |
| s_axi_arvalid                  | input     |                                                  |                        |
| s_axi_arready                  | output    |                                                  |                        |
| s_axi_araddr                   | input     | [10:0]                                           |                        |
| s_axi_arprot                   | input     | [2:0]                                            |                        |
| s_axi_rvalid                   | output    |                                                  |                        |
| s_axi_rready                   | input     |                                                  |                        |
| s_axi_rresp                    | output    | [1:0]                                            |                        |
| s_axi_rdata                    | output    | [31:0]                                           |                        |
| irq                            | output    |                                                  | Interrupt              |
| ctrl_enable                    | output    | reg                                              | Control interface      |
| ctrl_pause                     | output    | reg                                              |                        |
| request_valid                  | output    |                                                  | DMA request interface  |
| request_ready                  | input     |                                                  |                        |
| request_dest_address           | output    | [DMA_AXI_ADDR_WIDTH-1:BYTES_PER_BEAT_WIDTH_DEST] |                        |
| request_src_address            | output    | [DMA_AXI_ADDR_WIDTH-1:BYTES_PER_BEAT_WIDTH_SRC]  |                        |
| request_x_length               | output    | [DMA_LENGTH_WIDTH-1:0]                           |                        |
| request_y_length               | output    | [DMA_LENGTH_WIDTH-1:0]                           |                        |
| request_dest_stride            | output    | [DMA_LENGTH_WIDTH-1:0]                           |                        |
| request_src_stride             | output    | [DMA_LENGTH_WIDTH-1:0]                           |                        |
| request_sync_transfer_start    | output    |                                                  |                        |
| request_last                   | output    |                                                  |                        |
| response_eot                   | input     |                                                  | DMA response interface |
| response_measured_burst_length | input     | [BYTES_PER_BURST_WIDTH-1:0]                      |                        |
| response_partial               | input     |                                                  |                        |
| response_valid                 | input     |                                                  |                        |
| response_ready                 | output    |                                                  |                        |
| dbg_src_addr                   | input     | [DMA_AXI_ADDR_WIDTH-1:0]                         | Debug interface        |
| dbg_dest_addr                  | input     | [DMA_AXI_ADDR_WIDTH-1:0]                         |                        |
| dbg_status                     | input     | [11:0]                                           |                        |
| dbg_ids0                       | input     | [31:0]                                           |                        |
| dbg_ids1                       | input     | [31:0]                                           |                        |
## Signals

| Name                | Type        | Description                                               |
| ------------------- | ----------- | --------------------------------------------------------- |
| up_rdata            | reg [31:0]  | Register interface signals                                |
| up_wack             | reg         |                                                           |
| up_rack             | reg         |                                                           |
| up_wreq             | wire        |                                                           |
| up_rreq             | wire        |                                                           |
| up_wdata            | wire [31:0] |                                                           |
| up_waddr            | wire [8:0]  |                                                           |
| up_raddr            | wire [8:0]  |                                                           |
| up_rdata_request    | wire [31:0] |                                                           |
| up_scratch          | reg [31:0]  | Scratch register                                          |
| up_eot              | wire        | Asserted for one cycle when a transfer has been completed |
| up_sot              | wire        | Asserted for one cycle when a transfer has been queued    |
| up_irq_mask         | reg [1:0]   | Interupt handling                                         |
| up_irq_source       | reg [1:0]   |                                                           |
| up_irq_pending      | wire [1:0]  |                                                           |
| up_irq_trigger      | wire [1:0]  |                                                           |
| up_irq_source_clear | wire [1:0]  |                                                           |
## Constants

| Name          | Type | Value      | Description |
| ------------- | ---- | ---------- | ----------- |
| PCORE_VERSION |      | 'h00040361 |             |
## Processes
- unnamed: ( @(posedge s_axi_aclk) )
- unnamed: ( @(posedge s_axi_aclk) )
- unnamed: ( @(posedge s_axi_aclk) )
**Description**
Register Interface

- unnamed: ( @(posedge s_axi_aclk) )
- unnamed: ( @(posedge s_axi_aclk) )
## Instantiations

- i_regmap_request: axi_dmac_regmap_request
- i_up_axi: up_axi
