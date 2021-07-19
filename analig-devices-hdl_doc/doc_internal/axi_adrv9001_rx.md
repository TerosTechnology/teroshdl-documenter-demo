# Entity: axi_adrv9001_rx

- **File**: axi_adrv9001_rx.v
## Diagram

![Diagram](axi_adrv9001_rx.svg "Diagram")
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

| Generic name         | Type | Value | Description |
| -------------------- | ---- | ----- | ----------- |
| ID                   |      | 0     |             |
| ENABLED              |      | 1     |             |
| CMOS_LVDS_N          |      | 0     |             |
| COMMON_BASE_ADDR     |      | 'h00  |             |
| CHANNEL_BASE_ADDR    |      | 'h01  |             |
| MODE_R1              |      | 1     |             |
| FPGA_TECHNOLOGY      |      | 0     |             |
| FPGA_FAMILY          |      | 0     |             |
| SPEED_GRADE          |      | 0     |             |
| DEV_PACKAGE          |      | 0     |             |
| DATAFORMAT_DISABLE   |      | 0     |             |
| DCFILTER_DISABLE     |      | 0     |             |
| IQCORRECTION_DISABLE |      | 1     |             |
## Ports

| Port name        | Direction | Type    | Description            |
| ---------------- | --------- | ------- | ---------------------- |
| adc_rst          | output    |         | adc interface          |
| adc_clk          | input     |         |                        |
| adc_valid_A      | input     |         |                        |
| adc_data_i_A     | input     | [ 15:0] |                        |
| adc_data_q_A     | input     | [ 15:0] |                        |
| adc_valid_B      | input     |         |                        |
| adc_data_i_B     | input     | [ 15:0] |                        |
| adc_data_q_B     | input     | [ 15:0] |                        |
| adc_single_lane  | output    |         |                        |
| adc_sdr_ddr_n    | output    |         |                        |
| up_adc_r1_mode   | output    |         |                        |
| adc_clk_ratio    | input     | [ 31:0] |                        |
| dac_data_valid_A | input     |         | dac loopback interface |
| dac_data_i_A     | input     | [ 15:0] |                        |
| dac_data_q_A     | input     | [ 15:0] |                        |
| dac_data_valid_B | input     |         |                        |
| dac_data_i_B     | input     | [ 15:0] |                        |
| dac_data_q_B     | input     | [ 15:0] |                        |
| adc_valid        | output    |         | dma interface          |
| adc_enable_i0    | output    |         |                        |
| adc_data_i0      | output    | [ 15:0] |                        |
| adc_enable_q0    | output    |         |                        |
| adc_data_q0      | output    | [ 15:0] |                        |
| adc_enable_i1    | output    |         |                        |
| adc_data_i1      | output    | [ 15:0] |                        |
| adc_enable_q1    | output    |         |                        |
| adc_data_q1      | output    | [ 15:0] |                        |
| adc_dovf         | input     |         |                        |
| up_rstn          | input     |         | processor interface    |
| up_clk           | input     |         |                        |
| up_wreq          | input     |         |                        |
| up_waddr         | input     | [ 13:0] |                        |
| up_wdata         | input     | [ 31:0] |                        |
| up_wack          | output    |         |                        |
| up_rreq          | input     |         |                        |
| up_raddr         | input     | [ 13:0] |                        |
| up_rdata         | output    | [ 31:0] |                        |
| up_rack          | output    |         |                        |
