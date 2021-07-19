# Entity: pack_ctrl

- **File**: pack_ctrl.v
## Diagram

![Diagram](pack_ctrl.svg "Diagram")
## Description

***************************************************************************
 ***************************************************************************
 Copyright 2018 (c) Analog Devices, Inc. All rights reserved.
 In this HDL repository, there are many different and unique modules, consisting
 of various HDL (Verilog or VHDL) components. The individual modules are
 developed independently, and may be accompanied by separate and unique license
 terms.
 The user should read each of these license terms, and understand the
 freedoms and responsabilities that he or she has by using this source/core.
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

| Generic name       | Type | Value | Description |
| ------------------ | ---- | ----- | ----------- |
| PORT_ADDRESS_WIDTH |      | 2     |             |
| MUX_ORDER          |      | 1     |             |
| MIN_STAGE          |      | 0     |             |
| NUM_STAGES         |      | 2     |             |
| PACK               |      | 0     |             |
## Ports

| Port name    | Direction | Type                                             | Description |
| ------------ | --------- | ------------------------------------------------ | ----------- |
| rotate       | input     | [PORT_ADDRESS_WIDTH-1:0]                         |             |
| prefix_count | input     | [2**PORT_ADDRESS_WIDTH*PORT_ADDRESS_WIDTH-1:0]   |             |
| ctrl         | output    | [2**PORT_ADDRESS_WIDTH*MUX_ORDER*NUM_STAGES-1:0] |             |
## Signals

| Name  | Type                                         | Description |
| ----- | -------------------------------------------- | ----------- |
| ctrl1 | wire [NUM_OF_PORTS*MUX_ORDER*NUM_STAGES-1:0] |             |
| ctrl2 | reg [NUM_OF_PORTS*MUX_ORDER*NUM_STAGES-1:0]  |             |
## Constants

| Name         | Type | Value                 | Description |
| ------------ | ---- | --------------------- | ----------- |
| NUM_OF_PORTS |      | 2**PORT_ADDRESS_WIDTH |             |
