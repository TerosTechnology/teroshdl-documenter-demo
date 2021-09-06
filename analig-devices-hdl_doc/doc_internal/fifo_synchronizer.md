# Entity: fifo_synchronizer

- **File**: fifo_synchronizer.vhd
## Diagram

![Diagram](fifo_synchronizer.svg "Diagram")
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

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| DEPTH        | integer | 4     |             |
| WIDTH        | integer | 2     |             |
## Ports

| Port name  | Direction | Type                                 | Description |
| ---------- | --------- | ------------------------------------ | ----------- |
| in_clk     | in        | std_logic                            |             |
| in_resetn  | in        | std_logic                            |             |
| in_data    | in        | std_logic_vector(WIDTH - 1 downto 0) |             |
| in_tick    | in        | std_logic                            |             |
| out_clk    | in        | std_logic                            |             |
| out_resetn | in        | std_logic                            |             |
| out_data   | out       | std_logic_vector(WIDTH - 1 downto 0) |             |
| out_tick   | out       | std_logic                            |             |
## Signals

| Name                 | Type                         | Description |
| -------------------- | ---------------------------- | ----------- |
| fifo                 | DATA_SYNC_FIFO_TYPE          |             |
| rd_addr              | natural range 0 to DEPTH - 1 |             |
| wr_addr              | natural range 0 to DEPTH - 1 |             |
| cdc_sync_stage0_tick | std_logic                    |             |
| cdc_sync_stage1_tick | std_logic                    |             |
| cdc_sync_stage2_tick | std_logic                    |             |
| cdc_sync_stage3_tick | std_logic                    |             |
| tick                 | std_logic                    |             |
## Types

| Name                | Type | Description |
| ------------------- | ---- | ----------- |
| DATA_SYNC_FIFO_TYPE |      |             |
## Processes
- unnamed: ( in_clk )
- unnamed: ( in_clk )
- unnamed: ( out_clk )
- unnamed: ( out_clk )
- unnamed: ( out_clk )
