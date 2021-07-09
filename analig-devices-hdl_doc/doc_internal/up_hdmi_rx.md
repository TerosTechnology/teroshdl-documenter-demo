# Entity: up_hdmi_rx

## Diagram

![Diagram](up_hdmi_rx.svg "Diagram")
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

| Port name        | Direction | Type   | Description    |
| ---------------- | --------- | ------ | -------------- |
| hdmi_clk         | input     |        | hdmi interface |
| hdmi_rst         | output    |        |                |
| hdmi_edge_sel    | output    |        |                |
| hdmi_bgr         | output    |        |                |
| hdmi_packed      | output    |        |                |
| hdmi_csc_bypass  | output    |        |                |
| hdmi_vs_count    | output    | [15:0] |                |
| hdmi_hs_count    | output    | [15:0] |                |
| hdmi_dma_ovf     | input     |        |                |
| hdmi_dma_unf     | input     |        |                |
| hdmi_tpm_oos     | input     |        |                |
| hdmi_vs_oos      | input     |        |                |
| hdmi_hs_oos      | input     |        |                |
| hdmi_vs_mismatch | input     |        |                |
| hdmi_hs_mismatch | input     |        |                |
| hdmi_vs          | input     | [15:0] |                |
| hdmi_hs          | input     | [15:0] |                |
| hdmi_clk_ratio   | input     | [31:0] |                |
| up_rstn          | input     |        | bus interface  |
| up_clk           | input     |        |                |
| up_wreq          | input     |        |                |
| up_waddr         | input     | [13:0] |                |
| up_wdata         | input     | [31:0] |                |
| up_wack          | output    |        |                |
| up_rreq          | input     |        |                |
| up_raddr         | input     | [13:0] |                |
| up_rdata         | output    | [31:0] |                |
| up_rack          | output    |        |                |
## Signals

| Name             | Type           | Description         |
| ---------------- | -------------- | ------------------- |
| up_core_preset   | reg            | internal registers  |
| up_resetn        | reg            |                     |
| up_scratch       | reg     [31:0] |                     |
| up_edge_sel      | reg            |                     |
| up_bgr           | reg            |                     |
| up_packed        | reg            |                     |
| up_csc_bypass    | reg            |                     |
| up_dma_ovf       | reg            |                     |
| up_dma_unf       | reg            |                     |
| up_tpm_oos       | reg            |                     |
| up_vs_oos        | reg            |                     |
| up_hs_oos        | reg            |                     |
| up_vs_mismatch   | reg            |                     |
| up_hs_mismatch   | reg            |                     |
| up_vs_count      | reg     [15:0] |                     |
| up_hs_count      | reg     [15:0] |                     |
| up_wreq_s        | wire           | internal signals    |
| up_rreq_s        | wire           |                     |
| up_dma_ovf_s     | wire           |                     |
| up_dma_unf_s     | wire           |                     |
| up_vs_oos_s      | wire           |                     |
| up_hs_oos_s      | wire           |                     |
| up_vs_mismatch_s | wire           |                     |
| up_hs_mismatch_s | wire           |                     |
| up_vs_s          | wire [15:0]    |                     |
| up_hs_s          | wire [15:0]    |                     |
| up_clk_count_s   | wire [31:0]    |                     |
## Constants

| Name          | Type | Value        | Description |
| ------------- | ---- | ------------ | ----------- |
| PCORE_VERSION |      | 32'h00040063 |             |
## Processes
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
**Description**
processor write interface

- unnamed: ( @(negedge up_rstn or posedge up_clk) )
**Description**
processor read interface

## Instantiations

- i_hdmi_rst_reg: ad_rst
**Description**
resets

- i_hdmi_xfer_cntrl: up_xfer_cntrl
**Description**
hdmi control & status

- i_hdmi_xfer_status: up_xfer_status
- i_hdmi_clock_mon: up_clock_mon
