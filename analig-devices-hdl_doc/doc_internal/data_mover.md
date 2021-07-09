# Entity: dmac_data_mover

## Diagram

![Diagram](data_mover.svg "Diagram")
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
| DATA_WIDTH            |      | 64    |             |
| BEATS_PER_BURST_WIDTH |      | 4     |             |
| ALLOW_ABORT           |      | 0     |             |
## Ports

| Port name                  | Direction | Type                        | Description |
| -------------------------- | --------- | --------------------------- | ----------- |
| clk                        | input     |                             |             |
| resetn                     | input     |                             |             |
| request_id                 | input     | [ID_WIDTH-1:0]              |             |
| response_id                | output    | [ID_WIDTH-1:0]              |             |
| eot                        | input     |                             |             |
| rewind_req_valid           | output    |                             |             |
| rewind_req_ready           | input     |                             |             |
| rewind_req_data            | output    | [ID_WIDTH+3-1:0]            |             |
| bl_valid                   | output    | reg                         |             |
| bl_ready                   | input     |                             |             |
| measured_last_burst_length | output    | [BEATS_PER_BURST_WIDTH-1:0] |             |
| block_descr_to_dst         | output    |                             |             |
| source_id                  | output    | [ID_WIDTH-1:0]              |             |
| source_eot                 | output    |                             |             |
| xfer_req                   | output    |                             |             |
| s_axi_ready                | output    |                             |             |
| s_axi_valid                | input     |                             |             |
| s_axi_data                 | input     | [DATA_WIDTH-1:0]            |             |
| s_axi_last                 | input     |                             |             |
| s_axi_sync                 | input     |                             |             |
| m_axi_valid                | output    |                             |             |
| m_axi_data                 | output    | [DATA_WIDTH-1:0]            |             |
| m_axi_last                 | output    |                             |             |
| m_axi_partial_burst        | output    |                             |             |
| req_valid                  | input     |                             |             |
| req_ready                  | output    |                             |             |
| req_last_burst_length      | input     | [BEATS_PER_BURST_WIDTH-1:0] |             |
| req_sync_transfer_start    | input     |                             |             |
| req_xlast                  | input     |                             |             |
## Signals

| Name                   | Type                            | Description |
| ---------------------- | ------------------------------- | ----------- |
| last_burst_length      | reg [BEATS_PER_BURST_WIDTH-1:0] |             |
| beat_counter           | reg [BEATS_PER_BURST_WIDTH-1:0] |             |
| beat_counter_minus_one | reg [BEATS_PER_BURST_WIDTH-1:0] |             |
| id                     | reg [ID_WIDTH-1:0]              |             |
| id_next                | reg [ID_WIDTH-1:0]              |             |
| pending_burst          | reg                             |             |
| active                 | reg                             |             |
| last_eot               | reg                             |             |
| last_non_eot           | reg                             |             |
| needs_sync             | reg                             |             |
| has_sync               | wire                            |             |
| s_axi_sync_valid       | wire                            |             |
| transfer_abort_s       | wire                            |             |
| last_load              | wire                            |             |
| last                   | wire                            |             |
| early_tlast            | wire                            |             |
## Constants

| Name             | Type | Value     | Description |
| ---------------- | ---- | --------- | ----------- |
| BEAT_COUNTER_MAX |      | undefined |             |
## Processes
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(*) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
