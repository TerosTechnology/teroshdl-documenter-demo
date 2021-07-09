# Entity: pack_network

## Diagram

![Diagram](pack_network.svg "Diagram")
## Description

***************************************************************************
 ***************************************************************************
 Copyright 2017 (c) Analog Devices, Inc. All rights reserved.
 In this HDL repository, there are many different and unique modules, consisting
 of various HDL (Verilog or VHDL) components. The individual modules are
 developed independently, and may be accompanied by separate and unique license
 terms.
 The user should read each of these license terms, and understand the
 freedoms and responsabilities that he or she has by using this source/core.
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

| Generic name       | Type | Value | Description |
| ------------------ | ---- | ----- | ----------- |
| PORT_ADDRESS_WIDTH |      | 1     |             |
| MUX_ORDER          |      | 1     |             |
| MIN_STAGE          |      | 1     |             |
| NUM_STAGES         |      | 1     |             |
| PACK               |      | 0     |             |
| PORT_DATA_WIDTH    |      | 16    |             |
## Ports

| Port name    | Direction | Type                                           | Description |
| ------------ | --------- | ---------------------------------------------- | ----------- |
| clk          | input     |                                                |             |
| ce_ctrl      | input     |                                                |             |
| rotate       | input     | [PORT_ADDRESS_WIDTH-1:0]                       |             |
| prefix_count | input     | [2**PORT_ADDRESS_WIDTH*PORT_ADDRESS_WIDTH-1:0] |             |
| data_in      | input     | [PORT_DATA_WIDTH * 2**PORT_ADDRESS_WIDTH-1:0]  |             |
| data_out     | output    | [PORT_DATA_WIDTH * 2**PORT_ADDRESS_WIDTH-1:0]  |             |
## Signals

| Name   | Type                  | Description |
| ------ | --------------------- | ----------- |
| ctrl_s | wire [CTRL_WIDTH-1:0] |             |
| ctrl   | reg [CTRL_WIDTH-1:0]  |             |
| ctrl_  | wire [CTRL_WIDTH-1:0] |             |
## Constants

| Name       | Type | Value                                          | Description |
| ---------- | ---- | ---------------------------------------------- | ----------- |
| CTRL_WIDTH |      | 2**PORT_ADDRESS_WIDTH * NUM_STAGES * MUX_ORDER |             |
## Processes
- unnamed: ( @(posedge clk) )
## Instantiations

- i_ctrl: pack_ctrl
- i_interconnect: pack_interconnect
