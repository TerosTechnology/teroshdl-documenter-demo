# Entity: axi_adxcvr_es

- **File**: axi_adxcvr_es.v
## Diagram

![Diagram](axi_adxcvr_es.svg "Diagram")
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

| Generic name | Type    | Value | Description  |
| ------------ | ------- | ----- | ------------ |
| XCVR_TYPE    | integer | 0     |  parameters  |
| TX_OR_RX_N   | integer | 0     |              |
## Ports

| Port name       | Direction | Type   | Description    |
| --------------- | --------- | ------ | -------------- |
| up_rstn         | input     |        |  up interface  |
| up_clk          | input     |        |                |
| up_es_enb       | output    |        |                |
| up_es_addr      | output    | [11:0] |                |
| up_es_wr        | output    |        |                |
| up_es_wdata     | output    | [15:0] |                |
| up_es_rdata     | input     | [15:0] |                |
| up_es_ready     | input     |        |                |
| up_ch_lpm_dfe_n | input     |        |                |
| up_es_req       | input     |        |                |
| up_es_ack       | output    |        |                |
| up_es_pscale    | input     | [ 4:0] |                |
| up_es_vrange    | input     | [ 1:0] |                |
| up_es_vstep     | input     | [ 7:0] |                |
| up_es_vmax      | input     | [ 7:0] |                |
| up_es_vmin      | input     | [ 7:0] |                |
| up_es_hmax      | input     | [11:0] |                |
| up_es_hmin      | input     | [11:0] |                |
| up_es_hstep     | input     | [11:0] |                |
| up_es_saddr     | input     | [31:0] |                |
| up_es_status    | output    |        |                |
| up_axi_awvalid  | output    |        |  axi interface |
| up_axi_awaddr   | output    | [31:0] |                |
| up_axi_awprot   | output    | [ 2:0] |                |
| up_axi_awready  | input     |        |                |
| up_axi_wvalid   | output    |        |                |
| up_axi_wdata    | output    | [31:0] |                |
| up_axi_wstrb    | output    | [ 3:0] |                |
| up_axi_wready   | input     |        |                |
| up_axi_bvalid   | input     |        |                |
| up_axi_bresp    | input     | [ 1:0] |                |
| up_axi_bready   | output    |        |                |
| up_axi_arvalid  | output    |        |                |
| up_axi_araddr   | output    | [31:0] |                |
| up_axi_arprot   | output    | [ 2:0] |                |
| up_axi_arready  | input     |        |                |
| up_axi_rvalid   | input     |        |                |
| up_axi_rdata    | input     | [31:0] |                |
| up_axi_rresp    | input     | [ 1:0] |                |
| up_axi_rready   | output    |        |                |
## Signals

| Name          | Type           | Description          |
| ------------- | -------------- | -------------------- |
| up_awvalid    | reg            |  internal registers  |
| up_awaddr     | reg     [31:0] |                      |
| up_wvalid     | reg            |                      |
| up_wdata      | reg     [31:0] |                      |
| up_status     | reg            |                      |
| up_ut         | reg            |                      |
| up_daddr      | reg     [31:0] |                      |
| up_hindex     | reg     [11:0] |                      |
| up_vindex     | reg     [ 7:0] |                      |
| up_hdata      | reg     [15:0] |                      |
| up_vdata      | reg     [15:0] |                      |
| up_cdata      | reg     [15:0] |                      |
| up_sdata      | reg     [15:0] |                      |
| up_edata      | reg     [15:0] |                      |
| up_req_d      | reg            |                      |
| up_ack        | reg            |                      |
| up_fsm        | reg     [ 4:0] |                      |
| up_enb        | reg            |                      |
| up_addr       | reg     [11:0] |                      |
| up_wr         | reg            |                      |
| up_data       | reg     [15:0] |                      |
| up_heos_s     | wire           |  internal signals    |
| up_eos_s      | wire           |                      |
| up_ut_s       | wire           |                      |
| up_vindex_m_s | wire [ 7:0]    |                      |
| up_vindex_n_s | wire [ 7:0]    |                      |
| up_vindex_s   | wire [ 7:0]    |                      |
| up_start_s    | wire           |                      |
## Constants

