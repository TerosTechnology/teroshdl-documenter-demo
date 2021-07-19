# Entity: dmac_2d_transfer

- **File**: 2d_transfer.v
## Diagram

![Diagram](2d_transfer.svg "Diagram")
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

| Generic name              | Type | Value | Description |
| ------------------------- | ---- | ----- | ----------- |
| DMA_AXI_ADDR_WIDTH        |      | 32    |             |
| DMA_LENGTH_WIDTH          |      | 24    |             |
| BYTES_PER_BURST_WIDTH     |      | 7     |             |
| BYTES_PER_BEAT_WIDTH_SRC  |      | 3     |             |
| BYTES_PER_BEAT_WIDTH_DEST |      | 3     |             |
## Ports

| Port name                   | Direction | Type                                             | Description |
| --------------------------- | --------- | ------------------------------------------------ | ----------- |
| req_aclk                    | input     |                                                  |             |
| req_aresetn                 | input     |                                                  |             |
| req_valid                   | input     |                                                  |             |
| req_ready                   | output    |                                                  |             |
| req_dest_address            | input     | [DMA_AXI_ADDR_WIDTH-1:BYTES_PER_BEAT_WIDTH_DEST] |             |
| req_src_address             | input     | [DMA_AXI_ADDR_WIDTH-1:BYTES_PER_BEAT_WIDTH_SRC]  |             |
| req_x_length                | input     | [DMA_LENGTH_WIDTH-1:0]                           |             |
| req_y_length                | input     | [DMA_LENGTH_WIDTH-1:0]                           |             |
| req_dest_stride             | input     | [DMA_LENGTH_WIDTH-1:0]                           |             |
| req_src_stride              | input     | [DMA_LENGTH_WIDTH-1:0]                           |             |
| req_sync_transfer_start     | input     |                                                  |             |
| req_last                    | input     |                                                  |             |
| req_eot                     | output    |                                                  |             |
| req_measured_burst_length   | output    | [BYTES_PER_BURST_WIDTH-1:0]                      |             |
| req_response_partial        | output    |                                                  |             |
| req_response_valid          | output    |                                                  |             |
| req_response_ready          | input     |                                                  |             |
| out_abort_req               | input     |                                                  |             |
| out_req_valid               | output    |                                                  |             |
| out_req_ready               | input     |                                                  |             |
| out_req_dest_address        | output    | [DMA_AXI_ADDR_WIDTH-1:BYTES_PER_BEAT_WIDTH_DEST] |             |
| out_req_src_address         | output    | [DMA_AXI_ADDR_WIDTH-1:BYTES_PER_BEAT_WIDTH_SRC]  |             |
| out_req_length              | output    | [DMA_LENGTH_WIDTH-1:0]                           |             |
| out_req_sync_transfer_start | output    |                                                  |             |
| out_req_last                | output    |                                                  |             |
| out_eot                     | input     |                                                  |             |
| out_measured_burst_length   | input     | [BYTES_PER_BURST_WIDTH-1:0]                      |             |
| out_response_partial        | input     |                                                  |             |
| out_response_valid          | input     |                                                  |             |
| out_response_ready          | output    | reg                                              |             |
## Signals

| Name         | Type                                                 | Description |
| ------------ | ---------------------------------------------------- | ----------- |
| dest_address | reg [DMA_AXI_ADDR_WIDTH-1:BYTES_PER_BEAT_WIDTH_DEST] |             |
| src_address  | reg [DMA_AXI_ADDR_WIDTH-1:BYTES_PER_BEAT_WIDTH_SRC]  |             |
| x_length     | reg [DMA_LENGTH_WIDTH-1:0]                           |             |
| y_length     | reg [DMA_LENGTH_WIDTH-1:0]                           |             |
| dest_stride  | reg [DMA_LENGTH_WIDTH-1:0]                           |             |
| src_stride   | reg [DMA_LENGTH_WIDTH-1:0]                           |             |
| gen_last     | reg                                                  |             |
| req_id       | reg [1:0]                                            |             |
| eot_id       | reg [1:0]                                            |             |
| last_req     | reg [3:0]                                            |             |
| out_last     | wire                                                 |             |
## Processes
- unnamed: ( @(posedge req_aclk) )
- unnamed: ( @(posedge req_aclk) )
- unnamed: ( @(posedge req_aclk) )
- unnamed: ( @(posedge req_aclk) )
- unnamed: ( @(posedge req_aclk) )
- unnamed: ( @(posedge req_aclk) )
- unnamed: ( @(posedge req_aclk) )
