# Entity: ad_dcfilter

## Diagram

![Diagram](ad_dcfilter.svg "Diagram")
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
 dc filter- y(n) = c*x(n) + (1-c)*y(n-1)
 
## Generics

| Generic name | Type | Value | Description        |
| ------------ | ---- | ----- | ------------------ |
| DISABLE      |      | 0     | data path disable  |
## Ports

| Port name     | Direction | Type   | Description       |
| ------------- | --------- | ------ | ----------------- |
| clk           | input     |        | data interface    |
| valid         | input     |        |                   |
| data          | input     | [15:0] |                   |
| valid_out     | output    |        |                   |
| data_out      | output    | [15:0] |                   |
| dcfilt_enb    | input     |        | control interface |
| dcfilt_coeff  | input     | [15:0] |                   |
| dcfilt_offset | input     | [15:0] |                   |
## Signals

| Name           | Type           | Description         |
| -------------- | -------------- | ------------------- |
| dcfilt_coeff_d | reg     [15:0] | internal registers  |
| dc_offset      | reg     [47:0] |                     |
| dc_offset_d    | reg     [47:0] |                     |
| valid_d        | reg            |                     |
| data_d         | reg     [15:0] |                     |
| valid_2d       | reg            |                     |
| data_2d        | reg     [15:0] |                     |
| data_dcfilt    | reg     [15:0] |                     |
| valid_int      | reg            |                     |
| data_int       | reg     [15:0] |                     |
| dc_offset_s    | wire [47:0]    | internal signals    |
## Processes
- unnamed: ( @(posedge clk) )
**Description**
dcfilt_coeff is flopped so to remove warnings from vivado

- unnamed: ( @(posedge clk) )
**Description**
removing dc offset

## Instantiations

- i_dsp48e1: DSP48E1
**Description**
dsp slice instance ((D-A)*B)+C

