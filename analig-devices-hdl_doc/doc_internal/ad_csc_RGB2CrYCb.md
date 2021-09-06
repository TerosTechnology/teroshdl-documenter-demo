# Entity: ad_csc_RGB2CrYCb

- **File**: ad_csc_RGB2CrYCb.v
## Diagram

![Diagram](ad_csc_RGB2CrYCb.svg "Diagram")
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
 Transmit HDMI, RGB to CrYCb conversion
 The multiplication coefficients are in 1.4.12 format
 The addition coefficients are in 1.12.12 format
 Cr = (+112.439/256)*R + (-094.154/256)*G + (-018.285/256)*B + 128;
 Y  = (+065.738/256)*R + (+129.057/256)*G + (+025.064/256)*B +  16;
 Cb = (-037.945/256)*R + (-074.494/256)*G + (+112.439/256)*B + 128;

## Generics

| Generic name     | Type | Value | Description |
| ---------------- | ---- | ----- | ----------- |
| DELAY_DATA_WIDTH |      | 16    |             |
## Ports

| Port name  | Direction | Type                   | Description      |
| ---------- | --------- | ---------------------- | ---------------- |
| clk        | input     |                        |  R-G-B inputs    |
| RGB_sync   | input     | [DELAY_DATA_WIDTH-1:0] |                  |
| RGB_data   | input     | [23:0]                 |                  |
| CrYCb_sync | output    | [DELAY_DATA_WIDTH-1:0] |  Cr-Y-Cb outputs |
| CrYCb_data | output    | [23:0]                 |                  |
## Constants

| Name | Type | Value                | Description |
| ---- | ---- | -------------------- | ----------- |
| DW   |      | DELAY_DATA_WIDTH - 1 |             |
## Instantiations

- j_csc_1_Cr: ad_csc
</br>**Description**
 Cr (red-diff)

- j_csc_1_Y: ad_csc
</br>**Description**
 Y (luma)

- j_csc_1_Cb: ad_csc
</br>**Description**
 Cb (blue-diff)

