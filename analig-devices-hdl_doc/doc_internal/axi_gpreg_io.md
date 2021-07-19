# Entity: axi_gpreg_io

- **File**: axi_gpreg_io.v
## Diagram

![Diagram](axi_gpreg_io.svg "Diagram")
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
## Ports

| Port name   | Direction | Type   | Description   |
| ----------- | --------- | ------ | ------------- |
| up_gp_ioenb | output    | [31:0] | gpio          |
| up_gp_out   | output    | [31:0] |               |
| up_gp_in    | input     | [31:0] |               |
| up_rstn     | input     |        | bus interface |
| up_clk      | input     |        |               |
| up_wreq     | input     |        |               |
| up_waddr    | input     | [13:0] |               |
| up_wdata    | input     | [31:0] |               |
| up_wack     | output    |        |               |
| up_rreq     | input     |        |               |
| up_raddr    | input     | [13:0] |               |
| up_rdata    | output    | [31:0] |               |
| up_rack     | output    |        |               |
## Signals

| Name      | Type | Description                          |
| --------- | ---- | ------------------------------------ |
| up_wreq_s | wire | internal registers internal signals  |
| up_rreq_s | wire |                                      |
## Processes
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
**Description**
processor write interface

- unnamed: ( @(negedge up_rstn or posedge up_clk) )
**Description**
processor read interface

