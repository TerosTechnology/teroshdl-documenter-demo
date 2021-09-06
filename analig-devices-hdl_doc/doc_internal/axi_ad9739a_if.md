# Entity: axi_ad9739a_if

- **File**: axi_ad9739a_if.v
## Diagram

![Diagram](axi_ad9739a_if.svg "Diagram")
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
 This is the dac physical interface (drives samples from the low speed clock to the
 dac clock domain.

## Generics

| Generic name    | Type | Value | Description |
| --------------- | ---- | ----- | ----------- |
| FPGA_TECHNOLOGY |      | 0     |             |
## Ports

| Port name        | Direction | Type   | Description                 |
| ---------------- | --------- | ------ | --------------------------- |
| dac_clk_in_p     | input     |        |  dac interface              |
| dac_clk_in_n     | input     |        |                             |
| dac_clk_out_p    | output    |        |                             |
| dac_clk_out_n    | output    |        |                             |
| dac_data_out_a_p | output    | [13:0] |                             |
| dac_data_out_a_n | output    | [13:0] |                             |
| dac_data_out_b_p | output    | [13:0] |                             |
| dac_data_out_b_n | output    | [13:0] |                             |
| dac_rst          | input     |        |  internal resets and clocks |
| dac_clk          | output    |        |                             |
| dac_div_clk      | output    |        |                             |
| dac_status       | output    |        |                             |
| dac_data_00      | input     | [15:0] |  data interface             |
| dac_data_01      | input     | [15:0] |                             |
| dac_data_02      | input     | [15:0] |                             |
| dac_data_03      | input     | [15:0] |                             |
| dac_data_04      | input     | [15:0] |                             |
| dac_data_05      | input     | [15:0] |                             |
| dac_data_06      | input     | [15:0] |                             |
| dac_data_07      | input     | [15:0] |                             |
| dac_data_08      | input     | [15:0] |                             |
| dac_data_09      | input     | [15:0] |                             |
| dac_data_10      | input     | [15:0] |                             |
| dac_data_11      | input     | [15:0] |                             |
| dac_data_12      | input     | [15:0] |                             |
| dac_data_13      | input     | [15:0] |                             |
| dac_data_14      | input     | [15:0] |                             |
| dac_data_15      | input     | [15:0] |                             |
## Signals

| Name          | Type | Description                            |
| ------------- | ---- | -------------------------------------- |
| dac_clk_in_s  | wire |  internal registers  internal signals  |
| dac_div_clk_s | wire |                                        |
## Processes
- unnamed: ( @(posedge dac_div_clk) )
  - **Type:** always
</br>**Description**
 dac status 
## Instantiations

- i_serdes_out_data_a: ad_serdes_out
</br>**Description**
 dac data output serdes(s) & buffers

- i_serdes_out_data_b: ad_serdes_out
</br>**Description**
 dac data output serdes(s) & buffers

- i_serdes_out_clk: ad_serdes_out
</br>**Description**
 dac clock output serdes & buffer

- i_dac_clk_in_ibuf: IBUFGDS
</br>**Description**
 dac clock input buffers

- i_dac_clk_in_gbuf: BUFG
- i_dac_div_clk_rbuf: BUFR
- i_dac_div_clk_gbuf: BUFG
