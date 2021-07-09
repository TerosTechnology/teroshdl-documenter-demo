# Entity: axi_adrv9001_tx

## Diagram

![Diagram](axi_adrv9001_tx.svg "Diagram")
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

| Generic name            | Type | Value | Description |
| ----------------------- | ---- | ----- | ----------- |
| ID                      |      | 0     |             |
| ENABLED                 |      | 1     |             |
| CMOS_LVDS_N             |      | 0     |             |
| USE_RX_CLK_FOR_TX       |      | 0     |             |
| COMMON_BASE_ADDR        |      | 'h10  |             |
| CHANNEL_BASE_ADDR       |      | 'h11  |             |
| MODE_R1                 |      | 1     |             |
| FPGA_TECHNOLOGY         |      | 0     |             |
| FPGA_FAMILY             |      | 0     |             |
| SPEED_GRADE             |      | 0     |             |
| DEV_PACKAGE             |      | 0     |             |
| DISABLE                 |      | 0     |             |
| DDS_DISABLE             |      | 0     |             |
| IQCORRECTION_DISABLE    |      | 0     |             |
| DAC_DDS_TYPE            |      | 1     |             |
| DAC_DDS_CORDIC_DW       |      | 20    |             |
| DAC_DDS_CORDIC_PHASE_DW |      | 18    |             |
## Ports

| Port name        | Direction | Type    | Description         |
| ---------------- | --------- | ------- | ------------------- |
| dac_rst          | output    |         | dac interface       |
| dac_clk          | input     |         |                     |
| dac_data_valid_A | output    |         |                     |
| dac_data_i_A     | output    | [15:0]  |                     |
| dac_data_q_A     | output    | [15:0]  |                     |
| dac_data_valid_B | output    |         |                     |
| dac_data_i_B     | output    | [15:0]  |                     |
| dac_data_q_B     | output    | [15:0]  |                     |
| dac_single_lane  | output    |         |                     |
| dac_sdr_ddr_n    | output    |         |                     |
| up_dac_r1_mode   | output    |         |                     |
| tdd_tx_valid     | input     |         |                     |
| dac_clk_ratio    | input     | [ 31:0] |                     |
| dac_sync_in      | input     |         | master/slave        |
| dac_sync_out     | output    |         |                     |
| dac_valid        | output    |         | dma interface       |
| dac_enable_i0    | output    |         |                     |
| dac_data_i0      | input     | [ 15:0] |                     |
| dac_enable_q0    | output    |         |                     |
| dac_data_q0      | input     | [ 15:0] |                     |
| dac_enable_i1    | output    |         |                     |
| dac_data_i1      | input     | [ 15:0] |                     |
| dac_enable_q1    | output    |         |                     |
| dac_data_q1      | input     | [ 15:0] |                     |
| dac_dunf         | input     |         |                     |
| up_rstn          | input     |         | processor interface |
| up_clk           | input     |         |                     |
| up_wreq          | input     |         |                     |
| up_waddr         | input     | [ 13:0] |                     |
| up_wdata         | input     | [ 31:0] |                     |
| up_wack          | output    |         |                     |
| up_rreq          | input     |         |                     |
| up_raddr         | input     | [ 13:0] |                     |
| up_rdata         | output    | [ 31:0] |                     |
| up_rack          | output    |         |                     |
