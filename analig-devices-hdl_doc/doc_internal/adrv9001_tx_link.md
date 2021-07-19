# Entity: adrv9001_tx_link

- **File**: adrv9001_tx_link.v
## Diagram

![Diagram](adrv9001_tx_link.svg "Diagram")
## Description

***************************************************************************
 ***************************************************************************
 Copyright 2014 - 2020 (c) Analog Devices, Inc. All rights reserved.
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

| Generic name        | Type | Value | Description |
| ------------------- | ---- | ----- | ----------- |
| CMOS_LVDS_N         |      | 0     |             |
| CLK_DIV_IS_FAST_CLK |      | 0     |             |
## Ports

| Port name       | Direction | Type   | Description                |
| --------------- | --------- | ------ | -------------------------- |
| dac_clk_div     | input     |        |                            |
| dac_data_0      | output    | [7:0]  |                            |
| dac_data_1      | output    | [7:0]  |                            |
| dac_data_2      | output    | [7:0]  |                            |
| dac_data_3      | output    | [7:0]  |                            |
| dac_data_strobe | output    | [7:0]  |                            |
| dac_data_clk    | output    | [7:0]  |                            |
| dac_data_valid  | output    |        |                            |
| tx_clk          | output    |        | upper layer data interface |
| tx_rst          | input     |        |                            |
| tx_data_valid   | input     |        |                            |
| tx_data_i       | input     | [15:0] |                            |
| tx_data_q       | input     | [15:0] |                            |
| tx_sdr_ddr_n    | input     |        | Config interface           |
| tx_single_lane  | input     |        |                            |
## Signals

| Name        | Type       | Description |
| ----------- | ---------- | ----------- |
| data32sdr   | wire [7:0] |             |
| strobe32sdr | wire [7:0] |             |
| data8sdr_0  | wire [7:0] |             |
| data8sdr_1  | wire [7:0] |             |
| data8sdr_2  | wire [7:0] |             |
| data8sdr_3  | wire [7:0] |             |
| strobe8sdr  | wire [7:0] |             |
| ld_next     | wire       |             |
| data32      | reg [31:0] |             |
| strobe32    | reg [31:0] |             |
| data16_0    | reg [15:0] |             |
| data16_1    | reg [15:0] |             |
| strobe16    | reg [15:0] |             |
| data8_0     | reg [7:0]  |             |
| data8_1     | reg [7:0]  |             |
| data8_2     | reg [7:0]  |             |
| data8_3     | reg [7:0]  |             |
| strobe8     | reg [7:0]  |             |
| valid_gen   | reg [3:0]  |             |
## Processes
- unnamed: ( @(posedge tx_clk) )
**Description**
Serialization factor Per data lane 32

- unnamed: ( @(posedge tx_clk) )
**Description**
Serialization factor Per data lane 16

- unnamed: ( @(posedge tx_clk) )
**Description**
Serialization factor Per data lane 8

- unnamed: ( @(posedge tx_clk) )
