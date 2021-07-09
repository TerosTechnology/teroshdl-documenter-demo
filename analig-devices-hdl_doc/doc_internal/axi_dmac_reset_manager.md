# Entity: axi_dmac_reset_manager

## Diagram

![Diagram](axi_dmac_reset_manager.svg "Diagram")
## Description

***************************************************************************
 ***************************************************************************
 Copyright 2014 - 2018 (c) Analog Devices, Inc. All rights reserved.
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

| Generic name       | Type | Value | Description |
| ------------------ | ---- | ----- | ----------- |
| ASYNC_CLK_REQ_SRC  |      | 1     |             |
| ASYNC_CLK_SRC_DEST |      | 1     |             |
| ASYNC_CLK_DEST_REQ |      | 1     |             |
## Ports

| Port name       | Direction | Type   | Description |
| --------------- | --------- | ------ | ----------- |
| clk             | input     |        |             |
| resetn          | input     |        |             |
| ctrl_enable     | input     |        |             |
| ctrl_pause      | input     |        |             |
| req_resetn      | output    |        |             |
| req_enable      | output    |        |             |
| req_enabled     | input     |        |             |
| dest_clk        | input     |        |             |
| dest_ext_resetn | input     |        |             |
| dest_resetn     | output    |        |             |
| dest_enable     | output    |        |             |
| dest_enabled    | input     |        |             |
| src_clk         | input     |        |             |
| src_ext_resetn  | input     |        |             |
| src_resetn      | output    |        |             |
| src_enable      | output    |        |             |
| src_enabled     | input     |        |             |
| dbg_status      | output    | [11:0] |             |
## Signals

| Name              | Type       | Description |
| ----------------- | ---------- | ----------- |
| state             | reg [2:0]  |             |
| needs_reset       | reg        |             |
| do_reset          | reg        |             |
| do_enable         | reg        |             |
| enabled_dest      | wire       |             |
| enabled_src       | wire       |             |
| enabled_all       | wire       |             |
| disabled_all      | wire       |             |
| reset_async_chain | wire [3:0] |             |
| reset_sync_chain  | wire [3:0] |             |
| reset_chain_clks  | wire [2:0] |             |
## Constants

| Name            | Type | Value     | Description |
| --------------- | ---- | --------- | ----------- |
| STATE_DO_RESET  |      | 3'h0      |             |
| STATE_RESET     |      | 3'h1      |             |
| STATE_DISABLED  |      | 3'h2      |             |
| STATE_STARTUP   |      | 3'h3      |             |
| STATE_ENABLED   |      | 3'h4      |             |
| STATE_SHUTDOWN  |      | 3'h5      |             |
| GEN_ASYNC_RESET |      | undefined |             |
## Processes
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
## Instantiations

- i_sync_control_dest: sync_bits
- i_sync_status_dest: sync_bits
- i_sync_control_src: sync_bits
- i_sync_status_src: sync_bits
## State machines

![Diagram_state_machine_0]( stm_axi_dmac_reset_manager_00.svg "Diagram")