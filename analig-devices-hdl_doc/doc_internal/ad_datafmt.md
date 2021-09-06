# Entity: ad_datafmt

- **File**: ad_datafmt.v
## Diagram

![Diagram](ad_datafmt.svg "Diagram")
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
 data format (offset binary or 2's complement only)

## Generics

| Generic name      | Type | Value | Description      |
| ----------------- | ---- | ----- | ---------------- |
| DATA_WIDTH        |      | 16    |  data bus width  |
| OCTETS_PER_SAMPLE |      | 2     |                  |
| DISABLE           |      | 0     |                  |
## Ports

| Port name   | Direction | Type                        | Description      |
| ----------- | --------- | --------------------------- | ---------------- |
| clk         | input     |                             |  data path       |
| valid       | input     |                             |                  |
| data        | input     | [(DATA_WIDTH-1):0]          |                  |
| valid_out   | output    |                             |                  |
| data_out    | output    | [(8*OCTETS_PER_SAMPLE-1):0] |                  |
| dfmt_enable | input     |                             |  control signals |
| dfmt_type   | input     |                             |                  |
| dfmt_se     | input     |                             |                  |
## Signals

| Name       | Type                                | Description          |
| ---------- | ----------------------------------- | -------------------- |
| valid_int  | reg                                 |  internal registers  |
| data_int   | reg     [(8*OCTETS_PER_SAMPLE-1):0] |                      |
| type_s     | wire                                |  internal signals    |
| data_out_s | wire [(8*OCTETS_PER_SAMPLE-1):0]    |                      |
## Processes
- unnamed: ( @(posedge clk) )
  - **Type:** always
