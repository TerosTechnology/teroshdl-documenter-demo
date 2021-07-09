# Entity: axi_adxcvr_mstatus

## Diagram

![Diagram](axi_adxcvr_mstatus.svg "Diagram")
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

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| XCVR_ID      | integer | 0     | parameters  |
| NUM_OF_LANES | integer | 8     |             |
## Ports

| Port name         | Direction | Type | Description |
| ----------------- | --------- | ---- | ----------- |
| up_rstn           | input     |      |             |
| up_clk            | input     |      |             |
| up_pll_locked_in  | input     |      |             |
| up_rst_done_in    | input     |      |             |
| up_prbserr_in     | input     |      |             |
| up_prbslocked_in  | input     |      |             |
| up_pll_locked     | input     |      |             |
| up_rst_done       | input     |      |             |
| up_prbserr        | input     |      |             |
| up_prbslocked     | input     |      |             |
| up_pll_locked_out | output    |      |             |
| up_rst_done_out   | output    |      |             |
| up_prbserr_out    | output    |      |             |
| up_prbslocked_out | output    |      |             |
## Signals

| Name              | Type | Description         |
| ----------------- | ---- | ------------------- |
| up_pll_locked_int | reg  | internal registers  |
| up_rst_done_int   | reg  |                     |
| up_prbserr_int    | reg  |                     |
| up_prbslocked_int | reg  |                     |
| up_pll_locked_s   | wire | internal signals    |
| up_rst_done_s     | wire |                     |
| up_prbserr_s      | wire |                     |
| up_prbslocked_s   | wire |                     |
## Processes
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
