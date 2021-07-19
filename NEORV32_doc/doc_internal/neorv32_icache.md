# Entity: neorv32_icache

- **File**: neorv32_icache.vhd
## Diagram

![Diagram](neorv32_icache.svg "Diagram")
## Description

#################################################################################################
# << NEORV32 - Processor-Internal Instruction Cache >>                                          #
# ********************************************************************************************* #
# Direct mapped (ICACHE_NUM_SETS = 1) or 2-way set-associative (ICACHE_NUM_SETS = 2).           #
# Least recently used replacement policy (if ICACHE_NUM_SETS > 1).                              #
# ********************************************************************************************* #
# BSD 3-Clause License                                                                          #
#                                                                                               #
# Copyright (c) 2021, Stephan Nolting. All rights reserved.                                     #
#                                                                                               #
# Redistribution and use in source and binary forms, with or without modification, are          #
# permitted provided that the following conditions are met:                                     #
#                                                                                               #
# 1. Redistributions of source code must retain the above copyright notice, this list of        #
#    conditions and the following disclaimer.                                                   #
#                                                                                               #
# 2. Redistributions in binary form must reproduce the above copyright notice, this list of     #
#    conditions and the following disclaimer in the documentation and/or other materials        #
#    provided with the distribution.                                                            #
#                                                                                               #
# 3. Neither the name of the copyright holder nor the names of its contributors may be used to  #
#    endorse or promote products derived from this software without specific prior written      #
#    permission.                                                                                #
#                                                                                               #
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS   #
# OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF               #
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE    #
# COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,     #
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE #
# GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED    #
# AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING     #
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED  #
# OF THE POSSIBILITY OF SUCH DAMAGE.                                                            #
# ********************************************************************************************* #
# The NEORV32 Processor - https://github.com/stnolting/neorv32              (c) Stephan Nolting #
#################################################################################################
## Generics

| Generic name      | Type    | Value | Description                                                              |
| ----------------- | ------- | ----- | ------------------------------------------------------------------------ |
| ICACHE_NUM_BLOCKS | natural | 4     | number of blocks (min 1), has to be a power of 2                         |
| ICACHE_BLOCK_SIZE | natural | 16    | block size in bytes (min 4), has to be a power of 2                      |
| ICACHE_NUM_SETS   | natural | 1     | associativity / number of sets (1=direct_mapped), has to be a power of 2 |
## Ports

| Port name    | Direction | Type                                       | Description                     |
| ------------ | --------- | ------------------------------------------ | ------------------------------- |
| clk_i        | in        | std_ulogic                                 | global clock, rising edge       |
| rstn_i       | in        | std_ulogic                                 | global reset, low-active, async |
| clear_i      | in        | std_ulogic                                 | cache clear                     |
| host_addr_i  | in        | std_ulogic_vector(data_width_c-1 downto 0) | bus access address              |
| host_rdata_o | out       | std_ulogic_vector(data_width_c-1 downto 0) | bus read data                   |
| host_wdata_i | in        | std_ulogic_vector(data_width_c-1 downto 0) | bus write data                  |
| host_ben_i   | in        | std_ulogic_vector(03 downto 0)             | byte enable                     |
| host_we_i    | in        | std_ulogic                                 | write enable                    |
| host_re_i    | in        | std_ulogic                                 | read enable                     |
| host_ack_o   | out       | std_ulogic                                 | bus transfer acknowledge        |
| host_err_o   | out       | std_ulogic                                 | bus transfer error              |
| bus_addr_o   | out       | std_ulogic_vector(data_width_c-1 downto 0) | bus access address              |
| bus_rdata_i  | in        | std_ulogic_vector(data_width_c-1 downto 0) | bus read data                   |
| bus_wdata_o  | out       | std_ulogic_vector(data_width_c-1 downto 0) | bus write data                  |
| bus_ben_o    | out       | std_ulogic_vector(03 downto 0)             | byte enable                     |
| bus_we_o     | out       | std_ulogic                                 | write enable                    |
| bus_re_o     | out       | std_ulogic                                 | read enable                     |
| bus_ack_i    | in        | std_ulogic                                 | bus transfer acknowledge        |
| bus_err_i    | in        | std_ulogic                                 | bus transfer error              |
## Signals

| Name  | Type       | Description |
| ----- | ---------- | ----------- |
| cache | cache_if_t |             |
| ctrl  | ctrl_t     |             |
## Constants

| Name                | Type    | Value                                                | Description                        |
| ------------------- | ------- | ---------------------------------------------------- | ---------------------------------- |
| cache_offset_size_c | natural |  index_size_f(ICACHE_BLOCK_SIZE/4)                   | offset addresses full 32-bit words |
| cache_index_size_c  | natural |  index_size_f(ICACHE_NUM_BLOCKS)                     |                                    |
| cache_tag_size_c    | natural |  32 - (cache_offset_size_c + cache_index_size_c + 2) | 2 additonal bits for byte offset   |
## Types

| Name                | Type                                                                                                                                                                                                                                                                                                                                                                                                                                           | Description        |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| cache_if_t          |                                                                                                                                                                                                                                                                                                                                                                                                                                                | cache interface -- |
| ctrl_engine_state_t | (S_IDLE,<br><span style="padding-left:20px"> S_CACHE_CLEAR,<br><span style="padding-left:20px"> S_CACHE_CHECK,<br><span style="padding-left:20px"> S_CACHE_MISS,<br><span style="padding-left:20px"> S_BUS_DOWNLOAD_REQ,<br><span style="padding-left:20px"> S_BUS_DOWNLOAD_GET,<br><span style="padding-left:20px"> S_CACHE_RESYNC_0,<br><span style="padding-left:20px"> S_CACHE_RESYNC_1,<br><span style="padding-left:20px"> S_BUS_ERROR)  | control engine --  |
| ctrl_t              |                                                                                                                                                                                                                                                                                                                                                                                                                                                |                    |
## Processes
- ctrl_engine_fsm_sync_rst: ( rstn_i, clk_i )
**Description**
Control Engine FSM Sync ----------------------------------------------------------------
-------------------------------------------------------------------------------------------
registers that REQUIRE a specific reset state --

- ctrl_engine_fsm_sync: ( clk_i )
**Description**
registers that do not require a specific reset state --

- ctrl_engine_fsm_comb: ( ctrl, cache, clear_i, host_addr_i, host_re_i, bus_rdata_i, bus_ack_i, bus_err_i )
**Description**
Control Engine FSM Comb ----------------------------------------------------------------
-------------------------------------------------------------------------------------------

## Instantiations

- neorv32_icache_memory_inst: neorv32_icache_memory
**Description**
Cache Memory ---------------------------------------------------------------------------
-------------------------------------------------------------------------------------------

