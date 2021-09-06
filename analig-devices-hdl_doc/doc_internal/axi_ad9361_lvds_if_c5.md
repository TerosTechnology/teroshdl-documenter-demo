# Entity: axi_ad9361_lvds_if_c5

- **File**: axi_ad9361_lvds_if_c5.v
## Diagram

![Diagram](axi_ad9361_lvds_if_c5.svg "Diagram")
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

## Ports

| Port name      | Direction | Type   | Description                                  |
| -------------- | --------- | ------ | -------------------------------------------- |
| rx_clk_in_p    | input     |        |  physical interface (receive)                |
| rx_clk_in_n    | input     |        |                                              |
| rx_frame_in_p  | input     |        |                                              |
| rx_frame_in_n  | input     |        |                                              |
| rx_data_in_p   | input     | [ 5:0] |                                              |
| rx_data_in_n   | input     | [ 5:0] |                                              |
| tx_clk_out_p   | output    |        |  physical interface (transmit)               |
| tx_clk_out_n   | output    |        |                                              |
| tx_frame_out_p | output    |        |                                              |
| tx_frame_out_n | output    |        |                                              |
| tx_data_out_p  | output    | [ 5:0] |                                              |
| tx_data_out_n  | output    | [ 5:0] |                                              |
| enable         | output    |        |  ensm control                                |
| txnrx          | output    |        |                                              |
| clk            | output    |        |  clock (common to both receive and transmit) |
| rx_frame       | output    | [ 3:0] |  receive data path interface                 |
| rx_data_0      | output    | [ 5:0] |                                              |
| rx_data_1      | output    | [ 5:0] |                                              |
| rx_data_2      | output    | [ 5:0] |                                              |
| rx_data_3      | output    | [ 5:0] |                                              |
| tx_frame       | input     | [ 3:0] |  transmit data path interface                |
| tx_data_0      | input     | [ 5:0] |                                              |
| tx_data_1      | input     | [ 5:0] |                                              |
| tx_data_2      | input     | [ 5:0] |                                              |
| tx_data_3      | input     | [ 5:0] |                                              |
| tx_enable      | input     |        |                                              |
| tx_txnrx       | input     |        |                                              |
| locked         | output    |        |  locked (status)                             |
| up_clk         | input     |        |  delay interface                             |
| up_rstn        | input     |        |                                              |
## Signals

| Name               | Type           | Description          |
| ------------------ | -------------- | -------------------- |
| pll_rst            | reg            |  internal registers  |
| locked_int         | reg            |                      |
| tx_core_enable_int | reg            |                      |
| tx_core_txnrx_int  | reg            |                      |
| tx_core_data_int   | reg     [27:0] |                      |
| tx_core_enable     | reg            |                      |
| tx_core_txnrx      | reg            |                      |
| tx_core_data       | reg     [27:0] |                      |
| tx_locked_int      | reg            |                      |
| tx_locked          | reg            |                      |
| rx_core_data_s     | wire [27:0]    |  internal signals    |
| rx_locked_s        | wire           |                      |
| tx_core_clk        | wire           |                      |
| tx_locked_s        | wire           |                      |
## Processes
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
**Description**
 pll reset 
- unnamed: ( @(posedge clk) )
  - **Type:** always
- unnamed: ( @(negedge clk) )
  - **Type:** always
- unnamed: ( @(posedge tx_core_clk) )
  - **Type:** always
- unnamed: ( @(negedge tx_core_clk) )
  - **Type:** always
- unnamed: ( @(posedge clk) )
  - **Type:** always
## Instantiations

- i_altlvds_rx: altlvds_rx
**Description**
 instantiations

- i_altlvds_tx: altlvds_tx
- i_altddio_enable: altddio_out
- i_altddio_txnrx: altddio_out
