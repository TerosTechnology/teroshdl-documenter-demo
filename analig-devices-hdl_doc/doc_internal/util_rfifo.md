# Entity: util_rfifo

- **File**: util_rfifo.v
## Diagram

![Diagram](util_rfifo.svg "Diagram")
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

| Generic name      | Type | Value | Description |
| ----------------- | ---- | ----- | ----------- |
| NUM_OF_CHANNELS   |      | 4     |             |
| DIN_DATA_WIDTH    |      | 32    |             |
| DOUT_DATA_WIDTH   |      | 64    |             |
| DIN_ADDRESS_WIDTH |      | 8     |             |
## Ports

| Port name        | Direction | Type                  | Description     |
| ---------------- | --------- | --------------------- | --------------- |
| din_rstn         | input     |                       | d-in interface  |
| din_clk          | input     |                       |                 |
| din_enable_0     | output    |                       |                 |
| din_valid_0      | output    |                       |                 |
| din_valid_in_0   | input     |                       |                 |
| din_data_0       | input     | [DIN_DATA_WIDTH-1:0]  |                 |
| din_enable_1     | output    |                       |                 |
| din_valid_1      | output    |                       |                 |
| din_valid_in_1   | input     |                       |                 |
| din_data_1       | input     | [DIN_DATA_WIDTH-1:0]  |                 |
| din_enable_2     | output    |                       |                 |
| din_valid_2      | output    |                       |                 |
| din_valid_in_2   | input     |                       |                 |
| din_data_2       | input     | [DIN_DATA_WIDTH-1:0]  |                 |
| din_enable_3     | output    |                       |                 |
| din_valid_3      | output    |                       |                 |
| din_valid_in_3   | input     |                       |                 |
| din_data_3       | input     | [DIN_DATA_WIDTH-1:0]  |                 |
| din_enable_4     | output    |                       |                 |
| din_valid_4      | output    |                       |                 |
| din_valid_in_4   | input     |                       |                 |
| din_data_4       | input     | [DIN_DATA_WIDTH-1:0]  |                 |
| din_enable_5     | output    |                       |                 |
| din_valid_5      | output    |                       |                 |
| din_valid_in_5   | input     |                       |                 |
| din_data_5       | input     | [DIN_DATA_WIDTH-1:0]  |                 |
| din_enable_6     | output    |                       |                 |
| din_valid_6      | output    |                       |                 |
| din_valid_in_6   | input     |                       |                 |
| din_data_6       | input     | [DIN_DATA_WIDTH-1:0]  |                 |
| din_enable_7     | output    |                       |                 |
| din_valid_7      | output    |                       |                 |
| din_valid_in_7   | input     |                       |                 |
| din_data_7       | input     | [DIN_DATA_WIDTH-1:0]  |                 |
| din_unf          | input     |                       |                 |
| dout_rst         | input     |                       | d-out interface |
| dout_clk         | input     |                       |                 |
| dout_enable_0    | input     |                       |                 |
| dout_valid_0     | input     |                       |                 |
| dout_valid_out_0 | output    |                       |                 |
| dout_data_0      | output    | [DOUT_DATA_WIDTH-1:0] |                 |
| dout_enable_1    | input     |                       |                 |
| dout_valid_1     | input     |                       |                 |
| dout_valid_out_1 | output    |                       |                 |
| dout_data_1      | output    | [DOUT_DATA_WIDTH-1:0] |                 |
| dout_enable_2    | input     |                       |                 |
| dout_valid_2     | input     |                       |                 |
| dout_valid_out_2 | output    |                       |                 |
| dout_data_2      | output    | [DOUT_DATA_WIDTH-1:0] |                 |
| dout_enable_3    | input     |                       |                 |
| dout_valid_3     | input     |                       |                 |
| dout_valid_out_3 | output    |                       |                 |
| dout_data_3      | output    | [DOUT_DATA_WIDTH-1:0] |                 |
| dout_enable_4    | input     |                       |                 |
| dout_valid_4     | input     |                       |                 |
| dout_valid_out_4 | output    |                       |                 |
| dout_data_4      | output    | [DOUT_DATA_WIDTH-1:0] |                 |
| dout_enable_5    | input     |                       |                 |
| dout_valid_5     | input     |                       |                 |
| dout_valid_out_5 | output    |                       |                 |
| dout_data_5      | output    | [DOUT_DATA_WIDTH-1:0] |                 |
| dout_enable_6    | input     |                       |                 |
| dout_valid_6     | input     |                       |                 |
| dout_valid_out_6 | output    |                       |                 |
| dout_data_6      | output    | [DOUT_DATA_WIDTH-1:0] |                 |
| dout_enable_7    | input     |                       |                 |
| dout_valid_7     | input     |                       |                 |
| dout_valid_out_7 | output    |                       |                 |
| dout_data_7      | output    | [DOUT_DATA_WIDTH-1:0] |                 |
| dout_unf         | output    |                       |                 |
## Signals

