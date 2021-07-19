# Entity: spi_engine_interconnect

- **File**: spi_engine_interconnect.v
## Diagram

![Diagram](spi_engine_interconnect.svg "Diagram")
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

| Generic name | Type | Value | Description                             |
| ------------ | ---- | ----- | --------------------------------------- |
| DATA_WIDTH   |      | 8     | Valid data widths values are 8/16/24/32 |
| NUM_OF_SDI   |      | 1     |                                         |
## Ports

| Port name     | Direction | Type                            | Description |
| ------------- | --------- | ------------------------------- | ----------- |
| clk           | input     |                                 |             |
| resetn        | input     |                                 |             |
| m_cmd_valid   | output    |                                 |             |
| m_cmd_ready   | input     |                                 |             |
| m_cmd_data    | output    | [15:0]                          |             |
| m_sdo_valid   | output    |                                 |             |
| m_sdo_ready   | input     |                                 |             |
| m_sdo_data    | output    | [(DATA_WIDTH-1):0]              |             |
| m_sdi_valid   | input     |                                 |             |
| m_sdi_ready   | output    |                                 |             |
| m_sdi_data    | input     | [(NUM_OF_SDI * DATA_WIDTH-1):0] |             |
| m_sync_valid  | input     |                                 |             |
| m_sync_ready  | output    |                                 |             |
| m_sync        | input     | [7:0]                           |             |
| s0_cmd_valid  | input     |                                 |             |
| s0_cmd_ready  | output    |                                 |             |
| s0_cmd_data   | input     | [15:0]                          |             |
| s0_sdo_valid  | input     |                                 |             |
| s0_sdo_ready  | output    |                                 |             |
| s0_sdo_data   | input     | [(DATA_WIDTH-1):0]              |             |
| s0_sdi_valid  | output    |                                 |             |
| s0_sdi_ready  | input     |                                 |             |
| s0_sdi_data   | output    | [(NUM_OF_SDI * DATA_WIDTH-1):0] |             |
| s0_sync_valid | output    |                                 |             |
| s0_sync_ready | input     |                                 |             |
| s0_sync       | output    | [7:0]                           |             |
| s1_cmd_valid  | input     |                                 |             |
| s1_cmd_ready  | output    |                                 |             |
| s1_cmd_data   | input     | [15:0]                          |             |
| s1_sdo_valid  | input     |                                 |             |
| s1_sdo_ready  | output    |                                 |             |
| s1_sdo_data   | input     | [(DATA_WIDTH-1):0]              |             |
| s1_sdi_valid  | output    |                                 |             |
| s1_sdi_ready  | input     |                                 |             |
| s1_sdi_data   | output    | [(NUM_OF_SDI * DATA_WIDTH-1):0] |             |
| s1_sync_valid | output    |                                 |             |
| s1_sync_ready | input     |                                 |             |
| s1_sync       | output    | [7:0]                           |             |
## Signals

| Name     | Type | Description |
| -------- | ---- | ----------- |
| s_active | reg  |             |
| idle     | reg  |             |
## Processes
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
