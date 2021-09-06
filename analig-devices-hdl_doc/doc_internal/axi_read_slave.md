# Entity: axi_read_slave

- **File**: axi_read_slave.v
## Diagram

![Diagram](axi_read_slave.svg "Diagram")
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

| Generic name    | Type | Value | Description |
| --------------- | ---- | ----- | ----------- |
| DATA_WIDTH      |      | 32    |             |
| READ_ACCEPTANCE |      | 4     |             |
| MIN_LATENCY     |      | 48    |             |
| MAX_LATENCY     |      | 48    |             |
## Ports

| Port name | Direction | Type             | Description |
| --------- | --------- | ---------------- | ----------- |
| clk       | input     |                  |             |
| reset     | input     |                  |             |
| arvalid   | input     |                  |             |
| arready   | output    |                  |             |
| araddr    | input     | [31:0]           |             |
| arlen     | input     | [7:0]            |             |
| arsize    | input     | [2:0]            |             |
| arburst   | input     | [1:0]            |             |
| arprot    | input     | [2:0]            |             |
| arcache   | input     | [3:0]            |             |
| rvalid    | output    |                  |             |
| rready    | input     |                  |             |
| rdata     | output    | [DATA_WIDTH-1:0] |             |
| rresp     | output    | [1:0]            |             |
| rlast     | output    |                  |             |
## Signals

| Name      | Type                 | Description |
| --------- | -------------------- | ----------- |
| data      | reg [DATA_WIDTH-1:0] |             |
| beat_addr | wire [31:0]          |             |
## Processes
- gen_data: ( @(*) )
  - **Type:** always
## Instantiations

- i_axi_slave: axi_slave
