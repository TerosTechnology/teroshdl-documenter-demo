# Entity: dmac_request_generator

- **File**: request_generator.v
## Diagram

![Diagram](request_generator.svg "Diagram")
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
| ID_WIDTH                  |      | 3     |             |
| BURSTS_PER_TRANSFER_WIDTH |      | 17    |             |
## Ports

| Port name              | Direction | Type                            | Description |
| ---------------------- | --------- | ------------------------------- | ----------- |
| clk                    | input     |                                 |             |
| resetn                 | input     |                                 |             |
| request_id             | output    | [ID_WIDTH-1:0]                  |             |
| response_id            | input     | [ID_WIDTH-1:0]                  |             |
| rewind_req_valid       | input     |                                 |             |
| rewind_req_ready       | output    |                                 |             |
| rewind_req_data        | input     | [ID_WIDTH+3-1:0]                |             |
| rewind_state           | output    |                                 |             |
| abort_req              | output    |                                 |             |
| completion_req_valid   | output    | reg                             |             |
| completion_req_ready   | input     |                                 |             |
| completion_req_last    | output    |                                 |             |
| completion_transfer_id | output    | [1:0]                           |             |
| req_valid              | input     |                                 |             |
| req_ready              | output    |                                 |             |
| req_burst_count        | input     | [BURSTS_PER_TRANSFER_WIDTH-1:0] |             |
| req_xlast              | input     |                                 |             |
| enable                 | input     |                                 |             |
| eot                    | output    |                                 |             |
## Signals

| Name                    | Type                                | Description                                                                                                                                                                                                                                                                                                     |
| ----------------------- | ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| state                   | reg [2:0]                           |                                                                                                                                                                                                                                                                                                                 |
| nx_state                | reg [2:0]                           |                                                                                                                                                                                                                                                                                                                 |
| rew_transfer_id         | reg [1:0]                           |                                                                                                                                                                                                                                                                                                                 |
| rew_req_xlast           | reg                                 |                                                                                                                                                                                                                                                                                                                 |
| rew_id                  | reg [ID_WIDTH-1:0]                  |                                                                                                                                                                                                                                                                                                                 |
| cur_transfer_id         | reg                                 |                                                                                                                                                                                                                                                                                                                 |
| cur_req_xlast           | reg                                 |                                                                                                                                                                                                                                                                                                                 |
| transfer_id_match       | wire                                |                                                                                                                                                                                                                                                                                                                 |
| nx_completion_req_valid | reg                                 |                                                                                                                                                                                                                                                                                                                 |
| burst_count             | reg [BURSTS_PER_TRANSFER_WIDTH-1:0] |   * Here we only need to count the number of bursts, which means we can ignore  * the lower bits of the byte count. The last last burst may not contain the  * maximum number of bytes, but the address_generator and data_mover will take  * care that only the requested ammount of bytes is transfered.  */  |
| cur_burst_length        | reg [BURSTS_PER_TRANSFER_WIDTH-1:0] |                                                                                                                                                                                                                                                                                                                 |
| id                      | reg [ID_WIDTH-1:0]                  |                                                                                                                                                                                                                                                                                                                 |
| id_next                 | wire [ID_WIDTH-1:0]                 |                                                                                                                                                                                                                                                                                                                 |
| incr_en                 | wire                                |                                                                                                                                                                                                                                                                                                                 |
| incr_id                 | wire                                |                                                                                                                                                                                                                                                                                                                 |
## Constants

| Name            | Type | Value | Description |
| --------------- | ---- | ----- | ----------- |
| STATE_IDLE      |      | 3'h0  |             |
| STATE_GEN_ID    |      | 3'h1  |             |
| STATE_REWIND_ID |      | 3'h2  |             |
| STATE_CONSUME   |      | 3'h3  |             |
| STATE_WAIT_LAST |      | 3'h4  |             |
## Processes
- unnamed: ( @(posedge clk) )
  - **Type:** always
- unnamed: ( @(posedge clk) )
  - **Type:** always
- unnamed: ( @(posedge clk) )
  - **Type:** always
- unnamed: ( @(posedge clk) )
  - **Type:** always
- unnamed: ( @(posedge clk) )
  - **Type:** always
- unnamed: ( @(*) )
  - **Type:** always
**Description**
  * Once rewind request is received we need to stop incrementing the burst ID.  *  * If the current segment matches the segment that was interrupted and  * if it was a last segment we ignore consecutive segments until the last  * segment is received, in other case we can jump to the next segment.  *  * If the current segment is newer than the one got interrupted and the  * interrupted one was a last segment we need to replay the current  * segment with the adjusted burst ID. If the interrupted segment was not last  * we need to consume/ignore all segments until a last segment is received.  *  * Completion requests are generated for every segment that is  * consumed/ignored. These are handled by the response_manager once the  * interrupted segment got transferred to the destination.  */ 
- unnamed: ( @(posedge clk) )
  - **Type:** always
- unnamed: ( @(posedge clk) )
  - **Type:** always
- unnamed: ( @(posedge clk) )
  - **Type:** always
