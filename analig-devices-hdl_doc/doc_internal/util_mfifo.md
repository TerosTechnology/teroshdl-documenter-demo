# Entity: util_mfifo

## Diagram

![Diagram](util_mfifo.svg "Diagram")
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

| Generic name    | Type | Value | Description |
| --------------- | ---- | ----- | ----------- |
| NUM_OF_CHANNELS |      | 4     |             |
| DIN_DATA_WIDTH  |      | 32    |             |
| ADDRESS_WIDTH   |      | 8     |             |
## Ports

| Port name   | Direction | Type                 | Description     |
| ----------- | --------- | -------------------- | --------------- |
| din_rst     | input     |                      | d-in interface  |
| din_clk     | input     |                      |                 |
| din_valid   | input     |                      |                 |
| din_data_0  | input     | [DIN_DATA_WIDTH-1:0] |                 |
| din_data_1  | input     | [DIN_DATA_WIDTH-1:0] |                 |
| din_data_2  | input     | [DIN_DATA_WIDTH-1:0] |                 |
| din_data_3  | input     | [DIN_DATA_WIDTH-1:0] |                 |
| din_data_4  | input     | [DIN_DATA_WIDTH-1:0] |                 |
| din_data_5  | input     | [DIN_DATA_WIDTH-1:0] |                 |
| din_data_6  | input     | [DIN_DATA_WIDTH-1:0] |                 |
| din_data_7  | input     | [DIN_DATA_WIDTH-1:0] |                 |
| dout_rst    | input     |                      | d-out interface |
| dout_clk    | input     |                      |                 |
| dout_valid  | output    |                      |                 |
| dout_data_0 | output    | [15:0]               |                 |
| dout_data_1 | output    | [15:0]               |                 |
| dout_data_2 | output    | [15:0]               |                 |
| dout_data_3 | output    | [15:0]               |                 |
| dout_data_4 | output    | [15:0]               |                 |
| dout_data_5 | output    | [15:0]               |                 |
| dout_data_6 | output    | [15:0]               |                 |
| dout_data_7 | output    | [15:0]               |                 |
## Signals

| Name               | Type                           | Description         |
| ------------------ | ------------------------------ | ------------------- |
| din_dout_toggle_m1 | reg                            | internal registers  |
| din_dout_toggle_m2 | reg                            |                     |
| din_dout_toggle_m3 | reg                            |                     |
| din_wr             | reg                            |                     |
| din_waddr          | reg     [(ADDRESS_WIDTH-1):0]  |                     |
| din_enable         | reg                            |                     |
| din_toggle         | reg                            |                     |
| dout_din_toggle_m1 | reg                            |                     |
| dout_din_toggle_m2 | reg                            |                     |
| dout_din_toggle_m3 | reg                            |                     |
| dout_cnt           | reg     [ 4:0]                 |                     |
| dout_ld            | reg                            |                     |
| dout_ld_d          | reg                            |                     |
| dout_raddr         | reg     [(ADDRESS_WIDTH-1):0]  |                     |
| dout_enable        | reg                            |                     |
| dout_toggle        | reg                            |                     |
| dout_rdata_0       | reg     [(DIN_DATA_WIDTH-1):0] |                     |
| dout_rdata_1       | reg     [(DIN_DATA_WIDTH-1):0] |                     |
| dout_rdata_2       | reg     [(DIN_DATA_WIDTH-1):0] |                     |
| dout_rdata_3       | reg     [(DIN_DATA_WIDTH-1):0] |                     |
| dout_rdata_4       | reg     [(DIN_DATA_WIDTH-1):0] |                     |
| dout_rdata_5       | reg     [(DIN_DATA_WIDTH-1):0] |                     |
| dout_rdata_6       | reg     [(DIN_DATA_WIDTH-1):0] |                     |
| dout_rdata_7       | reg     [(DIN_DATA_WIDTH-1):0] |                     |
| din_wdata_s        | wire [(DIN_DATA_WIDTH-1):0]    | internal signals    |
| din_waddr_max_s    | wire                           |                     |
| din_dout_toggle_s  | wire                           |                     |
| dout_raddr_max_s   | wire                           |                     |
| dout_rd_s          | wire                           |                     |
| dout_din_toggle_s  | wire                           |                     |
| dout_rdata_s       | wire [(DIN_DATA_WIDTH-1):0]    |                     |
## Processes
- unnamed: ( @(posedge din_clk or posedge din_rst) )
- unnamed: ( @(posedge dout_clk or posedge dout_rst) )
- unnamed: ( @(posedge dout_clk or posedge dout_rst) )
