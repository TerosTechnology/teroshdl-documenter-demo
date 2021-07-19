# Entity: ad_mul

- **File**: ad_mul.v
## Diagram

![Diagram](ad_mul.svg "Diagram")
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

| Generic name     | Type | Value | Description |
| ---------------- | ---- | ----- | ----------- |
| A_DATA_WIDTH     |      | 17    |             |
| B_DATA_WIDTH     |      | 17    |             |
| DELAY_DATA_WIDTH |      | 16    |             |
## Ports

| Port name | Direction | Type                              | Description               |
| --------- | --------- | --------------------------------- | ------------------------- |
| clk       | input     |                                   | data_p = data_a * data_b; |
| data_a    | input     | [               A_DATA_WIDTH-1:0] |                           |
| data_b    | input     | [               B_DATA_WIDTH-1:0] |                           |
| data_p    | output    | [A_DATA_WIDTH + B_DATA_WIDTH-1:0] |                           |
| ddata_in  | input     | [(DELAY_DATA_WIDTH-1):0]          | delay interface           |
| ddata_out | output    | [(DELAY_DATA_WIDTH-1):0]          |                           |
## Signals

| Name     | Type                             | Description         |
| -------- | -------------------------------- | ------------------- |
| p1_ddata | reg     [(DELAY_DATA_WIDTH-1):0] | internal registers  |
| p2_ddata | reg     [(DELAY_DATA_WIDTH-1):0] |                     |
## Processes
- unnamed: ( @(posedge clk) )
**Description**
a/b reg, m-reg, p-reg delay match

## Instantiations

- i_mult_macro: MULT_MACRO
