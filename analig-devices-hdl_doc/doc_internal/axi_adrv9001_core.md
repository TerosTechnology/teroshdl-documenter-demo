# Entity: axi_ad9001_core

## Diagram

![Diagram](axi_adrv9001_core.svg "Diagram")
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

| Generic name             | Type | Value | Description |
| ------------------------ | ---- | ----- | ----------- |
| ID                       |      | 0     |             |
| CMOS_LVDS_N              |      | 0     |             |
| USE_RX_CLK_FOR_TX        |      | 0     |             |
| NUM_LANES                |      | 3     |             |
| DRP_WIDTH                |      | 5     |             |
| TDD_DISABLE              |      | 0     |             |
| DDS_DISABLE              |      | 0     |             |
| INDEPENDENT_1R1T_SUPPORT |      | 1     |             |
| COMMON_2R2T_SUPPORT      |      | 1     |             |
| FPGA_TECHNOLOGY          |      | 0     |             |
| FPGA_FAMILY              |      | 0     |             |
| SPEED_GRADE              |      | 0     |             |
| DEV_PACKAGE              |      | 0     |             |
| DAC_DDS_TYPE             |      | 1     |             |
| DAC_DDS_CORDIC_DW        |      | 20    |             |
| DAC_DDS_CORDIC_PHASE_DW  |      | 18    |             |
## Ports

| Port name        | Direction | Type                      | Description         |
| ---------------- | --------- | ------------------------- | ------------------- |
| rx1_clk          | input     |                           | ADC interface       |
| rx1_rst          | output    |                           |                     |
| rx1_data_valid   | input     |                           |                     |
| rx1_data_i       | input     | [15:0]                    |                     |
| rx1_data_q       | input     | [15:0]                    |                     |
| rx1_single_lane  | output    |                           |                     |
| rx1_sdr_ddr_n    | output    |                           |                     |
| rx2_clk          | input     |                           |                     |
| rx2_rst          | output    |                           |                     |
| rx2_data_valid   | input     |                           |                     |
| rx2_data_i       | input     | [15:0]                    |                     |
| rx2_data_q       | input     | [15:0]                    |                     |
| rx2_single_lane  | output    |                           |                     |
| rx2_sdr_ddr_n    | output    |                           |                     |
| tx1_clk          | input     |                           | DAC interface       |
| tx1_rst          | output    |                           |                     |
| tx1_data_valid   | output    |                           |                     |
| tx1_data_i       | output    | [15:0]                    |                     |
| tx1_data_q       | output    | [15:0]                    |                     |
| tx1_single_lane  | output    |                           |                     |
| tx1_sdr_ddr_n    | output    |                           |                     |
| tx2_clk          | input     |                           |                     |
| tx2_rst          | output    |                           |                     |
| tx2_data_valid   | output    |                           |                     |
| tx2_data_i       | output    | [15:0]                    |                     |
| tx2_data_q       | output    | [15:0]                    |                     |
| tx2_single_lane  | output    |                           |                     |
| tx2_sdr_ddr_n    | output    |                           |                     |
| adc_clk_ratio    | input     | [ 31:0]                   |                     |
| dac_clk_ratio    | input     | [ 31:0]                   |                     |
| adc_1_valid      | output    |                           | DMA interface       |
| adc_1_enable_i0  | output    |                           |                     |
| adc_1_data_i0    | output    | [15:0]                    |                     |
| adc_1_enable_q0  | output    |                           |                     |
| adc_1_data_q0    | output    | [15:0]                    |                     |
| adc_1_enable_i1  | output    |                           |                     |
| adc_1_data_i1    | output    | [15:0]                    |                     |
| adc_1_enable_q1  | output    |                           |                     |
| adc_1_data_q1    | output    | [15:0]                    |                     |
| adc_1_dovf       | input     |                           |                     |
| adc_2_valid      | output    |                           |                     |
| adc_2_enable_i   | output    |                           |                     |
| adc_2_data_i     | output    | [15:0]                    |                     |
| adc_2_enable_q   | output    |                           |                     |
| adc_2_data_q     | output    | [15:0]                    |                     |
| adc_2_dovf       | input     |                           |                     |
| dac_1_valid      | output    |                           |                     |
| dac_1_enable_i0  | output    |                           |                     |
| dac_1_data_i0    | input     | [15:0]                    |                     |
| dac_1_enable_q0  | output    |                           |                     |
| dac_1_data_q0    | input     | [15:0]                    |                     |
| dac_1_enable_i1  | output    |                           |                     |
| dac_1_data_i1    | input     | [15:0]                    |                     |
| dac_1_enable_q1  | output    |                           |                     |
| dac_1_data_q1    | input     | [15:0]                    |                     |
| dac_1_dunf       | input     |                           |                     |
| dac_2_valid      | output    |                           |                     |
| dac_2_enable_i0  | output    |                           |                     |
| dac_2_data_i0    | input     | [15:0]                    |                     |
| dac_2_enable_q0  | output    |                           |                     |
| dac_2_data_q0    | input     | [15:0]                    |                     |
| dac_2_dunf       | input     |                           |                     |
| delay_clk        | input     |                           | delay interface     |
| delay_rx1_rst    | output    |                           |                     |
| delay_rx1_locked | input     |                           |                     |
| delay_rx2_rst    | output    |                           |                     |
| delay_rx2_locked | input     |                           |                     |
| up_rx1_dld       | output    | [NUM_LANES-1:0]           |                     |
| up_rx1_dwdata    | output    | [DRP_WIDTH*NUM_LANES-1:0] |                     |
| up_rx1_drdata    | input     | [DRP_WIDTH*NUM_LANES-1:0] |                     |
| up_rx2_dld       | output    | [NUM_LANES-1:0]           |                     |
| up_rx2_dwdata    | output    | [DRP_WIDTH*NUM_LANES-1:0] |                     |
| up_rx2_drdata    | input     | [DRP_WIDTH*NUM_LANES-1:0] |                     |
| tdd_sync         | input     |                           | TDD interface       |
| tdd_sync_cntr    | output    |                           |                     |
| tdd_rx1_rf_en    | output    |                           |                     |
| tdd_tx1_rf_en    | output    |                           |                     |
| tdd_if1_mode     | output    |                           |                     |
| tdd_rx2_rf_en    | output    |                           |                     |
| tdd_tx2_rf_en    | output    |                           |                     |
| tdd_if2_mode     | output    |                           |                     |
| up_rstn          | input     |                           | processor interface |
| up_clk           | input     |                           |                     |
| up_wreq          | input     |                           |                     |
| up_waddr         | input     | [13:0]                    |                     |
| up_wdata         | input     | [31:0]                    |                     |
| up_wack          | output    |                           |                     |
| up_rreq          | input     |                           |                     |
| up_raddr         | input     | [13:0]                    |                     |
| up_rdata         | output    | [31:0]                    |                     |
| up_rack          | output    |                           |                     |
## Signals

