# Entity: deltaSigma_controller

- **File**: deltaSigma_controller.vhd
## Diagram

![Diagram](deltaSigma_controller.svg "Diagram")
## Description

***************************************************************************
***************************************************************************
Copyright 2019 (c) OscillatorIMP Digital
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

| Generic name | Type    | Value | Description       |
| ------------ | ------- | ----- | ----------------- |
| C_SLOT_WIDTH | integer | 24    | Width of one Slot |
## Ports

| Port name      | Direction | Type                          | Description                            |
| -------------- | --------- | ----------------------------- | -------------------------------------- |
| clk            | in        | std_logic                     | System clock                           |
| resetn         | in        | std_logic                     | System reset                           |
| data_clk       | in        | std_logic                     | Data clock should be less than clk / 4 |
| tx_enable      | in        | Boolean                       | Enable TX                              |
| tx_ack         | out       | std_logic                     | Request new Slot Data                  |
| tx_stb         | in        | std_logic                     | Request new Slot Data                  |
| tx_data_left   | in        | std_logic_vector(31 downto 0) | Slot Data in                           |
| tx_data_right  | in        | std_logic_vector(31 downto 0) | Slot Data in                           |
| bit_left_o     | out       | std_logic                     |                                        |
| bit_right_o    | out       | std_logic                     |                                        |
| bclk_div_rate  | in        | natural range 0 to 255        | Runtime parameter                      |
| lrclk_div_rate | in        | natural range 0 to 255        |                                        |
## Signals

| Name                 | Type                         | Description |
| -------------------- | ---------------------------- | ----------- |
| enable               | Boolean                      |             |
| cdc_sync_stage0_tick | std_logic                    |             |
| cdc_sync_stage1_tick | std_logic                    |             |
| cdc_sync_stage2_tick | std_logic                    |             |
| cdc_sync_stage3_tick | std_logic                    |             |
| BCLK_O_int           | std_logic                    |             |
| LRCLK_O_int          | std_logic                    |             |
| tx_bclk              | std_logic                    |             |
| tx_tick              | std_logic                    |             |
| tx_frame_sync        | std_logic                    |             |
| const_1              | std_logic                    |             |
| bclk_tick            | std_logic                    |             |
| data_resetn          | std_logic                    |             |
| data_reset_vec       | std_logic_vector(2 downto 0) |             |
| bit_left_s           | std_logic                    |             |
| bit_right_s          | std_logic                    |             |
## Processes
- unnamed: ( data_clk, resetn )
- unnamed: ( data_clk )
**Description**
Generate tick signal in the DATA_CLK_I domain

- unnamed: ( clk )
## Instantiations

- clkgen: deltaSigma_clkgen
- tx: deltaSigma_tx
