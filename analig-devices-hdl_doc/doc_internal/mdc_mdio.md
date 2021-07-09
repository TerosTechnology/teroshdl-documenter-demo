# Entity: mdc_mdio

## Diagram

![Diagram](mdc_mdio.svg "Diagram")
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

| Generic name | Type | Value    | Description |
| ------------ | ---- | -------- | ----------- |
| PHY_AD       |      | 5'b10000 |             |
## Ports

| Port name    | Direction | Type   | Description |
| ------------ | --------- | ------ | ----------- |
| mdio_mdc     | input     |        |             |
| mdio_in_w    | input     |        |             |
| mdio_in_r    | input     |        |             |
| speed_select | output    | [ 1:0] |             |
| duplex_mode  | output    |        |             |
## Signals

| Name          | Type       | Description |
| ------------- | ---------- | ----------- |
| preamble      | wire       |             |
| current_state | reg [ 1:0] |             |
| next_state    | reg [ 1:0] |             |
| data_in       | reg [31:0] |             |
| data_in_r     | reg [31:0] |             |
| data_counter  | reg [ 5:0] |             |
## Constants

| Name    | Type | Value | Description |
| ------- | ---- | ----- | ----------- |
| IDLE    |      | 2'b01 |             |
| ACQUIRE |      | 2'b10 |             |
## Processes
- unnamed: ( @(posedge mdio_mdc) )
- unnamed: ( @(negedge mdio_mdc) )
- unnamed: ( @(*) )
