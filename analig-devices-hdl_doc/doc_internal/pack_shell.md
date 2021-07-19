# Entity: pack_shell

- **File**: pack_shell.v
## Diagram

![Diagram](pack_shell.svg "Diagram")
## Description

***************************************************************************
 ***************************************************************************
 Copyright 2017 (c) Analog Devices, Inc. All rights reserved.
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
| PACK                |      | 0     |             |
## Ports

| Port name  | Direction | Type                                                        | Description |
| ---------- | --------- | ----------------------------------------------------------- | ----------- |
| clk        | input     |                                                             |             |
| reset      | input     |                                                             |             |
| reset_data | output    | reg                                                         |             |
| enable     | input     | [NUM_OF_CHANNELS-1:0]                                       |             |
| ce         | input     |                                                             |             |
| ready      | output    | reg                                                         |             |
| in_data    | input     | [NUM_OF_CHANNELS*SAMPLE_DATA_WIDTH*SAMPLES_PER_CHANNEL-1:0] |             |
| out_data   | output    | [NUM_OF_CHANNELS*SAMPLE_DATA_WIDTH*SAMPLES_PER_CHANNEL-1:0] |             |
| out_sync   | output    |                                                             |             |
| out_valid  | output    | [NUM_OF_CHANNELS*SAMPLES_PER_CHANNEL-1:0]                   |             |
## Signals

| Name          | Type                      | Description |
| ------------- | ------------------------- | ----------- |
| reset_ctrl    | reg                       |             |
| startup_ctrl  | reg                       |             |
| startup_ctrl2 | reg                       |             |
| enable_int    | reg [NUM_OF_CHANNELS-1:0] |             |
## Constants

| Name               | Type | Value                                   | Description                                                    |
| ------------------ | ---- | --------------------------------------- | -------------------------------------------------------------- |
| NON_POWER_OF_TWO   |      | NUM_OF_CHANNELS > 2                     | If the number of active channels can be a non-power of two */  |
| CHANNEL_DATA_WIDTH |      | SAMPLES_PER_CHANNEL * SAMPLE_DATA_WIDTH |                                                                |
| TOTAL_DATA_WIDTH   |      | CHANNEL_DATA_WIDTH * NUM_OF_CHANNELS    |                                                                |
| NUM_OF_SAMPLES     |      | NUM_OF_CHANNELS * SAMPLES_PER_CHANNEL   |                                                                |
## Processes
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
