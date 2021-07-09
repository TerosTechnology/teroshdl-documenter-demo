# Entity: ad_pnmon

## Diagram

![Diagram](ad_pnmon.svg "Diagram")
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
 PN monitors
 
## Generics

| Generic name       | Type | Value | Description |
| ------------------ | ---- | ----- | ----------- |
| DATA_WIDTH         |      | 16    |             |
| OOS_THRESHOLD      |      | 16    |             |
| ALLOW_ZERO_MASKING |      | 0     |             |
## Ports

| Port name            | Direction | Type               | Description              |
| -------------------- | --------- | ------------------ | ------------------------ |
| adc_clk              | input     |                    | adc interface            |
| adc_valid_in         | input     |                    |                          |
| adc_data_in          | input     | [(DATA_WIDTH-1):0] |                          |
| adc_data_pn          | input     | [(DATA_WIDTH-1):0] |                          |
| adc_pattern_has_zero | input     |                    |                          |
| adc_pn_oos           | output    |                    | pn out of sync and error |
| adc_pn_err           | output    |                    |                          |
## Signals

| Name             | Type             | Description         |
| ---------------- | ---------------- | ------------------- |
| adc_valid_d      | reg              | internal registers  |
| adc_pn_match_d   | reg              |                     |
| adc_pn_match_z   | reg              |                     |
| adc_pn_oos_int   | reg              |                     |
| adc_pn_err_int   | reg              |                     |
| adc_pn_oos_count | reg  [CNT_W-1:0] |                     |
| adc_valid_zero_d | reg              |                     |
| adc_pn_match_d_s | wire             | internal signals    |
| adc_pn_match_z_s | wire             |                     |
| adc_pn_match_s   | wire             |                     |
| adc_pn_update_s  | wire             |                     |
| adc_pn_err_s     | wire             |                     |
| adc_valid_zero   | wire             |                     |
## Constants

| Name  | Type | Value                 | Description |
| ----- | ---- | --------------------- | ----------- |
| CNT_W |      | $clog2(OOS_THRESHOLD) |             |
## Processes
- unnamed: ( @(posedge adc_clk) )
