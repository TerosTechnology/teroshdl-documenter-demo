# Entity: axi_logic_analyzer_trigger

- **File**: axi_logic_analyzer_trigger.v
## Diagram

![Diagram](axi_logic_analyzer_trigger.svg "Diagram")
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

| Port name          | Direction | Type   | Description |
| ------------------ | --------- | ------ | ----------- |
| clk                | input     |        |             |
| reset              | input     |        |             |
| data               | input     | [15:0] |             |
| data_valid         | input     |        |             |
| trigger_i          | input     | [ 1:0] |             |
| trigger_in         | input     |        |             |
| edge_detect_enable | input     | [17:0] |             |
| rise_edge_enable   | input     | [17:0] |             |
| fall_edge_enable   | input     | [17:0] |             |
| low_level_enable   | input     | [17:0] |             |
| high_level_enable  | input     | [17:0] |             |
| trigger_logic      | input     | [ 6:0] |             |
| trigger_out        | output    |        |             |
| trigger_out_adc    | output    |        |             |
## Signals

| Name                   | Type            | Description |
| ---------------------- | --------------- | ----------- |
| ext_t_m                | reg     [  1:0] |             |
| ext_t_low_level_hold   | reg     [  1:0] |             |
| ext_t_high_level_hold  | reg     [  1:0] |             |
| ext_t_edge_detect_hold | reg     [  1:0] |             |
| ext_t_rise_edge_hold   | reg     [  1:0] |             |
| ext_t_fall_edge_hold   | reg     [  1:0] |             |
| ext_t_low_level_ack    | reg             |             |
| ext_t_high_level_ack   | reg             |             |
| ext_t_edge_detect_ack  | reg             |             |
| ext_t_rise_edge_ack    | reg             |             |
| ext_t_fall_edge_ack    | reg             |             |
| data_m1                | reg     [ 15:0] |             |
| low_level              | reg     [ 15:0] |             |
| high_level             | reg     [ 15:0] |             |
| edge_detect            | reg     [ 15:0] |             |
| rise_edge              | reg     [ 15:0] |             |
| fall_edge              | reg     [ 15:0] |             |
| low_level_m            | reg     [ 15:0] |             |
| high_level_m           | reg     [ 15:0] |             |
| edge_detect_m          | reg     [ 15:0] |             |
| rise_edge_m            | reg     [ 15:0] |             |
| fall_edge_m            | reg     [ 15:0] |             |
| trigger_active         | reg             |             |
| trigger_active_mux     | reg             |             |
| trigger_active_d1      | reg             |             |
## Processes
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
**Description**
trigger logic:
0 OR
1 AND

- unnamed: ( @(*) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
**Description**
external trigger detect

