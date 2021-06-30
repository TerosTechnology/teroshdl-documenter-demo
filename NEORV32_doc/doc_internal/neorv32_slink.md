# Entity: neorv32_slink

## Diagram

![Diagram](neorv32_slink.svg "Diagram")
## Description

#################################################################################################
# << NEORV32 - Stream Link Interface (SLINK) >>                                                 #
# ********************************************************************************************* #
# Up to 8 input (RX) and up to 8 output (TX) stream links are supported. Each stream direction  #
# provides a global interrupt to indicate that a RX link has received new data or that a TX     #
# has finished sending data. Each link is provides an internal FIFO for buffering.              #
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

| Name              | Type                           | Description            |
| ----------------- | ------------------------------ | ---------------------- |
| ack_read          | std_ulogic                     | bus access control --  |
| ack_write         | std_ulogic                     |                        |
| acc_en            | std_ulogic                     |                        |
| addr              | std_ulogic_vector(31 downto 0) |                        |
| enable            | std_ulogic                     | global enable          |
| tx_fifo_free_buf  | std_ulogic_vector(7 downto 0)  | interrupt generator -- |
| rx_fifo_avail_buf | std_ulogic_vector(7 downto 0)  |                        |
| rx_fifo_rdata     | fifo_data_t                    |                        |
| fifo_clear        | std_ulogic                     |                        |
| link_sel          | std_ulogic_vector(7 downto 0)  |                        |
| tx_fifo_we        | std_ulogic_vector(7 downto 0)  |                        |
|  tx_fifo_free     | std_ulogic_vector(7 downto 0)  |                        |
| rx_fifo_re        | std_ulogic_vector(7 downto 0)  |                        |
|  rx_fifo_avail    | std_ulogic_vector(7 downto 0)  |                        |
## Constants

| Name             | Type    | Value                       | Description                                  |
| ---------------- | ------- | --------------------------- | -------------------------------------------- |
| hi_abb_c         | natural |  index_size_f(io_size_c)-1  | high address boundary bit                    |
| lo_abb_c         | natural |  index_size_f(slink_size_c) | low address boundary bit                     |
| ctrl_rx0_avail_c | natural |   0                         | r/-: set if TX link 0 is ready to send       |
| ctrl_rx1_avail_c | natural |   1                         | r/-: set if TX link 1 is ready to send       |
| ctrl_rx2_avail_c | natural |   2                         | r/-: set if TX link 2 is ready to send       |
| ctrl_rx3_avail_c | natural |   3                         | r/-: set if TX link 3 is ready to send       |
| ctrl_rx4_avail_c | natural |   4                         | r/-: set if TX link 4 is ready to send       |
| ctrl_rx5_avail_c | natural |   5                         | r/-: set if TX link 5 is ready to send       |
| ctrl_rx6_avail_c | natural |   6                         | r/-: set if TX link 6 is ready to send       |
| ctrl_rx7_avail_c | natural |   7                         | r/-: set if TX link 7 is ready to send       |
| ctrl_tx0_free_c  | natural |   8                         | r/-: set if RX link 0 data available         |
| ctrl_tx1_free_c  | natural |   9                         | r/-: set if RX link 1 data available         |
| ctrl_tx2_free_c  | natural |  10                         | r/-: set if RX link 2 data available         |
| ctrl_tx3_free_c  | natural |  11                         | r/-: set if RX link 3 data available         |
| ctrl_tx4_free_c  | natural |  12                         | r/-: set if RX link 4 data available         |
| ctrl_tx5_free_c  | natural |  13                         | r/-: set if RX link 5 data available         |
| ctrl_tx6_free_c  | natural |  14                         | r/-: set if RX link 6 data available         |
| ctrl_tx7_free_c  | natural |  15                         | r/-: set if RX link 7 data available         |
| ctrl_rx_num0_c   | natural |  16                         | r/-: number of implemented RX links -1 bit 0 |
| ctrl_rx_num1_c   | natural |  17                         | r/-: number of implemented RX links -1 bit 1 |
| ctrl_rx_num2_c   | natural |  18                         | r/-: number of implemented RX links -1 bit 2 |
| ctrl_tx_num0_c   | natural |  19                         | r/-: number of implemented TX links -1 bit 0 |
| ctrl_tx_num1_c   | natural |  20                         | r/-: number of implemented TX links -1 bit 1 |
| ctrl_tx_num2_c   | natural |  21                         | r/-: number of implemented TX links -1 bit 2 |
| ctrl_rx_size0_c  | natural |  22                         | r/-: log2(RX FIFO size) bit 0                |
| ctrl_rx_size1_c  | natural |  23                         | r/-: log2(RX FIFO size) bit 1                |
| ctrl_rx_size2_c  | natural |  24                         | r/-: log2(RX FIFO size) bit 2                |
| ctrl_rx_size3_c  | natural |  25                         | r/-: log2(RX FIFO size) bit 3                |
| ctrl_tx_size0_c  | natural |  26                         | r/-: log2(TX FIFO size) bit 0                |
| ctrl_tx_size1_c  | natural |  27                         | r/-: log2(TX FIFO size) bit 1                |
| ctrl_tx_size2_c  | natural |  28                         | r/-: log2(TX FIFO size) bit 2                |
| ctrl_tx_size3_c  | natural |  29                         | r/-: log2(TX FIFO size) bit 3                |
| ctrl_en_c        | natural |  31                         | r/w: global enable                           |
## Types

| Name        | Type | Description                   |
| ----------- | ---- | ----------------------------- |
| fifo_data_t |      | stream link fifo interface -- |
## Processes
- rw_access: ( clk_i )
**Description**
word aligned
Read/Write Access ----------------------------------------------------------------------
-------------------------------------------------------------------------------------------

- irq_generator: ( clk_i )
**Description**
Interrupt Generator --------------------------------------------------------------------
-------------------------------------------------------------------------------------------

- link_select: ( addr )
**Description**
Link Select ----------------------------------------------------------------------------
-------------------------------------------------------------------------------------------

