# Entity: ad_upack

- **File**: ad_upack.v
## Diagram

![Diagram](ad_upack.svg "Diagram")
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
 Unpacker:
   - unpack O_W number of data units from I_W number of data units
   - data unit defined in bits by UNIT_W e.g 8 is a byte
 Constraints:
   - O_W <= I_W
   - LATENCY 1 
   - no backpressure
 Data format:
  idata  [U(I_W-1) .... U(0)]
  odata  [U(O_W-1) .... U(0)]
 e.g
  I_W = 6
  O_W = 4
  UNIT_W = 8
  idata : [B5,B4,B3,B2,B1,B0],[B11,B10,B9,B8,B7,B6]
  odata :                     [B3,B2,B1,B0],[B7,B6,B5,B4],[B11,B10,B9,B8]
 
## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| I_W          |      | 4     |             |
| O_W          |      | 3     |             |
| UNIT_W       |      | 8     |             |
| O_REG        |      | 1     |             |
## Ports

| Port name | Direction | Type                 | Description |
| --------- | --------- | -------------------- | ----------- |
| clk       | input     |                      |             |
| reset     | input     |                      |             |
| idata     | input     | [I_W*UNIT_W-1:0]     |             |
| ivalid    | input     |                      |             |
| iready    | output    |                      |             |
| odata     | output    | reg [O_W*UNIT_W-1:0] |             |
| ovalid    | output    | reg                  |             |
## Signals

| Name       | Type                  | Description |
| ---------- | --------------------- | ----------- |
| i          | integer               |             |
| idata_sh   | reg [SH_W*UNIT_W-1:0] |             |
| idata_d    | reg [SH_W*UNIT_W-1:0] |             |
| idata_d_nx | reg [SH_W*UNIT_W-1:0] |             |
| in_use     | reg [SH_W-1:0]        |             |
| inmask     | reg [SH_W-1:0]        |             |
| out_mask   | wire [SH_W-1:0]       |             |
| in_use_nx  | wire [SH_W-1:0]       |             |
| unit_valid | wire [SH_W-1:0]       |             |
| odata_s    | wire [O_W*UNIT_W-1:0] |             |
| ovalid_s   | wire                  |             |
## Constants

| Name    | Type | Value     | Description                                                  |
| ------- | ---- | --------- | ------------------------------------------------------------ |
| SH_W    |      | O_W       | Width of shift reg is integer multiple of output data width  |
| STEP    |      | I_W % O_W |                                                              |
| LATENCY |      | 1         | Minimum input latency from iready to ivalid                  |
## Processes
- unnamed: ( @(posedge clk) )
- unnamed: ( @(*) )
- unnamed: ( @(*) )
- unnamed: ( @(posedge clk) )
