# Entity: neorv32_slink

- **File**: neorv32_slink.vhd
## Diagram

![Diagram](neorv32_slink.svg "Diagram")
## Description

#################################################################################################
# << NEORV32 - Stream Link Interface (SLINK) >>                                                 #
# ********************************************************************************************* #
# Up to 8 input (RX) and up to 8 output (TX) stream links are supported. Each link provides an  #
# internal FIFO for buffering. Each stream direction provides a global interrupt to indicate    #
# that a RX link has received new data or that a TX link has finished sending data              #
# (if FIFO_DEPTH = 1) OR if RX/TX link FIFO has become half full (if FIFO_DEPTH > 1).           #
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

| Generic name  | Type    | Value | Description                             |
| ------------- | ------- | ----- | --------------------------------------- |
| SLINK_NUM_TX  | natural | 8     | number of TX links (0..8)               |
| SLINK_NUM_RX  | natural | 8     | number of TX links (0..8)               |
| SLINK_TX_FIFO | natural | 1     | TX fifo depth, has to be a power of two |
| SLINK_RX_FIFO | natural | 1     | RX fifo depth, has to be a power of two |
## Ports

| Port name      | Direction | Type                           | Description          |
| -------------- | --------- | ------------------------------ | -------------------- |
| clk_i          | in        | std_ulogic                     | global clock line    |
| addr_i         | in        | std_ulogic_vector(31 downto 0) | address              |
| rden_i         | in        | std_ulogic                     | read enable          |
| wren_i         | in        | std_ulogic                     | write enable         |
| data_i         | in        | std_ulogic_vector(31 downto 0) | data in              |
| data_o         | out       | std_ulogic_vector(31 downto 0) | data out             |
| ack_o          | out       | std_ulogic                     | transfer acknowledge |
| irq_tx_o       | out       | std_ulogic                     | transmission done    |
| irq_rx_o       | out       | std_ulogic                     | data received        |
| slink_tx_dat_o | out       | sdata_8x32_t                   | output data          |
| slink_tx_val_o | out       | std_ulogic_vector(7 downto 0)  | valid output         |
| slink_tx_rdy_i | in        | std_ulogic_vector(7 downto 0)  | ready to send        |
| slink_rx_dat_i | in        | sdata_8x32_t                   | input data           |
| slink_rx_val_i | in        | std_ulogic_vector(7 downto 0)  | valid input          |
| slink_rx_rdy_o | out       | std_ulogic_vector(7 downto 0)  | ready to receive     |
## Signals

| Name              | Type                           | Description           |
| ----------------- | ------------------------------ | --------------------- |
| ack_read          | std_ulogic                     | bus access control -- |
| ack_write         | std_ulogic                     |                       |
| acc_en            | std_ulogic                     |                       |
| addr              | std_ulogic_vector(31 downto 0) |                       |
| enable            | std_ulogic                     | global enable         |
| rx_fifo_rdata     | fifo_data_t                    |                       |
| rx_fifo_level     | fifo_rx_level_t                |                       |
| tx_fifo_level     | fifo_tx_level_t                |                       |
| fifo_clear        | std_ulogic                     |                       |
| link_sel          | std_ulogic_vector(7 downto 0)  |                       |
| tx_fifo_we        | std_ulogic_vector(7 downto 0)  |                       |
|     rx_fifo_re    | std_ulogic_vector(7 downto 0)  |                       |
| rx_fifo_avail     | std_ulogic_vector(7 downto 0)  |                       |
|  rx_fifo_avail_ff | std_ulogic_vector(7 downto 0)  |                       |
| tx_fifo_free      | std_ulogic_vector(7 downto 0)  |                       |
|   tx_fifo_free_ff | std_ulogic_vector(7 downto 0)  |                       |
| rx_fifo_half      | std_ulogic_vector(7 downto 0)  |                       |
|   rx_fifo_half_ff | std_ulogic_vector(7 downto 0)  |                       |
| tx_fifo_half      | std_ulogic_vector(7 downto 0)  |                       |
|   tx_fifo_half_ff | std_ulogic_vector(7 downto 0)  |                       |
| irq               | irq_t                          |                       |
## Constants

| Name                  | Type    | Value                       | Description                                              |
| --------------------- | ------- | --------------------------- | -------------------------------------------------------- |
| hi_abb_c              | natural |  index_size_f(io_size_c)-1  | high address boundary bit                                |
| lo_abb_c              | natural |  index_size_f(slink_size_c) | low address boundary bit                                 |
| ctrl_rx_num_lsb_c     | natural |   0                         | r/-: number of implemented RX links                      |
| ctrl_rx_num_msb_c     | natural |   3                         |                                                          |
| ctrl_tx_num_lsb_c     | natural |   4                         | r/-: number of implemented TX links                      |
| ctrl_tx_num_msb_c     | natural |   7                         |                                                          |
| ctrl_rx_size_lsb_c    | natural |   8                         | r/-: log2(RX FIFO size)                                  |
| ctrl_rx_size_msb_c    | natural |  11                         |                                                          |
| ctrl_tx_size_lsb_c    | natural |  12                         | r/-: log2(TX FIFO size)                                  |
| ctrl_tx_size_msb_c    | natural |  15                         |                                                          |
| ctrl_en_c             | natural |  31                         | r/w: global enable                                       |
| status_rx_avail_lsb_c | natural |   0                         | r/-: set if TX link 0..7 is ready to send                |
| status_rx_avail_msb_c | natural |   7                         |                                                          |
| status_tx_free_lsb_c  | natural |   8                         | r/-: set if RX link 0..7 data available                  |
| status_tx_free_msb_c  | natural |  15                         |                                                          |
| status_rx_half_lsb_c  | natural |  16                         | r/-: set if TX link 0..7 FIFO fill-level is >= half-full |
| status_rx_half_msb_c  | natural |  23                         |                                                          |
| status_tx_half_lsb_c  | natural |  24                         | r/-: set if RX link 0..7 FIFO fill-level is > half-full  |
| status_tx_half_msb_c  | natural |  31                         |                                                          |
## Types

| Name            | Type | Description                   |
| --------------- | ---- | ----------------------------- |
| fifo_data_t     |      | stream link fifo interface -- |
| fifo_rx_level_t |      |                               |
| fifo_tx_level_t |      |                               |
| irq_t           |      | interrupt controller --       |
## Processes
- rw_access: ( clk_i )
**Description**
word aligned
Read/Write Access ----------------------------------------------------------------------
-------------------------------------------------------------------------------------------

- level_monitor: ( rx_fifo_level, tx_fifo_level )
**Description**
FIFO Level Monitoring ------------------------------------------------------------------
-------------------------------------------------------------------------------------------

- irq_arbiter: ( clk_i )
**Description**
Interrupt Generator --------------------------------------------------------------------
-------------------------------------------------------------------------------------------

- irq_generator_sync: ( clk_i )
**Description**
status buffer --

- irq_generator_comb: ( clk_i )
**Description**
IRQ event detector --

- link_select: ( addr )
**Description**
Link Select ----------------------------------------------------------------------------
-------------------------------------------------------------------------------------------

