# Entity: dmac_src_fifo_inf

- **File**: src_fifo_inf.v
## Diagram

![Diagram](src_fifo_inf.svg "Diagram")
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

| Port name                  | Direction | Type                        | Description |
| -------------------------- | --------- | --------------------------- | ----------- |
| clk                        | input     |                             |             |
| resetn                     | input     |                             |             |
| enable                     | input     |                             |             |
| enabled                    | output    |                             |             |
| request_id                 | input     | [ID_WIDTH-1:0]              |             |
| response_id                | output    | [ID_WIDTH-1:0]              |             |
| eot                        | input     |                             |             |
| bl_valid                   | output    |                             |             |
| bl_ready                   | input     |                             |             |
| measured_last_burst_length | output    | [BEATS_PER_BURST_WIDTH-1:0] |             |
| en                         | input     |                             |             |
| din                        | input     | [DATA_WIDTH-1:0]            |             |
| overflow                   | output    |                             |             |
| sync                       | input     |                             |             |
| xfer_req                   | output    |                             |             |
| fifo_valid                 | output    |                             |             |
| fifo_data                  | output    | [DATA_WIDTH-1:0]            |             |
| fifo_last                  | output    |                             |             |
| req_valid                  | input     |                             |             |
| req_ready                  | output    |                             |             |
| req_last_burst_length      | input     | [BEATS_PER_BURST_WIDTH-1:0] |             |
| req_sync_transfer_start    | input     |                             |             |
## Signals

| Name  | Type | Description |
| ----- | ---- | ----------- |
| ready | wire |             |
| valid | wire |             |
## Processes
- unnamed: ( @(posedge clk) )
  - **Type:** always
## Instantiations

- i_data_mover: dmac_data_mover
