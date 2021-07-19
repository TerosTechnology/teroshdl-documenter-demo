# Entity: axi_dmac_burst_memory

- **File**: axi_dmac_burst_memory.v
## Diagram

![Diagram](axi_dmac_burst_memory.svg "Diagram")
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

| Generic name             | Type | Value                       | Description |
| ------------------------ | ---- | --------------------------- | ----------- |
| DATA_WIDTH_SRC           |      | 64                          |             |
| DATA_WIDTH_DEST          |      | 64                          |             |
| ID_WIDTH                 |      | 3                           |             |
| MAX_BYTES_PER_BURST      |      | 128                         |             |
| ASYNC_CLK                |      | 1                           |             |
| BYTES_PER_BEAT_WIDTH_SRC |      | $clog2(DATA_WIDTH_SRC/8)    |             |
| BYTES_PER_BURST_WIDTH    |      | $clog2(MAX_BYTES_PER_BURST) |             |
| DMA_LENGTH_ALIGN         |      | 3                           |             |
| ENABLE_DIAGNOSTICS_IF    |      | 0                           |             |
| ALLOW_ASYM_MEM           |      | 0                           |             |
## Ports

| Port name               | Direction | Type                           | Description           |
| ----------------------- | --------- | ------------------------------ | --------------------- |
| src_clk                 | input     |                                |                       |
| src_reset               | input     |                                |                       |
| src_data_valid          | input     |                                |                       |
| src_data                | input     | [DATA_WIDTH_SRC-1:0]           |                       |
| src_data_last           | input     |                                |                       |
| src_data_valid_bytes    | input     | [BYTES_PER_BEAT_WIDTH_SRC-1:0] |                       |
| src_data_partial_burst  | input     |                                |                       |
| src_data_request_id     | output    | [ID_WIDTH-1:0]                 |                       |
| dest_clk                | input     |                                |                       |
| dest_reset              | input     |                                |                       |
| dest_data_valid         | output    |                                |                       |
| dest_data_ready         | input     |                                |                       |
| dest_data               | output    | [DATA_WIDTH_DEST-1:0]          |                       |
| dest_data_last          | output    |                                |                       |
| dest_data_strb          | output    | [DATA_WIDTH_DEST/8-1:0]        |                       |
| dest_burst_info_length  | output    | [BYTES_PER_BURST_WIDTH-1:0]    |                       |
| dest_burst_info_partial | output    |                                |                       |
| dest_burst_info_id      | output    | [ID_WIDTH-1:0]                 |                       |
| dest_burst_info_write   | output    | reg                            |                       |
| dest_request_id         | output    | [ID_WIDTH-1:0]                 |                       |
| dest_data_request_id    | input     | [ID_WIDTH-1:0]                 |                       |
| dest_data_response_id   | output    | [ID_WIDTH-1:0]                 |                       |
| dest_diag_level_bursts  | output    | [7:0]                          | Diagnostics interface |
## Signals

