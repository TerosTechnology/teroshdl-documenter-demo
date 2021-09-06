# Entity: axi_intr_monitor

- **File**: axi_intr_monitor.v
## Diagram

![Diagram](axi_intr_monitor.svg "Diagram")
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

| Generic name | Type | Value        | Description |
| ------------ | ---- | ------------ | ----------- |
| VERSION      |      | 32'h00010000 |             |
## Ports

| Port name     | Direction | Type   | Description    |
| ------------- | --------- | ------ | -------------- |
| irq           | output    |        |                |
| s_axi_aclk    | input     |        |  axi interface |
| s_axi_aresetn | input     |        |                |
| s_axi_awvalid | input     |        |                |
| s_axi_awaddr  | input     | [15:0] |                |
| s_axi_awready | output    |        |                |
| s_axi_wvalid  | input     |        |                |
| s_axi_wdata   | input     | [31:0] |                |
| s_axi_wstrb   | input     | [3:0]  |                |
| s_axi_wready  | output    |        |                |
| s_axi_bvalid  | output    |        |                |
| s_axi_bresp   | output    | [1:0]  |                |
| s_axi_bready  | input     |        |                |
| s_axi_arvalid | input     |        |                |
| s_axi_araddr  | input     | [15:0] |                |
| s_axi_arready | output    |        |                |
| s_axi_rvalid  | output    |        |                |
| s_axi_rresp   | output    | [1:0]  |                |
| s_axi_rdata   | output    | [31:0] |                |
| s_axi_rready  | input     |        |                |
| s_axi_awprot  | input     | [ 2:0] |                |
| s_axi_arprot  | input     | [ 2:0] |                |
## Signals

| Name                       | Type           | Description                                                                                                                                                                                                                                   |
| -------------------------- | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| up_rdata                   | reg     [31:0] | ------------------------------------------------------------------------------ ----------- Registers Declarations ------------------------------------------- ------------------------------------------------------------------------------  |
| up_wack                    | reg            |                                                                                                                                                                                                                                               |
| up_rack                    | reg            |                                                                                                                                                                                                                                               |
| pwm_gen_clk                | reg            |                                                                                                                                                                                                                                               |
| scratch                    | reg     [31:0] |                                                                                                                                                                                                                                               |
| control                    | reg     [31:0] |                                                                                                                                                                                                                                               |
| interrupt                  | reg            |                                                                                                                                                                                                                                               |
| counter_to_interrupt       | reg     [31:0] |                                                                                                                                                                                                                                               |
| counter_to_interrupt_cnt   | reg     [31:0] |                                                                                                                                                                                                                                               |
| counter_from_interrupt     | reg     [31:0] |                                                                                                                                                                                                                                               |
| counter_interrupt_handling | reg     [31:0] |                                                                                                                                                                                                                                               |
| min_interrupt_handling     | reg     [31:0] |                                                                                                                                                                                                                                               |
| max_interrupt_handling     | reg     [31:0] |                                                                                                                                                                                                                                               |
| interrupt_d1               | reg            |                                                                                                                                                                                                                                               |
| arm_counter                | reg            |                                                                                                                                                                                                                                               |
| counter_active             | reg            |                                                                                                                                                                                                                                               |
| up_rreq_s                  | wire           | ------------------------------------------------------------------------------ ----------- Wires Declarations ----------------------------------------------- ------------------------------------------------------------------------------  |
| up_wreq_s                  | wire           |                                                                                                                                                                                                                                               |
| up_raddr_s                 | wire [13:0]    |                                                                                                                                                                                                                                               |
| up_waddr_s                 | wire [13:0]    |                                                                                                                                                                                                                                               |
| up_wdata_s                 | wire [31:0]    |                                                                                                                                                                                                                                               |
## Processes
- unnamed: ( @(negedge s_axi_aresetn or posedge s_axi_aclk) )
  - **Type:** always
- unnamed: ( @(negedge s_axi_aresetn or posedge s_axi_aclk) )
  - **Type:** always
- unnamed: ( @(negedge s_axi_aresetn or posedge s_axi_aclk) )
  - **Type:** always
## Instantiations

- i_up_axi: up_axi
**Description**
 up bus interface

