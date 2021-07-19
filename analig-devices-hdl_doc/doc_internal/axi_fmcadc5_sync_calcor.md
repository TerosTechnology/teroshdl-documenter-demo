# Entity: axi_fmcadc5_sync_calcor

- **File**: axi_fmcadc5_sync_calcor.v
## Diagram

![Diagram](axi_fmcadc5_sync_calcor.svg "Diagram")
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
 poor man's version of calibration & correction (scale & offset only)
 assumes linear frequency response on all discrete components
 looking for a rich man's version? fidus.com (FSF-AD15000A)
 
## Ports

| Port name       | Direction | Type    | Description         |
| --------------- | --------- | ------- | ------------------- |
| rx_clk          | input     |         | receive interface   |
| rx_enable_0     | input     |         |                     |
| rx_data_0       | input     | [255:0] |                     |
| rx_enable_1     | input     |         |                     |
| rx_data_1       | input     | [255:0] |                     |
| rx_enable       | output    |         |                     |
| rx_data         | output    | [511:0] |                     |
| rx_cal_enable   | input     |         | calibration signals |
| rx_cal_done_t   | output    |         |                     |
| rx_cal_max_0    | output    | [ 15:0] |                     |
| rx_cal_min_0    | output    | [ 15:0] |                     |
| rx_cal_max_1    | output    | [ 15:0] |                     |
| rx_cal_min_1    | output    | [ 15:0] |                     |
| rx_cor_scale_0  | input     | [ 15:0] |                     |
| rx_cor_offset_0 | input     | [ 15:0] |                     |
| rx_cor_scale_1  | input     | [ 15:0] |                     |
| rx_cor_offset_1 | input     | [ 15:0] |                     |
## Signals

| Name              | Type            | Description         |
| ----------------- | --------------- | ------------------- |
| rx_enable_int     | reg             | internal registers  |
| rx_cor_data_0     | reg     [ 15:0] |                     |
| rx_cor_data_1     | reg     [ 15:0] |                     |
| rx_cal_done_int_t | reg             |                     |
| rx_cal_max_0_6    | reg     [ 15:0] |                     |
| rx_cal_min_0_6    | reg     [ 15:0] |                     |
| rx_cal_max_1_6    | reg     [ 15:0] |                     |
| rx_cal_min_1_6    | reg     [ 15:0] |                     |
| rx_cal_max_0_5    | reg     [ 15:0] |                     |
| rx_cal_min_0_5    | reg     [ 15:0] |                     |
| rx_cal_max_1_5    | reg     [ 15:0] |                     |
| rx_cal_min_1_5    | reg     [ 15:0] |                     |
| rx_cal_max_0_4    | reg     [ 15:0] |                     |
| rx_cal_min_0_4    | reg     [ 15:0] |                     |
| rx_cal_max_1_4    | reg     [ 15:0] |                     |
| rx_cal_min_1_4    | reg     [ 15:0] |                     |
| rx_cal_max_0_3    | reg     [ 15:0] |                     |
| rx_cal_min_0_3    | reg     [ 15:0] |                     |
| rx_cal_max_1_3    | reg     [ 15:0] |                     |
| rx_cal_min_1_3    | reg     [ 15:0] |                     |
| rx_cal_max_0_2    | reg     [ 15:0] |                     |
| rx_cal_min_0_2    | reg     [ 15:0] |                     |
| rx_cal_max_1_2    | reg     [ 15:0] |                     |
| rx_cal_min_1_2    | reg     [ 15:0] |                     |
| rx_cal_max_0_1    | reg     [ 15:0] |                     |
| rx_cal_min_0_1    | reg     [ 15:0] |                     |
| rx_cal_max_1_1    | reg     [ 15:0] |                     |
| rx_cal_min_1_1    | reg     [ 15:0] |                     |
| rx_cor_data_0_s   | wire [ 33:0]    | internal signals    |
| rx_cor_data_1_s   | wire [ 33:0]    |                     |
| rx_data_0_s       | wire [ 15:0]    |                     |
| rx_data_1_s       | wire [ 15:0]    |                     |
## Processes
- unnamed: ( @(posedge rx_clk) )
- unnamed: ( @(posedge rx_clk) )
- unnamed: ( @(posedge rx_clk) )
**Description**
run-time peaks

