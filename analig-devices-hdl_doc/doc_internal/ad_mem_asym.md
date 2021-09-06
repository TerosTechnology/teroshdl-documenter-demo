# Entity: ad_mem_asym

- **File**: ad_mem_asym.v
## Diagram

![Diagram](ad_mem_asym.svg "Diagram")
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
 A simple asymetric memory. The write and read memory space must have the same size.
 2^A_ADDRESS_WIDTH * A_DATA_WIDTH == 2^B_ADDRESS_WIDTH * B_DATA_WIDTH

## Generics

| Generic name    | Type | Value | Description |
| --------------- | ---- | ----- | ----------- |
| A_ADDRESS_WIDTH |      | 8     |             |
| A_DATA_WIDTH    |      | 256   |             |
| B_ADDRESS_WIDTH |      | 10    |             |
| B_DATA_WIDTH    |      | 64    |             |
## Ports

| Port name | Direction | Type                  | Description |
| --------- | --------- | --------------------- | ----------- |
| clka      | input     |                       |             |
| wea       | input     |                       |             |
| addra     | input     | [A_ADDRESS_WIDTH-1:0] |             |
| dina      | input     | [A_DATA_WIDTH-1:0]    |             |
| clkb      | input     |                       |             |
| reb       | input     |                       |             |
| addrb     | input     | [B_ADDRESS_WIDTH-1:0] |             |
| doutb     | output    | [B_DATA_WIDTH-1:0]    |             |
## Signals

| Name  | Type                          | Description |
| ----- | ----------------------------- | ----------- |
| m_ram | reg      [MEM_DATA_WIDTH-1:0] |             |
## Constants

| Name              | Type | Value                  | Description |
| ----------------- | ---- | ---------------------- | ----------- |
| MEM_ADDRESS_WIDTH |      | A_ADDRESS_WIDTH        |             |
| B_ADDRESS_WIDTH   |      | undefined              |             |
| MIN_WIDTH         |      | A_DATA_WIDTH           |             |
| B_DATA_WIDTH      |      | undefined              |             |
| MAX_WIDTH         |      | A_DATA_WIDTH           |             |
| B_DATA_WIDTH      |      | undefined              |             |
| MEM_DATA_WIDTH    |      | MIN_WIDTH              |             |
| MEM_SIZE          |      | 2 ** MEM_ADDRESS_WIDTH |             |
| MEM_RATIO         |      | MAX_WIDTH / MIN_WIDTH  |             |
| MEM_RATIO_LOG2    |      | clog2(MEM_RATIO)       |             |
## Functions
- clog2 <font id="function_arguments">()</font> <font id="function_return">return (integer)</font>
