# Entity: up_dac_common

## Diagram

![Diagram](up_dac_common.svg "Diagram")
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

| Generic name      | Type   | Value | Description |
| ----------------- | ------ | ----- | ----------- |
| ID                |        | 0     | parameters  |
| FPGA_TECHNOLOGY   | [ 7:0] | 0     |             |
| FPGA_FAMILY       | [ 7:0] | 0     |             |
| SPEED_GRADE       | [ 7:0] | 0     |             |
| DEV_PACKAGE       | [ 7:0] | 0     |             |
| CONFIG            |        | 0     |             |
| CLK_EDGE_SEL      | [ 0:0] | 1'b0  |             |
| COMMON_ID         |        | 6'h10 |             |
| DRP_DISABLE       |        | 0     |             |
| USERPORTS_DISABLE |        | 0     |             |
| GPIO_DISABLE      |        | 0     |             |
## Ports

| Port name          | Direction | Type   | Description          |
| ------------------ | --------- | ------ | -------------------- |
| mmcm_rst           | output    |        | mmcm reset           |
| dac_clk            | input     |        | dac interface        |
| dac_rst            | output    |        |                      |
| dac_num_lanes      | output    | [4:0]  |                      |
| dac_sdr_ddr_n      | output    |        |                      |
| dac_sync           | output    |        |                      |
| dac_frame          | output    |        |                      |
| dac_clksel         | output    |        |                      |
| dac_par_type       | output    |        |                      |
| dac_par_enb        | output    |        |                      |
| dac_r1_mode        | output    |        |                      |
| dac_datafmt        | output    |        |                      |
| dac_datarate       | output    | [15:0] |                      |
| dac_status         | input     |        |                      |
| dac_sync_in_status | input     |        |                      |
| dac_status_unf     | input     |        |                      |
| dac_clk_ratio      | input     | [31:0] |                      |
| up_dac_ce          | output    |        |                      |
| up_pps_rcounter    | input     | [31:0] |                      |
| up_pps_status      | input     |        |                      |
| up_pps_irq_mask    | output    |        |                      |
| up_dac_r1_mode     | output    | reg    |                      |
| up_drp_sel         | output    |        | drp interface        |
| up_drp_wr          | output    |        |                      |
| up_drp_addr        | output    | [11:0] |                      |
| up_drp_wdata       | output    | [31:0] |                      |
| up_drp_rdata       | input     | [31:0] |                      |
| up_drp_ready       | input     |        |                      |
| up_drp_locked      | input     |        |                      |
| up_usr_chanmax     | output    | [ 7:0] | user channel control |
| dac_usr_chanmax    | input     | [ 7:0] |                      |
| up_dac_gpio_in     | input     | [31:0] |                      |
| up_dac_gpio_out    | output    | [31:0] |                      |
| up_rstn            | input     |        | bus interface        |
| up_clk             | input     |        |                      |
| up_wreq            | input     |        |                      |
| up_waddr           | input     | [13:0] |                      |
| up_wdata           | input     | [31:0] |                      |
| up_wack            | output    |        |                      |
| up_rreq            | input     |        |                      |
| up_raddr           | input     | [13:0] |                      |
| up_rdata           | output    | [31:0] |                      |
| up_rack            | output    |        |                      |
## Signals

| Name                | Type           | Description         |
| ------------------- | -------------- | ------------------- |
| up_core_preset      | reg            | internal registers  |
| up_mmcm_preset      | reg            |                     |
| up_wack_int         | reg            |                     |
| up_scratch          | reg     [31:0] |                     |
| up_dac_clk_enb_int  | reg            |                     |
| up_dac_clk_enb      | reg            |                     |
| up_mmcm_resetn      | reg            |                     |
| up_resetn           | reg            |                     |
| up_dac_sync         | reg            |                     |
| up_dac_num_lanes    | reg      [4:0] |                     |
| up_dac_sdr_ddr_n    | reg            |                     |
| up_dac_par_type     | reg            |                     |
| up_dac_par_enb      | reg            |                     |
| up_dac_datafmt      | reg            |                     |
| up_dac_datarate     | reg     [15:0] |                     |
| up_dac_frame        | reg            |                     |
| up_dac_clksel       | reg            |                     |
| up_status_unf       | reg            |                     |
| up_usr_chanmax_int  | reg     [ 7:0] |                     |
| up_dac_gpio_out_int | reg     [31:0] |                     |
| up_timer            | reg     [31:0] |                     |
| up_rack_int         | reg            |                     |
| up_rdata_int        | reg     [31:0] |                     |
| dac_sync_d          | reg            |                     |
| dac_sync_2d         | reg            |                     |
| dac_sync_count      | reg     [ 5:0] |                     |
| dac_sync_int        | reg            |                     |
| dac_frame_d         | reg            |                     |
| dac_frame_2d        | reg            |                     |
| dac_frame_int       | reg            |                     |
| up_wreq_s           | wire           | internal signals    |
| up_rreq_s           | wire           |                     |
| up_xfer_done_s      | wire           |                     |
| up_status_s         | wire           |                     |
| up_sync_in_status   | wire           |                     |
| up_status_unf_s     | wire           |                     |
| dac_sync_s          | wire           |                     |
| dac_frame_s         | wire           |                     |
| up_dac_clk_count_s  | wire [31:0]    |                     |
| up_drp_status_s     | wire           |                     |
| up_drp_rwn_s        | wire           |                     |
| up_drp_rdata_hold_s | wire [31:0]    |                     |
| dac_rst_n           | wire           |                     |
| dac_rst_s           | wire           |                     |
## Constants

| Name    | Type | Value        | Description |
| ------- | ---- | ------------ | ----------- |
| VERSION |      | 32'h00090162 | parameters  |
## Processes
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
**Description**
timer with premature termination

- unnamed: ( @(negedge up_rstn or posedge up_clk) )
- unnamed: ( @(posedge dac_clk) )
## Instantiations

- i_mmcm_rst_reg: ad_rst
**Description**
resets

- i_core_rst_reg: ad_rst
- i_xfer_cntrl: up_xfer_cntrl
**Description**
dac control & status

- i_xfer_status: up_xfer_status
- i_clock_mon: up_clock_mon
**Description**
dac clock monitor

