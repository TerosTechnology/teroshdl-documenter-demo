# Entity: util_adxcvr_xcm

## Diagram

![Diagram](util_adxcvr_xcm.svg "Diagram")
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

| Generic name     | Type    | Value                | Description |
| ---------------- | ------- | -------------------- | ----------- |
| XCVR_TYPE        | integer | 0                    | parameters  |
| QPLL_REFCLK_DIV  | integer | 1                    |             |
| QPLL_FBDIV_RATIO | integer | 1                    |             |
| POR_CFG          | [15:0]  | 16'b0000000000000110 |             |
| PPF0_CFG         | [15:0]  | 16'b0000011000000000 |             |
| PPF1_CFG         | [15:0]  | 16'b0000011000000000 |             |
| QPLL_CFG         | [26:0]  | 27'h0680181          |             |
| QPLL_FBDIV       | [ 9:0]  | 10'b0000110000       |             |
| QPLL_CFG0        | [15:0]  | 16'b0011001100011100 |             |
| QPLL_CFG1        | [15:0]  | 16'b1101000000111000 |             |
| QPLL_CFG1_G3     | [15:0]  | 16'b1101000000111000 |             |
| QPLL_CFG2        | [15:0]  | 16'b0000111111000000 |             |
| QPLL_CFG2_G3     | [15:0]  | 16'b0000111111000000 |             |
| QPLL_CFG3        | [15:0]  | 16'b0000000100100000 |             |
| QPLL_CFG4        | [15:0]  | 16'b0000000000000011 |             |
| QPLL_CP_G3       | [15:0]  | 10'b0000011111       |             |
| QPLL_LPF         | [15:0]  | 10'b0100110111       |             |
| QPLL_CP          | [15:0]  | 10'b0001111111       |             |
## Ports

| Port name       | Direction | Type   | Description      |
| --------------- | --------- | ------ | ---------------- |
| qpll_ref_clk    | input     |        | reset and clocks |
| qpll_sel        | input     |        |                  |
| qpll2ch_clk     | output    |        |                  |
| qpll2ch_ref_clk | output    |        |                  |
| qpll2ch_locked  | output    |        |                  |
| qpll1_clk       | output    |        |                  |
| qpll1_ref_clk   | output    |        |                  |
| qpll1_locked    | output    |        |                  |
| up_rstn         | input     |        | drp interface    |
| up_clk          | input     |        |                  |
| up_qpll_rst     | input     |        |                  |
| up_cm_enb       | input     |        |                  |
| up_cm_addr      | input     | [11:0] |                  |
| up_cm_wr        | input     |        |                  |
| up_cm_wdata     | input     | [15:0] |                  |
| up_cm_rdata     | output    | [15:0] |                  |
| up_cm_ready     | output    |        |                  |
## Signals

| Name         | Type           | Description         |
| ------------ | -------------- | ------------------- |
| up_enb_int   | reg            | internal registers  |
| up_addr_int  | reg     [11:0] |                     |
| up_wr_int    | reg            |                     |
| up_wdata_int | reg     [15:0] |                     |
| up_rdata_int | reg     [15:0] |                     |
| up_ready_int | reg            |                     |
| up_sel_int   | reg            |                     |
| up_rdata_s   | wire [15:0]    | internal signals    |
| up_ready_s   | wire           |                     |
## Constants

| Name               | Type | Value | Description |
| ------------------ | ---- | ----- | ----------- |
| GTXE2_TRANSCEIVERS |      | 2     |             |
| GTHE3_TRANSCEIVERS |      | 5     |             |
| GTHE4_TRANSCEIVERS |      | 8     |             |
| GTYE4_TRANSCEIVERS |      | 9     |             |
## Processes
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
