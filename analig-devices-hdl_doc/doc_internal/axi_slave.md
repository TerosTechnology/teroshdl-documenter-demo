# Entity: axi_slave

- **File**: axi_slave.v
## Diagram

![Diagram](axi_slave.svg "Diagram")
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

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| DATA_WIDTH   |      | 32    |             |
| ACCEPTANCE   |      | 3     |             |
| MIN_LATENCY  |      | 16    |             |
| MAX_LATENCY  |      | 32    |             |
## Ports

| Port name | Direction | Type   | Description |
| --------- | --------- | ------ | ----------- |
| clk       | input     |        |             |
| reset     | input     |        |             |
| valid     | input     |        |             |
| ready     | output    |        |             |
| addr      | input     | [31:0] |             |
| len       | input     | [7:0]  |             |
| size      | input     | [2:0]  |             |
| burst     | input     | [1:0]  |             |
| prot      | input     | [2:0]  |             |
| cache     | input     | [3:0]  |             |
| beat_stb  | output    |        |             |
| beat_ack  | input     |        |             |
| beat_addr | output    | [31:0] |             |
| beat_last | output    |        |             |
## Signals

| Name           | Type              | Description |
| -------------- | ----------------- | ----------- |
| timestamp      | reg [31:0]        |             |
| req_fifo       | reg [32+32+8-1:0] |             |
| req_fifo_rd    | reg [3:0]         |             |
| req_fifo_wr    | reg [3:0]         |             |
| req_fifo_level | wire [3:0]        |             |
| beat_counter   | reg [7:0]         |             |
## Processes
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
