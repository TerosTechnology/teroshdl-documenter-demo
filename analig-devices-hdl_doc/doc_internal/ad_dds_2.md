# Entity: ad_dds_2

- **File**: ad_dds_2.v
## Diagram

![Diagram](ad_dds_2.svg "Diagram")
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

| Generic name    | Type | Value | Description                                            |
| --------------- | ---- | ----- | ------------------------------------------------------ |
| DDS_DW          |      | 16    | Range = 8-24                                           |
| PHASE_DW        |      | 16    | Range = 8-24                                           |
| DDS_TYPE        |      | 1     | Set 1 for CORDIC or 2 for Polynomial                   |
| CORDIC_DW       |      | 16    | Range = 8-24                                           |
| CORDIC_PHASE_DW |      | 16    | Range = 8-24 ( make sure CORDIC_PHASE_DW < CORDIC_DW)  |
## Ports

| Port name   | Direction | Type           | Description |
| ----------- | --------- | -------------- | ----------- |
| clk         | input     |                | interface   |
| dds_format  | input     |                |             |
| dds_phase_0 | input     | [PHASE_DW-1:0] |             |
| dds_scale_0 | input     | [        15:0] |             |
| dds_phase_1 | input     | [PHASE_DW-1:0] |             |
| dds_scale_1 | input     | [        15:0] |             |
| dds_data    | output    | [  DDS_DW-1:0] |             |
## Signals

| Name           | Type                   | Description         |
| -------------- | ---------------------- | ------------------- |
| dds_data_width | reg     [  DDS_DW-1:0] | internal registers  |
| dds_data_rownd | reg     [DDS_D_DW-1:0] |                     |
| dds_data_int   | reg     [DDS_D_DW-1:0] |                     |
| dds_scale_0_d  | reg     [        15:0] |                     |
| dds_scale_1_d  | reg     [        15:0] |                     |
| dds_data_out   | reg     [  DDS_DW-1:0] |                     |
| dds_data_0_s   | wire [DDS_D_DW-1:0]    | internal signals    |
| dds_data_1_s   | wire [DDS_D_DW-1:0]    |                     |
| dds_phase_0_s  | wire [DDS_P_DW-1:0]    |                     |
| dds_phase_1_s  | wire [DDS_P_DW-1:0]    |                     |
## Constants

| Name       | Type | Value           | Description                                 |
| ---------- | ---- | --------------- | ------------------------------------------- |
| CORDIC     |      | 1               | Local parameters                            |
| POLYNOMIAL |      | 2               |                                             |
| DDS_D_DW   |      | CORDIC_DW       | The width for Polynomial DDS is fixed (16)  |
| DDS_P_DW   |      | CORDIC_PHASE_DW |                                             |
| C_T_WIDTH  |      | undefined       | concatenation or truncation width           |
