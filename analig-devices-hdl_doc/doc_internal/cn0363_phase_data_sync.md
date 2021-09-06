# Entity: cn0363_phase_data_sync

- **File**: cn0363_phase_data_sync.v
## Diagram

![Diagram](cn0363_phase_data_sync.svg "Diagram")
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

## Ports

| Port name           | Direction | Type   | Description |
| ------------------- | --------- | ------ | ----------- |
| clk                 | input     |        |             |
| resetn              | input     |        |             |
| processing_resetn   | input     |        |             |
| s_axis_sample_ready | output    |        |             |
| s_axis_sample_valid | input     |        |             |
| s_axis_sample_data  | input     | [7:0]  |             |
| sample_has_stat     | input     |        |             |
| conv_done           | input     |        |             |
| phase               | input     | [31:0] |             |
| m_axis_sample_valid | output    |        |             |
| m_axis_sample_ready | input     |        |             |
| m_axis_sample_data  | output    | [23:0] |             |
| m_axis_phase_valid  | output    |        |             |
| m_axis_phase_ready  | input     |        |             |
| m_axis_phase_data   | output    | [31:0] |             |
| overflow            | output    |        |             |
## Signals

| Name              | Type       | Description |
| ----------------- | ---------- | ----------- |
| data_counter      | reg [1:0]  |             |
| phase_hold        | reg [31:0] |             |
| sample_hold       | reg [23:0] |             |
| sample_hold_valid | reg        |             |
| conv_done_d1      | reg        |             |
| synced            | reg        |             |
| sync              | wire       |             |
## Processes
- unnamed: ( @(posedge clk) )
  - **Type:** always
- unnamed: ( @(posedge clk) )
  - **Type:** always
- unnamed: ( @(posedge clk) )
  - **Type:** always
**Description**
 If the STAT register is included in the sample we get 4 bytes per sample and  * are able to detect channel swaps and synchronize the first output sample to  * the first channel. If the STAT register is not included we only get 3 bytes  * per sample and rely on that the first sample will always be from the first  * channel */ 
- unnamed: ( @(posedge clk) )
  - **Type:** always
- unnamed: ( @(posedge clk) )
  - **Type:** always
- unnamed: ( @(posedge clk) )
  - **Type:** always
