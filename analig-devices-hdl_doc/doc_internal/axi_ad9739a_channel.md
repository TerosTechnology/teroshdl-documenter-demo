# Entity: axi_ad9739a_channel

## Diagram

![Diagram](axi_ad9739a_channel.svg "Diagram")
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
| CHANNEL_ID              |      | 32'h0 |             |
| DAC_DDS_TYPE            |      | 1     |             |
| DAC_DDS_CORDIC_DW       |      | 16    |             |
| DAC_DDS_CORDIC_PHASE_DW |      | 16    |             |
| DATAPATH_DISABLE        |      | 0     |             |
## Ports

| Port name      | Direction | Type    | Description         |
| -------------- | --------- | ------- | ------------------- |
| dac_div_clk    | input     |         | dac interface       |
| dac_rst        | input     |         |                     |
| dac_enable     | output    |         |                     |
| dac_data_00    | output    | [ 15:0] |                     |
| dac_data_01    | output    | [ 15:0] |                     |
| dac_data_02    | output    | [ 15:0] |                     |
| dac_data_03    | output    | [ 15:0] |                     |
| dac_data_04    | output    | [ 15:0] |                     |
| dac_data_05    | output    | [ 15:0] |                     |
| dac_data_06    | output    | [ 15:0] |                     |
| dac_data_07    | output    | [ 15:0] |                     |
| dac_data_08    | output    | [ 15:0] |                     |
| dac_data_09    | output    | [ 15:0] |                     |
| dac_data_10    | output    | [ 15:0] |                     |
| dac_data_11    | output    | [ 15:0] |                     |
| dac_data_12    | output    | [ 15:0] |                     |
| dac_data_13    | output    | [ 15:0] |                     |
| dac_data_14    | output    | [ 15:0] |                     |
| dac_data_15    | output    | [ 15:0] |                     |
| dma_data       | input     | [255:0] |                     |
| dac_data_sync  | input     |         | processor interface |
| dac_dds_format | input     |         |                     |
| up_rstn        | input     |         | bus interface       |
| up_clk         | input     |         |                     |
| up_wreq        | input     |         |                     |
| up_waddr       | input     | [ 13:0] |                     |
| up_wdata       | input     | [ 31:0] |                     |
| up_wack        | output    |         |                     |
| up_rreq        | input     |         |                     |
| up_raddr       | input     | [ 13:0] |                     |
| up_rdata       | output    | [ 31:0] |                     |
| up_rack        | output    |         |                     |
## Signals

| Name              | Type         | Description       |
| ----------------- | ------------ | ----------------- |
| dac_dds_data_s    | wire [255:0] | internal signals  |
| dac_dds_scale_1_s | wire [ 15:0] |                   |
| dac_dds_init_1_s  | wire [ 15:0] |                   |
| dac_dds_incr_1_s  | wire [ 15:0] |                   |
| dac_dds_scale_2_s | wire [ 15:0] |                   |
| dac_dds_init_2_s  | wire [ 15:0] |                   |
| dac_dds_incr_2_s  | wire [ 15:0] |                   |
| dac_pat_data_1_s  | wire [ 15:0] |                   |
| dac_pat_data_2_s  | wire [ 15:0] |                   |
| dac_data_sel_s    | wire [  3:0] |                   |
## Processes
- unnamed: ( @(posedge dac_div_clk) )
**Description**
dac data select

## Instantiations

- i_dds: ad_dds
**Description**
dds

- i_up_dac_channel: up_dac_channel
**Description**
single channel processor

