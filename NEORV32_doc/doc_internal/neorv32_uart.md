# Entity: neorv32_uart

## Diagram

![Diagram](neorv32_uart.svg "Diagram")
## Description

#################################################################################################
# << NEORV32 - Universal Asynchronous Receiver and Transmitter (UART0/1) >>                     #
# ********************************************************************************************* #
# Frame configuration: 1 start bit, 8 bit data, parity bit (none/even/odd), 1 stop bit,         #
# programmable BAUD rate via clock pre-scaler and 12-bit BAUD value config register. RX engine  #
# a simple 2-entry data buffer (for double-buffering).                                          #
# Interrupts: UART_RX_available, UART_TX_done                                                   #
#                                                                                               #
# Support for RTS("RTR")/CTS hardware flow control:                                             #
# * uart_rts_o = 0: RX is ready to receive a new char, enabled via CTRL.ctrl_uart_rts_en_c      #
# * uart_cts_i = 0: TX is allowed to send a new char, enabled via CTRL.ctrl_uart_cts_en_c       #
#                                                                                               #
# UART0 / UART1:                                                                                #
# This module is used for implementing UART0 and UART1. The UART_PRIMARY generic configures the #
# interface register addresses and simulation output setting for UART0 (UART_PRIMARY = true)    #
# or UART1 (UART_PRIMARY = false).                                                              #
#                                                                                               #
# SIMULATION MODE:                                                                              #
# When the simulation mode is enabled (setting the ctrl.ctrl_uart_sim_en_c bit) any write       #
# access to the TX register will not trigger any UART activity. Instead, the written data is    #
# output to the simulation environment. The lowest 8 bits of the written data are printed as    #
# ASCII char to the simulator console.                                                          #
# This char is also stored to the file "neorv32.uartX.sim_mode.text.out" (where X = 0 for UART0 #
# and X = 1 for UART1). The full 32-bit write data is also stored as 8-digit hexadecimal value  #
# to the file "neorv32.uartX.sim_mode.data.out" (where X = 0 for UART0 and X = 1 for UART1).    #
# No interrupts are triggered when in SIMULATION MODE.                                          #
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
obviously only for simulation
## Generics

| Generic name | Type    | Value | Description                                                 |
| ------------ | ------- | ----- | ----------------------------------------------------------- |
| UART_PRIMARY | boolean | true  | true = primary UART (UART0), false = secondary UART (UART1) |
## Ports

| Port name   | Direction | Type                           | Description                                            |
| ----------- | --------- | ------------------------------ | ------------------------------------------------------ |
| clk_i       | in        | std_ulogic                     | global clock line                                      |
| addr_i      | in        | std_ulogic_vector(31 downto 0) | address                                                |
| rden_i      | in        | std_ulogic                     | read enable                                            |
| wren_i      | in        | std_ulogic                     | write enable                                           |
| data_i      | in        | std_ulogic_vector(31 downto 0) | data in                                                |
| data_o      | out       | std_ulogic_vector(31 downto 0) | data out                                               |
| ack_o       | out       | std_ulogic                     | transfer acknowledge                                   |
| clkgen_en_o | out       | std_ulogic                     | enable clock generator                                 |
| clkgen_i    | in        | std_ulogic_vector(07 downto 0) |                                                        |
| uart_txd_o  | out       | std_ulogic                     | com lines --                                           |
| uart_rxd_i  | in        | std_ulogic                     |                                                        |
| uart_rts_o  | out       | std_ulogic                     | UART.RX ready to receive ("RTR"), low-active, optional |
| uart_cts_i  | in        | std_ulogic                     | UART.TX allowed to transmit, low-active, optional      |
| irq_rxd_o   | out       | std_ulogic                     | uart data received interrupt                           |
| irq_txd_o   | out       | std_ulogic                     | uart transmission done interrupt                       |
## Signals

