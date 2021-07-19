# Entity: axi_dmac_regmap_request

- **File**: axi_dmac_regmap_request.v
## Diagram

![Diagram](axi_dmac_regmap_request.svg "Diagram")
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
| DISABLE_DEBUG_REGISTERS   |      | 0     |             |
| BYTES_PER_BEAT_WIDTH_DEST |      | 1     |             |
| BYTES_PER_BEAT_WIDTH_SRC  |      | 1     |             |
| BYTES_PER_BURST_WIDTH     |      | 7     |             |
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
| clk                            | input     |                                                  |                        |
| reset                          | input     |                                                  |                        |
| up_sot                         | output    |                                                  | Interrupts             |
| up_eot                         | output    |                                                  |                        |
| up_wreq                        | input     |                                                  | Register map interface |
| up_rreq                        | input     |                                                  |                        |
| up_waddr                       | input     | [8:0]                                            |                        |
| up_wdata                       | input     | [31:0]                                           |                        |
| up_raddr                       | input     | [8:0]                                            |                        |
| up_rdata                       | output    | [31:0]                                           |                        |
| ctrl_enable                    | input     |                                                  | Control interface      |
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
| response_ready                 | output    | reg                                              |                        |
## Signals

| Name                         | Type                                                 | Description           |
| ---------------------------- | ---------------------------------------------------- | --------------------- |
| up_dma_req_valid             | reg                                                  | DMA transfer signals  |
| up_dma_req_ready             | wire                                                 |                       |
| up_transfer_id               | reg [1:0]                                            |                       |
| up_transfer_id_eot           | reg [1:0]                                            |                       |
| up_transfer_done_bitmap      | reg [3:0]                                            |                       |
| up_dma_dest_address          | reg [DMA_AXI_ADDR_WIDTH-1:BYTES_PER_BEAT_WIDTH_DEST] |                       |
| up_dma_src_address           | reg [DMA_AXI_ADDR_WIDTH-1:BYTES_PER_BEAT_WIDTH_SRC]  |                       |
| up_dma_x_length              | reg [DMA_LENGTH_WIDTH-1:0]                           |                       |
| up_dma_cyclic                | reg                                                  |                       |
| up_dma_last                  | reg                                                  |                       |
| up_dma_enable_tlen_reporting | reg                                                  |                       |
| up_tlf_s_ready               | wire                                                 |                       |
| up_tlf_s_valid               | reg                                                  |                       |
| up_tlf_data                  | wire [MEASURED_LENGTH_WIDTH+2-1:0]                   |                       |
| up_tlf_valid                 | wire                                                 |                       |
| up_tlf_rd                    | wire                                                 |                       |
| up_partial_length_valid      | reg                                                  |                       |
| up_measured_transfer_length  | reg [MEASURED_LENGTH_WIDTH-1:0]                      |                       |
| up_clear_tl                  | reg                                                  |                       |
| up_transfer_id_eot_d         | reg [1:0]                                            |                       |
| up_bl_partial                | wire                                                 |                       |
## Constants

| Name                  | Type | Value | Description |
| --------------------- | ---- | ----- | ----------- |
| MEASURED_LENGTH_WIDTH |      | 32    |             |
## Processes
- unnamed: ( @(posedge clk) )
- unnamed: ( @(*) )
- unnamed: ( @(posedge clk) )
**Description**
Request ID and Request done bitmap handling

- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
## Instantiations

- i_transfer_lenghts_fifo: util_axis_fifo
**Description**
Buffer the length and transfer ID of partial transfers

