# Entity: axi_xcvrlb_1

- **File**: axi_xcvrlb_1.v
## Diagram

![Diagram](axi_xcvrlb_1.svg "Diagram")
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

| Generic name   | Type | Value | Description  |
| -------------- | ---- | ----- | ------------ |
| CPLL_FBDIV     |      | 1     |  parameters  |
| CPLL_FBDIV_4_5 |      | 5     |              |
| XCVR_TYPE      |      | 2     |              |
## Ports

| Port name     | Direction | Type | Description            |
| ------------- | --------- | ---- | ---------------------- |
| ref_clk       | input     |      |  transceiver interface |
| rx_p          | input     |      |                        |
| rx_n          | input     |      |                        |
| tx_p          | output    |      |                        |
| tx_n          | output    |      |                        |
| up_rstn       | input     |      |  processor interface   |
| up_clk        | input     |      |                        |
| up_resetn     | input     |      |                        |
| up_status     | output    |      |                        |
| up_pll_locked | output    |      |                        |
## Signals

| Name               | Type           | Description          |
| ------------------ | -------------- | -------------------- |
| rx_kcount          | reg     [ 3:0] |  internal registers  |
| rx_calign          | reg            |                      |
| rx_data            | reg     [31:0] |                      |
| rx_pn_data         | reg     [31:0] |                      |
| tx_charisk         | reg            |                      |
| tx_data            | reg     [31:0] |                      |
| tx_pn_data         | reg     [31:0] |                      |
| up_pll_rst_cnt     | reg     [ 3:0] |                      |
| up_rst_cnt         | reg     [ 3:0] |                      |
| up_user_ready_cnt  | reg     [ 6:0] |                      |
| up_status_int      | reg            |                      |
| clk                | wire           |  internal signals    |
| rx_status_s        | wire           |                      |
| rx_pn_data_s       | wire [31:0]    |                      |
| rx_pn_oos_s        | wire           |                      |
| rx_pn_err_s        | wire           |                      |
| rx_charisk_s       | wire [ 3:0]    |                      |
| rx_error_s         | wire [ 7:0]    |                      |
| rx_data_s          | wire [31:0]    |                      |
| up_pll_rst_s       | wire           |                      |
| up_rst_s           | wire           |                      |
| up_user_ready_s    | wire           |                      |
| up_pll_locked_s    | wire           |                      |
| up_rst_done_s      | wire           |                      |
| up_pn_oos_s        | wire           |                      |
| up_pn_err_s        | wire           |                      |
| up_rx_pll_locked_s | wire           |                      |
| up_rx_rst_done_s   | wire           |                      |
| up_tx_pll_locked_s | wire           |                      |
| up_tx_rst_done_s   | wire           |                      |
## Functions
- pn31 <font id="function_arguments">()</font> <font id="function_return">return ([31:0])</font>
</br>**Description**
 pn31 function

## Processes
- unnamed: ( @(posedge clk) )
  - **Type:** always
- unnamed: ( @(posedge clk) )
  - **Type:** always
- unnamed: ( @(posedge clk) )
  - **Type:** always
</br>**Description**
 transmit 
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
## Instantiations

- i_pnmon: ad_pnmon
</br>**Description**
 instantiations

- i_xfer_status: up_xfer_status
- i_xch: util_adxcvr_xch
