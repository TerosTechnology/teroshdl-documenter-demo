# Entity: dmac_src_mm_axi

- **File**: src_axi_mm.v
## Diagram

![Diagram](src_axi_mm.svg "Diagram")
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

| Generic name          | Type | Value | Description |
| --------------------- | ---- | ----- | ----------- |
| ID_WIDTH              |      | 3     |             |
| DMA_DATA_WIDTH        |      | 64    |             |
| DMA_ADDR_WIDTH        |      | 32    |             |
| BYTES_PER_BEAT_WIDTH  |      | 3     |             |
| BEATS_PER_BURST_WIDTH |      | 4     |             |
| AXI_LENGTH_WIDTH      |      | 8     |             |
## Ports

| Port name                  | Direction | Type                                    | Description                                                                                                                                              |
| -------------------------- | --------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| m_axi_aclk                 | input     |                                         |                                                                                                                                                          |
| m_axi_aresetn              | input     |                                         |                                                                                                                                                          |
| req_valid                  | input     |                                         |                                                                                                                                                          |
| req_ready                  | output    |                                         |                                                                                                                                                          |
| req_address                | input     | [DMA_ADDR_WIDTH-1:BYTES_PER_BEAT_WIDTH] |                                                                                                                                                          |
| req_last_burst_length      | input     | [BEATS_PER_BURST_WIDTH-1:0]             |                                                                                                                                                          |
| req_last_beat_bytes        | input     | [BYTES_PER_BEAT_WIDTH-1:0]              |                                                                                                                                                          |
| enable                     | input     |                                         |                                                                                                                                                          |
| enabled                    | output    | reg                                     |                                                                                                                                                          |
| bl_valid                   | output    |                                         |                                                                                                                                                          |
| bl_ready                   | input     |                                         |                                                                                                                                                          |
| measured_last_burst_length | output    | [BEATS_PER_BURST_WIDTH-1:0]             |                                                                                                                                                          |
| request_id                 | input     | [ID_WIDTH-1:0]                          |   output                          response_valid,   input                           response_ready,   output [1:0]                    response_resp, */  |
| response_id                | output    | [ID_WIDTH-1:0]                          |                                                                                                                                                          |
| data_id                    | output    | [ID_WIDTH-1:0]                          |                                                                                                                                                          |
| address_id                 | output    | [ID_WIDTH-1:0]                          |                                                                                                                                                          |
| address_eot                | input     |                                         |                                                                                                                                                          |
| fifo_valid                 | output    |                                         |                                                                                                                                                          |
| fifo_data                  | output    | [DMA_DATA_WIDTH-1:0]                    |                                                                                                                                                          |
| fifo_valid_bytes           | output    | [BYTES_PER_BEAT_WIDTH-1:0]              |                                                                                                                                                          |
| fifo_last                  | output    |                                         |                                                                                                                                                          |
| m_axi_arready              | input     |                                         |  Read address                                                                                                                                            |
| m_axi_arvalid              | output    |                                         |                                                                                                                                                          |
| m_axi_araddr               | output    | [DMA_ADDR_WIDTH-1:0]                    |                                                                                                                                                          |
| m_axi_arlen                | output    | [AXI_LENGTH_WIDTH-1:0]                  |                                                                                                                                                          |
| m_axi_arsize               | output    | [ 2:0]                                  |                                                                                                                                                          |
| m_axi_arburst              | output    | [ 1:0]                                  |                                                                                                                                                          |
| m_axi_arprot               | output    | [ 2:0]                                  |                                                                                                                                                          |
| m_axi_arcache              | output    | [ 3:0]                                  |                                                                                                                                                          |
| m_axi_rdata                | input     | [DMA_DATA_WIDTH-1:0]                    |  Read data and response                                                                                                                                  |
| m_axi_rready               | output    |                                         |                                                                                                                                                          |
| m_axi_rvalid               | input     |                                         |                                                                                                                                                          |
| m_axi_rlast                | input     |                                         |                                                                                                                                                          |
| m_axi_rresp                | input     | [ 1:0]                                  |                                                                                                                                                          |
## Signals

| Name                | Type                           | Description |
| ------------------- | ------------------------------ | ----------- |
| id                  | reg [ID_WIDTH-1:0]             |             |
| address_enabled     | wire                           |             |
| req_ready_ag        | wire                           |             |
| req_valid_ag        | wire                           |             |
| bl_ready_ag         | wire                           |             |
| bl_valid_ag         | wire                           |             |
| last_beat_bytes     | reg [BYTES_PER_BEAT_WIDTH-1:0] |             |
| last_beat_bytes_mem | reg [BYTES_PER_BEAT_WIDTH-1:0] |             |
## Processes
- unnamed: ( @(posedge m_axi_aclk) )
  - **Type:** always
- unnamed: ( @(posedge m_axi_aclk) )
  - **Type:** always
- unnamed: ( @(posedge m_axi_aclk) )
  - **Type:** always
</br>**Description**
  * There is a requirement that data_id <= address_id (modulo 2**ID_WIDTH).  We  * know that we will never receive data before we have requested it so there is  * an implicit dependency between data_id and address_id and no need to  * explicitly track it.  */ 
- unnamed: ( @(posedge m_axi_aclk) )
  - **Type:** always
</br>**Description**
  * We need to complete all bursts for which an address has been put onto the  * AXI-MM interface.  */ 
## Instantiations

- i_req_splitter: splitter
- i_addr_gen: dmac_address_generator
