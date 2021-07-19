# Entity: ad_dds

- **File**: ad_dds.v
## Diagram

![Diagram](ad_dds.svg "Diagram")
## Description

***************************************************************************
 ***************************************************************************
 Copyright 2014 - 2018 (c) Analog Devices, Inc. All rights reserved.
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
 single channel dds (dual tone)
 
## Generics

| Generic name    | Type | Value | Description                                                                               |
| --------------- | ---- | ----- | ----------------------------------------------------------------------------------------- |
| DISABLE         |      | 0     |                                                                                           |
| DDS_DW          |      | 16    | range 8-24                                                                                |
| PHASE_DW        |      | 16    | range 8-16 (FIX ME)                                                                       |
| DDS_TYPE        |      | 1     | set 1 for CORDIC or 2 for Polynomial                                                      |
| CORDIC_DW       |      | 16    | range 8-24                                                                                |
| CORDIC_PHASE_DW |      | 16    | range 8-24 (make sure CORDIC_PHASE_DW < CORDIC_DW)                                        |
| CLK_RATIO       |      | 1     | the clock radtio between the device clock(sample rate) and the dac_core clock 2^N, 1<N<6  |
## Ports

| Port name          | Direction | Type                   | Description |
| ------------------ | --------- | ---------------------- | ----------- |
| clk                | input     |                        | interface   |
| dac_dds_format     | input     |                        |             |
| dac_data_sync      | input     |                        |             |
| dac_valid          | input     |                        |             |
| tone_1_scale       | input     | [                15:0] |             |
| tone_2_scale       | input     | [                15:0] |             |
| tone_1_init_offset | input     | [                15:0] |             |
| tone_2_init_offset | input     | [                15:0] |             |
| tone_1_freq_word   | input     | [        PHASE_DW-1:0] |             |
| tone_2_freq_word   | input     | [        PHASE_DW-1:0] |             |
| dac_dds_data       | output    | [DDS_DW*CLK_RATIO-1:0] |             |
## Signals

| Name            | Type                        | Description |
| --------------- | --------------------------- | ----------- |
| dac_dds_data_s  | wire [DDS_DW*CLK_RATIO-1:0] |             |
| dac_data_sync_m | reg                         |             |
## Processes
- unnamed: ( @(posedge clk) )
