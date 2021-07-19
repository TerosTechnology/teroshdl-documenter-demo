# Entity: dmac_src_axi_stream

- **File**: src_axi_stream.v
## Diagram

![Diagram](src_axi_stream.svg "Diagram")
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
| S_AXIS_DATA_WIDTH     |      | 64    |             |
| LENGTH_WIDTH          |      | 24    |             |
| BEATS_PER_BURST_WIDTH |      | 4     |             |
## Ports

| Port name                  | Direction | Type                        | Description |
| -------------------------- | --------- | --------------------------- | ----------- |
| s_axis_aclk                | input     |                             |             |
| s_axis_aresetn             | input     |                             |             |
| enable                     | input     |                             |             |
| enabled                    | output    |                             |             |
| request_id                 | input     | [ID_WIDTH-1:0]              |             |
| response_id                | output    | [ID_WIDTH-1:0]              |             |
| eot                        | input     |                             |             |
| rewind_req_valid           | output    |                             |             |
| rewind_req_ready           | input     |                             |             |
| rewind_req_data            | output    | [ID_WIDTH+3-1:0]            |             |
| bl_valid                   | output    |                             |             |
| bl_ready                   | input     |                             |             |
| measured_last_burst_length | output    | [BEATS_PER_BURST_WIDTH-1:0] |             |
| block_descr_to_dst         | output    |                             |             |
| source_id                  | output    | [ID_WIDTH-1:0]              |             |
| source_eot                 | output    |                             |             |
| s_axis_ready               | output    |                             |             |
| s_axis_valid               | input     |                             |             |
| s_axis_data                | input     | [S_AXIS_DATA_WIDTH-1:0]     |             |
| s_axis_user                | input     | [0:0]                       |             |
| s_axis_last                | input     |                             |             |
| s_axis_xfer_req            | output    |                             |             |
| fifo_valid                 | output    |                             |             |
| fifo_data                  | output    | [S_AXIS_DATA_WIDTH-1:0]     |             |
| fifo_last                  | output    |                             |             |
| fifo_partial_burst         | output    |                             |             |
| req_valid                  | input     |                             |             |
| req_ready                  | output    |                             |             |
| req_last_burst_length      | input     | [BEATS_PER_BURST_WIDTH-1:0] |             |
| req_sync_transfer_start    | input     |                             |             |
| req_xlast                  | input     |                             |             |
## Instantiations

- i_data_mover: dmac_data_mover
