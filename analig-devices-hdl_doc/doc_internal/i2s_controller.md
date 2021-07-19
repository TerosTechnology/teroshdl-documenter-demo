# Entity: i2s_controller

- **File**: i2s_controller.vhd
## Diagram

![Diagram](i2s_controller.svg "Diagram")
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

| Generic name | Type    | Value | Description                                        |
| ------------ | ------- | ----- | -------------------------------------------------- |
| C_SLOT_WIDTH | integer | 24    | Width of one Slot                                  |
| C_BCLK_POL   | integer | 0     | BCLK Polarity (0 - Falling edge, 1 - Rising edge)  |
| C_LRCLK_POL  | integer | 0     | LRCLK Polarity (0 - Falling edge, 1 - Rising edge) |
| C_NUM_CH     | integer | 1     |                                                    |
| C_HAS_TX     | integer | 1     |                                                    |
| C_HAS_RX     | integer | 1     |                                                    |
## Ports

| Port name      | Direction | Type                                      | Description                            |
| -------------- | --------- | ----------------------------------------- | -------------------------------------- |
| clk            | in        | std_logic                                 | System clock                           |
| resetn         | in        | std_logic                                 | System reset                           |
| data_clk       | in        | std_logic                                 | Data clock should be less than clk / 4 |
| bclk_o         | out       | std_logic_vector(C_NUM_CH - 1 downto 0)   | Bit Clock                              |
| lrclk_o        | out       | std_logic_vector(C_NUM_CH - 1 downto 0)   | Frame Clock                            |
| sdata_o        | out       | std_logic_vector(C_NUM_CH - 1 downto 0)   | Serial Data Output                     |
| sdata_i        | in        | std_logic_vector(C_NUM_CH - 1 downto 0)   | Serial Data Input                      |
| tx_enable      | in        | Boolean                                   | Enable TX                              |
| tx_ack         | out       | std_logic                                 | Request new Slot Data                  |
| tx_stb         | in        | std_logic                                 | Request new Slot Data                  |
| tx_data        | in        | std_logic_vector(C_SLOT_WIDTH-1 downto 0) | Slot Data in                           |
| rx_enable      | in        | Boolean                                   | Enable RX                              |
| rx_ack         | in        | std_logic                                 |                                        |
| rx_stb         | out       | std_logic                                 | Valid Slot Data                        |
| rx_data        | out       | std_logic_vector(C_SLOT_WIDTH-1 downto 0) | Slot Data out                          |
| bclk_div_rate  | in        | natural range 0 to 255                    | Runtime parameter                      |
| lrclk_div_rate | in        | natural range 0 to 255                    |                                        |
## Signals

| Name                 | Type                                    | Description |
| -------------------- | --------------------------------------- | ----------- |
| enable               | Boolean                                 |             |
| cdc_sync_stage0_tick | std_logic                               |             |
| cdc_sync_stage1_tick | std_logic                               |             |
| cdc_sync_stage2_tick | std_logic                               |             |
| cdc_sync_stage3_tick | std_logic                               |             |
| BCLK_O_int           | std_logic                               |             |
| LRCLK_O_int          | std_logic                               |             |
| tx_bclk              | std_logic                               |             |
| tx_lrclk             | std_logic                               |             |
| tx_sdata             | std_logic_vector(C_NUM_CH - 1 downto 0) |             |
| tx_tick              | std_logic                               |             |
| tx_channel_sync      | std_logic                               |             |
| tx_frame_sync        | std_logic                               |             |
| const_1              | std_logic                               |             |
| bclk_tick            | std_logic                               |             |
| rx_bclk              | std_logic                               |             |
| rx_lrclk             | std_logic                               |             |
| rx_sdata             | std_logic_vector(NUM_RX - 1 downto 0)   |             |
| rx_channel_sync      | std_logic                               |             |
| rx_frame_sync        | std_logic                               |             |
| tx_sync_fifo_out     | std_logic_vector(3 + NUM_TX downto 0)   |             |
| tx_sync_fifo_in      | std_logic_vector(3 + NUM_TX downto 0)   |             |
| rx_sync_fifo_out     | std_logic_vector(3 + NUM_RX downto 0)   |             |
| rx_sync_fifo_in      | std_logic_vector(3 + NUM_RX downto 0)   |             |
| data_resetn          | std_logic                               |             |
| data_reset_vec       | std_logic_vector(2 downto 0)            |             |
## Constants

| Name   | Type    | Value                | Description |
| ------ | ------- | -------------------- | ----------- |
| NUM_TX | integer |  C_HAS_TX * C_NUM_CH |             |
| NUM_RX | integer |  C_HAS_RX * C_NUM_CH |             |
## Processes
- unnamed: ( data_clk, resetn )
- unnamed: ( data_clk )
**Description**
Generate tick signal in the DATA_CLK_I domain

- unnamed: ( clk )
- unnamed: ( data_clk )
## Instantiations

- tx_sync: fifo_synchronizer
- clkgen: i2s_clkgen
