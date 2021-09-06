# Entity: up_dac_channel

- **File**: up_dac_channel.v
## Diagram

![Diagram](up_dac_channel.svg "Diagram")
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

| Generic name         | Type | Value | Description  |
| -------------------- | ---- | ----- | ------------ |
| COMMON_ID            |      | 6'h11 |  parameters  |
| CHANNEL_ID           |      | 4'h0  |              |
| CHANNEL_NUMBER       |      | 8'b0  |              |
| DDS_DISABLE          |      | 0     |              |
| USERPORTS_DISABLE    |      | 0     |              |
| IQCORRECTION_DISABLE |      | 0     |              |
| XBAR_ENABLE          |      | 0     |              |
## Ports

| Port name                   | Direction | Type   | Description    |
| --------------------------- | --------- | ------ | -------------- |
| dac_clk                     | input     |        |  dac interface |
| dac_rst                     | input     |        |                |
| dac_dds_scale_1             | output    | [15:0] |                |
| dac_dds_init_1              | output    | [15:0] |                |
| dac_dds_incr_1              | output    | [15:0] |                |
| dac_dds_scale_2             | output    | [15:0] |                |
| dac_dds_init_2              | output    | [15:0] |                |
| dac_dds_incr_2              | output    | [15:0] |                |
| dac_pat_data_1              | output    | [15:0] |                |
| dac_pat_data_2              | output    | [15:0] |                |
| dac_data_sel                | output    | [ 3:0] |                |
| dac_mask_enable             | output    |        |                |
| dac_iq_mode                 | output    | [ 1:0] |                |
| dac_iqcor_enb               | output    |        |                |
| dac_iqcor_coeff_1           | output    | [15:0] |                |
| dac_iqcor_coeff_2           | output    | [15:0] |                |
| dac_src_chan_sel            | output    | [7:0]  |                |
| up_usr_datatype_be          | output    |        |  user controls |
| up_usr_datatype_signed      | output    |        |                |
| up_usr_datatype_shift       | output    | [ 7:0] |                |
| up_usr_datatype_total_bits  | output    | [ 7:0] |                |
| up_usr_datatype_bits        | output    | [ 7:0] |                |
| up_usr_interpolation_m      | output    | [15:0] |                |
| up_usr_interpolation_n      | output    | [15:0] |                |
| dac_usr_datatype_be         | input     |        |                |
| dac_usr_datatype_signed     | input     |        |                |
| dac_usr_datatype_shift      | input     | [ 7:0] |                |
| dac_usr_datatype_total_bits | input     | [ 7:0] |                |
| dac_usr_datatype_bits       | input     | [ 7:0] |                |
| dac_usr_interpolation_m     | input     | [15:0] |                |
| dac_usr_interpolation_n     | input     | [15:0] |                |
| up_rstn                     | input     |        |  bus interface |
| up_clk                      | input     |        |                |
| up_wreq                     | input     |        |                |
| up_waddr                    | input     | [13:0] |                |
| up_wdata                    | input     | [31:0] |                |
| up_wack                     | output    |        |                |
| up_rreq                     | input     |        |                |
| up_raddr                    | input     | [13:0] |                |
| up_rdata                    | output    | [31:0] |                |
| up_rack                     | output    |        |                |
## Signals

| Name                           | Type           | Description          |
| ------------------------------ | -------------- | -------------------- |
| up_wack_int                    | reg            |  internal registers  |
| up_dac_dds_scale_1             | reg     [15:0] |                      |
| up_dac_dds_init_1              | reg     [15:0] |                      |
| up_dac_dds_incr_1              | reg     [15:0] |                      |
| up_dac_dds_scale_2             | reg     [15:0] |                      |
| up_dac_dds_init_2              | reg     [15:0] |                      |
| up_dac_dds_incr_2              | reg     [15:0] |                      |
| up_dac_pat_data_2              | reg     [15:0] |                      |
| up_dac_pat_data_1              | reg     [15:0] |                      |
| up_dac_iqcor_enb               | reg            |                      |
| up_dac_lb_enb                  | reg            |                      |
| up_dac_pn_enb                  | reg            |                      |
| up_dac_data_sel                | reg     [ 3:0] |                      |
| up_dac_iqcor_coeff_1           | reg     [15:0] |                      |
| up_dac_iqcor_coeff_2           | reg     [15:0] |                      |
| up_usr_datatype_be_int         | reg            |                      |
| up_usr_datatype_signed_int     | reg            |                      |
| up_usr_datatype_shift_int      | reg     [ 7:0] |                      |
| up_usr_datatype_total_bits_int | reg     [ 7:0] |                      |
| up_usr_datatype_bits_int       | reg     [ 7:0] |                      |
| up_usr_interpolation_m_int     | reg     [15:0] |                      |
| up_usr_interpolation_n_int     | reg     [15:0] |                      |
| up_dac_iq_mode                 | reg     [ 1:0] |                      |
| up_rack_int                    | reg            |                      |
| up_rdata_int                   | reg     [31:0] |                      |
| up_dac_dds_scale_tc_1          | reg     [15:0] |                      |
| up_dac_dds_scale_tc_2          | reg     [15:0] |                      |
| up_dac_iqcor_coeff_tc_1        | reg     [15:0] |                      |
| up_dac_iqcor_coeff_tc_2        | reg     [15:0] |                      |
| up_dac_data_sel_m              | reg     [ 3:0] |                      |
| up_dac_src_chan_sel            | reg     [ 7:0] |                      |
| up_dac_mask_enable             | reg            |                      |
| up_wreq_s                      | wire           |  internal signals    |
| up_rreq_s                      | wire           |                      |
## Functions
- sm2tc <font id="function_arguments">()</font> <font id="function_return">return ([15:0])</font>
</br>**Description**
 2's complement function

## Processes
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
</br>**Description**
 change coefficients to 2's complements 
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
</br>**Description**
 backward compatibility 
## Instantiations

- i_xfer_cntrl: up_xfer_cntrl
</br>**Description**
 dac control & status