| Name                | Type          | Description |
| ------------------- | ------------- | ----------- |
| up_wack_s           | wire [7:0]    |             |
| up_rdata_s          | wire [31:0]   |             |
| up_rack_s           | wire [7:0]    |             |
| tx1_data_valid_A    | wire          |             |
| tx1_data_i_A        | wire [15:0]   |             |
| tx1_data_q_A        | wire [15:0]   |             |
| tx1_data_valid_B    | wire          |             |
| tx1_data_i_B        | wire [15:0]   |             |
| tx1_data_q_B        | wire [15:0]   |             |
| tx2_data_valid_A    | wire          |             |
| tx2_data_i_A        | wire [15:0]   |             |
| tx2_data_q_A        | wire [15:0]   |             |
| up_rx1_r1_mode      | wire          |             |
| rx1_r1_mode         | wire          |             |
| rx2_rst_loc         | wire          |             |
| rx2_single_lane_loc | wire          |             |
| rx2_sdr_ddr_n_loc   | wire          |             |
| up_tx1_r1_mode      | wire          |             |
| tx1_r1_mode         | wire          |             |
| tx2_rst_loc         | wire          |             |
| tx2_single_lane_loc | wire          |             |
| tx2_sdr_ddr_n_loc   | wire          |             |
| tx1_data_valid_A_d  | reg           |             |
| tx1_data_i_A_d      | reg    [15:0] |             |
| tx1_data_q_A_d      | reg    [15:0] |             |
| tx1_data_valid_B_d  | reg           |             |
| tx1_data_i_B_d      | reg    [15:0] |             |
| tx1_data_q_B_d      | reg    [15:0] |             |
| tx2_data_valid_A_d  | reg           |             |
| tx2_data_i_A_d      | reg    [15:0] |             |
| tx2_data_q_A_d      | reg    [15:0] |             |
## Processes
- unnamed: ( @(posedge tx1_clk) )
- unnamed: ( @(posedge tx2_clk) )
- unnamed: ( @(posedge tx2_clk) )
**Description**
Use tx1_r1_mode as clock enable when the two clocks have different frequency

- unnamed: ( @(negedge up_rstn or posedge up_clk) )
**Description**
processor read interface

## Instantiations

- i_rx1_ctrl_sync: sync_bits
**Description**
rx1_r1_mode and tx1_r1_mode considered static during operation
rx1_r1_mode should be 0 only when rx1_clk and rx2_clk have the same frequency
tx1_r1_mode should be 0 only when tx1_clk and tx2_clk have the same frequency

- i_tx1_ctrl_sync: sync_bits
- i_rx1: axi_adrv9001_rx
- i_rx2: axi_adrv9001_rx
- i_tx1: axi_adrv9001_tx
- i_tx2: axi_adrv9001_tx
- i_delay_cntrl_rx1: up_delay_cntrl
**Description**
adc delay control

- i_delay_cntrl_rx2: up_delay_cntrl
