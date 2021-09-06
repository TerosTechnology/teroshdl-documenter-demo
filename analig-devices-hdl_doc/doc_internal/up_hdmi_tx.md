# Entity: up_hdmi_tx

- **File**: up_hdmi_tx.v
## Diagram

![Diagram](up_hdmi_tx.svg "Diagram")
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

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| ID           |      | 0     |             |
## Ports

| Port name       | Direction | Type   | Description     |
| --------------- | --------- | ------ | --------------- |
| hdmi_clk        | input     |        |  hdmi interface |
| hdmi_rst        | output    |        |                 |
| hdmi_csc_bypass | output    |        |                 |
| hdmi_ss_bypass  | output    |        |                 |
| hdmi_srcsel     | output    | [ 1:0] |                 |
| hdmi_const_rgb  | output    | [23:0] |                 |
| hdmi_hl_active  | output    | [15:0] |                 |
| hdmi_hl_width   | output    | [15:0] |                 |
| hdmi_hs_width   | output    | [15:0] |                 |
| hdmi_he_max     | output    | [15:0] |                 |
| hdmi_he_min     | output    | [15:0] |                 |
| hdmi_vf_active  | output    | [15:0] |                 |
| hdmi_vf_width   | output    | [15:0] |                 |
| hdmi_vs_width   | output    | [15:0] |                 |
| hdmi_ve_max     | output    | [15:0] |                 |
| hdmi_ve_min     | output    | [15:0] |                 |
| hdmi_clip_max   | output    | [23:0] |                 |
| hdmi_clip_min   | output    | [23:0] |                 |
| hdmi_status     | input     |        |                 |
| hdmi_tpm_oos    | input     |        |                 |
| hdmi_clk_ratio  | input     | [31:0] |                 |
| vdma_clk        | input     |        |  vdma interface |
| vdma_rst        | output    |        |                 |
| vdma_ovf        | input     |        |                 |
| vdma_unf        | input     |        |                 |
| vdma_tpm_oos    | input     |        |                 |
| up_rstn         | input     |        |  bus interface  |
| up_clk          | input     |        |                 |
| up_wreq         | input     |        |                 |
| up_waddr        | input     | [13:0] |                 |
| up_wdata        | input     | [31:0] |                 |
| up_wack         | output    |        |                 |
| up_rreq         | input     |        |                 |
| up_raddr        | input     | [13:0] |                 |
| up_rdata        | output    | [31:0] |                 |
| up_rack         | output    |        |                 |
## Signals

| Name                | Type           | Description          |
| ------------------- | -------------- | -------------------- |
| up_core_preset      | reg            |  internal registers  |
| up_scratch          | reg     [31:0] |                      |
| up_resetn           | reg            |                      |
| up_csc_bypass       | reg            |                      |
| up_ss_bypass        | reg            |                      |
| up_srcsel           | reg     [ 1:0] |                      |
| up_const_rgb        | reg     [23:0] |                      |
| up_vdma_ovf         | reg            |                      |
| up_vdma_unf         | reg            |                      |
| up_hdmi_tpm_oos     | reg            |                      |
| up_vdma_tpm_oos     | reg            |                      |
| up_hl_active        | reg     [15:0] |                      |
| up_hl_width         | reg     [15:0] |                      |
| up_hs_width         | reg     [15:0] |                      |
| up_he_max           | reg     [15:0] |                      |
| up_he_min           | reg     [15:0] |                      |
| up_vf_active        | reg     [15:0] |                      |
| up_vf_width         | reg     [15:0] |                      |
| up_vs_width         | reg     [15:0] |                      |
| up_ve_max           | reg     [15:0] |                      |
| up_ve_min           | reg     [15:0] |                      |
| up_clip_max         | reg     [23:0] |                      |
| up_clip_min         | reg     [23:0] |                      |
| up_wreq_s           | wire           |  internal signals    |
| up_rreq_s           | wire           |                      |
| up_hdmi_status_s    | wire           |                      |
| up_hdmi_tpm_oos_s   | wire           |                      |
| up_hdmi_clk_count_s | wire [31:0]    |                      |
| up_vdma_ovf_s       | wire           |                      |
| up_vdma_unf_s       | wire           |                      |
| up_vdma_tpm_oos_s   | wire           |                      |
## Constants

| Name          | Type | Value        | Description |
| ------------- | ---- | ------------ | ----------- |
| PCORE_VERSION |      | 32'h00040063 |             |
## Processes
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
**Description**
 processor write interface 
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
**Description**
 processor read interface 
## Instantiations

- i_core_rst_reg: ad_rst
**Description**
 resets

- i_vdma_rst_reg: ad_rst
- i_xfer_cntrl: up_xfer_cntrl
**Description**
 hdmi control & status

- i_xfer_status: up_xfer_status
- i_clock_mon: up_clock_mon
**Description**
 hdmi clock monitor

- i_vdma_xfer_status: up_xfer_status
**Description**
 vdma control & status

