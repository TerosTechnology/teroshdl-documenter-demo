# Entity: up_adc_channel

## Diagram

![Diagram](up_adc_channel.svg "Diagram")
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

| Generic name         | Type | Value | Description |
| -------------------- | ---- | ----- | ----------- |
| COMMON_ID            |      | 6'h01 | parameters  |
| CHANNEL_ID           |      | 4'h0  |             |
| USERPORTS_DISABLE    |      | 0     |             |
| DATAFORMAT_DISABLE   |      | 0     |             |
| DCFILTER_DISABLE     |      | 0     |             |
| IQCORRECTION_DISABLE |      | 0     |             |
## Ports

| Port name                   | Direction | Type   | Description   |
| --------------------------- | --------- | ------ | ------------- |
| adc_clk                     | input     |        | adc interface |
| adc_rst                     | input     |        |               |
| adc_enable                  | output    |        |               |
| adc_iqcor_enb               | output    |        |               |
| adc_dcfilt_enb              | output    |        |               |
| adc_dfmt_se                 | output    |        |               |
| adc_dfmt_type               | output    |        |               |
| adc_dfmt_enable             | output    |        |               |
| adc_dcfilt_offset           | output    | [15:0] |               |
| adc_dcfilt_coeff            | output    | [15:0] |               |
| adc_iqcor_coeff_1           | output    | [15:0] |               |
| adc_iqcor_coeff_2           | output    | [15:0] |               |
| adc_pnseq_sel               | output    | [ 3:0] |               |
| adc_data_sel                | output    | [ 3:0] |               |
| adc_pn_err                  | input     |        |               |
| adc_pn_oos                  | input     |        |               |
| adc_or                      | input     |        |               |
| up_adc_pn_err               | output    |        |               |
| up_adc_pn_oos               | output    |        |               |
| up_adc_or                   | output    |        |               |
| up_usr_datatype_be          | output    |        | user controls |
| up_usr_datatype_signed      | output    |        |               |
| up_usr_datatype_shift       | output    | [ 7:0] |               |
| up_usr_datatype_total_bits  | output    | [ 7:0] |               |
| up_usr_datatype_bits        | output    | [ 7:0] |               |
| up_usr_decimation_m         | output    | [15:0] |               |
| up_usr_decimation_n         | output    | [15:0] |               |
| adc_usr_datatype_be         | input     |        |               |
| adc_usr_datatype_signed     | input     |        |               |
| adc_usr_datatype_shift      | input     | [ 7:0] |               |
| adc_usr_datatype_total_bits | input     | [ 7:0] |               |
| adc_usr_datatype_bits       | input     | [ 7:0] |               |
| adc_usr_decimation_m        | input     | [15:0] |               |
| adc_usr_decimation_n        | input     | [15:0] |               |
| up_rstn                     | input     |        | bus interface |
| up_clk                      | input     |        |               |
| up_wreq                     | input     |        |               |
| up_waddr                    | input     | [13:0] |               |
| up_wdata                    | input     | [31:0] |               |
| up_wack                     | output    |        |               |
| up_rreq                     | input     |        |               |
| up_raddr                    | input     | [13:0] |               |
| up_rdata                    | output    | [31:0] |               |
| up_rack                     | output    |        |               |
## Signals

| Name                           | Type           | Description         |
| ------------------------------ | -------------- | ------------------- |
| up_wack_int                    | reg            | internal registers  |
| up_adc_lb_enb                  | reg            |                     |
| up_adc_pn_sel                  | reg            |                     |
| up_adc_iqcor_enb               | reg            |                     |
| up_adc_dcfilt_enb              | reg            |                     |
| up_adc_dfmt_se                 | reg            |                     |
| up_adc_dfmt_type               | reg            |                     |
| up_adc_dfmt_enable             | reg            |                     |
| up_adc_pn_type                 | reg            |                     |
| up_adc_enable                  | reg            |                     |
| up_adc_pn_err_int              | reg            |                     |
| up_adc_pn_oos_int              | reg            |                     |
| up_adc_or_int                  | reg            |                     |
| up_adc_dcfilt_offset           | reg     [15:0] |                     |
| up_adc_dcfilt_coeff            | reg     [15:0] |                     |
| up_adc_iqcor_coeff_1           | reg     [15:0] |                     |
| up_adc_iqcor_coeff_2           | reg     [15:0] |                     |
| up_adc_pnseq_sel               | reg     [ 3:0] |                     |
| up_adc_data_sel                | reg     [ 3:0] |                     |
| up_usr_datatype_be_int         | reg            |                     |
| up_usr_datatype_signed_int     | reg            |                     |
| up_usr_datatype_shift_int      | reg     [ 7:0] |                     |
| up_usr_datatype_total_bits_int | reg     [ 7:0] |                     |
| up_usr_datatype_bits_int       | reg     [ 7:0] |                     |
| up_usr_decimation_m_int        | reg     [15:0] |                     |
| up_usr_decimation_n_int        | reg     [15:0] |                     |
| up_rack_int                    | reg            |                     |
| up_rdata_int                   | reg     [31:0] |                     |
| up_adc_iqcor_coeff_tc_1        | reg     [15:0] |                     |
| up_adc_iqcor_coeff_tc_2        | reg     [15:0] |                     |
| up_adc_pnseq_sel_m             | reg     [ 3:0] |                     |
| up_adc_data_sel_m              | reg     [ 3:0] |                     |
| up_wreq_s                      | wire           | internal signals    |
| up_rreq_s                      | wire           |                     |
| up_adc_pn_err_s                | wire           |                     |
| up_adc_pn_oos_s                | wire           |                     |
| up_adc_or_s                    | wire           |                     |
## Functions
- sm2tc <font id="function_arguments">()</font> <font id="function_return">return ([15:0])</font>
**Description**
2's complement function

## Processes
- unnamed: ( @(posedge up_clk) )
- unnamed: ( @(posedge up_clk) )
- unnamed: ( @(posedge up_clk) )
- unnamed: ( @(posedge up_clk) )
- unnamed: ( @(posedge up_clk) )
**Description**
change coefficients to 2's complements

- unnamed: ( @(posedge up_clk) )
**Description**
data/pn sources

## Instantiations

- i_xfer_cntrl: up_xfer_cntrl
**Description**
adc control & status

- i_xfer_status: up_xfer_status
