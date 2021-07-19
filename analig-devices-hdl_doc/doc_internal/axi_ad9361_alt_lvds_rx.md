# Entity: axi_ad9361_alt_lvds_rx

- **File**: axi_ad9361_alt_lvds_rx.v
## Diagram

![Diagram](axi_ad9361_alt_lvds_rx.svg "Diagram")
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

| Port name     | Direction | Type   | Description                  |
| ------------- | --------- | ------ | ---------------------------- |
| rx_clk_in_p   | input     |        | physical interface (receive) |
| rx_clk_in_n   | input     |        |                              |
| rx_frame_in_p | input     |        |                              |
| rx_frame_in_n | input     |        |                              |
| rx_data_in_p  | input     | [ 5:0] |                              |
| rx_data_in_n  | input     | [ 5:0] |                              |
| clk           | output    |        | data interface               |
| rx_frame      | output    | [ 3:0] |                              |
| rx_data_0     | output    | [ 5:0] |                              |
| rx_data_1     | output    | [ 5:0] |                              |
| rx_data_2     | output    | [ 5:0] |                              |
| rx_data_3     | output    | [ 5:0] |                              |
| rx_locked     | output    |        |                              |
## Signals

| Name      | Type        | Description       |
| --------- | ----------- | ----------------- |
| rx_data_s | wire [27:0] | internal signals  |
## Instantiations

- i_altlvds_rx: altlvds_rx
