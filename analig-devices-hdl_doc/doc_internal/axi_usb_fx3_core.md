# Entity: axi_usb_fx3_core

- **File**: axi_usb_fx3_core.v
## Diagram

![Diagram](axi_usb_fx3_core.svg "Diagram")
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

| Port name         | Direction | Type   | Description                                              |
| ----------------- | --------- | ------ | -------------------------------------------------------- |
| clk               | input     |        |                                                          |
| reset             | input     |        |                                                          |
| s_axis_tdata      | input     | [31:0] | s2mm                                                     |
| s_axis_tkeep      | input     | [ 3:0] |                                                          |
| s_axis_tlast      | input     |        |                                                          |
| s_axis_tready     | output    |        |                                                          |
| s_axis_tvalid     | input     |        |                                                          |
| m_axis_tdata      | output    | [31:0] | mm2s                                                     |
| m_axis_tkeep      | output    | [ 3:0] |                                                          |
| m_axis_tlast      | output    |        |                                                          |
| m_axis_tready     | input     |        |                                                          |
| m_axis_tvalid     | output    |        |                                                          |
| fifo0_header_size | input     | [ 7:0] | configuration                                            |
| fifo0_buffer_size | input     | [15:0] |                                                          |
| fifo1_header_size | input     | [ 7:0] |                                                          |
| fifo1_buffer_size | input     | [15:0] |                                                          |
| fifo2_header_size | input     | [ 7:0] |                                                          |
| fifo2_buffer_size | input     | [15:0] |                                                          |
| fifo3_header_size | input     | [ 7:0] |                                                          |
| fifo3_buffer_size | input     | [15:0] |                                                          |
| fifo4_header_size | input     | [ 7:0] |                                                          |
| fifo4_buffer_size | input     | [15:0] |                                                          |
| fifo5_header_size | input     | [ 7:0] |                                                          |
| fifo5_buffer_size | input     | [15:0] |                                                          |
| fifo6_header_size | input     | [ 7:0] |                                                          |
| fifo6_buffer_size | input     | [15:0] |                                                          |
| fifo7_header_size | input     | [ 7:0] |                                                          |
| fifo7_buffer_size | input     | [15:0] |                                                          |
| fifo8_header_size | input     | [ 7:0] |                                                          |
| fifo8_buffer_size | input     | [15:0] |                                                          |
| fifo9_header_size | input     | [ 7:0] |                                                          |
| fifo9_buffer_size | input     | [15:0] |                                                          |
| fifoa_header_size | input     | [ 7:0] |                                                          |
| fifoa_buffer_size | input     | [15:0] |                                                          |
| fifob_header_size | input     | [ 7:0] |                                                          |
| fifob_buffer_size | input     | [15:0] |                                                          |
| fifoc_header_size | input     | [ 7:0] |                                                          |
| fifoc_buffer_size | input     | [15:0] |                                                          |
| fifod_header_size | input     | [ 7:0] |                                                          |
| fifod_buffer_size | input     | [15:0] |                                                          |
| fifoe_header_size | input     | [ 7:0] |                                                          |
| fifoe_buffer_size | input     | [15:0] |                                                          |
| fifof_header_size | input     | [ 7:0] |                                                          |
| fifof_buffer_size | input     | [15:0] |                                                          |
| length_fx32dma    | output    | [31:0] |                                                          |
| length_dma2fx3    | output    | [31:0] |                                                          |
| fx32dma_valid     | input     |        | fx3 interfaceIN -> TO HOST / FX3 OUT -> FROM HOST / FX3  |
| fx32dma_ready     | output    |        |                                                          |
| fx32dma_data      | input     | [31:0] |                                                          |
| fx32dma_sop       | input     |        |                                                          |
| fx32dma_eop       | output    |        |                                                          |
| dma2fx3_ready     | input     |        |                                                          |
| dma2fx3_valid     | output    |        |                                                          |
| dma2fx3_data      | output    | [31:0] |                                                          |
| dma2fx3_eop       | output    |        |                                                          |
| error             | output    |        |                                                          |
| eot_fx32dma       | output    |        |                                                          |
| eot_dma2fx3       | output    |        |                                                          |
| test_mode_tpm     | input     | [ 2:0] |                                                          |
| test_mode_tpg     | input     | [ 2:0] |                                                          |
| monitor_error     | output    |        |                                                          |
| zlp               | input     |        |                                                          |
| fifo_num          | input     | [ 4:0] |                                                          |
## Signals

| Name                  | Type           | Description         |
| --------------------- | -------------- | ------------------- |
| test_mode_active_tpm  | wire           | internal signals    |
| test_mode_active_tpg  | wire           |                     |
| data_size_transaction | reg     [31:0] | internal registers  |
| buffer_size_current   | reg     [15:0] |                     |
| header_size_current   | reg     [ 7:0] |                     |
| error_fx32dma         | reg            |                     |
| error_dma2fx3         | reg            |                     |
| state_fx32dma         | reg     [ 2:0] |                     |
| next_state_fx32dma    | reg     [ 2:0] |                     |
| state_dma2fx3         | reg     [ 2:0] |                     |
| next_state_dma2fx3    | reg     [ 2:0] |                     |
| header_pointer        | reg     [ 7:0] |                     |
| header_read           | reg            |                     |
| dma2fx3_counter       | reg     [31:0] |                     |
| footer_pointer        | reg     [ 7:0] |                     |
| dma2fx3_data_reg      | reg     [31:0] |                     |
| expected_data         | reg     [31:0] |                     |
| first_transfer        | reg            |                     |
## Constants

| Name        | Type | Value  | Description          |
| ----------- | ---- | ------ | -------------------- |
| IDLE        |      | 3'b001 | internal parameters  |
| READ_HEADER |      | 3'b010 |                      |
| ADD_FOOTER  |      | 3'b010 |                      |
| READ_DATA   |      | 3'b100 |                      |
## Functions
- pn23 <font id="function_arguments">()</font> <font id="function_return">return ([31:0])</font>
- pn9 <font id="function_arguments">()</font> <font id="function_return">return ([31:0])</font>
## Processes
- unnamed: ( @(*) )
- unnamed: ( @(posedge clk) )
**Description**
state machine

- unnamed: ( @(*) )
- unnamed: ( @(*) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
**Description**
dma2fx3

- unnamed: ( @(*) )
- unnamed: ( @(*) )
- unnamed: ( @(posedge clk) )
