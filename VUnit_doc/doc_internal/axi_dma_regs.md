# Entity: axi_dma_regs

- **File**: axi_dma_regs.vhd
## Diagram

![Diagram](axi_dma_regs.svg "Diagram")
## Description

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this file,
You can obtain one at http://mozilla.org/MPL/2.0/.
Copyright (c) 2014-2021, Lars Asplund lars.anders.asplund@gmail.com
## Ports

| Port name      | Direction | Type                          | Description |
| -------------- | --------- | ----------------------------- | ----------- |
| clk            | in        | std_logic                     |             |
| axils_m2s      | in        | axil_m2s_t                    |             |
| axils_s2m      | out       | axil_s2m_t                    |             |
| start_transfer | out       | std_logic                     |             |
| transfer_done  | in        | std_logic                     |             |
| src_address    | out       | std_logic_vector(31 downto 0) |             |
| dst_address    | out       | std_logic_vector(31 downto 0) |             |
| num_bytes      | out       | std_logic_vector(31 downto 0) |             |
## Signals

| Name  | Type                                      | Description |
| ----- | ----------------------------------------- | ----------- |
| state | state_t                                   |             |
| addr  | std_logic_vector(axils_m2s.ar.addr'range) |             |
## Types

| Name    | Type                                                                                                                                                  | Description |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| state_t | (idle,<br><span style="padding-left:20px"> writing,<br><span style="padding-left:20px"> write_response,<br><span style="padding-left:20px"> reading)  |             |
## Functions
- cmp_word_address <font id="function_arguments">(byte_addr : std_logic_vector;<br><span style="padding-left:20px"> word_addr : natural) </font> <font id="function_return">return boolean </font>
**Description**
Compare addresses of 32-bit words discarding byte address
## Processes
- main: (  )
## State machines

![Diagram_state_machine_0]( stm_axi_dma_regs_00.svg "Diagram")