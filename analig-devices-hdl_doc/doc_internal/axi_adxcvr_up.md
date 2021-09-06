# Entity: axi_adxcvr_up

- **File**: axi_adxcvr_up.v
## Diagram

![Diagram](axi_adxcvr_up.svg "Diagram")
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

| Generic name    | Type    | Value | Description                |
| --------------- | ------- | ----- | -------------------------- |
| ID              | integer | 0     |  parameters                |
| NUM_OF_LANES    | integer | 8     |                            |
| XCVR_TYPE       | integer | 0     |                            |
| LINK_MODE       | integer | 1     |  2 - 64B/66B;  1 - 8B/10B  |
| FPGA_TECHNOLOGY | [ 7:0]  | 0     |                            |
| FPGA_FAMILY     | [ 7:0]  | 0     |                            |
| SPEED_GRADE     | [ 7:0]  | 0     |                            |
| DEV_PACKAGE     | [ 7:0]  | 0     |                            |
| FPGA_VOLTAGE    | [15:0]  | 0     |                            |
| TX_OR_RX_N      | integer | 0     |                            |
| QPLL_ENABLE     | integer | 1     |                            |
| LPM_OR_DFE_N    |         | 1     |                            |
| RATE            | [ 2:0]  | 3'd0  |                            |
| TX_DIFFCTRL     | [ 3:0]  | 4'd8  |                            |
| TX_POSTCURSOR   | [ 4:0]  | 5'd0  |                            |
| TX_PRECURSOR    | [ 4:0]  | 5'd0  |                            |
| SYS_CLK_SEL     | [ 1:0]  | 2'd3  |                            |
| OUT_CLK_SEL     | [ 2:0]  | 3'd4  |                            |
## Ports

| Port name           | Direction | Type       | Description    |
| ------------------- | --------- | ---------- | -------------- |
| up_cm_sel           | output    | [ 7:0]     |  common        |
| up_cm_enb           | output    |            |                |
| up_cm_addr          | output    | [11:0]     |                |
| up_cm_wr            | output    |            |                |
| up_cm_wdata         | output    | [15:0]     |                |
| up_cm_rdata         | input     | [15:0]     |                |
| up_cm_ready         | input     |            |                |
| up_ch_pll_locked    | input     |            |  channel       |
| up_ch_rst           | output    |            |                |
| up_ch_user_ready    | output    |            |                |
| up_ch_rst_done      | input     |            |                |
| up_ch_prbsforceerr  | output    |            |                |
| up_ch_prbssel       | output    | [ 3:0]     |                |
| up_ch_prbscntreset  | output    |            |                |
| up_ch_prbserr       | input     |            |                |
| up_ch_prbslocked    | input     |            |                |
| up_ch_lpm_dfe_n     | output    |            |                |
| up_ch_rate          | output    | [ 2:0]     |                |
| up_ch_sys_clk_sel   | output    | [ 1:0]     |                |
| up_ch_out_clk_sel   | output    | [ 2:0]     |                |
| up_ch_tx_diffctrl   | output    | [ 4:0]     |                |
| up_ch_tx_postcursor | output    | [ 4:0]     |                |
| up_ch_tx_precursor  | output    | [ 4:0]     |                |
| up_ch_sel           | output    | [ 7:0]     |                |
| up_ch_enb           | output    |            |                |
| up_ch_addr          | output    | [11:0]     |                |
| up_ch_wr            | output    |            |                |
| up_ch_wdata         | output    | [15:0]     |                |
| up_ch_rdata         | input     | [15:0]     |                |
| up_ch_ready         | input     |            |                |
| up_es_sel           | output    | [ 7:0]     |  eye-scan      |
| up_es_req           | output    |            |                |
| up_es_reset         | output    | reg [15:0] |                |
| up_es_ack           | input     |            |                |
| up_es_pscale        | output    | [ 4:0]     |                |
| up_es_vrange        | output    | [ 1:0]     |                |
| up_es_vstep         | output    | [ 7:0]     |                |
| up_es_vmax          | output    | [ 7:0]     |                |
| up_es_vmin          | output    | [ 7:0]     |                |
| up_es_hmax          | output    | [11:0]     |                |
| up_es_hmin          | output    | [11:0]     |                |
| up_es_hstep         | output    | [11:0]     |                |
| up_es_saddr         | output    | [31:0]     |                |
| up_es_status        | input     |            |                |
| up_status           | output    |            |  status        |
| up_pll_rst          | output    |            |                |
| up_rstn             | input     |            |  bus interface |
| up_clk              | input     |            |                |
| up_wreq             | input     |            |                |
| up_waddr            | input     | [ 9:0]     |                |
| up_wdata            | input     | [31:0]     |                |
| up_wack             | output    |            |                |
| up_rreq             | input     |            |                |
| up_raddr            | input     | [ 9:0]     |                |
| up_rdata            | output    | [31:0]     |                |
| up_rack             | output    |            |                |
## Signals

