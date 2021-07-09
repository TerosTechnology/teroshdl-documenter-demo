# Entity: ad_serdes_in

## Diagram

![Diagram](ad_serdes_in.svg "Diagram")
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

| Generic name     | Type | Value                | Description |
| ---------------- | ---- | -------------------- | ----------- |
| FPGA_TECHNOLOGY  |      | 0                    |             |
| CMOS_LVDS_N      |      | 0                    |             |
| DDR_OR_SDR_N     |      | 0                    |             |
| SERDES_FACTOR    |      | 8                    |             |
| DATA_WIDTH       |      | 16                   |             |
| DRP_WIDTH        |      | 5                    |             |
| IODELAY_CTRL     |      | 0                    |             |
| IODELAY_GROUP    |      | "dev_if_delay_group" |             |
| REFCLK_FREQUENCY |      | 200                  |             |
## Ports

| Port name    | Direction | Type                           | Description             |
| ------------ | --------- | ------------------------------ | ----------------------- |
| rst          | input     |                                | reset and clocks        |
| clk          | input     |                                |                         |
| div_clk      | input     |                                |                         |
| loaden       | input     |                                |                         |
| phase        | input     | [ 7:0]                         |                         |
| locked       | input     |                                |                         |
| data_s0      | output    | [(DATA_WIDTH-1):0]             | last bit received       |
| data_s1      | output    | [(DATA_WIDTH-1):0]             |                         |
| data_s2      | output    | [(DATA_WIDTH-1):0]             |                         |
| data_s3      | output    | [(DATA_WIDTH-1):0]             |                         |
| data_s4      | output    | [(DATA_WIDTH-1):0]             |                         |
| data_s5      | output    | [(DATA_WIDTH-1):0]             |                         |
| data_s6      | output    | [(DATA_WIDTH-1):0]             |                         |
| data_s7      | output    | [(DATA_WIDTH-1):0]             | 1st bit received        |
| data_in_p    | input     | [(DATA_WIDTH-1):0]             |                         |
| data_in_n    | input     | [(DATA_WIDTH-1):0]             |                         |
| up_clk       | input     |                                | delay-data interface    |
| up_dld       | input     | [(DATA_WIDTH-1):0]             |                         |
| up_dwdata    | input     | [((DATA_WIDTH*DRP_WIDTH)-1):0] |                         |
| up_drdata    | output    | [((DATA_WIDTH*DRP_WIDTH)-1):0] |                         |
| delay_clk    | input     |                                | delay-control interface |
| delay_rst    | input     |                                |                         |
| delay_locked | output    |                                |                         |
## Signals

| Name             | Type                    | Description       |
| ---------------- | ----------------------- | ----------------- |
| data_in_ibuf_s   | wire [(DATA_WIDTH-1):0] | internal signals  |
| data_in_idelay_s | wire [(DATA_WIDTH-1):0] |                   |
| data_shift1_s    | wire [(DATA_WIDTH-1):0] |                   |
| data_shift2_s    | wire [(DATA_WIDTH-1):0] |                   |
| serdes_rst_seq   | reg [6:0]               |                   |
| serdes_rst       | wire                    |                   |
## Constants

| Name                  | Type | Value | Description |
| --------------------- | ---- | ----- | ----------- |
| SEVEN_SERIES          |      | 1     |             |
| ULTRASCALE            |      | 2     |             |
| ULTRASCALE_PLUS       |      | 3     |             |
| DATA_RATE             |      | "DDR" |             |
| SIM_DEVICE            |      |       |             |
| SIM_DEVICE_IDELAYCTRL |      |       |             |
## Processes
- unnamed: ( @ (posedge div_clk) )
