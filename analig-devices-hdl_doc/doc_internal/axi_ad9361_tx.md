# Entity: axi_ad9361_tx

- **File**: axi_ad9361_tx.v
## Diagram

![Diagram](axi_ad9361_tx.svg "Diagram")
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

| Generic name            | Type | Value | Description |
| ----------------------- | ---- | ----- | ----------- |
| ID                      |      | 0     | parameters  |
| FPGA_TECHNOLOGY         |      | 0     |             |
| FPGA_FAMILY             |      | 0     |             |
| SPEED_GRADE             |      | 0     |             |
| DEV_PACKAGE             |      | 0     |             |
| MODE_1R1T               |      | 0     |             |
| CLK_EDGE_SEL            |      | 0     |             |
| CMOS_OR_LVDS_N          |      | 0     |             |
| PPS_RECEIVER_ENABLE     |      | 0     |             |
| INIT_DELAY              |      | 0     |             |
| DAC_DDS_DISABLE         |      | 0     |             |
| DAC_DDS_TYPE            |      | 1     |             |
| DAC_DDS_CORDIC_DW       |      | 14    |             |
| DAC_DDS_CORDIC_PHASE_DW |      | 13    |             |
| USERPORTS_DISABLE       |      | 0     |             |
| DELAYCNTRL_DISABLE      |      | 0     |             |
| IQCORRECTION_DISABLE    |      | 0     |             |
## Ports

| Port name       | Direction | Type   | Description                          |
| --------------- | --------- | ------ | ------------------------------------ |
| dac_clk         | input     |        | dac interface                        |
| dac_valid       | output    |        |                                      |
| dac_data        | output    | [47:0] |                                      |
| dac_clksel      | output    |        |                                      |
| dac_r1_mode     | output    |        |                                      |
| adc_data        | input     | [47:0] |                                      |
| up_dld          | output    | [15:0] | delay interface                      |
| up_dwdata       | output    | [79:0] |                                      |
| up_drdata       | input     | [79:0] |                                      |
| delay_clk       | input     |        |                                      |
| delay_rst       | output    |        |                                      |
| delay_locked    | input     |        |                                      |
| dac_sync_enable | input     |        | master/slave                         |
| dac_sync_in     | input     |        |                                      |
| dac_sync_out    | output    |        |                                      |
| dac_enable_i0   | output    |        | dma interface                        |
| dac_valid_i0    | output    |        |                                      |
| dac_data_i0     | input     | [15:0] |                                      |
| dac_enable_q0   | output    |        |                                      |
| dac_valid_q0    | output    |        |                                      |
| dac_data_q0     | input     | [15:0] |                                      |
| dac_enable_i1   | output    |        |                                      |
| dac_valid_i1    | output    |        |                                      |
| dac_data_i1     | input     | [15:0] |                                      |
| dac_enable_q1   | output    |        |                                      |
| dac_valid_q1    | output    |        |                                      |
| dac_data_q1     | input     | [15:0] |                                      |
| dac_dunf        | input     |        |                                      |
| up_dac_gpio_in  | input     | [31:0] | gpio                                 |
| up_dac_gpio_out | output    | [31:0] |                                      |
| up_pps_rcounter | input     | [31:0] | 1PPS reporting counter and interrupt |
| up_pps_status   | input     |        |                                      |
| up_pps_irq_mask | output    |        |                                      |
| up_rstn         | input     |        | processor interface                  |
| up_clk          | input     |        |                                      |
| up_wreq         | input     |        |                                      |
| up_waddr        | input     | [13:0] |                                      |
| up_wdata        | input     | [31:0] |                                      |
| up_wack         | output    |        |                                      |
| up_rreq         | input     |        |                                      |
| up_raddr        | input     | [13:0] |                                      |
| up_rdata        | output    | [31:0] |                                      |
| up_rack         | output    |        |                                      |
## Signals

| Name             | Type           | Description                |
| ---------------- | -------------- | -------------------------- |
| dac_rate_cnt     | reg     [15:0] |                            |
| dac_valid_int    | reg            |                            |
| dac_valid_i0_int | reg            |                            |
| dac_valid_q0_int | reg            |                            |
| dac_valid_i1_int | reg            |                            |
| dac_valid_q1_int | reg            |                            |
| up_wack_int      | reg            |                            |
| up_rack_int      | reg            |                            |
| up_rdata_int     | reg     [31:0] |                            |
| dac_rst          | wire           | internal clock and resets  |
| dac_data_sync_s  | wire           | internal signals           |
| dac_dds_format_s | wire           |                            |
| dac_datarate_s   | wire [15:0]    |                            |
| dac_data_int_s   | wire [47:0]    |                            |
| up_wack_s        | wire [ 5:0]    |                            |
| up_rack_s        | wire [ 5:0]    |                            |
| up_rdata_s       | wire [31:0]    |                            |
## Constants

| Name   | Type | Value | Description             |
| ------ | ---- | ----- | ----------------------- |
| CONFIG |      |       | configuration settings  |
## Processes
- unnamed: ( @(posedge dac_clk) )
- unnamed: ( @(posedge dac_clk) )
**Description**
rate counters and data sync signals

- unnamed: ( @(posedge dac_clk) )
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
## Instantiations

- i_tx_channel_0: axi_ad9361_tx_channel
**Description**
dac channel

- i_tx_channel_1: axi_ad9361_tx_channel
**Description**
dac channel

- i_tx_channel_2: axi_ad9361_tx_channel
**Description**
dac channel

- i_tx_channel_3: axi_ad9361_tx_channel
**Description**
dac channel

- i_up_dac_common: up_dac_common
**Description**
dac common processor interface

- i_delay_cntrl: up_delay_cntrl
**Description**
dac delay control

