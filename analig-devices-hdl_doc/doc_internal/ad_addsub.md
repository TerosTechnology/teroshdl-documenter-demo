# Entity: ad_addsub

- **File**: ad_addsub.v
## Diagram

![Diagram](ad_addsub.svg "Diagram")
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
 A simple adder/substracter width preconfigured input ports width and turn-around value
 Output = A - B_constant or A + B_constant
 Constraints: Awidth >= Bwidth

## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| A_DATA_WIDTH |      | 32    |             |
| B_DATA_VALUE |      | 32'h1 |             |
| ADD_OR_SUB_N |      | 0     |             |
## Ports

| Port name | Direction | Type                 | Description |
| --------- | --------- | -------------------- | ----------- |
| clk       | input     |                      |             |
| A         | input     | [(A_DATA_WIDTH-1):0] |             |
| Amax      | input     | [(A_DATA_WIDTH-1):0] |             |
| out       | output    | [(A_DATA_WIDTH-1):0] |             |
| CE        | input     |                      |             |
## Signals

| Name    | Type                         | Description     |
| ------- | ---------------------------- | --------------- |
| out_d   | reg     [A_DATA_WIDTH:0]     |  registers      |
| out_d2  | reg     [A_DATA_WIDTH:0]     |                 |
| A_d     | reg     [(A_DATA_WIDTH-1):0] |                 |
| Amax_d  | reg     [(A_DATA_WIDTH-1):0] |                 |
| Amax_d2 | reg     [(A_DATA_WIDTH-1):0] |                 |
| B_reg   | reg     [(A_DATA_WIDTH-1):0] |  constant regs  |
## Constants

| Name        | Type | Value | Description |
| ----------- | ---- | ----- | ----------- |
| ADDER       |      | 1     |             |
| SUBSTRACTER |      | 0     |             |
## Processes
- unnamed: ( @(posedge clk) )
  - **Type:** always
</br>**Description**
 latch the inputs 
- unnamed: ( @(posedge clk) )
  - **Type:** always
</br>**Description**
 ADDER/SUBSTRACTER 
- unnamed: ( @(posedge clk) )
  - **Type:** always
</br>**Description**
 Resolve 
- unnamed: ( @(posedge clk) )
  - **Type:** always
</br>**Description**
 output logic 
