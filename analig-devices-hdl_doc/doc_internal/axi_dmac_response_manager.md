# Entity: axi_dmac_response_manager

- **File**: axi_dmac_response_manager.v
## Diagram

![Diagram](axi_dmac_response_manager.svg "Diagram")
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

| Generic name             | Type | Value                        | Description |
| ------------------------ | ---- | ---------------------------- | ----------- |
| DMA_DATA_WIDTH_SRC       |      | 64                           |             |
| DMA_DATA_WIDTH_DEST      |      | 64                           |             |
| DMA_LENGTH_WIDTH         |      | 24                           |             |
| BYTES_PER_BURST_WIDTH    |      | 7                            |             |
| BYTES_PER_BEAT_WIDTH_SRC |      | $clog2(DMA_DATA_WIDTH_SRC/8) |             |
| ASYNC_CLK_DEST_REQ       |      | 1                            |             |
## Ports

| Port name                       | Direction | Type                            | Description                   |
| ------------------------------- | --------- | ------------------------------- | ----------------------------- |
| dest_clk                        | input     |                                 | Interface to destination side |
| dest_resetn                     | input     |                                 |                               |
| dest_response_valid             | input     |                                 |                               |
| dest_response_ready             | output    |                                 |                               |
| dest_response_resp              | input     | [1:0]                           |                               |
| dest_response_partial           | input     |                                 |                               |
| dest_response_resp_eot          | input     |                                 |                               |
| dest_response_data_burst_length | input     | [BYTES_PER_BURST_WIDTH-1:0]     |                               |
| req_clk                         | input     |                                 | Interface to processor        |
| req_resetn                      | input     |                                 |                               |
| response_eot                    | output    |                                 |                               |
| measured_burst_length           | output    | reg [BYTES_PER_BURST_WIDTH-1:0] |                               |
| response_partial                | output    |                                 |                               |
| response_valid                  | output    | reg                             |                               |
| response_ready                  | input     |                                 |                               |
| completion_req_valid            | input     |                                 | Interface to requester side   |
| completion_req_ready            | output    | reg                             |                               |
| completion_req_last             | input     |                                 |                               |
| completion_transfer_id          | input     | [1:0]                           |                               |
## Signals

| Name                                | Type                             | Description |
| ----------------------------------- | -------------------------------- | ----------- |
| state                               | reg [2:0]                        |             |
| nx_state                            | reg [2:0]                        |             |
| do_acc_st                           | wire                             |             |
| do_compl                            | wire                             |             |
| req_eot                             | reg                              |             |
| req_response_partial                | reg                              |             |
| req_response_dest_data_burst_length | reg [BYTES_PER_BURST_WIDTH-1:0]  |             |
| response_dest_valid                 | wire                             |             |
| response_dest_ready                 | reg                              |             |
| response_dest_resp                  | wire [1:0]                       |             |
| response_dest_resp_eot              | wire                             |             |
| response_dest_data_burst_length     | wire [BYTES_PER_BURST_WIDTH-1:0] |             |
| completion_req                      | wire                             |             |
| to_complete_count                   | reg [1:0]                        |             |
| transfer_id                         | reg [1:0]                        |             |
| completion_req_last_found           | reg                              |             |
## Constants

| Name                 | Type | Value                                           | Description |
| -------------------- | ---- | ----------------------------------------------- | ----------- |
| STATE_IDLE           |      | 3'h0                                            |             |
| STATE_ACC            |      | 3'h1                                            |             |
| STATE_WRITE_RESPR    |      | 3'h2                                            |             |
| STATE_ZERO_COMPL     |      | 3'h3                                            |             |
| STATE_WRITE_ZRCMPL   |      | 3'h4                                            |             |
| DEST_SRC_RATIO       |      | DMA_DATA_WIDTH_DEST/DMA_DATA_WIDTH_SRC          |             |
| DEST_SRC_RATIO_WIDTH |      |                                                 |             |
| BYTES_PER_BEAT_WIDTH |      | DEST_SRC_RATIO_WIDTH + BYTES_PER_BEAT_WIDTH_SRC |             |
| BURST_LEN_WIDTH      |      | BYTES_PER_BURST_WIDTH - BYTES_PER_BEAT_WIDTH    |             |
## Processes
- unnamed: ( @(posedge req_clk) )
- unnamed: ( @(posedge req_clk) )
- unnamed: ( @(posedge req_clk) )
- unnamed: ( @(posedge req_clk) )
- unnamed: ( @(*) )
- unnamed: ( @(posedge req_clk) )
- unnamed: ( @(posedge req_clk) )
**Description**
Once the last completion request from request generator is received
we can wait for completions from the destination side

- unnamed: ( @(posedge req_clk) )
**Description**
Once the last completion is received wit until all completions are done

- unnamed: ( @(posedge req_clk) )
**Description**
Track transfers so we can tell when did the destination completed all its
transfers

- unnamed: ( @(posedge req_clk) )
**Description**
Count how many transfers we need to complete

## Instantiations

- i_dest_response_fifo: util_axis_fifo
