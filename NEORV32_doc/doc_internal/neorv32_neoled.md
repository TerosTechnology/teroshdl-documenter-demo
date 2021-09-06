# Entity: neorv32_neoled

- **File**: neorv32_neoled.vhd
## Diagram

![Diagram](neorv32_neoled.svg "Diagram")
## Description

 #################################################################################################
 # << NEORV32 - Smart LED (WS2811/WS2812) Interface (NEOLED) >>                                  #
 # ********************************************************************************************* #
 # Hardware interface for direct control of "smart LEDs" using an asynchronous serial data       #
 # line. Compatible with the WS2811 and WS2812 LEDs.                                             #
 #                                                                                               #
 # NeoPixel-compatible, RGB (24-bit) and RGBW (32-bit) modes supported (in "parallel")           #
 # (TM) "NeoPixel" is a trademark of Adafruit Industries.                                        #
 #                                                                                               #
 # The interface uses a programmable carrier frequency (800 KHz for the WS2812 LEDs)             #
 # configurable via the control register's clock prescaler bits (ctrl_clksel*_c) and the period  #
 # length configuration bits (ctrl_t_tot_*_c). "high-times" for sending a ZERO or a ONE bit are  #
 # configured using the ctrl_t_0h_*_c and ctrl_t_1h_*_c bits, respectively. 32-bit transfers     #
 # (for RGBW modules) and 24-bit transfers (for RGB modules) are supported via ctrl_mode__c.     #
 #                                                                                               #
 # The device features a TX buffer (FIFO) with <FIFO_DEPTH> entries. An IRQ is triggered if the  #
 # FIFO falls below "half-full" fill level.                                                      #
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

| Generic name | Type    | Value | Description                           |
| ------------ | ------- | ----- | ------------------------------------- |
| FIFO_DEPTH   | natural |       |  TX FIFO depth (1..32k, power of two) |
## Ports

| Port name   | Direction | Type                           | Description             |
| ----------- | --------- | ------------------------------ | ----------------------- |
| clk_i       | in        | std_ulogic                     |  global clock line      |
| addr_i      | in        | std_ulogic_vector(31 downto 0) |  address                |
| rden_i      | in        | std_ulogic                     |  read enable            |
| wren_i      | in        | std_ulogic                     |  write enable           |
| data_i      | in        | std_ulogic_vector(31 downto 0) |  data in                |
| data_o      | out       | std_ulogic_vector(31 downto 0) |  data out               |
| ack_o       | out       | std_ulogic                     |  transfer acknowledge   |
| clkgen_en_o | out       | std_ulogic                     |  enable clock generator |
| clkgen_i    | in        | std_ulogic_vector(07 downto 0) |                         |
| irq_o       | out       | std_ulogic                     |  interrupt request      |
| neoled_o    | out       | std_ulogic                     |  serial async data line |
## Signals

| Name      | Type                           | Description           |
| --------- | ------------------------------ | --------------------- |
| acc_en    | std_ulogic                     |  module access enable |
| addr      | std_ulogic_vector(31 downto 0) |  access address       |
| wren      | std_ulogic                     |  word write enable    |
| rden      | std_ulogic                     |  read enable          |
| ctrl      | ctrl_t                         |                       |
| tx_buffer | tx_buffer_t                    |                       |
| serial    | serial_t                       |                       |
## Constants

