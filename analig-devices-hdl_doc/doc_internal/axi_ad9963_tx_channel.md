# Entity: axi_ad9963_tx_channel

- **File**: axi_ad9963_tx_channel.v
## Diagram

![Diagram](axi_ad9963_tx_channel.svg "Diagram")
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

| Generic name            | Type | Value | Description  |
| ----------------------- | ---- | ----- | ------------ |
| CHANNEL_ID              |      | 32'h0 |  parameters  |
| Q_OR_I_N                |      | 0     |              |
| DAC_DDS_TYPE            |      | 1     |              |
| DAC_DDS_CORDIC_DW       |      | 14    |              |
| DAC_DDS_CORDIC_PHASE_DW |      | 13    |              |
| DATAPATH_DISABLE        |      | 0     |              |
## Ports

| Port name      | Direction | Type   | Description          |
| -------------- | --------- | ------ | -------------------- |
| dac_clk        | input     |        |  dac interface       |
| dac_rst        | input     |        |                      |
| dac_valid      | input     |        |                      |
| dma_data       | input     | [15:0] |                      |
| adc_data       | input     | [11:0] |                      |
| dac_data       | output    | [11:0] |                      |
| dac_data_out   | output    | [11:0] |                      |
| dac_data_in    | input     | [11:0] |                      |
| dma_valid      | input     |        |                      |
| out_data_valid | output    |        |                      |
| dac_enable     | output    |        |  processor interface |
| dac_data_sync  | input     |        |                      |
| dac_dds_format | input     |        |                      |
| up_rstn        | input     |        |  bus interface       |
| up_clk         | input     |        |                      |
| up_wreq        | input     |        |                      |
| up_waddr       | input     | [13:0] |                      |
| up_wdata       | input     | [31:0] |                      |
| up_wack        | output    |        |                      |
| up_rreq        | input     |        |                      |
| up_raddr       | input     | [13:0] |                      |
| up_rdata       | output    | [31:0] |                      |
| up_rack        | output    |        |                      |
## Signals

| Name                | Type           | Description          |
| ------------------- | -------------- | -------------------- |
| dac_valid_sel       | reg            |  internal registers  |
| data_source_valid   | reg            |                      |
| dac_test_data       | reg     [23:0] |                      |
| dac_test_counter    | reg     [15:0] |                      |
| dac_pat_data        | reg     [15:0] |                      |
| dma_valid_m         | reg            |                      |
| dac_iqcor_valid_s   | wire           |  internal signals    |
| dac_iqcor_data_s    | wire [15:0]    |                      |
| dac_dds_data_s      | wire [11:0]    |                      |
| dac_dds_scale_1_s   | wire [15:0]    |                      |
| dac_dds_init_1_s    | wire [15:0]    |                      |
| dac_dds_incr_1_s    | wire [15:0]    |                      |
| dac_dds_scale_2_s   | wire [15:0]    |                      |
| dac_dds_init_2_s    | wire [15:0]    |                      |
| dac_dds_incr_2_s    | wire [15:0]    |                      |
| dac_pat_data_1_s    | wire [15:0]    |                      |
| dac_pat_data_2_s    | wire [15:0]    |                      |
| dac_data_sel_s      | wire [ 3:0]    |                      |
| dac_iqcor_enb_s     | wire           |                      |
| dac_iqcor_coeff_1_s | wire [15:0]    |                      |
| dac_iqcor_coeff_2_s | wire [15:0]    |                      |
## Constants

| Name     | Type | Value      | Description |
| -------- | ---- | ---------- | ----------- |
| PRBS_SEL |      | CHANNEL_ID |             |
| PRBS_P09 |      | 0          |             |
| PRBS_P11 |      | 1          |             |
| PRBS_P15 |      | 2          |             |
| PRBS_P20 |      | 3          |             |
## Functions
- pn23 <font id="function_arguments">()</font> <font id="function_return">return ([23:0])</font>
## Processes
- unnamed: ( @(posedge dac_clk) )
  - **Type:** always
</br>**Description**
 dac iq correction 
- unnamed: ( @(posedge dac_clk) )
  - **Type:** always
</br>**Description**
 dac mux 
- unnamed: ( @(posedge dac_clk) )
  - **Type:** always
- unnamed: ( @(posedge dac_clk) )
  - **Type:** always
</br>**Description**
 pattern 
- unnamed: ( @(posedge dac_clk) )
  - **Type:** always
## Instantiations

- i_dds: ad_dds
</br>**Description**
 dds

- i_up_dac_channel: up_dac_channel
</br>**Description**
 single channel processor

