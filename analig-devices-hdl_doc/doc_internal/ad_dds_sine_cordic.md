# Entity: ad_dds_sine_cordic

## Diagram

![Diagram](ad_dds_sine_cordic.svg "Diagram")
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

| Generic name | Type | Value | Description   |
| ------------ | ---- | ----- | ------------- |
| PHASE_DW     |      | 16    | Range = 8-24  |
| CORDIC_DW    |      | 16    | Range = 8-24  |
| DELAY_DW     |      | 1     | Range = N/A   |
## Ports

| Port name | Direction | Type            | Description |
| --------- | --------- | --------------- | ----------- |
| clk       | input     |                 | interface   |
| angle     | input     | [ PHASE_DW-1:0] |             |
| sine      | output    | [CORDIC_DW-1:0] |             |
| cosine    | output    | [CORDIC_DW-1:0] |             |
| ddata_in  | input     | [ DELAY_DW-1:0] |             |
| ddata_out | output    | [ DELAY_DW-1:0] |             |
## Signals

| Name       | Type                 | Description             |
| ---------- | -------------------- | ----------------------- |
| x0         | reg  [CORDIC_DW-1:0] | Registers Declarations  |
| y0         | reg  [CORDIC_DW-1:0] |                         |
| z0         | reg  [ PHASE_DW-1:0] |                         |
| x_s        | wire [CORDIC_DW-1:0] | Wires Declarations      |
| y_s        | wire [CORDIC_DW-1:0] |                         |
| z_s        | wire [ PHASE_DW-1:0] |                         |
| data_in_d  | wire [ DELAY_DW-1:0] |                         |
| atan_table | wire [ PHASE_DW-1:0] |                         |
| quadrant   | wire [          1:0] |                         |
## Constants

| Name              | Type            | Value              | Description                   |
| ----------------- | --------------- | ------------------ | ----------------------------- |
| LUT_FSCALE        |                 | 1                  | Local Parameters              |
| X_FSCALE          |                 | 1                  | 1.64676025812 =~ system gain  |
| APROX_DW_GAIN_ERR |                 | 4 :                |                               |
| X_VALUE           | [CORDIC_DW-1:0] | -APROX_DW_GAIN_ERR | ((2^N)/2)/1.647...            |
## Processes
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
**Description**
x and y are cos(angle) and sin(angle)

