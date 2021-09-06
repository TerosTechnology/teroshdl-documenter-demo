# Entity: axi_adc_decimate_filter

- **File**: axi_adc_decimate_filter.v
## Diagram

![Diagram](axi_adc_decimate_filter.svg "Diagram")
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

| Generic name       | Type | Value | Description |
| ------------------ | ---- | ----- | ----------- |
| CORRECTION_DISABLE |      | 1     |             |
## Ports

| Port name                    | Direction | Type   | Description |
| ---------------------------- | --------- | ------ | ----------- |
| adc_clk                      | input     |        |             |
| adc_rst                      | input     |        |             |
| decimation_ratio             | input     | [31:0] |             |
| filter_mask                  | input     | [ 2:0] |             |
| adc_correction_enable_a      | input     |        |             |
| adc_correction_enable_b      | input     |        |             |
| adc_correction_coefficient_a | input     | [15:0] |             |
| adc_correction_coefficient_b | input     | [15:0] |             |
| adc_valid_a                  | input     |        |             |
| adc_valid_b                  | input     |        |             |
| adc_data_a                   | input     | [11:0] |             |
| adc_data_b                   | input     | [11:0] |             |
| adc_dec_data_a               | output    | [15:0] |             |
| adc_dec_data_b               | output    | [15:0] |             |
| adc_dec_valid_a              | output    |        |             |
| adc_dec_valid_b              | output    |        |             |
## Signals

| Name                   | Type           | Description        |
| ---------------------- | -------------- | ------------------ |
| decimation_counter     | reg     [31:0] |  internal signals  |
| adc_dec_valid_a_filter | reg            |                    |
| adc_dec_valid_b_filter | reg            |                    |
| filter_enable          | reg     [4:0]  |                    |
| adc_dec_data_a_r       | reg     [15:0] |                    |
| adc_dec_data_b_r       | reg     [15:0] |                    |
| adc_dec_valid_a_r      | reg            |                    |
| adc_dec_valid_b_r      | reg            |                    |
| adc_fir_data_a         | wire [25:0]    |                    |
| adc_fir_valid_a        | wire           |                    |
| adc_fir_data_b         | wire [25:0]    |                    |
| adc_fir_valid_b        | wire           |                    |
| adc_cic_data_a         | wire [11:0]    |                    |
| adc_cic_valid_a        | wire           |                    |
| adc_cic_data_b         | wire [11:0]    |                    |
| adc_cic_valid_b        | wire           |                    |
## Processes
- unnamed: ( @(posedge adc_clk) )
  - **Type:** always
- unnamed: ( @(*) )
  - **Type:** always
- unnamed: ( @(posedge adc_clk) )
  - **Type:** always
## Instantiations

- cic_decimation_a: cic_decim
- cic_decimation_b: cic_decim
- fir_decimation_a: fir_decim
- fir_decimation_b: fir_decim
- i_scale_correction_a: ad_iqcor
- i_scale_correction_b: ad_iqcor
