# Entity: dmac_dest_mm_axi

- **File**: dest_axi_mm.v
## Diagram

![Diagram](dest_axi_mm.svg "Diagram")
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

| Generic name          | Type | Value                       | Description |
| --------------------- | ---- | --------------------------- | ----------- |
| ID_WIDTH              |      | 3                           |             |
| DMA_DATA_WIDTH        |      | 64                          |             |
| DMA_ADDR_WIDTH        |      | 32                          |             |
| BYTES_PER_BEAT_WIDTH  |      | $clog2(DMA_DATA_WIDTH/8)    |             |
| BEATS_PER_BURST_WIDTH |      | 4                           |             |
| MAX_BYTES_PER_BURST   |      | 128                         |             |
| BYTES_PER_BURST_WIDTH |      | $clog2(MAX_BYTES_PER_BURST) |             |
| AXI_LENGTH_WIDTH      |      | 8                           |             |
## Ports

| Port name                  | Direction | Type                                    | Description     |
| -------------------------- | --------- | --------------------------------------- | --------------- |
| m_axi_aclk                 | input     |                                         |                 |
| m_axi_aresetn              | input     |                                         |                 |
| req_valid                  | input     |                                         |                 |
| req_ready                  | output    |                                         |                 |
| req_address                | input     | [DMA_ADDR_WIDTH-1:BYTES_PER_BEAT_WIDTH] |                 |
| bl_valid                   | input     |                                         |                 |
| bl_ready                   | output    |                                         |                 |
| measured_last_burst_length | input     | [BEATS_PER_BURST_WIDTH-1:0]             |                 |
| enable                     | input     |                                         |                 |
| enabled                    | output    |                                         |                 |
| response_valid             | output    |                                         |                 |
| response_ready             | input     |                                         |                 |
| response_resp              | output    | [1:0]                                   |                 |
| response_resp_eot          | output    |                                         |                 |
| response_resp_partial      | output    |                                         |                 |
| response_data_burst_length | output    | [BYTES_PER_BURST_WIDTH-1:0]             |                 |
| request_id                 | input     | [ID_WIDTH-1:0]                          |                 |
| response_id                | output    | [ID_WIDTH-1:0]                          |                 |
| address_id                 | output    | [ID_WIDTH-1:0]                          |                 |
| address_eot                | input     |                                         |                 |
| response_eot               | input     |                                         |                 |
| fifo_valid                 | input     |                                         |                 |
| fifo_ready                 | output    |                                         |                 |
| fifo_data                  | input     | [DMA_DATA_WIDTH-1:0]                    |                 |
| fifo_strb                  | input     | [DMA_DATA_WIDTH/8-1:0]                  |                 |
| fifo_last                  | input     |                                         |                 |
| dest_burst_info_length     | input     | [BYTES_PER_BURST_WIDTH-1:0]             |                 |
| dest_burst_info_partial    | input     |                                         |                 |
| dest_burst_info_id         | input     | [ID_WIDTH-1:0]                          |                 |
| dest_burst_info_write      | input     |                                         |                 |
| m_axi_awready              | input     |                                         |  Write address  |
| m_axi_awvalid              | output    |                                         |                 |
| m_axi_awaddr               | output    | [DMA_ADDR_WIDTH-1:0]                    |                 |
| m_axi_awlen                | output    | [AXI_LENGTH_WIDTH-1:0]                  |                 |
| m_axi_awsize               | output    | [ 2:0]                                  |                 |
| m_axi_awburst              | output    | [ 1:0]                                  |                 |
| m_axi_awprot               | output    | [ 2:0]                                  |                 |
| m_axi_awcache              | output    | [ 3:0]                                  |                 |
| m_axi_wdata                | output    | [DMA_DATA_WIDTH-1:0]                    |  Write data     |
| m_axi_wstrb                | output    | [(DMA_DATA_WIDTH/8)-1:0]                |                 |
| m_axi_wready               | input     |                                         |                 |
| m_axi_wvalid               | output    |                                         |                 |
| m_axi_wlast                | output    |                                         |                 |
| m_axi_bvalid               | input     |                                         |  Write response |
| m_axi_bresp                | input     | [ 1:0]                                  |                 |
| m_axi_bready               | output    |                                         |                 |
## Signals

| Name            | Type                              | Description |
| --------------- | --------------------------------- | ----------- |
| address_enabled | wire                              |             |
| bl_mem          | reg [BYTES_PER_BURST_WIDTH+1-1:0] |             |
## Processes
- unnamed: ( @(posedge m_axi_aclk) )
  - **Type:** always
## Instantiations

- i_addr_gen: dmac_address_generator
- i_response_handler: dmac_response_handler
