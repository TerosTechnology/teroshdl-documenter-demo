# Entity: ad_serdes_clk

- **File**: ad_serdes_clk.v
## Diagram

![Diagram](ad_serdes_clk.svg "Diagram")
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
 serial data output interface: serdes(x8)
 
## Generics

| Generic name      | Type | Value  | Description |
| ----------------- | ---- | ------ | ----------- |
| FPGA_TECHNOLOGY   |      | 0      |             |
| DDR_OR_SDR_N      |      | 1      |             |
| CLKIN_DS_OR_SE_N  |      | 1      |             |
| SERDES_FACTOR     |      | 8      |             |
| MMCM_OR_BUFR_N    |      | 1      |             |
| MMCM_CLKIN_PERIOD |      | 1.667  |             |
| MMCM_VCO_DIV      |      | 6      |             |
| MMCM_VCO_MUL      |      | 12.000 |             |
| MMCM_CLK0_DIV     |      | 2.000  |             |
| MMCM_CLK1_DIV     |      | 6      |             |
## Ports

| Port name     | Direction | Type   | Description             |
| ------------- | --------- | ------ | ----------------------- |
| rst           | input     |        | clock and divided clock |
| clk_in_p      | input     |        |                         |
| clk_in_n      | input     |        |                         |
| clk           | output    |        |                         |
| div_clk       | output    |        |                         |
| out_clk       | output    |        |                         |
| loaden        | output    |        |                         |
| phase         | output    | [ 7:0] |                         |
| up_clk        | input     |        | drp interface           |
| up_rstn       | input     |        |                         |
| up_drp_sel    | input     |        |                         |
| up_drp_wr     | input     |        |                         |
| up_drp_addr   | input     | [11:0] |                         |
| up_drp_wdata  | input     | [31:0] |                         |
| up_drp_rdata  | output    | [31:0] |                         |
| up_drp_ready  | output    |        |                         |
| up_drp_locked | output    |        |                         |
## Signals

| Name     | Type | Description       |
| -------- | ---- | ----------------- |
| clk_in_s | wire | internal signals  |
## Constants

| Name        | Type | Value             | Description |
| ----------- | ---- | ----------------- | ----------- |
| BUFR_DIVIDE |      | SERDES_FACTOR / 2 |             |