| Name                 | Type   | Value                                              | Description        |
| -------------------- | ------ | -------------------------------------------------- | ------------------ |
| GTXE2                |        | 2                                                  |  local parameters  |
| GTHE3                |        | 5                                                  |                    |
| GTHE4                |        | 8                                                  |                    |
| GTYE4                |        | 9                                                  |                    |
| ES_DRP_CTRL_ADDR     | [11:0] | 12'h03d : (XCVR_TYPE == GTHE3) ? 12'h03c : 12'h03c |  addresses         |
| ES_DRP_HOFFSET_ADDR  | [11:0] | 12'h03c : (XCVR_TYPE == GTHE3) ? 12'h04f : 12'h04f |                    |
| ES_DRP_VOFFSET_ADDR  | [11:0] | 12'h03b : (XCVR_TYPE == GTHE3) ? 12'h097 : 12'h097 |                    |
| ES_DRP_STATUS_ADDR   | [11:0] | 12'h151 : (XCVR_TYPE == GTHE3) ? 12'h153 : 12'h253 |                    |
| ES_DRP_SCNT_ADDR     | [11:0] | 12'h150 : (XCVR_TYPE == GTHE3) ? 12'h152 : 12'h252 |                    |
| ES_DRP_ECNT_ADDR     | [11:0] | 12'h14f : (XCVR_TYPE == GTHE3) ? 12'h151 : 12'h251 |                    |
| ES_FSM_IDLE          | [ 4:0] | 6'h00                                              |  fsm-states        |
| ES_FSM_HOFFSET_READ  | [ 4:0] | 6'h01                                              |                    |
| ES_FSM_HOFFSET_RRDY  | [ 4:0] | 6'h02                                              |                    |
| ES_FSM_HOFFSET_WRITE | [ 4:0] | 6'h03                                              |                    |
| ES_FSM_HOFFSET_WRDY  | [ 4:0] | 6'h04                                              |                    |
| ES_FSM_VOFFSET_READ  | [ 4:0] | 6'h05                                              |                    |
| ES_FSM_VOFFSET_RRDY  | [ 4:0] | 6'h06                                              |                    |
| ES_FSM_VOFFSET_WRITE | [ 4:0] | 6'h07                                              |                    |
| ES_FSM_VOFFSET_WRDY  | [ 4:0] | 6'h08                                              |                    |
| ES_FSM_CTRL_READ     | [ 4:0] | 6'h09                                              |                    |
| ES_FSM_CTRL_RRDY     | [ 4:0] | 6'h0a                                              |                    |
| ES_FSM_START_WRITE   | [ 4:0] | 6'h0b                                              |                    |
| ES_FSM_START_WRDY    | [ 4:0] | 6'h0c                                              |                    |
| ES_FSM_STATUS_READ   | [ 4:0] | 6'h0d                                              |                    |
| ES_FSM_STATUS_RRDY   | [ 4:0] | 6'h0e                                              |                    |
| ES_FSM_STOP_WRITE    | [ 4:0] | 6'h0f                                              |                    |
| ES_FSM_STOP_WRDY     | [ 4:0] | 6'h10                                              |                    |
| ES_FSM_SCNT_READ     | [ 4:0] | 6'h11                                              |                    |
| ES_FSM_SCNT_RRDY     | [ 4:0] | 6'h12                                              |                    |
| ES_FSM_ECNT_READ     | [ 4:0] | 6'h13                                              |                    |
| ES_FSM_ECNT_RRDY     | [ 4:0] | 6'h14                                              |                    |
| ES_FSM_AXI_WRITE     | [ 4:0] | 6'h15                                              |                    |
| ES_FSM_AXI_READY     | [ 4:0] | 6'h16                                              |                    |
| ES_FSM_UPDATE        | [ 4:0] | 6'h17                                              |                    |
## Processes
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
**Description**
 axi write 
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
**Description**
 read-modify-write 
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
**Description**
 es-fsm 
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
**Description**
 channel access 
## State machines

- es-fsm![Diagram_state_machine_0]( stm_axi_adxcvr_es_00.svg "Diagram")