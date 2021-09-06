# Entity: ad_csc_CrYCb2RGB

- **File**: ad_csc_CrYCb2RGB.v
## Diagram

![Diagram](ad_csc_CrYCb2RGB.svg "Diagram")
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
 Transmit HDMI, CrYCb to RGB conversion
 The multiplication coefficients are in 1.4.12 format
 The addition coefficients are in 1.12.12 format
 R = (+408.583/256)*Cr + (+298.082/256)*Y + ( 000.000/256)*Cb + (-222.921);
 G = (-208.120/256)*Cr + (+298.082/256)*Y + (-100.291/256)*Cb + (+135.576);
 B = ( 000.000/256)*Cr + (+298.082/256)*Y + (+516.412/256)*Cb + (-276.836);

## Generics

| Generic name     | Type | Value | Description |
| ---------------- | ---- | ----- | ----------- |
| DELAY_DATA_WIDTH |      | 16    |             |
## Ports

| Port name  | Direction | Type                   | Description     |
| ---------- | --------- | ---------------------- | --------------- |
| clk        | input     |                        |  Cr-Y-Cb inputs |
| CrYCb_sync | input     | [DELAY_DATA_WIDTH-1:0] |                 |
| CrYCb_data | input     | [23:0]                 |                 |
| RGB_sync   | output    | [DELAY_DATA_WIDTH-1:0] |  R-G-B outputs  |
| RGB_data   | output    | [23:0]                 |                 |
## Constants

| Name | Type | Value                | Description |
| ---- | ---- | -------------------- | ----------- |
| DW   |      | DELAY_DATA_WIDTH - 1 |             |
## Instantiations

- i_csc_R: ad_csc
</br>**Description**
 red

- i_csc_G: ad_csc
</br>**Description**
 green

- i_csc_B: ad_csc
</br>**Description**
 blue

