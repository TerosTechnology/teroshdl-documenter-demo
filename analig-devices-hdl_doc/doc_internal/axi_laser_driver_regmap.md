# Entity: axi_laser_driver_regmap

- **File**: axi_laser_driver_regmap.v
## Diagram

![Diagram](axi_laser_driver_regmap.svg "Diagram")
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

| Generic name    | Type | Value | Description |
| --------------- | ---- | ----- | ----------- |
| ID              |      | 0     |             |
| LASER_DRIVER_ID |      | 1     |             |
## Ports

| Port name        | Direction | Type   | Description                |
| ---------------- | --------- | ------ | -------------------------- |
| clk              | input     |        | control and status signals |
| driver_en_n      | output    |        |                            |
| driver_otw_n     | input     |        |                            |
| pulse            | input     |        |                            |
| irq              | output    |        |                            |
| up_ext_clk_count | input     | [31:0] |                            |
| sequence_en      | output    |        | TIA sequencer              |
| auto_sequence    | output    |        |                            |
| sequence_offset  | output    | [31:0] |                            |
| auto_seq0        | output    | [ 1:0] |                            |
| auto_seq1        | output    | [ 1:0] |                            |
| auto_seq2        | output    | [ 1:0] |                            |
| auto_seq3        | output    | [ 1:0] |                            |
| manual_select    | output    | [ 7:0] |                            |
| up_rstn          | input     |        | processor interface        |
| up_clk           | input     |        |                            |
| up_wreq          | input     |        |                            |
| up_waddr         | input     | [13:0] |                            |
| up_wdata         | input     | [31:0] |                            |
| up_wack          | output    |        |                            |
| up_rreq          | input     |        |                            |
| up_raddr         | input     | [13:0] |                            |
| up_rdata         | output    | [31:0] |                            |
| up_rack          | output    |        |                            |
## Signals

| Name                    | Type         | Description         |
| ----------------------- | ------------ | ------------------- |
| up_driver_en_n          | reg          | internal registers  |
| up_irq_mask             | reg   [2:0]  |                     |
| up_irq_source           | reg   [2:0]  |                     |
| up_driver_otw_n_int     | reg          |                     |
| up_sequence_en          | reg          |                     |
| up_auto_sequence        | reg          |                     |
| up_sequence_offset      | reg   [31:0] |                     |
| up_auto_seq0            | reg   [ 1:0] |                     |
| up_auto_seq1            | reg   [ 1:0] |                     |
| up_auto_seq2            | reg   [ 1:0] |                     |
| up_auto_seq3            | reg   [ 1:0] |                     |
| up_manual_select        | reg   [ 7:0] |                     |
| up_wreq_int_s           | wire         | internal signals    |
| up_rreq_int_s           | wire         |                     |
| up_driver_otw_n_s       | wire         |                     |
| up_irq_pending_s        | wire [2:0]   |                     |
| up_irq_trigger_s        | wire [2:0]   |                     |
| up_irq_source_clear_s   | wire [2:0]   |                     |
| up_pulse_s              | wire         |                     |
| up_driver_otw_n_enter_s | wire         |                     |
| up_driver_otw_n_exit_s  | wire         |                     |
## Processes
- unnamed: ( @(posedge up_clk) )
- unnamed: ( @(posedge up_clk) )
- unnamed: ( @(posedge up_clk) )
- unnamed: ( @(posedge up_clk) )
- unnamed: ( @(posedge up_clk) )
## Instantiations

- i_driver_otw_sync: sync_bits
**Description**
CDC logic

- i_pulse_sync: sync_bits
- i_sequence_control_sync: sync_bits
- i_sequencer_sync: sync_bits
- i_sequence_offset_sync: sync_bits
