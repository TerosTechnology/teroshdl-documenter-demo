# Entity: axi_pwm_gen_regmap

## Diagram

![Diagram](axi_pwm_gen_regmap.svg "Diagram")
## Description

***************************************************************************
 ***************************************************************************
 Copyright 2014 - 2019 (c) Analog Devices, Inc. All rights reserved.
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

| Generic name     | Type | Value | Description |
| ---------------- | ---- | ----- | ----------- |
| ID               |      | 0     |             |
| CORE_MAGIC       |      | 0     |             |
| CORE_VERSION     |      | 0     |             |
| ASYNC_CLK_EN     |      | 1     |             |
| N_PWMS           |      | 3     |             |
| PULSE_0_WIDTH    |      | 7     |             |
| PULSE_1_WIDTH    |      | 7     |             |
| PULSE_2_WIDTH    |      | 7     |             |
| PULSE_3_WIDTH    |      | 7     |             |
| PULSE_0_PERIOD   |      | 10    |             |
| PULSE_1_PERIOD   |      | 10    |             |
| PULSE_2_PERIOD   |      | 10    |             |
| PULSE_3_PERIOD   |      | 10    |             |
| PULSE_0_EXT_SYNC |      | 0     |             |
| PULSE_0_OFFSET   |      | 0     |             |
| PULSE_1_OFFSET   |      | 0     |             |
| PULSE_2_OFFSET   |      | 0     |             |
| PULSE_3_OFFSET   |      | 0     |             |
## Ports

| Port name      | Direction | Type    | Description                |
| -------------- | --------- | ------- | -------------------------- |
| ext_clk        | input     |         | external clock             |
| clk_out        | output    |         | control and status signals |
| pwm_gen_resetn | output    |         |                            |
| pwm_width      | output    | [127:0] |                            |
| pwm_period     | output    | [127:0] |                            |
| pwm_offset     | output    | [127:0] |                            |
| load_config    | output    |         |                            |
| up_rstn        | input     |         | processor interface        |
| up_clk         | input     |         |                            |
| up_wreq        | input     |         |                            |
| up_waddr       | input     | [13:0]  |                            |
| up_wdata       | input     | [31:0]  |                            |
| up_wack        | output    |         |                            |
| up_rreq        | input     |         |                            |
| up_raddr       | input     | [13:0]  |                            |
| up_rdata       | output    | [31:0]  |                            |
| up_rack        | output    |         |                            |
## Signals

| Name            | Type           | Description         |
| --------------- | -------------- | ------------------- |
| up_scratch      | reg     [31:0] | internal registers  |
| up_pwm_width_0  | reg     [31:0] |                     |
| up_pwm_width_1  | reg     [31:0] |                     |
| up_pwm_width_2  | reg     [31:0] |                     |
| up_pwm_width_3  | reg     [31:0] |                     |
| up_pwm_period_0 | reg     [31:0] |                     |
| up_pwm_period_1 | reg     [31:0] |                     |
| up_pwm_period_2 | reg     [31:0] |                     |
| up_pwm_period_3 | reg     [31:0] |                     |
| up_pwm_offset_0 | reg     [31:0] |                     |
| up_pwm_offset_1 | reg     [31:0] |                     |
| up_pwm_offset_2 | reg     [31:0] |                     |
| up_pwm_offset_3 | reg     [31:0] |                     |
| up_load_config  | reg            |                     |
| up_reset        | reg            |                     |
## Processes
- unnamed: ( @(posedge up_clk) )
- unnamed: ( @(posedge up_clk) )
