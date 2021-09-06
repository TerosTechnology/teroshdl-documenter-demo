# Entity: ad_mmcm_drp

- **File**: ad_mmcm_drp.v
## Diagram

![Diagram](ad_mmcm_drp.svg "Diagram")
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
 MMCM_OR_BUFR_N with DRP and device specific

## Generics

| Generic name       | Type | Value  | Description |
| ------------------ | ---- | ------ | ----------- |
| FPGA_TECHNOLOGY    |      | 0      |             |
| MMCM_CLKIN_PERIOD  |      | 1.667  |             |
| MMCM_CLKIN2_PERIOD |      | 1.667  |             |
| MMCM_VCO_DIV       |      | 6      |             |
| MMCM_VCO_MUL       |      | 12.000 |             |
| MMCM_CLK0_DIV      |      | 2.000  |             |
| MMCM_CLK0_PHASE    |      | 0.000  |             |
| MMCM_CLK1_DIV      |      | 6      |             |
| MMCM_CLK1_PHASE    |      | 0.000  |             |
| MMCM_CLK2_DIV      |      | 2.000  |             |
| MMCM_CLK2_PHASE    |      | 0.000  |             |
## Ports

| Port name     | Direction | Type   | Description    |
| ------------- | --------- | ------ | -------------- |
| clk           | input     |        |  clocks        |
| clk2          | input     |        |                |
| clk_sel       | input     |        |                |
| mmcm_rst      | input     |        |                |
| mmcm_clk_0    | output    |        |                |
| mmcm_clk_1    | output    |        |                |
| mmcm_clk_2    | output    |        |                |
| up_clk        | input     |        |  drp interface |
| up_rstn       | input     |        |                |
| up_drp_sel    | input     |        |                |
| up_drp_wr     | input     |        |                |
| up_drp_addr   | input     | [11:0] |                |
| up_drp_wdata  | input     | [15:0] |                |
| up_drp_rdata  | output    | [15:0] |                |
| up_drp_ready  | output    |        |                |
| up_drp_locked | output    |        |                |
## Signals

| Name             | Type        | Description          |
| ---------------- | ----------- | -------------------- |
| up_drp_locked_m1 | reg         |  internal registers  |
| bufg_fb_clk_s    | wire        |  internal signals    |
| mmcm_fb_clk_s    | wire        |                      |
| mmcm_clk_0_s     | wire        |                      |
| mmcm_clk_1_s     | wire        |                      |
| mmcm_clk_2_s     | wire        |                      |
| mmcm_locked_s    | wire        |                      |
| up_drp_rdata_s   | wire [15:0] |                      |
| up_drp_ready_s   | wire        |                      |
## Constants

| Name            | Type | Value | Description |
| --------------- | ---- | ----- | ----------- |
| SEVEN_SERIES    |      | 1     |             |
| ULTRASCALE      |      | 2     |             |
| ULTRASCALE_PLUS |      | 3     |             |
## Processes
- unnamed: ( @(posedge up_clk) )
  - **Type:** always
</br>**Description**
 drp read and locked 
