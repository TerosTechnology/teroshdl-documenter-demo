# Entity: util_fir_int

## Diagram

![Diagram](util_fir_int.svg "Diagram")
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
 
## Ports

| Port name          | Direction | Type   | Description |
| ------------------ | --------- | ------ | ----------- |
| aclk               | input     |        |             |
| s_axis_data_tvalid | input     |        |             |
| s_axis_data_tready | output    |        |             |
| s_axis_data_tdata  | input     | [31:0] |             |
| channel_0          | output    | [15:0] |             |
| channel_1          | output    | [15:0] |             |
| m_axis_data_tvalid | output    |        |             |
| interpolate        | input     |        |             |
| dac_read           | input     |        |             |
## Signals

| Name                 | Type        | Description |
| -------------------- | ----------- | ----------- |
| m_axis_data_tdata_s  | wire [31:0] |             |
| s_axis_data_tvalid_s | wire        |             |
| s_axis_data_tready_r | reg         |             |
| s_axis_data_tvalid_r | reg         |             |
| ready_counter        | reg   [2:0] |             |
## Processes
- unnamed: ( @(posedge aclk) )
## Instantiations

- interpolator: fir_interp
