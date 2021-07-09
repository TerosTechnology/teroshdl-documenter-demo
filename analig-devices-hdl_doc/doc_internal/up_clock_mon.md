# Entity: up_clock_mon

## Diagram

![Diagram](up_clock_mon.svg "Diagram")
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
| TOTAL_WIDTH  |      | 32    |             |
## Ports

| Port name  | Direction | Type              | Description         |
| ---------- | --------- | ----------------- | ------------------- |
| up_rstn    | input     |                   | processor interface |
| up_clk     | input     |                   |                     |
| up_d_count | output    | [TOTAL_WIDTH-1:0] |                     |
| d_rst      | input     |                   | device interface    |
| d_clk      | input     |                   |                     |
## Signals

| Name                | Type                    | Description         |
| ------------------- | ----------------------- | ------------------- |
| up_count            | reg     [15:0]          | internal registers  |
| up_count_run        | reg                     |                     |
| up_count_running_m1 | reg                     |                     |
| up_count_running_m2 | reg                     |                     |
| up_count_running_m3 | reg                     |                     |
| d_count_run_m1      | reg                     |                     |
| d_count_run_m2      | reg                     |                     |
| d_count_run_m3      | reg                     |                     |
| d_count             | reg     [TOTAL_WIDTH:0] |                     |
| up_count_capture_s  | wire                    | internal signals    |
| d_count_reset_s     | wire                    |                     |
## Processes
- unnamed: ( @(posedge up_clk) )
- unnamed: ( @(posedge up_clk) )
- unnamed: ( @(posedge up_clk) )
- unnamed: ( @(posedge d_clk or posedge d_rst) )
- unnamed: ( @(posedge d_clk) )