| Name            | Type    | Value                        | Description                                                                   |
| --------------- | ------- | ---------------------------- | ----------------------------------------------------------------------------- |
| hi_abb_c        | natural |  index_size_f(io_size_c)-1   |  high address boundary bit                                                    |
| lo_abb_c        | natural |  index_size_f(neoled_size_c) |  low address boundary bit                                                     |
| ctrl_enable_c   | natural |   0                          |  r/w: module enable                                                           |
| ctrl_mode_c     | natural |   1                          |  r/w: 0 = 24-bit RGB mode, 1 = 32-bit RGBW mode                               |
| ctrl_strobe_c   | natural |   2                          |  r/w: 0 = send normal data, 1 = send LED strobe command (RESET) on data write |
| ctrl_clksel0_c  | natural |   3                          |  r/w: prescaler select bit 0                                                  |
| ctrl_clksel1_c  | natural |   4                          |  r/w: prescaler select bit 1                                                  |
| ctrl_clksel2_c  | natural |   5                          |  r/w: prescaler select bit 2                                                  |
| ctrl_bufs_0_c   | natural |   6                          |  r/-: log2(FIFO_DEPTH) bit 0                                                  |
| ctrl_bufs_1_c   | natural |   7                          |  r/-: log2(FIFO_DEPTH) bit 1                                                  |
| ctrl_bufs_2_c   | natural |   8                          |  r/-: log2(FIFO_DEPTH) bit 2                                                  |
| ctrl_bufs_3_c   | natural |   9                          |  r/-: log2(FIFO_DEPTH) bit 3                                                  |
| ctrl_t_tot_0_c  | natural |  10                          |  r/w: pulse-clock ticks per total period bit 0                                |
| ctrl_t_tot_1_c  | natural |  11                          |  r/w: pulse-clock ticks per total period bit 1                                |
| ctrl_t_tot_2_c  | natural |  12                          |  r/w: pulse-clock ticks per total period bit 2                                |
| ctrl_t_tot_3_c  | natural |  13                          |  r/w: pulse-clock ticks per total period bit 3                                |
| ctrl_t_tot_4_c  | natural |  14                          |  r/w: pulse-clock ticks per total period bit 4                                |
| ctrl_t_0h_0_c   | natural |  15                          |  r/w: pulse-clock ticks per ZERO high-time bit 0                              |
| ctrl_t_0h_1_c   | natural |  16                          |  r/w: pulse-clock ticks per ZERO high-time bit 1                              |
| ctrl_t_0h_2_c   | natural |  17                          |  r/w: pulse-clock ticks per ZERO high-time bit 2                              |
| ctrl_t_0h_3_c   | natural |  18                          |  r/w: pulse-clock ticks per ZERO high-time bit 3                              |
| ctrl_t_0h_4_c   | natural |  19                          |  r/w: pulse-clock ticks per ZERO high-time bit 4                              |
| ctrl_t_1h_0_c   | natural |  20                          |  r/w: pulse-clock ticks per ONE high-time bit 0                               |
| ctrl_t_1h_1_c   | natural |  21                          |  r/w: pulse-clock ticks per ONE high-time bit 1                               |
| ctrl_t_1h_2_c   | natural |  22                          |  r/w: pulse-clock ticks per ONE high-time bit 2                               |
| ctrl_t_1h_3_c   | natural |  23                          |  r/w: pulse-clock ticks per ONE high-time bit 3                               |
| ctrl_t_1h_4_c   | natural |  24                          |  r/w: pulse-clock ticks per ONE high-time bit 4                               |
| ctrl_tx_empty_c | natural |  28                          |  r/-: TX FIFO is empty                                                        |
| ctrl_tx_half_c  | natural |  29                          |  r/-: TX FIFO is at least half-full                                           |
| ctrl_tx_full_c  | natural |  30                          |  r/-: TX FIFO is full                                                         |
| ctrl_tx_busy_c  | natural |  31                          |  r/-: serial TX engine busy when set                                          |
## Types

| Name           | Type                                                                                                                                                                                           | Description                     |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| ctrl_t         |                                                                                                                                                                                                |  control register --            |
| tx_buffer_t    |                                                                                                                                                                                                |  transmission buffer --         |
| serial_state_t | (S_IDLE,<br><span style="padding-left:20px"> S_INIT,<br><span style="padding-left:20px"> S_GETBIT,<br><span style="padding-left:20px"> S_PULSE,<br><span style="padding-left:20px"> S_STROBE)  |  serial transmission engine --  |
| serial_t       |                                                                                                                                                                                                |                                 |
## Processes
- rw_access: ( clk_i )
**Description**
 Read/Write Access ----------------------------------------------------------------------  ------------------------------------------------------------------------------------------- 
- irq_generator: ( clk_i )
**Description**
 IRQ Generator --------------------------------------------------------------------------  ------------------------------------------------------------------------------------------- 
- serial_engine: ( clk_i )
**Description**
 Serial TX Engine -----------------------------------------------------------------------  ------------------------------------------------------------------------------------------- 
## Instantiations

- tx_data_fifo: neorv32_fifo
**Description**
 TX Buffer (FIFO) -----------------------------------------------------------------------
 -------------------------------------------------------------------------------------------

