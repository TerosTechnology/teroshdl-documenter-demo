# Entity: axi_dmac_resize_dest

- **File**: axi_dmac_resize_dest.v
## Diagram

![Diagram](axi_dmac_resize_dest.svg "Diagram")
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
| DATA_WIDTH_DEST |      | 64    |             |
| DATA_WIDTH_MEM  |      | 64    |             |
## Ports

| Port name       | Direction | Type                    | Description |
| --------------- | --------- | ----------------------- | ----------- |
| clk             | input     |                         |             |
| reset           | input     |                         |             |
| mem_data_valid  | input     |                         |             |
| mem_data_ready  | output    |                         |             |
| mem_data        | input     | [DATA_WIDTH_MEM-1:0]    |             |
| mem_data_last   | input     |                         |             |
| mem_data_strb   | input     | [DATA_WIDTH_MEM/8-1:0]  |             |
| dest_data_valid | output    |                         |             |
| dest_data_ready | input     |                         |             |
| dest_data       | output    | [DATA_WIDTH_DEST-1:0]   |             |
| dest_data_last  | output    |                         |             |
| dest_data_strb  | output    | [DATA_WIDTH_DEST/8-1:0] |             |
