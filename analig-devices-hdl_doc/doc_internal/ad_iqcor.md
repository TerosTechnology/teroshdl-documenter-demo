# Entity: ad_iqcor

- **File**: ad_iqcor.v
## Diagram

![Diagram](ad_iqcor.svg "Diagram")
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
 iq correction = a*(i+x) + b*(q+y); offsets are added in dcfilter.
 if SCALE_ONLY is set to 1, b*(q+y) is set to 0, and the module is used for
 scale correction of channel I
 Assumption CR smaller or equal to 16

## Generics

| Generic name | Type | Value | Description              |
| ------------ | ---- | ----- | ------------------------ |
| Q_OR_I_N     |      | 0     |  select i/q if disabled  |
| SCALE_ONLY   |      | 0     |                          |
| DISABLE      |      | 0     |                          |
| CR           |      | 16    |  Converter Resolution    |
| DPW          |      | 1     |  Data Path Width         |
## Ports

| Port name     | Direction | Type         | Description        |
| ------------- | --------- | ------------ | ------------------ |
| clk           | input     |              |  data interface    |
| valid         | input     |              |                    |
| data_in       | input     | [DPW*CR-1:0] |                    |
| data_iq       | input     | [DPW*CR-1:0] |                    |
| valid_out     | output    |              |                    |
| data_out      | output    | [DPW*CR-1:0] |                    |
| iqcor_enable  | input     |              |  control interface |
| iqcor_coeff_1 | input     | [15:0]       |                    |
| iqcor_coeff_2 | input     | [15:0]       |                    |
## Signals

| Name            | Type              | Description          |
| --------------- | ----------------- | -------------------- |
| iqcor_coeff_1_r | reg     [15:0]    |  internal registers  |
| iqcor_coeff_2_r | reg     [15:0]    |                      |
| valid_int_loc   | wire [DPW-1:0]    |  internal signals    |
| data_int_loc    | wire [DPW*CR-1:0] |                      |
## Processes
- unnamed: ( @(posedge clk) )
  - **Type:** always
</br>**Description**
 coefficients are flopped to remove warnings from vivado 
