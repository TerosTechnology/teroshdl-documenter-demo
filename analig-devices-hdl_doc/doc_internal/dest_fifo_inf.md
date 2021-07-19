# Entity: dmac_dest_fifo_inf

- **File**: dest_fifo_inf.v
## Diagram

![Diagram](dest_fifo_inf.svg "Diagram")
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
## Ports

| Port name         | Direction | Type               | Description |
| ----------------- | --------- | ------------------ | ----------- |
| clk               | input     |                    |             |
| resetn            | input     |                    |             |
| enable            | input     |                    |             |
| enabled           | output    |                    |             |
| req_valid         | input     |                    |             |
| req_ready         | output    |                    |             |
| response_id       | output    | [ID_WIDTH-1:0]     |             |
| data_id           | output    | reg [ID_WIDTH-1:0] |             |
| data_eot          | input     |                    |             |
| response_eot      | input     |                    |             |
| en                | input     |                    |             |
| dout              | output    | [DATA_WIDTH-1:0]   |             |
| valid             | output    |                    |             |
| underflow         | output    |                    |             |
| xfer_req          | output    |                    |             |
| fifo_ready        | output    |                    |             |
| fifo_valid        | input     |                    |             |
| fifo_data         | input     | [DATA_WIDTH-1:0]   |             |
| fifo_last         | input     |                    |             |
| response_valid    | output    |                    |             |
| response_ready    | input     |                    |             |
| response_resp_eot | output    |                    |             |
| response_resp     | output    | [1:0]              |             |
## Signals

| Name           | Type | Description                  |
| -------------- | ---- | ---------------------------- |
| active         | reg  |                              |
| fifo_last_beat | wire | Last beat of the burst */    |
| fifo_eot_beat  | wire | Last beat of the segment */  |
## Processes
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
## Instantiations

- i_response_generator: dmac_response_generator