| Name                 | Type           | Description          |
| -------------------- | -------------- | -------------------- |
| up_wreq_d            | reg            |  internal registers  |
| up_scratch           | reg     [31:0] |                      |
| up_resetn            | reg            |                      |
| up_pll_rst_cnt       | reg     [ 3:0] |                      |
| up_rst_cnt           | reg     [ 3:0] |                      |
| up_user_ready_cnt    | reg     [ 6:0] |                      |
| up_status_int        | reg            |                      |
| up_lpm_dfe_n         | reg            |                      |
| up_rate              | reg     [ 2:0] |                      |
| up_sys_clk_sel       | reg     [ 1:0] |                      |
| up_out_clk_sel       | reg     [ 2:0] |                      |
| up_tx_diffctrl       | reg     [ 4:0] |                      |
| up_tx_postcursor     | reg     [ 4:0] |                      |
| up_tx_precursor      | reg     [ 4:0] |                      |
| up_icm_sel           | reg     [ 7:0] |                      |
| up_icm_enb           | reg            |                      |
| up_icm_wr            | reg            |                      |
| up_icm_data          | reg     [28:0] |                      |
| up_icm_rdata         | reg     [15:0] |                      |
| up_icm_busy          | reg            |                      |
| up_ich_sel           | reg     [ 7:0] |                      |
| up_ich_enb           | reg            |                      |
| up_ich_wr            | reg            |                      |
| up_ich_data          | reg     [28:0] |                      |
| up_ich_rdata         | reg     [15:0] |                      |
| up_ich_busy          | reg            |                      |
| up_ies_sel           | reg     [ 7:0] |                      |
| up_ies_req           | reg            |                      |
| up_ies_prescale      | reg     [ 4:0] |                      |
| up_ies_voffset_range | reg     [ 1:0] |                      |
| up_ies_voffset_step  | reg     [ 7:0] |                      |
| up_ies_voffset_max   | reg     [ 7:0] |                      |
| up_ies_voffset_min   | reg     [ 7:0] |                      |
| up_ies_hoffset_max   | reg     [11:0] |                      |
| up_ies_hoffset_min   | reg     [11:0] |                      |
| up_ies_hoffset_step  | reg     [11:0] |                      |
| up_ies_start_addr    | reg     [31:0] |                      |
| up_ies_status        | reg            |                      |
| up_rreq_d            | reg            |                      |
| up_rdata_d           | reg     [31:0] |                      |
| up_prbssel           | reg      [3:0] |                      |
| up_prbscntreset      | reg            |                      |
| up_prbsforceerr      | reg            |                      |
| up_rparam_s          | wire [31:0]    |  internal signals    |
## Constants

| Name    | Type   | Value        | Description  |
| ------- | ------ | ------------ | ------------ |
| VERSION | [31:0] | 32'h00110461 |  parameters  |
## Processes
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
</br>**Description**
 reset-controller 
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
