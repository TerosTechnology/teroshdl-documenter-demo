# Entity: util_axis_fifo_asym

- **File**: util_axis_fifo_asym.v
## Diagram

![Diagram](util_axis_fifo_asym.svg "Diagram")
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

| Generic name           | Type | Value | Description |
| ---------------------- | ---- | ----- | ----------- |
| ASYNC_CLK              |      | 1     |             |
| S_DATA_WIDTH           |      | 64    |             |
| S_ADDRESS_WIDTH        |      | 5     |             |
| M_DATA_WIDTH           |      | 128   |             |
| M_AXIS_REGISTERED      |      | 1     |             |
| ALMOST_EMPTY_THRESHOLD |      | 4     |             |
| ALMOST_FULL_THRESHOLD  |      | 4     |             |
| TLAST_EN               |      | 0     |             |
| TKEEP_EN               |      | 0     |             |
## Ports

| Port name           | Direction | Type                  | Description |
| ------------------- | --------- | --------------------- | ----------- |
| m_axis_aclk         | input     |                       |             |
| m_axis_aresetn      | input     |                       |             |
| m_axis_ready        | input     |                       |             |
| m_axis_valid        | output    |                       |             |
| m_axis_data         | output    | [M_DATA_WIDTH-1:0]    |             |
| m_axis_tkeep        | output    | [M_DATA_WIDTH/8-1:0]  |             |
| m_axis_tlast        | output    |                       |             |
| m_axis_empty        | output    |                       |             |
| m_axis_almost_empty | output    |                       |             |
| m_axis_level        | output    | [31:0]                |             |
| s_axis_aclk         | input     |                       |             |
| s_axis_aresetn      | input     |                       |             |
| s_axis_ready        | output    |                       |             |
| s_axis_valid        | input     |                       |             |
| s_axis_data         | input     | [S_DATA_WIDTH-1:0]    |             |
| s_axis_tkeep        | input     | [S_DATA_WIDTH/8-1:0]  |             |
| s_axis_tlast        | input     |                       |             |
| s_axis_full         | output    |                       |             |
| s_axis_almost_full  | output    |                       |             |
| s_axis_room         | output    | [S_ADDRESS_WIDTH-1:0] |             |
## Signals

| Name                      | Type                       | Description                   |
| ------------------------- | -------------------------- | ----------------------------- |
| s_axis_counter            | reg [$clog2(RATIO)-1:0]    |  slave and master sequencers  |
| m_axis_counter            | reg [$clog2(RATIO)-1:0]    |                               |
| m_axis_ready_int_s        | wire [RATIO-1:0]           |                               |
| m_axis_valid_int_s        | wire [RATIO-1:0]           |                               |
| m_axis_data_int_s         | wire [RATIO*A_WIDTH-1:0]   |                               |
| m_axis_tkeep_int_s        | wire [RATIO*A_WIDTH/8-1:0] |                               |
| m_axis_tlast_int_s        | wire [RATIO-1:0]           |                               |
| m_axis_empty_int_s        | wire [RATIO-1:0]           |                               |
| m_axis_almost_empty_int_s | wire [RATIO-1:0]           |                               |
| m_axis_level_int_s        | wire [RATIO*A_ADDRESS-1:0] |                               |
| s_axis_ready_int_s        | wire [RATIO-1:0]           |                               |
| s_axis_valid_int_s        | wire [RATIO-1:0]           |                               |
| s_axis_data_int_s         | wire [RATIO*A_WIDTH-1:0]   |                               |
| s_axis_tkeep_int_s        | wire [RATIO*A_WIDTH/8-1:0] |                               |
| s_axis_tlast_int_s        | wire [RATIO-1:0]           |                               |
| s_axis_full_int_s         | wire [RATIO-1:0]           |                               |
| s_axis_almost_full_int_s  | wire [RATIO-1:0]           |                               |
| s_axis_room_int_s         | wire [RATIO*A_ADDRESS-1:0] |                               |
| s_axis_tlast_d            | reg                        |  slave handshake counter      |
## Constants

| Name                     | Type | Value                     | Description                                                                 |
| ------------------------ | ---- | ------------------------- | --------------------------------------------------------------------------- |
| RATIO                    |      | S_DATA_WIDTH/M_DATA_WIDTH |  bus width ratio                                                            |
| A_WIDTH                  |      | M_DATA_WIDTH              |  atomic parameters - NOTE: depth is always defined by the slave attributes  |
| A_ADDRESS                |      | S_ADDRESS_WIDTH           |                                                                             |
| A_ALMOST_FULL_THRESHOLD  |      | ALMOST_FULL_THRESHOLD     |                                                                             |
| A_ALMOST_EMPTY_THRESHOLD |      | ALMOST_EMPTY_THRESHOLD    |                                                                             |
## Processes
- unnamed: ( @(posedge s_axis_aclk) )
  - **Type:** always
