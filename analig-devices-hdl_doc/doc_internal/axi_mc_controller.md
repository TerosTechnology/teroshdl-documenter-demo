# Entity: axi_mc_controller

- **File**: axi_mc_controller.v
## Diagram

![Diagram](axi_mc_controller.svg "Diagram")
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

| Port name     | Direction | Type   | Description                         |
| ------------- | --------- | ------ | ----------------------------------- |
| ref_clk       | input     |        | 100 MHz                             |
| ctrl_data_clk | input     |        |                                     |
| fmc_en_o      | output    |        |  physical interface                 |
| pwm_ah_o      | output    |        |                                     |
| pwm_al_o      | output    |        |                                     |
| pwm_bh_o      | output    |        |                                     |
| pwm_bl_o      | output    |        |                                     |
| pwm_ch_o      | output    |        |                                     |
| pwm_cl_o      | output    |        |                                     |
| gpo_o         | output    | [3:0]  |                                     |
| pwm_a_i       | input     |        |   controller connections            |
| pwm_b_i       | input     |        |                                     |
| pwm_c_i       | input     |        |                                     |
| sensors_o     | output    | [1:0]  |  interconnection with other modules |
| position_i    | input     | [2:0]  |                                     |
| s_axi_aclk    | input     |        |  axi interface                      |
| s_axi_aresetn | input     |        |                                     |
| s_axi_awvalid | input     |        |                                     |
| s_axi_awaddr  | input     | [15:0] |                                     |
| s_axi_awready | output    |        |                                     |
| s_axi_wvalid  | input     |        |                                     |
| s_axi_wdata   | input     | [31:0] |                                     |
| s_axi_wstrb   | input     | [3:0]  |                                     |
| s_axi_wready  | output    |        |                                     |
| s_axi_bvalid  | output    |        |                                     |
| s_axi_bresp   | output    | [1:0]  |                                     |
| s_axi_bready  | input     |        |                                     |
| s_axi_arvalid | input     |        |                                     |
| s_axi_araddr  | input     | [15:0] |                                     |
| s_axi_arready | output    |        |                                     |
| s_axi_rvalid  | output    |        |                                     |
| s_axi_rresp   | output    | [1:0]  |                                     |
| s_axi_rdata   | output    | [31:0] |                                     |
| s_axi_rready  | input     |        |                                     |
| s_axi_awprot  | input     | [ 2:0] |                                     |
| s_axi_arprot  | input     | [ 2:0] |                                     |
## Signals

| Name               | Type           | Description                                                                                                                                                                                                                                                             |
| ------------------ | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| up_rdata           | reg     [31:0] | ------------------------------------------------------------------------------ ----------- Registers Declarations ------------------------------------------- ------------------------------------------------------------------------------  internal registers        |
| up_wack            | reg            |                                                                                                                                                                                                                                                                         |
| up_rack            | reg            |                                                                                                                                                                                                                                                                         |
| pwm_gen_clk        | reg            |                                                                                                                                                                                                                                                                         |
| adc_rst            | wire           | ------------------------------------------------------------------------------ ----------- Wires Declarations ----------------------------------------------- ------------------------------------------------------------------------------  internal clocks & resets  |
| up_rstn            | wire           |                                                                                                                                                                                                                                                                         |
| up_clk             | wire           |                                                                                                                                                                                                                                                                         |
| up_rreq_s          | wire           |  internal signals                                                                                                                                                                                                                                                       |
| up_wreq_s          | wire           |                                                                                                                                                                                                                                                                         |
| up_raddr_s         | wire [13:0]    |                                                                                                                                                                                                                                                                         |
| up_waddr_s         | wire [13:0]    |                                                                                                                                                                                                                                                                         |
| up_wdata_s         | wire [31:0]    |                                                                                                                                                                                                                                                                         |
| up_control_rdata_s | wire [31:0]    |                                                                                                                                                                                                                                                                         |
| up_control_wack_s  | wire           |                                                                                                                                                                                                                                                                         |
| up_control_rack_s  | wire           |                                                                                                                                                                                                                                                                         |
| run_s              | wire           |                                                                                                                                                                                                                                                                         |
| star_delta_s       | wire           |                                                                                                                                                                                                                                                                         |
| dir_s              | wire           |                                                                                                                                                                                                                                                                         |
| pwm_open_s         | wire [10:0]    |                                                                                                                                                                                                                                                                         |
| pwm_s              | wire [10:0]    |                                                                                                                                                                                                                                                                         |
| dpwm_ah_s          | wire           |                                                                                                                                                                                                                                                                         |
| dpwm_al_s          | wire           |                                                                                                                                                                                                                                                                         |
| dpwm_bh_s          | wire           |                                                                                                                                                                                                                                                                         |
| dpwm_bl_s          | wire           |                                                                                                                                                                                                                                                                         |
| dpwm_ch_s          | wire           |                                                                                                                                                                                                                                                                         |
| dpwm_cl_s          | wire           |                                                                                                                                                                                                                                                                         |
| foc_ctrl_s         | wire           |                                                                                                                                                                                                                                                                         |
## Processes
- unnamed: ( @(posedge ref_clk) )
  - **Type:** always
**Description**
 clock generation 
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
**Description**
 processor read interface 
## Instantiations

- motor_driver_inst: motor_driver
**Description**
 main (device interface)

- control_reg_inst: control_registers
- i_up_axi: up_axi
**Description**
 up bus interface

