# Entity: axi_pwm_gen_1

- **File**: axi_pwm_gen_1.v
## Diagram

![Diagram](axi_pwm_gen_1.svg "Diagram")
## Description

 ***************************************************************************
 ***************************************************************************
 Copyright (c) Analog Devices, Inc. All rights reserved.

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

| Generic name | Type | Value     | Description                                                  |
| ------------ | ---- | --------- | ------------------------------------------------------------ |
| PULSE_WIDTH  |      | 7         |  the width and period are defined in number of clock cycles  |
| PULSE_PERIOD |      | 100000000 |                                                              |
## Ports

| Port name     | Direction | Type   | Description |
| ------------- | --------- | ------ | ----------- |
| clk           | input     |        |             |
| rstn          | input     |        |             |
| pulse_width   | input     | [31:0] |             |
| pulse_period  | input     | [31:0] |             |
| load_config   | input     |        |             |
| sync          | input     |        |             |
| pulse         | output    |        |             |
| pulse_counter | output    | [31:0] |             |
## Signals

| Name              | Type           | Description          |
| ----------------- | -------------- | -------------------- |
| pulse_period_cnt  | reg     [31:0] |  internal registers  |
| pulse_period_read | reg     [31:0] |                      |
| pulse_width_read  | reg     [31:0] |                      |
| pulse_period_d    | reg     [31:0] |                      |
| pulse_width_d     | reg     [31:0] |                      |
| phase_align_armed | reg            |                      |
| phase_align       | wire           |  internal wires      |
| end_of_period     | wire           |                      |
| end_of_pulse      | wire           |                      |
| pulse_enable      | wire           |                      |
## Processes
- unnamed: ( @(posedge clk) )
  - **Type:** always
</br>**Description**
 flop the desired period 
- unnamed: ( @(posedge clk) )
  - **Type:** always
</br>**Description**
 phase align to the first sync pulse until another load_config 
- unnamed: ( @(posedge clk) )
  - **Type:** always
</br>**Description**
 a free running counter 
- unnamed: ( @ (posedge clk) )
  - **Type:** always
</br>**Description**
 generate pulse with a specified width 
