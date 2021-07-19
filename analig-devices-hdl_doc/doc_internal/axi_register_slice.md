# Entity: axi_register_slice

- **File**: axi_register_slice.v
## Diagram

![Diagram](axi_register_slice.svg "Diagram")
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

| Generic name        | Type | Value | Description |
| ------------------- | ---- | ----- | ----------- |
| DATA_WIDTH          |      | 32    |             |
| FORWARD_REGISTERED  |      | 0     |             |
| BACKWARD_REGISTERED |      | 0     |             |
## Ports

| Port name   | Direction | Type             | Description |
| ----------- | --------- | ---------------- | ----------- |
| clk         | input     |                  |             |
| resetn      | input     |                  |             |
| s_axi_valid | input     |                  |             |
| s_axi_ready | output    |                  |             |
| s_axi_data  | input     | [DATA_WIDTH-1:0] |             |
| m_axi_valid | output    |                  |             |
| m_axi_ready | input     |                  |             |
| m_axi_data  | output    | [DATA_WIDTH-1:0] |             |
## Signals

| Name        | Type                  | Description |
| ----------- | --------------------- | ----------- |
| bwd_data_s  | wire [DATA_WIDTH-1:0] |             |
| bwd_valid_s | wire                  |             |
| bwd_ready_s | wire                  |             |
| fwd_data_s  | wire [DATA_WIDTH-1:0] |             |
| fwd_valid_s | wire                  |             |
| fwd_ready_s | wire                  |             |
