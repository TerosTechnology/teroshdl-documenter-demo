# Entity: util_axis_upscale

- **File**: util_axis_upscale.v
## Diagram

![Diagram](util_axis_upscale.svg "Diagram")
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
  + A simple AXI stream data upscale module, which can be used with devices
    with resolution which can not be aligned to a WORD (32 bits). Eg. 24 bits
  + It has the same control interface as the ad_datafmt module, which controls
    the data format inside a generic AXI converter core.
  + Supports multiple channels. Contains a single register stage.

## Generics

| Generic name    | Type | Value | Description |
| --------------- | ---- | ----- | ----------- |
| NUM_OF_CHANNELS |      | 4     |             |
| DATA_WIDTH      |      | 24    |             |
| UDATA_WIDTH     |      | 32    |             |
## Ports

| Port name    | Direction | Type                                | Description |
| ------------ | --------- | ----------------------------------- | ----------- |
| clk          | input     |                                     |             |
| resetn       | input     |                                     |             |
| s_axis_valid | input     |                                     |             |
| s_axis_ready | output    |                                     |             |
| s_axis_data  | input     | [(NUM_OF_CHANNELS*DATA_WIDTH)-1:0]  |             |
| m_axis_valid | output    |                                     |             |
| m_axis_ready | input     |                                     |             |
| m_axis_data  | output    | [(NUM_OF_CHANNELS*UDATA_WIDTH)-1:0] |             |
| dfmt_enable  | input     |                                     |             |
| dfmt_type    | input     |                                     |             |
| dfmt_se      | input     |                                     |             |
## Signals

| Name       | Type                                     | Description |
| ---------- | ---------------------------------------- | ----------- |
| type_s     | wire                                     |             |
| signext_s  | wire                                     |             |
| data_out_s | wire [(NUM_OF_CHANNELS*UDATA_WIDTH)-1:0] |             |
## Constants

| Name      | Type | Value                    | Description |
| --------- | ---- | ------------------------ | ----------- |
| MSB_WIDTH |      | UDATA_WIDTH - DATA_WIDTH |             |
## Processes
- unnamed: ( @(posedge clk) )
  - **Type:** always
