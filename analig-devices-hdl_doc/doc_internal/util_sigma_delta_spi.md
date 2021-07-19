# Entity: util_sigma_delta_spi

- **File**: util_sigma_delta_spi.v
## Diagram

![Diagram](util_sigma_delta_spi.svg "Diagram")
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
| NUM_OF_CS    |      | 1     |             |
| CS_PIN       |      | 0     |             |
| IDLE_TIMEOUT |      | 63    |             |
## Ports

| Port name  | Direction | Type            | Description |
| ---------- | --------- | --------------- | ----------- |
| clk        | input     |                 |             |
| resetn     | input     |                 |             |
| spi_active | input     |                 |             |
| s_sclk     | input     |                 |             |
| s_sdo      | input     |                 |             |
| s_sdo_t    | input     |                 |             |
| s_sdi      | output    |                 |             |
| s_cs       | input     | [NUM_OF_CS-1:0] |             |
| m_sclk     | output    |                 |             |
| m_sdo      | output    |                 |             |
| m_sdo_t    | output    |                 |             |
| m_sdi      | input     |                 |             |
| m_cs       | output    | [NUM_OF_CS-1:0] |             |
| data_ready | output    |                 |             |
## Signals

| Name    | Type                           | Description |
| ------- | ------------------------------ | ----------- |
| counter | reg [$clog2(IDLE_TIMEOUT)-1:0] |             |
| sdi_d   | reg [2:0]                      |             |
## Processes
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
