# Entity: axi_gpreg_clock_mon

- **File**: axi_gpreg_clock_mon.v
## Diagram

![Diagram](axi_gpreg_clock_mon.svg "Diagram")
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

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| ID           |      | 0     |             |
| BUF_ENABLE   |      | 0     |             |
## Ports

| Port name | Direction | Type   | Description   |
| --------- | --------- | ------ | ------------- |
| d_clk     | input     |        | clock         |
| up_rstn   | input     |        | bus interface |
| up_clk    | input     |        |               |
| up_wreq   | input     |        |               |
| up_waddr  | input     | [13:0] |               |
| up_wdata  | input     | [31:0] |               |
| up_wack   | output    |        |               |
| up_rreq   | input     |        |               |
| up_raddr  | input     | [13:0] |               |
| up_rdata  | output    | [31:0] |               |
| up_rack   | output    |        |               |
## Signals

| Name         | Type        | Description         |
| ------------ | ----------- | ------------------- |
| up_d_preset  | reg         | internal registers  |
| up_d_resetn  | reg         |                     |
| up_wreq_s    | wire        | internal signals    |
| up_rreq_s    | wire        |                     |
| up_d_count_s | wire [31:0] |                     |
| d_rst        | wire        |                     |
| d_clk_g      | wire        |                     |
## Processes
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
**Description**
processor write interface

- unnamed: ( @(negedge up_rstn or posedge up_clk) )
**Description**
processor read interface

## Instantiations

- i_clock_mon: up_clock_mon
**Description**
clock monitor

- i_d_rst_reg: ad_rst
