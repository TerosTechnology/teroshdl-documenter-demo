# Entity: util_fir_dec

- **File**: util_fir_dec.v
## Diagram

![Diagram](util_fir_dec.svg "Diagram")
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
| channel_0          | input     | [15:0] |             |
| channel_1          | input     | [15:0] |             |
| decimate           | input     |        |             |
| m_axis_data_tvalid | output    |        |             |
| m_axis_data_tdata  | output    | [31:0] |             |
## Signals

| Name                 | Type        | Description |
| -------------------- | ----------- | ----------- |
| s_axis_data_tdata    | wire [31:0] |             |
| m_axis_data_tvalid_s | wire        |             |
| m_axis_data_tdata_s  | wire [31:0] |             |
## Instantiations

- decimator: fir_decim
