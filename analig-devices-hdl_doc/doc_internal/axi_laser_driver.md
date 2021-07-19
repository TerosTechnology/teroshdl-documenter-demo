# Entity: axi_laser_driver

- **File**: axi_laser_driver.v
## Diagram

![Diagram](axi_laser_driver.svg "Diagram")
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

| Generic name | Type  | Value | Description |
| ------------ | ----- | ----- | ----------- |
| ID           |       | 0     |             |
| ASYNC_CLK_EN | [0:0] | 1     |             |
| PULSE_WIDTH  |       | 7     |             |
| PULSE_PERIOD |       | 10    |             |
## Ports

| Port name       | Direction | Type   | Description                               |
| --------------- | --------- | ------ | ----------------------------------------- |
| s_axi_aclk      | input     |        | axi interface                             |
| s_axi_aresetn   | input     |        |                                           |
| s_axi_awvalid   | input     |        |                                           |
| s_axi_awaddr    | input     | [15:0] |                                           |
| s_axi_awprot    | input     | [ 2:0] |                                           |
| s_axi_awready   | output    |        |                                           |
| s_axi_wvalid    | input     |        |                                           |
| s_axi_wdata     | input     | [31:0] |                                           |
| s_axi_wstrb     | input     | [ 3:0] |                                           |
| s_axi_wready    | output    |        |                                           |
| s_axi_bvalid    | output    |        |                                           |
| s_axi_bresp     | output    | [ 1:0] |                                           |
| s_axi_bready    | input     |        |                                           |
| s_axi_arvalid   | input     |        |                                           |
| s_axi_araddr    | input     | [15:0] |                                           |
| s_axi_arprot    | input     | [ 2:0] |                                           |
| s_axi_arready   | output    |        |                                           |
| s_axi_rvalid    | output    |        |                                           |
| s_axi_rresp     | output    | [ 1:0] |                                           |
| s_axi_rdata     | output    | [31:0] |                                           |
| s_axi_rready    | input     |        |                                           |
| ext_clk         | input     |        | external clock and control/status signals |
| driver_en_n     | output    |        |                                           |
| driver_pulse    | output    |        |                                           |
| driver_otw_n    | input     |        |                                           |
| driver_dp_reset | output    |        |                                           |
| tia_chsel       | output    | [ 7:0] |                                           |
| irq             | output    |        | interrupt                                 |
## Signals

| Name               | Type           | Description       |
| ------------------ | -------------- | ----------------- |
| up_wack            | reg            | internal signals  |
| up_rack            | reg            |                   |
| up_rdata           | reg     [31:0] |                   |
| driver_pulse_int_d | reg            |                   |
| sequence_counter   | reg     [ 1:0] |                   |
| clk                | wire           | internal signals  |
| up_clk             | wire           |                   |
| up_rstn            | wire           |                   |
| up_rreq_s          | wire           |                   |
| up_rack_ld_s       | wire           |                   |
| up_rack_pwm_s      | wire           |                   |
| up_raddr_s         | wire [13:0]    |                   |
| up_rdata_ld_s      | wire [31:0]    |                   |
| up_rdata_pwm_s     | wire [31:0]    |                   |
| up_wreq_s          | wire           |                   |
| up_wack_ld_s       | wire           |                   |
| up_wack_pwm_s      | wire           |                   |
| up_waddr_s         | wire [13:0]    |                   |
| up_wdata_s         | wire [31:0]    |                   |
| pulse_width_s      | wire [31:0]    |                   |
| pulse_period_s     | wire [31:0]    |                   |
| load_config_s      | wire           |                   |
| pulse_gen_resetn   | wire           |                   |
| pulse_counter_s    | wire [31:0]    |                   |
| driver_pulse_int_s | wire           |                   |
| up_ext_clk_count_s | wire [31:0]    |                   |
| sequence_en_s      | wire           |                   |
| auto_sequence_s    | wire           |                   |
| sequence_offset_s  | wire [31:0]    |                   |
| auto_seq0_s        | wire [ 1:0]    |                   |
| auto_seq1_s        | wire [ 1:0]    |                   |
| auto_seq2_s        | wire [ 1:0]    |                   |
| auto_seq3_s        | wire [ 1:0]    |                   |
| manual_select_s    | wire [ 7:0]    |                   |
## Constants

| Name         | Type   | Value                                        | Description |
| ------------ | ------ | -------------------------------------------- | ----------- |
| CORE_VERSION | [31:0] | {<br><span style="padding-left:20px">16'h000 | MAJOR */    |
| CORE_MAGIC   | [31:0] | 32'h4C534452                                 | LSDR        |
## Processes
- unnamed: ( @(posedge up_clk) )
**Description**
read interface merge

- unnamed: ( @(posedge clk) )
**Description**
data path reset generation
this logic will generate a reset signal right before the generated pulse
in order to use it for resetting the cpack module, to synchronize it to
the driver pulse

- unnamed: ( @(posedge clk) )
**Description**
TIA sequencer

- unnamed: ( @(posedge clk) )
## Instantiations

- i_pwm_regmap: axi_pulse_gen_regmap
**Description**
register maps

- i_laser_driver_regmap: axi_laser_driver_regmap
- i_laser_driver_pulse: util_pulse_gen
**Description**
generic PWM generator's

- i_clock_mon: up_clock_mon
**Description**
clock monitor for the external clock

- i_up_axi: up_axi
**Description**
AXI Memory Mapped Wrapper

