# Entity: util_cpack2_impl

## Diagram

![Diagram](util_cpack2_impl.svg "Diagram")
## Description

***************************************************************************
 ***************************************************************************
 Copyright 2018 (c) Analog Devices, Inc. All rights reserved.
 In this HDL repository, there are many different and unique modules, consisting
 of various HDL (Verilog or VHDL) components. The individual modules are
 developed independently, and may be accompanied by separate and unique license
 terms.
 The user should read each of these license terms, and understand the
 freedoms and responsabilities that he or she has by using this source/core.
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

| Generic name        | Type | Value | Description |
| ------------------- | ---- | ----- | ----------- |
| NUM_OF_CHANNELS     |      | 4     |             |
| SAMPLES_PER_CHANNEL |      | 1     |             |
| SAMPLE_DATA_WIDTH   |      | 16    |             |
## Ports

| Port name               | Direction | Type                                                            | Description |
| ----------------------- | --------- | --------------------------------------------------------------- | ----------- |
| clk                     | input     |                                                                 |             |
| reset                   | input     |                                                                 |             |
| enable                  | input     | [NUM_OF_CHANNELS-1:0]                                           |             |
| fifo_wr_en              | input     | [NUM_OF_CHANNELS-1:0]                                           |             |
| fifo_wr_overflow        | output    |                                                                 |             |
| fifo_wr_data            | input     | [NUM_OF_CHANNELS*SAMPLE_DATA_WIDTH*SAMPLES_PER_CHANNEL-1:0]     |             |
| packed_fifo_wr_en       | output    | reg                                                             |             |
| packed_fifo_wr_overflow | input     |                                                                 |             |
| packed_fifo_wr_sync     | output    | reg                                                             |             |
| packed_fifo_wr_data     | output    | reg [NUM_OF_CHANNELS*SAMPLE_DATA_WIDTH*SAMPLES_PER_CHANNEL-1:0] |             |
## Signals

| Name             | Type                                           | Description |
| ---------------- | ---------------------------------------------- | ----------- |
| reset_data       | wire                                           |             |
| ready            | wire                                           |             |
| interleaved_data | wire [TOTAL_DATA_WIDTH-1:0]                    |             |
| out_data         | wire [TOTAL_DATA_WIDTH-1:0]                    |             |
| out_sync         | wire                                           |             |
| out_valid        | wire [NUM_OF_CHANNELS*SAMPLES_PER_CHANNEL-1:0] |             |
| data_wr_en       | wire                                           |             |
## Constants

| Name             | Type | Value                                                     | Description |
| ---------------- | ---- | --------------------------------------------------------- | ----------- |
| TOTAL_DATA_WIDTH |      | SAMPLE_DATA_WIDTH * SAMPLES_PER_CHANNEL * NUM_OF_CHANNELS |             |
## Processes
- unnamed: ( @(posedge clk) )
- gen_packed_fifo_wr_data: ( @(posedge clk) )
## Instantiations

- i_interleave: ad_perfect_shuffle
- i_pack_shell: pack_shell
