# Entity: util_axis_fifo_address_generator

- **File**: util_axis_fifo_address_generator.v
## Diagram

![Diagram](util_axis_fifo_address_generator.svg "Diagram")
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

| Generic name  | Type                | Value | Description                         |
| ------------- | ------------------- | ----- | ----------------------------------- |
| ASYNC_CLK     |                     | 0     | single or double clocked FIFO       |
| ADDRESS_WIDTH |                     | 4     | address width, effective FIFO depth |
| ADDRESS_WIDTH | [ADDRESS_WIDTH-1:0] | 16    |                                     |
| ADDRESS_WIDTH | [ADDRESS_WIDTH-1:0] | 16    |                                     |
## Ports

| Port name           | Direction | Type                | Description                   |
| ------------------- | --------- | ------------------- | ----------------------------- |
| m_axis_aclk         | input     |                     | Read interface - Sink side    |
| m_axis_aresetn      | input     |                     |                               |
| m_axis_ready        | input     |                     |                               |
| m_axis_valid        | output    |                     |                               |
| m_axis_empty        | output    |                     |                               |
| m_axis_almost_empty | output    |                     |                               |
| m_axis_raddr        | output    | [ADDRESS_WIDTH-1:0] |                               |
| m_axis_level        | output    | [ADDRESS_WIDTH-1:0] |                               |
| s_axis_aclk         | input     |                     | Write interface - Source side |
| s_axis_aresetn      | input     |                     |                               |
| s_axis_ready        | output    |                     |                               |
| s_axis_valid        | input     |                     |                               |
| s_axis_full         | output    |                     |                               |
| s_axis_almost_full  | output    |                     |                               |
| s_axis_waddr        | output    | [ADDRESS_WIDTH-1:0] |                               |
| s_axis_room         | output    | [ADDRESS_WIDTH-1:0] |                               |
## Signals

| Name             | Type                     | Description                                                                                     |
| ---------------- | ------------------------ | ----------------------------------------------------------------------------------------------- |
| s_axis_waddr_reg | reg [ADDRESS_WIDTH:0]    | Definition of address counters All the counters are wider with one bit to indicate wraparounds  |
| m_axis_raddr_reg | reg [ADDRESS_WIDTH:0]    |                                                                                                 |
| s_axis_raddr_reg | wire [ADDRESS_WIDTH:0]   |                                                                                                 |
| m_axis_waddr_reg | wire [ADDRESS_WIDTH:0]   |                                                                                                 |
| s_axis_write_s   | wire                     |                                                                                                 |
| s_axis_ready_s   | wire                     |                                                                                                 |
| m_axis_read_s    | wire                     |                                                                                                 |
| m_axis_valid_s   | wire                     |                                                                                                 |
| m_axis_level_s   | wire [ADDRESS_WIDTH-1:0] |                                                                                                 |
| s_axis_fifo_fill | wire [ADDRESS_WIDTH:0]   |                                                                                                 |
| m_axis_fifo_fill | wire [ADDRESS_WIDTH:0]   |                                                                                                 |
## Constants

| Name       | Type | Value     | Description |
| ---------- | ---- | --------- | ----------- |
| FIFO_DEPTH |      | undefined |             |
## Processes
- unnamed: ( @(posedge s_axis_aclk) )
- unnamed: ( @(posedge m_axis_aclk) )
