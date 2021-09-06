# Entity: axi_adc_trigger_reg

- **File**: axi_adc_trigger_reg.v
## Diagram

![Diagram](axi_adc_trigger_reg.svg "Diagram")
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

| Port name             | Direction | Type   | Description    |
| --------------------- | --------- | ------ | -------------- |
| clk                   | input     |        |                |
| io_selection          | output    | [ 7:0] |                |
| trigger_o             | output    | [ 1:0] |                |
| triggered             | input     |        |                |
| low_level             | output    | [ 1:0] |                |
| high_level            | output    | [ 1:0] |                |
| any_edge              | output    | [ 1:0] |                |
| rise_edge             | output    | [ 1:0] |                |
| fall_edge             | output    | [ 1:0] |                |
| limit_a               | output    | [15:0] |                |
| function_a            | output    | [ 1:0] |                |
| hysteresis_a          | output    | [31:0] |                |
| trigger_l_mix_a       | output    | [ 3:0] |                |
| limit_b               | output    | [15:0] |                |
| function_b            | output    | [ 1:0] |                |
| hysteresis_b          | output    | [31:0] |                |
| trigger_l_mix_b       | output    | [ 3:0] |                |
| trigger_out_control   | output    | [16:0] |                |
| fifo_depth            | output    | [31:0] |                |
| trigger_delay         | output    | [31:0] |                |
| trigger_holdoff       | output    | [31:0] |                |
| trigger_out_hold_pins | output    | [19:0] |                |
| streaming             | output    |        |                |
| up_rstn               | input     |        |  bus interface |
| up_clk                | input     |        |                |
| up_wreq               | input     |        |                |
| up_waddr              | input     | [ 4:0] |                |
| up_wdata              | input     | [31:0] |                |
| up_wack               | output    |        |                |
| up_rreq               | input     |        |                |
| up_raddr              | input     | [ 4:0] |                |
| up_rdata              | output    | [31:0] |                |
| up_rack               | output    |        |                |
## Signals

| Name                     | Type           | Description          |
| ------------------------ | -------------- | -------------------- |
| config_trigger_i         | wire [ 9:0]    |  internal signals    |
| up_version               | reg     [31:0] |  internal registers  |
| up_scratch               | reg     [31:0] |                      |
| up_io_selection          | reg     [ 7:0] |                      |
| up_trigger_o             | reg     [ 1:0] |                      |
| up_config_trigger_i      | reg     [ 9:0] |                      |
| up_limit_a               | reg     [15:0] |                      |
| up_function_a            | reg     [ 1:0] |                      |
| up_hysteresis_a          | reg     [31:0] |                      |
| up_trigger_l_mix_a       | reg     [ 3:0] |                      |
| up_limit_b               | reg     [15:0] |                      |
| up_function_b            | reg     [ 1:0] |                      |
| up_hysteresis_b          | reg     [31:0] |                      |
| up_trigger_l_mix_b       | reg     [ 3:0] |                      |
| up_trigger_out_control   | reg     [16:0] |                      |
| up_fifo_depth            | reg     [31:0] |                      |
| up_trigger_delay         | reg     [31:0] |                      |
| up_trigger_holdoff       | reg     [31:0] |                      |
| up_trigger_out_hold_pins | reg     [19:0] |                      |
| up_triggered             | reg            |                      |
| up_streaming             | reg            |                      |
## Constants

| Name             | Type | Value  | Description |
| ---------------- | ---- | ------ | ----------- |
| DEFAULT_OUT_HOLD |      | 100000 | 1ms         |
## Processes
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
</br>**Description**
 processor read interface 
## Instantiations

- i_xfer_cntrl: up_xfer_cntrl
