# Entity: axi_dmac_reset_manager

- **File**: axi_dmac_reset_manager.v
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

| Name              | Type       | Description                                                                                                                                                                                                                               |
| ----------------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| state             | reg [2:0]  |                                                                                                                                                                                                                                           |
| needs_reset       | reg        |                                                                                                                                                                                                                                           |
| do_reset          | reg        |                                                                                                                                                                                                                                           |
| do_enable         | reg        |                                                                                                                                                                                                                                           |
| enabled_dest      | wire       |                                                                                                                                                                                                                                           |
| enabled_src       | wire       |                                                                                                                                                                                                                                           |
| enabled_all       | wire       |                                                                                                                                                                                                                                           |
| disabled_all      | wire       |                                                                                                                                                                                                                                           |
| reset_async_chain | wire [3:0] |   * Chain the reset through all clock domains. This makes sure that is asserted  * for at least 4 clock cycles of the slowest domain, no matter what. If  * successive domains have the same clock they'll share their reset signal.  */  |
| reset_sync_chain  | wire [3:0] |                                                                                                                                                                                                                                           |
| reset_chain_clks  | wire [2:0] |                                                                                                                                                                                                                                           |
## Constants

| Name            | Type | Value     | Description                                                                                                                                                                                                                                                                                                                           |
| --------------- | ---- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| STATE_DO_RESET  |      | 3'h0      |   * TODO:  * If an external reset is asserted for a domain that domain will go into reset  * immediately. If a transfer is currently active the transfer will be aborted  * and other domains will be shutdown gracefully. The reset manager will stay in  * the shutdown state until all external resets have been de-asserted.  */  |
| STATE_RESET     |      | 3'h1      |                                                                                                                                                                                                                                                                                                                                       |
| STATE_DISABLED  |      | 3'h2      |                                                                                                                                                                                                                                                                                                                                       |
| STATE_STARTUP   |      | 3'h3      |                                                                                                                                                                                                                                                                                                                                       |
| STATE_ENABLED   |      | 3'h4      |                                                                                                                                                                                                                                                                                                                                       |
| STATE_SHUTDOWN  |      | 3'h5      |                                                                                                                                                                                                                                                                                                                                       |
| GEN_ASYNC_RESET |      | undefined |                                                                                                                                                                                                                                                                                                                                       |
## Processes
- unnamed: ( @(posedge clk) )
  - **Type:** always
- unnamed: ( @(posedge clk) )
  - **Type:** always
- unnamed: ( @(posedge clk) )
  - **Type:** always
**Description**
  * If ctrl_enable goes from 1 to 0 a shutdown procedure is initiated. During the  * shutdown procedure all domains are signaled that a shutdown should occur. The  * domains will then complete any active transactions that are required to  * complete according to the interface semantics. Once a domain has completed  * its transactions it will indicate that it has been shutdown. Once all domains  * indicate that they have been disabled a reset pulse will be generated to all  * domains to clear all residual state. The reset pulse is long enough so that it  * is active in all domains for at least 4 clock cycles.  *  * Once the reset signal is de-asserted the DMA is in an idle state and can be  * enabled again. If the DMA receives a enable while it is performing a shutdown  * sequence it will only be re-enabled once the shutdown sequence has  * successfully completed.  *  * If ctrl_pause is asserted all domains will be disabled. But there will be no  * reset, so when the ctrl_pause signal is de-asserted again the DMA will resume  * with its previous state.  *  */<br>  * If ctrl_enable goes low, even for a single clock cycle, we want to go through  * a full reset sequence. This might happen when the state machine is busy, e.g.  * going through a startup sequence. To avoid missing the event store it for  * later.  */ 
- unnamed: ( @(posedge clk) )
  - **Type:** always
## Instantiations

- i_sync_control_dest: sync_bits
- i_sync_status_dest: sync_bits
- i_sync_control_src: sync_bits
- i_sync_status_src: sync_bits
## State machines

![Diagram_state_machine_0]( stm_axi_dmac_reset_manager_00.svg "Diagram")