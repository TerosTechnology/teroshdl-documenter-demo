# Entity: ad_dds_cordic_pipe

- **File**: ad_dds_cordic_pipe.v
## Diagram

![Diagram](ad_dds_cordic_pipe.svg "Diagram")
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

| Generic name | Type | Value | Description               |
| ------------ | ---- | ----- | ------------------------- |
| P_DW         |      | 16    |  parameters  Range = N/A  |
| D_DW         |      | 16    |  Range = N/A              |
| DELAY_DW     |      | 1     |  Range = N/A              |
| SHIFT        |      | 0     |  Range = 0-(DW - 1)       |
## Ports

| Port name      | Direction | Type         | Description |
| -------------- | --------- | ------------ | ----------- |
| clk            | input     |              |  Interface  |
| dir            | input     |              |             |
| dataa_x        | input     | [  D_DW-1:0] |             |
| dataa_y        | input     | [  D_DW-1:0] |             |
| dataa_z        | input     | [  P_DW-1:0] |             |
| datab_z        | input     | [  P_DW-1:0] |             |
| result_x       | output    | [  D_DW-1:0] |             |
| result_y       | output    | [  D_DW-1:0] |             |
| result_z       | output    | [  P_DW-1:0] |             |
| data_delay_in  | input     | [DELAY_DW:1] |             |
| data_delay_out | output    | [DELAY_DW:1] |             |
## Signals

| Name        | Type               | Description              |
| ----------- | ------------------ | ------------------------ |
| data_delay  | reg   [DELAY_DW:1] |  Registers Declarations  |
| sgn_shift_x | wire [  D_DW-1:0]  |  Wires Declarations      |
| sgn_shift_y | wire [  D_DW-1:0]  |                          |
| dir_inv     | wire               |                          |
## Processes
- unnamed: ( @(posedge clk) )
  - **Type:** always
**Description**
 Stage rotation 
