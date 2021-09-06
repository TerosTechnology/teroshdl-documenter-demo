# Entity: ad_dds_sine

- **File**: ad_dds_sine.v
## Diagram

![Diagram](ad_dds_sine.svg "Diagram")
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
 this is a sine function (approximate), the basic idea is to approximate sine as a
 polynomial function (there are a lot of stuff about this on the web)

## Generics

| Generic name     | Type | Value | Description |
| ---------------- | ---- | ----- | ----------- |
| DELAY_DATA_WIDTH |      | 16    |             |
## Ports

| Port name | Direction | Type                     | Description        |
| --------- | --------- | ------------------------ | ------------------ |
| clk       | input     |                          |  sine = sin(angle) |
| angle     | input     | [15:0]                   |                    |
| sine      | output    | [15:0]                   |                    |
| ddata_in  | input     | [(DELAY_DATA_WIDTH-1):0] |                    |
| ddata_out | output    | [(DELAY_DATA_WIDTH-1):0] |                    |
## Signals

| Name          | Type                             | Description          |
| ------------- | -------------------------------- | -------------------- |
| s1_data_p     | reg     [33:0]                   |  internal registers  |
| s1_data_n     | reg     [33:0]                   |                      |
| s1_angle      | reg     [15:0]                   |                      |
| s1_ddata      | reg     [(DELAY_DATA_WIDTH-1):0] |                      |
| s2_data_0     | reg     [18:0]                   |                      |
| s2_data_1     | reg     [18:0]                   |                      |
| s2_ddata      | reg     [(DELAY_DATA_WIDTH-1):0] |                      |
| s3_data       | reg     [18:0]                   |                      |
| s3_ddata      | reg     [(DELAY_DATA_WIDTH-1):0] |                      |
| s4_data2_p    | reg     [33:0]                   |                      |
| s4_data2_n    | reg     [33:0]                   |                      |
| s4_data1_p    | reg     [16:0]                   |                      |
| s4_data1_n    | reg     [16:0]                   |                      |
| s4_ddata      | reg     [(DELAY_DATA_WIDTH-1):0] |                      |
| s5_data2_0    | reg     [16:0]                   |                      |
| s5_data2_1    | reg     [16:0]                   |                      |
| s5_data1      | reg     [16:0]                   |                      |
| s5_ddata      | reg     [(DELAY_DATA_WIDTH-1):0] |                      |
| s6_data2      | reg     [16:0]                   |                      |
| s6_data1      | reg     [16:0]                   |                      |
| s6_ddata      | reg     [(DELAY_DATA_WIDTH-1):0] |                      |
| s7_data       | reg     [33:0]                   |                      |
| s7_ddata      | reg     [(DELAY_DATA_WIDTH-1):0] |                      |
| sine_int      | reg     [15:0]                   |                      |
| ddata_out_int | reg     [(DELAY_DATA_WIDTH-1):0] |                      |
| angle_s       | wire [15:0]                      |  internal signals    |
| s1_data_s     | wire [33:0]                      |                      |
| s1_ddata_s    | wire [(DELAY_DATA_WIDTH-1):0]    |                      |
| s1_angle_s    | wire [15:0]                      |                      |
| s4_data2_s    | wire [33:0]                      |                      |
| s4_ddata_s    | wire [(DELAY_DATA_WIDTH-1):0]    |                      |
| s4_data1_s    | wire [16:0]                      |                      |
| s7_data2_s    | wire [33:0]                      |                      |
| s7_data1_s    | wire [33:0]                      |                      |
| s7_ddata_s    | wire [(DELAY_DATA_WIDTH-1):0]    |                      |
## Processes
- unnamed: ( @(posedge clk) )
  - **Type:** always
</br>**Description**
 2's complement versions 
- unnamed: ( @(posedge clk) )
  - **Type:** always
</br>**Description**
 select partial products 
- unnamed: ( @(posedge clk) )
  - **Type:** always
</br>**Description**
 unit-sine 
- unnamed: ( @(posedge clk) )
  - **Type:** always
</br>**Description**
 2's complement versions 
- unnamed: ( @(posedge clk) )
  - **Type:** always
</br>**Description**
 select partial products 
- unnamed: ( @(posedge clk) )
  - **Type:** always
</br>**Description**
 corrected-sine 
- unnamed: ( @(posedge clk) )
  - **Type:** always
</br>**Description**
 corrected sum 
- unnamed: ( @(posedge clk) )
  - **Type:** always
## Instantiations

- i_mul_s1: ad_mul
</br>**Description**
 level 1 - intermediate

- i_mul_s2: ad_mul
</br>**Description**
 level 2 - final

- i_mul_s3_2: ad_mul
</br>**Description**
 full-scale

- i_mul_s3_1: ad_mul