| Name                       | Type                                               | Description |
| -------------------------- | -------------------------------------------------- | ----------- |
| src_id_next                | reg [ID_WIDTH-1:0]                                 |             |
| src_id                     | reg [ID_WIDTH-1:0]                                 |             |
| src_id_reduced_msb         | reg                                                |             |
| src_beat_counter           | reg [BURST_LEN_WIDTH_SRC-1:0]                      |             |
| dest_id_next               | reg [ID_WIDTH-1:0]                                 |             |
| dest_id_reduced_msb_next   | reg                                                |             |
| dest_id_reduced_msb        | reg                                                |             |
| dest_id                    | reg [ID_WIDTH-1:0]                                 |             |
| dest_beat_counter          | reg [BURST_LEN_WIDTH_DEST-1:0]                     |             |
| dest_burst_len             | wire [BURST_LEN_WIDTH_DEST-1:0]                    |             |
| dest_valid                 | reg                                                |             |
| dest_mem_data_valid        | reg                                                |             |
| dest_mem_data_last         | reg                                                |             |
| dest_mem_data_strb         | reg [DATA_WIDTH_MEM_DEST/8-1:0]                    |             |
| burst_len_mem              | reg [BYTES_PER_BURST_WIDTH+1-1-DMA_LENGTH_ALIGN:0] |             |
| src_burst_len_data         | wire [BYTES_PER_BURST_WIDTH+1-1:0]                 |             |
| dest_burst_len_data        | reg [BYTES_PER_BURST_WIDTH+1-1:0]                  |             |
| src_beat                   | wire                                               |             |
| src_last_beat              | wire                                               |             |
| src_dest_id                | wire [ID_WIDTH-1:0]                                |             |
| src_waddr                  | wire [ADDRESS_WIDTH_SRC-1:0]                       |             |
| src_id_reduced             | wire [ID_WIDTH-2:0]                                |             |
| src_mem_data_valid         | wire                                               |             |
| src_mem_data_last          | wire                                               |             |
| src_mem_data               | wire [DATA_WIDTH_MEM_SRC-1:0]                      |             |
| src_mem_data_valid_bytes   | wire [BYTES_PER_BEAT_WIDTH_MEM_SRC-1:0]            |             |
| src_mem_data_partial_burst | wire                                               |             |
| dest_beat                  | wire                                               |             |
| dest_last_beat             | wire                                               |             |
| dest_last                  | wire                                               |             |
| dest_src_id                | wire [ID_WIDTH-1:0]                                |             |
| dest_raddr                 | wire [ADDRESS_WIDTH_DEST-1:0]                      |             |
| dest_id_reduced_next       | wire [ID_WIDTH-2:0]                                |             |
| dest_id_next_inc           | wire [ID_WIDTH-1:0]                                |             |
| dest_id_reduced            | wire [ID_WIDTH-2:0]                                |             |
| dest_burst_valid           | wire                                               |             |
| dest_burst_ready           | wire                                               |             |
| dest_ready                 | wire                                               |             |
| dest_mem_data              | wire [DATA_WIDTH_MEM_DEST-1:0]                     |             |
| dest_mem_data_ready        | wire                                               |             |
## Constants

| Name                         | Type | Value                                        | Description                          |
| ---------------------------- | ---- | -------------------------------------------- | ------------------------------------ |
| DATA_WIDTH_MEM               |      | DATA_W                                       |                                      |
| MEM_RATIO                    |      | DATA_WIDTH_SRC / DATA_WIDTH_DEST             |                                      |
| BURST_LEN                    |      | MAX_BYTES_PER_BURST                          | A burst can have up to 256 beats */  |
| BURST_LEN_WIDTH              |      |                                              |                                      |
| AUX_FIFO_SIZE                |      | 2                                            |                                      |
| MEM_RATIO_WIDTH              |      | MEM_RATIO == 2 ? 1 :                         |                                      |
| BURST_LEN_WIDTH_SRC          |      | BURST_LEN_WIDTH                              |                                      |
| BURST_LEN_WIDTH_DEST         |      | BURST_LEN_WIDTH                              |                                      |
| DATA_WIDTH_MEM_SRC           |      | DATA_WIDTH_MEM                               |                                      |
| DATA_WIDTH_MEM_DEST          |      | DATA_WIDTH_MEM                               |                                      |
| ADDRESS_WIDTH_SRC            |      | BURST_LEN_WIDTH_SRC + ID_WIDTH - 1           |                                      |
| ADDRESS_WIDTH_DEST           |      | BURST_LEN_WIDTH_DEST + ID_WIDTH - 1          |                                      |
| BYTES_PER_BEAT_WIDTH_MEM_SRC |      | BYTES_PER_BURST_WIDTH - BURST_LEN_WIDTH_SRC  |                                      |
| BYTES_PER_BEAT_WIDTH_DEST    |      | BYTES_PER_BURST_WIDTH - BURST_LEN_WIDTH_DEST |                                      |
## Processes
- unnamed: ( @(*) )
- unnamed: ( @(posedge src_clk) )
- unnamed: ( @(posedge src_clk) )
- unnamed: ( @(posedge src_clk) )
- unnamed: ( @(posedge dest_clk) )
- unnamed: ( @(posedge dest_clk) )
- unnamed: ( @(posedge dest_clk) )
- unnamed: ( @(posedge dest_clk) )
- unnamed: ( @(posedge dest_clk) )
- unnamed: ( @(posedge dest_clk) )
- unnamed: ( @(posedge dest_clk) )
- unnamed: ( @(posedge dest_clk) )
- unnamed: ( @(posedge dest_clk) )
## Instantiations

- i_resize_src: axi_dmac_resize_src
- i_mem: ad_mem_asym
- i_resize_dest: axi_dmac_resize_dest
- i_dest_sync_id: sync_bits
- i_src_sync_id: sync_bits
