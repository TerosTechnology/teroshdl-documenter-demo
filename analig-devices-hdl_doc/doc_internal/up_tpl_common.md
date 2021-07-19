# Entity: up_tpl_common

- **File**: up_tpl_common.v
## Diagram

![Diagram](up_tpl_common.svg "Diagram")
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

| Generic name | Type | Value | Description             |
| ------------ | ---- | ----- | ----------------------- |
| COMMON_ID    |      | 2'h0  | Offset of regmap        |
| NUM_PROFILES |      | 1     | Number of JESD profiles |
## Ports

| Port name      | Direction | Type                         | Description   |
| -------------- | --------- | ---------------------------- | ------------- |
| jesd_m         | input     | [NUM_PROFILES*8-1: 0]        |               |
| jesd_l         | input     | [NUM_PROFILES*8-1: 0]        |               |
| jesd_s         | input     | [NUM_PROFILES*8-1: 0]        |               |
| jesd_f         | input     | [NUM_PROFILES*8-1: 0]        |               |
| jesd_n         | input     | [NUM_PROFILES*8-1: 0]        |               |
| jesd_np        | input     | [NUM_PROFILES*8-1: 0]        |               |
| up_profile_sel | output    | reg [$clog2(NUM_PROFILES):0] |               |
| up_rstn        | input     |                              | bus interface |
| up_clk         | input     |                              |               |
| up_wreq        | input     |                              |               |
| up_waddr       | input     | [10:0]                       |               |
| up_wdata       | input     | [31:0]                       |               |
| up_wack        | output    |                              |               |
| up_rreq        | input     |                              |               |
| up_raddr       | input     | [10:0]                       |               |
| up_rdata       | output    | [31:0]                       |               |
| up_rack        | output    |                              |               |
## Signals

| Name                 | Type           | Description         |
| -------------------- | -------------- | ------------------- |
| up_rack_int          | reg            | internal registers  |
| up_wack_int          | reg            |                     |
| up_rdata_int         | reg     [31:0] |                     |
| up_wreq_s            | wire           | internal signals    |
| up_rreq_s            | wire           |                     |
| up_rdata_jesd_params | reg     [31:0] |                     |
| i                    | integer        |                     |
## Processes
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
- unnamed: ( @(*) )
