# Entity: ad_csc

## Diagram

![Diagram](ad_csc.svg "Diagram")
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
 csc = c1*d[23:16] + c2*d[15:8] + c3*d[7:0] + c4;
 
## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| DELAY_DW     |      | 16    |             |
| MUL_COEF_DW  |      | 17    |             |
| SUM_COEF_DW  |      | 24    |             |
| YCbCr_2_RGB  |      | 0     |             |
## Ports

| Port name | Direction | Type                     | Description           |
| --------- | --------- | ------------------------ | --------------------- |
| clk       | input     |                          | data                  |
| sync      | input     | [   DELAY_DW-1:0]        |                       |
| data      | input     | [           23:0]        |                       |
| C1        | input     | signed [MUL_COEF_DW-1:0] | constants             |
| C2        | input     | signed [MUL_COEF_DW-1:0] |                       |
| C3        | input     | signed [MUL_COEF_DW-1:0] |                       |
| C4        | input     | signed [SUM_COEF_DW-1:0] |                       |
| csc_sync  | output    | [   DELAY_DW-1:0]        | sync is delay matched |
| csc_data  | output    | [            7:0]        |                       |
## Signals

| Name       | Type                       | Description     |
| ---------- | -------------------------- | --------------- |
| data_d1    | reg  signed [        23:0] | internal wires  |
| data_d2    | reg  signed [        23:0] |                 |
| data_1     | reg  signed [    MUL_DW:0] |                 |
| data_2     | reg  signed [    MUL_DW:0] |                 |
| data_3     | reg  signed [    MUL_DW:0] |                 |
| s_data_1   | reg  signed [    MUL_DW:0] |                 |
| s_data_2   | reg  signed [    MUL_DW:0] |                 |
| s_data_3   | reg  signed [    MUL_DW:0] |                 |
| sync_1_m   | reg         [DELAY_DW-1:0] |                 |
| sync_2_m   | reg         [DELAY_DW-1:0] |                 |
| sync_3_m   | reg         [DELAY_DW-1:0] |                 |
| sync_4_m   | reg         [DELAY_DW-1:0] |                 |
| csc_data_d | reg         [         7:0] |                 |
| color1     | wire [8:0]                 |                 |
| color2     | wire [8:0]                 |                 |
| color3     | wire [8:0]                 |                 |
## Constants

| Name     | Type | Value                     | Description   |
| -------- | ---- | ------------------------- | ------------- |
| PIXEL_WD |      | 9                         | sign extended |
| MUL_DW   |      | MUL_COEF_DW + PIXEL_WD -1 |               |
## Processes
- unnamed: ( @(posedge clk) )
**Description**
delay signals

- unnamed: ( @(posedge clk) )
**Description**
pipeline DSPs for multiplications and additions

- unnamed: ( @(posedge clk) )