| Name        | Type                           | Description                              |
| ----------- | ------------------------------ | ---------------------------------------- |
| ctrl        | std_ulogic_vector(31 downto 0) | control register --                      |
| acc_en      | std_ulogic                     | module access enable                     |
| addr        | std_ulogic_vector(31 downto 0) | access address                           |
| wr_en       | std_ulogic                     | word write enable                        |
| rd_en       | std_ulogic                     | read enable                              |
| uart_clk    | std_ulogic                     | clock generator --                       |
| num_bits    | std_ulogic_vector(03 downto 0) | numbers of bits in transmission frame -- |
| uart_cts_ff | std_ulogic_vector(1 downto 0)  | hardware flow-control IO buffer --       |
| uart_rts    | std_ulogic                     |                                          |
| uart_tx     | uart_tx_t                      |                                          |
| uart_rx     | uart_rx_t                      |                                          |
## Constants

| Name                   | Type                                       | Value                                                                                                                                                                          | Description                                                         |
| ---------------------- | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| uart_id_base_c         | std_ulogic_vector(data_width_c-1 downto 0) |  cond_sel_stdulogicvector_f(UART_PRIMARY,<br><span style="padding-left:20px"> uart0_base_c,<br><span style="padding-left:20px">      uart1_base_c)                             |                                                                     |
| uart_id_size_c         | natural                                    |  cond_sel_natural_f(        UART_PRIMARY,<br><span style="padding-left:20px"> uart0_size_c,<br><span style="padding-left:20px">      uart1_size_c)                             |                                                                     |
| uart_id_ctrl_addr_c    | std_ulogic_vector(data_width_c-1 downto 0) |  cond_sel_stdulogicvector_f(UART_PRIMARY,<br><span style="padding-left:20px"> uart0_ctrl_addr_c,<br><span style="padding-left:20px"> uart1_ctrl_addr_c)                        |                                                                     |
| uart_id_rtx_addr_c     | std_ulogic_vector(data_width_c-1 downto 0) |  cond_sel_stdulogicvector_f(UART_PRIMARY,<br><span style="padding-left:20px"> uart0_rtx_addr_c,<br><span style="padding-left:20px">  uart1_rtx_addr_c)                         |                                                                     |
| hi_abb_c               | natural                                    |  index_size_f(io_size_c)-1                                                                                                                                                     | high address boundary bit                                           |
| lo_abb_c               | natural                                    |  index_size_f(uart_id_size_c)                                                                                                                                                  | low address boundary bit                                            |
| sim_screen_output_en_c | boolean                                    |  true                                                                                                                                                                          | output lowest byte as char to simulator console when enabled        |
| sim_text_output_en_c   | boolean                                    |  true                                                                                                                                                                          | output lowest byte as char to text file when enabled                |
| sim_data_output_en_c   | boolean                                    |  true                                                                                                                                                                          | dump 32-word to file when enabled                                   |
| sim_uart_text_file_c   | string                                     |  cond_sel_string_f(UART_PRIMARY,<br><span style="padding-left:20px"> "neorv32.uart0.sim_mode.text.out",<br><span style="padding-left:20px"> "neorv32.uart1.sim_mode.text.out") | simulation output file configuration --                             |
| sim_uart_data_file_c   | string                                     |  cond_sel_string_f(UART_PRIMARY,<br><span style="padding-left:20px"> "neorv32.uart0.sim_mode.data.out",<br><span style="padding-left:20px"> "neorv32.uart1.sim_mode.data.out") |                                                                     |
| ctrl_uart_baud00_c     | natural                                    |   0                                                                                                                                                                            | r/w: UART baud config bit 0                                         |
| ctrl_uart_baud01_c     | natural                                    |   1                                                                                                                                                                            | r/w: UART baud config bit 1                                         |
| ctrl_uart_baud02_c     | natural                                    |   2                                                                                                                                                                            | r/w: UART baud config bit 2                                         |
| ctrl_uart_baud03_c     | natural                                    |   3                                                                                                                                                                            | r/w: UART baud config bit 3                                         |
| ctrl_uart_baud04_c     | natural                                    |   4                                                                                                                                                                            | r/w: UART baud config bit 4                                         |
| ctrl_uart_baud05_c     | natural                                    |   5                                                                                                                                                                            | r/w: UART baud config bit 5                                         |
| ctrl_uart_baud06_c     | natural                                    |   6                                                                                                                                                                            | r/w: UART baud config bit 6                                         |
| ctrl_uart_baud07_c     | natural                                    |   7                                                                                                                                                                            | r/w: UART baud config bit 7                                         |
| ctrl_uart_baud08_c     | natural                                    |   8                                                                                                                                                                            | r/w: UART baud config bit 8                                         |
| ctrl_uart_baud09_c     | natural                                    |   9                                                                                                                                                                            | r/w: UART baud config bit 9                                         |
| ctrl_uart_baud10_c     | natural                                    |  10                                                                                                                                                                            | r/w: UART baud config bit 10                                        |
| ctrl_uart_baud11_c     | natural                                    |  11                                                                                                                                                                            | r/w: UART baud config bit 11                                        |
| ctrl_uart_sim_en_c     | natural                                    |  12                                                                                                                                                                            | r/w: UART <<SIMULATION MODE>> enable                                |
| ctrl_uart_rts_en_c     | natural                                    |  20                                                                                                                                                                            | r/w: enable hardware flow control: assert rts_o if ready to receive |
| ctrl_uart_cts_en_c     | natural                                    |  21                                                                                                                                                                            | r/w: enable hardware flow control: send only if cts_i is asserted   |
| ctrl_uart_pmode0_c     | natural                                    |  22                                                                                                                                                                            | r/w: Parity config (0=even; 1=odd)                                  |
| ctrl_uart_pmode1_c     | natural                                    |  23                                                                                                                                                                            | r/w: Enable parity bit                                              |
| ctrl_uart_prsc0_c      | natural                                    |  24                                                                                                                                                                            | r/w: UART baud prsc bit 0                                           |
| ctrl_uart_prsc1_c      | natural                                    |  25                                                                                                                                                                            | r/w: UART baud prsc bit 1                                           |
| ctrl_uart_prsc2_c      | natural                                    |  26                                                                                                                                                                            | r/w: UART baud prsc bit 2                                           |
| ctrl_uart_cts_c        | natural                                    |  27                                                                                                                                                                            | r/-: current state of CTS input                                     |
| ctrl_uart_en_c         | natural                                    |  28                                                                                                                                                                            | r/w: UART enable                                                    |
| ctrl_uart_tx_busy_c    | natural                                    |  31                                                                                                                                                                            | r/-: UART transmitter is busy                                       |
| data_rx_perr_c         | natural                                    |  28                                                                                                                                                                            | r/-: Rx parity error                                                |
| data_rx_ferr_c         | natural                                    |  29                                                                                                                                                                            | r/-: Rx frame error                                                 |
| data_rx_overr_c        | natural                                    |  30                                                                                                                                                                            | r/-: Rx data overrun                                                |
| data_rx_avail_c        | natural                                    |  31                                                                                                                                                                            | r/-: Rx data available                                              |
## Types

| Name          | Type | Description     |
| ------------- | ---- | --------------- |
| uart_tx_t     |      | uart tx unit -- |
| ry_data_buf_t |      | uart rx unit -- |
| uart_rx_t     |      |                 |
## Processes
- rw_access: ( clk_i )
**Description**
Read/Write Access ----------------------------------------------------------------------
-------------------------------------------------------------------------------------------

- uart_tx_unit: ( clk_i )
**Description**
UART Transmitter -----------------------------------------------------------------------
-------------------------------------------------------------------------------------------

- uart_rx_unit: ( clk_i )
**Description**
UART Receiver --------------------------------------------------------------------------
-------------------------------------------------------------------------------------------

- flow_control_buffer: ( clk_i )
**Description**
output is low-active
flow-control input/output synchronizer --

- sim_output: ( clk_i )
**Description**
SIMULATION Output ----------------------------------------------------------------------
-------------------------------------------------------------------------------------------
pragma translate_off
synthesis translate_off
RTL_SYNTHESIS OFF

