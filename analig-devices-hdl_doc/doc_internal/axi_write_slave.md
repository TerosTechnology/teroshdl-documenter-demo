# Entity: axi_write_slave

- **File**: axi_write_slave.v
## Diagram

![Diagram](axi_write_slave.svg "Diagram")
## Description

 ***************************************************************************
 ***************************************************************************
 Copyright 2018 (c) Analog Devices, Inc. All rights reserved.

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

| Generic name     | Type | Value | Description |
| ---------------- | ---- | ----- | ----------- |
| DATA_WIDTH       |      | 32    |             |
| WRITE_ACCEPTANCE |      | 3     |             |
## Ports

| Port name | Direction | Type               | Description |
| --------- | --------- | ------------------ | ----------- |
| clk       | input     |                    |             |
| reset     | input     |                    |             |
| awvalid   | input     |                    |             |
| awready   | output    |                    |             |
| awaddr    | input     | [31:0]             |             |
| awlen     | input     | [7:0]              |             |
| awsize    | input     | [2:0]              |             |
| awburst   | input     | [1:0]              |             |
| awprot    | input     | [2:0]              |             |
| awcache   | input     | [3:0]              |             |
| wvalid    | input     |                    |             |
| wready    | output    |                    |             |
| wdata     | input     | [DATA_WIDTH-1:0]   |             |
| wstrb     | input     | [DATA_WIDTH/8-1:0] |             |
| wlast     | input     |                    |             |
| bvalid    | output    |                    |             |
| bready    | input     |                    |             |
| bresp     | output    | [1:0]              |             |
## Signals

| Name            | Type                 | Description |
| --------------- | -------------------- | ----------- |
| beat_last       | wire                 |             |
| resp_count      | reg [4:0]            |             |
| resp_count_next | wire [4:0]           |             |
| data_cmp        | reg [DATA_WIDTH-1:0] |             |
| failed          | reg                  |             |
| resp_count_dec  | wire                 |             |
| resp_count_inc  | wire                 |             |
| byte_count      | integer              |             |
## Processes
- unnamed: ( @(posedge clk) )
  - **Type:** always
- unnamed: ( @(posedge clk) )
  - **Type:** always
- count: ( @(*) )
  - **Type:** always
- gen_data_cmp: ( @(posedge clk) )
  - **Type:** always
## Instantiations

- i_axi_slave: axi_slave
