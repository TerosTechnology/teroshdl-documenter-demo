# Entity: i2s_rx

- **File**: i2s_rx.vhd
## Diagram

![Diagram](i2s_rx.svg "Diagram")
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

| Generic name | Type    | Value | Description        |
| ------------ | ------- | ----- | ------------------ |
| C_SLOT_WIDTH | integer | 24    |  Width of one Slot |
| C_NUM        | integer | 1     |                    |
## Ports

| Port name    | Direction | Type                                      | Description             |
| ------------ | --------- | ----------------------------------------- | ----------------------- |
| clk          | in        | std_logic                                 |  System clock           |
| resetn       | in        | std_logic                                 |  System reset           |
| enable       | in        | Boolean                                   |  Enable RX              |
| bclk         | in        | std_logic                                 |  Bit Clock              |
| channel_sync | in        | std_logic                                 |  Channel Sync           |
| frame_sync   | in        | std_logic                                 |  Frame Sync             |
| sdata        | in        | std_logic_vector(C_NUM - 1 downto 0)      |  Serial Data Output     |
| stb          | out       | std_logic                                 |  Data available         |
| ack          | in        | std_logic                                 |  Data has been consumed |
| data         | out       | std_logic_vector(C_SLOT_WIDTH-1 downto 0) |  Slot Data in           |
## Signals

| Name             | Type                         | Description |
| ---------------- | ---------------------------- | ----------- |
| data_int         | mem                          |             |
| data_latched     | mem_latched                  |             |
| reset_int        | Boolean                      |             |
| enable_int       | Boolean                      |             |
| bit_sync         | std_logic                    |             |
| channel_sync_int | std_logic                    |             |
| frame_sync_int   | std_logic                    |             |
| bclk_d1          | std_logic                    |             |
| sequencer_state  | sequencer_state_type         |             |
| seq              | natural range 0 to C_NUM - 1 |             |
| ovf_frame_cnt    | natural range 0 to 1         |             |
## Types

| Name                 | Type                                                | Description |
| -------------------- | --------------------------------------------------- | ----------- |
| mem                  |                                                     |             |
| mem_latched          |                                                     |             |
| sequencer_state_type | (IDLE,<br><span style="padding-left:20px"> ACTIVE)  |             |
## Processes
- unnamed: ( clk )
- sequencer: ( clk )
- enable_sync: ( clk )
## State machines

![Diagram_state_machine_0]( stm_i2s_rx_00.svg "Diagram")