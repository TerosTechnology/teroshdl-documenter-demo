# Entity: neorv32_twi

- **File**: neorv32_twi.vhd
## Diagram

![Diagram](neorv32_twi.svg "Diagram")
## Description

#################################################################################################
# << NEORV32 - Two-Wire Interface Controller (TWI) >>                                           #
# ********************************************************************************************* #
# Supports START and STOP conditions, 8 bit data + ACK/NACK transfers and clock stretching.     #
# Supports ACKs by the constroller. No multi-controller support and no peripheral mode support  #
# yet. Interrupt: TWI_transfer_done                                                             #
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
## Ports

| Port name   | Direction | Type                           | Description            |
| ----------- | --------- | ------------------------------ | ---------------------- |
| clk_i       | in        | std_ulogic                     | global clock line      |
| addr_i      | in        | std_ulogic_vector(31 downto 0) | address                |
| rden_i      | in        | std_ulogic                     | read enable            |
| wren_i      | in        | std_ulogic                     | write enable           |
| data_i      | in        | std_ulogic_vector(31 downto 0) | data in                |
| data_o      | out       | std_ulogic_vector(31 downto 0) | data out               |
| ack_o       | out       | std_ulogic                     | transfer acknowledge   |
| clkgen_en_o | out       | std_ulogic                     | enable clock generator |
| clkgen_i    | in        | std_ulogic_vector(07 downto 0) |                        |
| twi_sda_io  | inout     | std_logic                      | serial data line       |
| twi_scl_io  | inout     | std_logic                      | serial clock line      |
| irq_o       | out       | std_ulogic                     | transfer done IRQ      |
## Signals

| Name           | Type                           | Description             |
| -------------- | ------------------------------ | ----------------------- |
| acc_en         | std_ulogic                     | module access enable    |
| addr           | std_ulogic_vector(31 downto 0) | access address          |
| wr_en          | std_ulogic                     | word write enable       |
| rd_en          | std_ulogic                     | read enable             |
| twi_clk        | std_ulogic                     | twi clocking --         |
| twi_phase_gen  | std_ulogic_vector(3 downto 0)  |                         |
| twi_clk_phase  | std_ulogic_vector(3 downto 0)  |                         |
| twi_clk_halt   | std_ulogic                     | twi clock stretching -- |
| ctrl           | std_ulogic_vector(7 downto 0)  | unit's control register |
| arbiter        | std_ulogic_vector(2 downto 0)  |                         |
| twi_bitcnt     | std_ulogic_vector(3 downto 0)  |                         |
| twi_rtx_sreg   | std_ulogic_vector(8 downto 0)  | main rx/tx shift reg    |
| twi_sda_i_ff0  | std_ulogic                     | sda input sync          |
|  twi_sda_i_ff1 | std_ulogic                     | sda input sync          |
| twi_scl_i_ff0  | std_ulogic                     | sda input sync          |
|  twi_scl_i_ff1 | std_ulogic                     | sda input sync          |
| twi_sda_i      | std_ulogic                     |                         |
|      twi_sda_o | std_ulogic                     |                         |
| twi_scl_i      | std_ulogic                     |                         |
|      twi_scl_o | std_ulogic                     |                         |
## Constants

| Name              | Type    | Value                      | Description                                      |
| ----------------- | ------- | -------------------------- | ------------------------------------------------ |
| hi_abb_c          | natural |  index_size_f(io_size_c)-1 | high address boundary bit                        |
| lo_abb_c          | natural |  index_size_f(twi_size_c)  | low address boundary bit                         |
| ctrl_twi_en_c     | natural |  0                         | r/w: TWI enable                                  |
| ctrl_twi_start_c  | natural |  1                         | -/w: Generate START condition                    |
| ctrl_twi_stop_c   | natural |  2                         | -/w: Generate STOP condition                     |
| ctrl_twi_prsc0_c  | natural |  3                         | r/w: CLK prsc bit 0                              |
| ctrl_twi_prsc1_c  | natural |  4                         | r/w: CLK prsc bit 1                              |
| ctrl_twi_prsc2_c  | natural |  5                         | r/w: CLK prsc bit 2                              |
| ctrl_twi_mack_c   | natural |  6                         | r/w: generate ACK by controller for transmission |
| ctrl_twi_cksten_c | natural |  7                         | r/w: enable clock stretching by peripheral       |
| ctrl_twi_ack_c    | natural |  30                        | r/-: Set if ACK received                         |
| ctrl_twi_busy_c   | natural |  31                        | r/-: Set if TWI unit is busy                     |
## Processes
- rw_access: ( clk_i )
**Description**
Read/Write Access ----------------------------------------------------------------------
-------------------------------------------------------------------------------------------

- clock_phase_gen: ( clk_i )
**Description**
generate four non-overlapping clock ticks at twi_clk/4 --

- twi_rtx_unit: ( clk_i )
**Description**
last step
TWI Transceiver ------------------------------------------------------------------------
-------------------------------------------------------------------------------------------

- clock_stretching: ( ctrl, arbiter, twi_scl_o, twi_scl_i_ff1 )
**Description**
Clock Stretching Detector --------------------------------------------------------------
-------------------------------------------------------------------------------------------

