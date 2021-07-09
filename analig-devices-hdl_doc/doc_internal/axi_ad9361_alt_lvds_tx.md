# Entity: axi_ad9361_alt_lvds_tx

## Diagram

![Diagram](axi_ad9361_alt_lvds_tx.svg "Diagram")
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

| Port name      | Direction | Type   | Description                   |
| -------------- | --------- | ------ | ----------------------------- |
| tx_clk_out_p   | output    |        | physical interface (transmit) |
| tx_clk_out_n   | output    |        |                               |
| tx_frame_out_p | output    |        |                               |
| tx_frame_out_n | output    |        |                               |
| tx_data_out_p  | output    | [ 5:0] |                               |
| tx_data_out_n  | output    | [ 5:0] |                               |
| tx_clk         | input     |        | data interface                |
| clk            | input     |        |                               |
| tx_frame       | input     | [ 3:0] |                               |
| tx_data_0      | input     | [ 5:0] |                               |
| tx_data_1      | input     | [ 5:0] |                               |
| tx_data_2      | input     | [ 5:0] |                               |
| tx_data_3      | input     | [ 5:0] |                               |
| tx_locked      | output    |        |                               |
## Signals

| Name      | Type           | Description         |
| --------- | -------------- | ------------------- |
| tx_data_n | reg     [27:0] | internal registers  |
| tx_data_p | reg     [27:0] |                     |
| core_clk  | wire           | internal signals    |
| tx_data_s | wire [27:0]    |                     |
## Processes
- unnamed: ( @(negedge clk) )
- unnamed: ( @(posedge core_clk) )
## Instantiations

- i_altlvds_tx: altlvds_tx
