# Entity: ad_pack

## Diagram

![Diagram](ad_pack.svg "Diagram")
## Description

***************************************************************************
 ***************************************************************************
 Copyright 2014 - 2020 (c) Analog Devices, Inc. All rights reserved.
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
 Packer:
   - pack I_W number of data units into O_W number of data units
   - data unit defined in bits by UNIT_W e.g 8 is a byte
 Constraints:
   - O_W >= I_W
   - no backpressure
 Data format:
  idata  [U(I_W-1) .... U(0)]
  odata [U(O_W-1) .... U(0)] 
 e.g 
  I_W = 4
  O_W = 6
  UNIT_W = 8
  idata : [B3,B2,B1,B0],[B7,B6,B5,B4],[B11,B10,B9,B8]
  odata:                             [B5,B4,B3,B2,B1,B0],[B11,B10,B9,B8,B7,B6]
 
## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| I_W          |      | 4     |             |
| O_W          |      | 6     |             |
| UNIT_W       |      | 8     |             |
| I_REG        |      | 0     |             |
| O_REG        |      | 1     |             |
## Ports

| Port name | Direction | Type                 | Description |
| --------- | --------- | -------------------- | ----------- |
| clk       | input     |                      |             |
| reset     | input     |                      |             |
| idata     | input     | [I_W*UNIT_W-1:0]     |             |
| ivalid    | input     |                      |             |
| odata     | output    | reg [O_W*UNIT_W-1:0] |             |
| ovalid    | output    | reg                  |             |
## Signals

| Name         | Type                   | Description |
| ------------ | ---------------------- | ----------- |
| idata_packed | reg [O_W*UNIT_W-1:0]   |             |
| idata_d      | reg [SH_W*UNIT_W-1:0]  |             |
| ivalid_d     | reg                    |             |
| idata_dd     | reg [SH_W*UNIT_W-1:0]  |             |
| in_use       | reg [SH_W-1:0]         |             |
| out_mask     | reg [SH_W-1:0]         |             |
| idata_dd_nx  | wire [SH_W*UNIT_W-1:0] |             |
| in_use_nx    | wire [SH_W-1:0]        |             |
| pack_wr      | wire                   |             |
| i            | integer                |             |
## Constants

| Name | Type | Value     | Description                                                 |
| ---- | ---- | --------- | ----------------------------------------------------------- |
| SH_W |      | I_W       | Width of shift reg is integer multiple of input data width  |
| STEP |      | O_W % I_W |                                                             |
## Processes
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(*) )
