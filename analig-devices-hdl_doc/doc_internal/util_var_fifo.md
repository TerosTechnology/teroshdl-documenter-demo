# Entity: util_var_fifo

- **File**: util_var_fifo.v
## Diagram

![Diagram](util_var_fifo.svg "Diagram")
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

| Generic name  | Type | Value | Description  |
| ------------- | ---- | ----- | ------------ |
| DATA_WIDTH    |      | 32    |  parameters  |
| ADDRESS_WIDTH |      | 13    |              |
## Ports

| Port name      | Direction | Type                | Description |
| -------------- | --------- | ------------------- | ----------- |
| clk            | input     |                     |             |
| rst            | input     |                     |             |
| depth          | input     | [31:0]              |             |
| data_in        | input     | [DATA_WIDTH -1:0]   |             |
| data_in_valid  | input     |                     |             |
| data_out       | output    | [DATA_WIDTH-1:0]    |             |
| data_out_valid | output    |                     |             |
| wea_w          | output    |                     |             |
| en_w           | output    |                     |             |
| addr_w         | output    | [ADDRESS_WIDTH-1:0] |             |
| din_w          | output    | [DATA_WIDTH-1:0]    |             |
| en_r           | output    |                     |             |
| addr_r         | output    | [ADDRESS_WIDTH-1:0] |             |
| dout_r         | input     | [DATA_WIDTH-1:0]    |             |
## Signals

| Name                  | Type                    | Description          |
| --------------------- | ----------------------- | -------------------- |
| addra                 | reg [ADDRESS_WIDTH-1:0] |  internal registers  |
| addrb                 | reg [ADDRESS_WIDTH-1:0] |                      |
| depth_d1              | reg [31:0]              |                      |
| data_in_d1            | reg [DATA_WIDTH-1:0]    |                      |
| data_in_d2            | reg [DATA_WIDTH-1:0]    |                      |
| data_in_d3            | reg [DATA_WIDTH-1:0]    |                      |
| data_in_d4            | reg [DATA_WIDTH-1:0]    |                      |
| data_active           | reg                     |                      |
| fifo_active           | reg                     |                      |
| data_in_valid_d1      | reg                     |                      |
| data_in_valid_d2      | reg                     |                      |
| interpolation_on      | reg                     |                      |
| interpolation_on_d1   | reg                     |                      |
| interpolation_by_2    | reg                     |                      |
| interpolation_by_2_d1 | reg                     |                      |
| data_out_d1           | reg [DATA_WIDTH-1:0]    |                      |
| data_out_d2           | reg [DATA_WIDTH-1:0]    |                      |
| data_out_d3           | reg [DATA_WIDTH-1:0]    |                      |
| reset                 | wire                    |  internal signals    |
| data_out_s            | wire [DATA_WIDTH-1:0]   |                      |
| data_out_valid_s      | wire                    |                      |
## Constants

| Name      | Type | Value                    | Description |
| --------- | ---- | ------------------------ | ----------- |
| MAX_DEPTH |      | (2 ** ADDRESS_WIDTH) - 1 |             |
## Processes
- unnamed: ( @(posedge clk) )
  - **Type:** always
</br>**Description**
 in case the interpolation is on, the data is available with one sample  delay. If interpolation is off, the data is available with two or three  sample delay. Add an extra delay if interpolation is on. 
- unnamed: ( @(posedge clk) )
  - **Type:** always
- unnamed: ( @(posedge clk) )
  - **Type:** always