| Name          | Type                                  | Description         |
| ------------- | ------------------------------------- | ------------------- |
| din_wdata     | reg         [(DATA_WIDTH-1):0]        | internal registers  |
| din_waddr     | reg         [(ADDRESS_WIDTH-1):0]     |                     |
| din_wr        | reg                                   |                     |
| din_valid     | reg                                   |                     |
| din_req_cnt   | reg         [ 6:0]                    |                     |
| din_enable_m1 | reg         [ 7:0]                    |                     |
| din_enable    | reg         [ 7:0]                    |                     |
| din_req_t_m1  | reg                                   |                     |
| din_req_t_m2  | reg                                   |                     |
| din_req_t_m3  | reg                                   |                     |
| din_req       | reg                                   |                     |
| din_init      | reg                                   |                     |
| din_unf_d     | reg                                   |                     |
| dout_valid    | reg         [ 7:0]                    |                     |
| dout_data     | reg         [(T_DOUT_DATA_WIDTH+1):0] |                     |
| dout_rdata    | reg         [(DATA_WIDTH-1):0]        |                     |
| dout_enable   | reg         [ 7:0]                    |                     |
| dout_req_t    | reg                                   |                     |
| dout_init     | reg                                   |                     |
| dout_raddr    | reg         [(ADDRESS_WIDTH-1):0]     |                     |
| dout_unf_m1   | reg                                   |                     |
| din_data_s    | wire [(T_DIN_DATA_WIDTH-1):0]         | internal signals    |
| din_req_s     | wire                                  |                     |
| dout_enable_s | wire [ 7:0]                           |                     |
| dout_valid_s  | wire [ 7:0]                           |                     |
| dout_data_s   | wire [(T_DOUT_DATA_WIDTH+1):0]        |                     |
| dout_init_s   | wire                                  |                     |
| dout_rdata_s  | wire [(DATA_WIDTH-1):0]               |                     |
| din_wcnt_s    | wire [ 2:0]                           |                     |
## Constants

| Name              | Type | Value                             | Description |
| ----------------- | ---- | --------------------------------- | ----------- |
| M_MEM_RATIO       |      | DOUT_DATA_WIDTH/DIN_DATA_WIDTH    |             |
| ADDRESS_WIDTH     |      | DIN_ADDRESS_WIDTH                 |             |
| DATA_WIDTH        |      | DOUT_DATA_WIDTH * NUM_OF_CHANNELS |             |
| T_DIN_DATA_WIDTH  |      | DIN_DATA_WIDTH * 8                |             |
| T_DOUT_DATA_WIDTH |      | DOUT_DATA_WIDTH * 8               |             |
## Processes
- unnamed: ( @(posedge din_clk or negedge din_rstn) )
- unnamed: ( @(posedge din_clk or negedge din_rstn) )
- unnamed: ( @(posedge din_clk or negedge din_rstn) )
- unnamed: ( @(posedge dout_clk) )
- unnamed: ( @(posedge dout_clk) )
- unnamed: ( @(posedge dout_clk) )
- unnamed: ( @(posedge dout_clk) )
## Instantiations

- i_mem: ad_mem
**Description**
instantiations

