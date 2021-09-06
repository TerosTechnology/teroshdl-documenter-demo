# Entity: axi_usb_fx3_reg

- **File**: axi_usb_fx3_reg.v
## Diagram

![Diagram](axi_usb_fx3_reg.svg "Diagram")
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

| Port name         | Direction | Type   | Description    |
| ----------------- | --------- | ------ | -------------- |
| fifo_rdy          | input     | [10:0] |  gpif ii       |
| eot_fx32dma       | input     |        |                |
| eot_dma2fx3       | input     |        |                |
| trig              | output    |        |                |
| zlp               | output    |        |                |
| fifo_num          | output    | [ 4:0] |                |
| error             | input     |        |                |
| test_mode_tpm     | output    | [ 2:0] |                |
| test_mode_tpg     | output    | [ 2:0] |                |
| monitor_error     | input     |        |                |
| irq               | output    |        |                |
| fifo0_direction   | output    |        |                |
| fifo0_header_size | output    | [ 7:0] |                |
| fifo0_buffer_size | output    | [15:0] |                |
| fifo1_direction   | output    |        |                |
| fifo1_header_size | output    | [ 7:0] |                |
| fifo1_buffer_size | output    | [15:0] |                |
| fifo2_direction   | output    |        |                |
| fifo2_header_size | output    | [ 7:0] |                |
| fifo2_buffer_size | output    | [15:0] |                |
| fifo3_direction   | output    |        |                |
| fifo3_header_size | output    | [ 7:0] |                |
| fifo3_buffer_size | output    | [15:0] |                |
| fifo4_direction   | output    |        |                |
| fifo4_header_size | output    | [ 7:0] |                |
| fifo4_buffer_size | output    | [15:0] |                |
| fifo5_direction   | output    |        |                |
| fifo5_header_size | output    | [ 7:0] |                |
| fifo5_buffer_size | output    | [15:0] |                |
| fifo6_direction   | output    |        |                |
| fifo6_header_size | output    | [ 7:0] |                |
| fifo6_buffer_size | output    | [15:0] |                |
| fifo7_direction   | output    |        |                |
| fifo7_header_size | output    | [ 7:0] |                |
| fifo7_buffer_size | output    | [15:0] |                |
| fifo8_direction   | output    |        |                |
| fifo8_header_size | output    | [ 7:0] |                |
| fifo8_buffer_size | output    | [15:0] |                |
| fifo9_direction   | output    |        |                |
| fifo9_header_size | output    | [ 7:0] |                |
| fifo9_buffer_size | output    | [15:0] |                |
| fifoa_direction   | output    |        |                |
| fifoa_header_size | output    | [ 7:0] |                |
| fifoa_buffer_size | output    | [15:0] |                |
| length_fx32dma    | input     | [31:0] |                |
| length_dma2fx3    | input     | [31:0] |                |
| up_rstn           | input     |        |  bus interface |
| up_clk            | input     |        |                |
| up_wreq           | input     |        |                |
| up_waddr          | input     | [13:0] |                |
| up_wdata          | input     | [31:0] |                |
| up_wack           | output    |        |                |
| up_rreq           | input     |        |                |
| up_raddr          | input     | [13:0] |                |
| up_rdata          | output    | [31:0] |                |
| up_rack           | output    |        |                |
## Signals

| Name            | Type           | Description                                                     |
| --------------- | -------------- | --------------------------------------------------------------- |
| up_wreq_s       | wire           |  internal signals                                               |
| up_rreq_s       | wire           |                                                                 |
| fifo0_enable    | wire           |                                                                 |
| fifo1_enable    | wire           |                                                                 |
| fifo2_enable    | wire           |                                                                 |
| fifo3_enable    | wire           |                                                                 |
| fifo4_enable    | wire           |                                                                 |
| fifo5_enable    | wire           |                                                                 |
| fifo6_enable    | wire           |                                                                 |
| fifo7_enable    | wire           |                                                                 |
| fifo8_enable    | wire           |                                                                 |
| fifo9_enable    | wire           |                                                                 |
| fifoa_enable    | wire           |                                                                 |
| fifo0_config    | reg     [31:0] |  internal registers                                             |
| fifo1_config    | reg     [31:0] |                                                                 |
| fifo2_config    | reg     [31:0] |                                                                 |
| fifo3_config    | reg     [31:0] |                                                                 |
| fifo4_config    | reg     [31:0] |                                                                 |
| fifo5_config    | reg     [31:0] |                                                                 |
| fifo6_config    | reg     [31:0] |                                                                 |
| fifo7_config    | reg     [31:0] |                                                                 |
| fifo8_config    | reg     [31:0] |                                                                 |
| fifo9_config    | reg     [31:0] |                                                                 |
| fifoa_config    | reg     [31:0] |                                                                 |
| fifo_status     | reg     [31:0] |                                                                 |
| irq_config      | reg     [31:0] | bit 1 - enable error interrupt, bit 0 - enable ready interrupt  |
| transfer_config | reg     [31:0] |                                                                 |
| transfer_status | reg     [31:0] |                                                                 |
| tpm_config      | reg     [31:0] |                                                                 |
| tpm_status      | reg     [31:0] |                                                                 |
| tpg_config      | reg     [31:0] |                                                                 |
| tpg_status      | reg     [31:0] |                                                                 |
## Processes
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
**Description**
 processor read interface 
