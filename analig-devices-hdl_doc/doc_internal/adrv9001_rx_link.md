# Entity: adrv9001_rx_link

## Diagram

![Diagram](adrv9001_rx_link.svg "Diagram")
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
 
## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| CMOS_LVDS_N  |      | 0     |             |
## Ports

| Port name       | Direction | Type   | Description                |
| --------------- | --------- | ------ | -------------------------- |
| adc_rst         | input     |        |                            |
| adc_clk_div     | input     |        |                            |
| adc_data_0      | input     | [7:0]  |                            |
| adc_data_1      | input     | [7:0]  |                            |
| adc_data_2      | input     | [7:0]  |                            |
| adc_data_3      | input     | [7:0]  |                            |
| adc_data_strobe | input     | [7:0]  |                            |
| adc_valid       | input     |        |                            |
| rx_clk          | output    |        | upper layer data interface |
| rx_data_valid   | output    |        |                            |
| rx_data_i       | output    | [15:0] |                            |
| rx_data_q       | output    | [15:0] |                            |
| rx_sdr_ddr_n    | input     |        | Config interface           |
| rx_single_lane  | input     |        |                            |
## Signals

| Name                     | Type        | Description |
| ------------------------ | ----------- | ----------- |
| data_0                   | wire [7:0]  |             |
| data_1                   | wire [7:0]  |             |
| data_2                   | wire [7:0]  |             |
| data_3                   | wire [7:0]  |             |
| data_strobe              | wire [7:0]  |             |
| data_valid               | wire        |             |
| rx_data8_0_aligned       | wire [7:0]  | ADC         |
| rx_data8_1_aligned       | wire [7:0]  |             |
| rx_data8_2_aligned       | wire [7:0]  |             |
| rx_data8_3_aligned       | wire [7:0]  |             |
| rx_data8_strobe_aligned  | wire [7:0]  |             |
| rx_data8_0_aligned_valid | wire        |             |
| rx_data8_1_aligned_valid | wire        |             |
| rx_data16_0_packed       | wire [15:0] |             |
| rx_data16_1_packed       | wire [15:0] |             |
| rx_data16_0_packed_valid | wire        |             |
| rx_data16_0_packed_osof  | wire        |             |
| rx_data32_0_packed       | wire [31:0] |             |
| rx_data32_0_packed_valid | wire        |             |
## Instantiations

- i_rx_aligner8_0: adrv9001_aligner8
- i_rx_aligner8_1: adrv9001_aligner8
- i_rx_strobe_aligner: adrv9001_aligner8
- i_rx_pack_8_to_16_0: adrv9001_pack
- i_rx_pack_8_to_16_1: adrv9001_pack
- i_rx_pack_16_to_32_0: adrv9001_pack
