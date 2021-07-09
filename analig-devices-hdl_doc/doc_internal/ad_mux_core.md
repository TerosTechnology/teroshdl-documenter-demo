# Entity: ad_mux_core

## Diagram

![Diagram](ad_mux_core.svg "Diagram")
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
| CH_W         |      | 16    |             |
| CH_CNT       |      | 8     |             |
| EN_REG       |      | 0     |             |
## Ports

| Port name | Direction | Type                 | Description |
| --------- | --------- | -------------------- | ----------- |
| clk       | input     |                      |             |
| data_in   | input     | [CH_W*CH_CNT-1:0]    |             |
| ch_sel    | input     | [$clog2(CH_CNT)-1:0] |             |
| data_out  | output    | [CH_W-1:0]           |             |
## Signals

| Name         | Type            | Description |
| ------------ | --------------- | ----------- |
| data_out_loc | wire [CH_W-1:0] |             |
