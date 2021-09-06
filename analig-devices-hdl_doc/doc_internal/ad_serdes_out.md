# Entity: ad_serdes_out

- **File**: ad_serdes_out.v
## Diagram

![Diagram](ad_serdes_out.svg "Diagram")
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

| Generic name    | Type | Value | Description |
| --------------- | ---- | ----- | ----------- |
| FPGA_TECHNOLOGY |      | 0     |             |
| CMOS_LVDS_N     |      | 0     |             |
| DDR_OR_SDR_N    |      | 1     |             |
| SERDES_FACTOR   |      | 8     |             |
| DATA_WIDTH      |      | 16    |             |
## Ports

| Port name   | Direction | Type               | Description                |
| ----------- | --------- | ------------------ | -------------------------- |
| rst         | input     |                    |  reset and clocks          |
| clk         | input     |                    |                            |
| div_clk     | input     |                    |                            |
| loaden      | input     |                    |                            |
| data_oe     | input     |                    |  data interface            |
| data_s0     | input     | [(DATA_WIDTH-1):0] | 1st bit to be transmitted  |
| data_s1     | input     | [(DATA_WIDTH-1):0] |                            |
| data_s2     | input     | [(DATA_WIDTH-1):0] |                            |
| data_s3     | input     | [(DATA_WIDTH-1):0] |                            |
| data_s4     | input     | [(DATA_WIDTH-1):0] |                            |
| data_s5     | input     | [(DATA_WIDTH-1):0] |                            |
| data_s6     | input     | [(DATA_WIDTH-1):0] |                            |
| data_s7     | input     | [(DATA_WIDTH-1):0] | last bit to be transmitted |
| data_out_se | output    | [(DATA_WIDTH-1):0] |                            |
| data_out_p  | output    | [(DATA_WIDTH-1):0] |                            |
| data_out_n  | output    | [(DATA_WIDTH-1):0] |                            |
## Signals

| Name            | Type                    | Description        |
| --------------- | ----------------------- | ------------------ |
| data_out_s      | wire [(DATA_WIDTH-1):0] |  internal signals  |
| serdes_shift1_s | wire [(DATA_WIDTH-1):0] |                    |
| serdes_shift2_s | wire [(DATA_WIDTH-1):0] |                    |
| data_t          | wire [(DATA_WIDTH-1):0] |                    |
| buffer_disable  | wire                    |                    |
| serdes_rst_seq  | reg [6:0]               |  instantiations    |
| serdes_rst      | wire                    |                    |
## Constants

| Name            | Type | Value | Description |
| --------------- | ---- | ----- | ----------- |
| SEVEN_SERIES    |      | 1     |             |
| ULTRASCALE      |      | 2     |             |
| ULTRASCALE_PLUS |      | 3     |             |
| DR_OQ_DDR       |      | "DDR" |             |
| SIM_DEVICE      |      |       |             |
## Processes
- unnamed: ( @ (posedge div_clk) )
  - **Type:** always
