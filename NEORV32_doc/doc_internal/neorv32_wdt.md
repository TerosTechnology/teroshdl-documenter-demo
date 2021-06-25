# Entity: neorv32_wdt
## Diagram
![Diagram](neorv32_wdt.svg "Diagram")
## Description
#################################################################################################
# << NEORV32 - Watch Dog Timer (WDT) >>                                                         #
# ********************************************************************************************* #
# Watchdog counter to trigger an action if the CPU gets stuck.                                  #
# The internal counter is 20-bit wide. If this counter overflows one of two possible actions is #
# triggered: Generate an IRQ or force a hardware reset of the system.                           #
# A WDT action can also be triggered manually at any time by setting the FORCE bit.             #
#                                                                                               #
# Access to the control register can be permanently locked by setting the lock bit. This bit    #
# can only be cleared by a hardware reset (external or caused by the watchdog itself).          #
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
| Port name   | Direction | Type                           | Description                             |
| ----------- | --------- | ------------------------------ | --------------------------------------- |
| clk_i       | in        | std_ulogic                     | global clock line                       |
| rstn_i      | in        | std_ulogic                     | global reset line, low-active           |
| addr_i      | in        | std_ulogic_vector(31 downto 0) | address                                 |
| rden_i      | in        | std_ulogic                     | read enable                             |
| wren_i      | in        | std_ulogic                     | write enable                            |
| data_i      | in        | std_ulogic_vector(31 downto 0) | data in                                 |
| data_o      | out       | std_ulogic_vector(31 downto 0) | data out                                |
| ack_o       | out       | std_ulogic                     | transfer acknowledge                    |
| clkgen_en_o | out       | std_ulogic                     | enable clock generator                  |
| clkgen_i    | in        | std_ulogic_vector(07 downto 0) |                                         |
| irq_o       | out       | std_ulogic                     | timeout IRQ                             |
| rstn_o      | out       | std_ulogic                     | timeout reset, low_active, use as async |
## Signals
| Name      | Type                           | Description                          |
| --------- | ------------------------------ | ------------------------------------ |
| acc_en    | std_ulogic                     | module access enable                 |
| wren      | std_ulogic                     |                                      |
| rden      | std_ulogic                     |                                      |
| ctrl_reg  | ctrl_reg_t                     |                                      |
| prsc_tick | std_ulogic                     | prescaler clock generator --         |
| wdt_cnt   | std_ulogic_vector(20 downto 0) | WDT core --                          |
| hw_rst    | std_ulogic                     |                                      |
| rst_gen   | std_ulogic_vector(03 downto 0) |                                      |
| rstn_sync | std_ulogic                     | internal reset (sync, low-active) -- |
## Constants
| Name           | Type    | Value                      | Description                                                                  |
| -------------- | ------- | -------------------------- | ---------------------------------------------------------------------------- |
| hi_abb_c       | natural |  index_size_f(io_size_c)-1 | high address boundary bit                                                    |
| lo_abb_c       | natural |  index_size_f(wdt_size_c)  | low address boundary bit                                                     |
| ctrl_enable_c  | natural |  0                         | r/w: WDT enable                                                              |
| ctrl_clksel0_c | natural |  1                         | r/w: prescaler select bit 0                                                  |
| ctrl_clksel1_c | natural |  2                         | r/w: prescaler select bit 1                                                  |
| ctrl_clksel2_c | natural |  3                         | r/w: prescaler select bit 2                                                  |
| ctrl_mode_c    | natural |  4                         | r/w: 0: WDT timeout triggers interrupt, 1: WDT timeout triggers hard reset   |
| ctrl_rcause_c  | natural |  5                         | r/-: cause of last action (reset/IRQ): 0=external reset, 1=watchdog overflow |
| ctrl_reset_c   | natural |  6                         | -/w: reset WDT if set                                                        |
| ctrl_force_c   | natural |  7                         | -/w: force WDT action                                                        |
| ctrl_lock_c    | natural |  8                         | r/w: lock access to control register when set                                |
## Types
| Name       | Type | Description         |
| ---------- | ---- | ------------------- |
| ctrl_reg_t |      | control register -- |
## Processes
- write_access: _( rstn_i, clk_i )_
Write Access ---------------------------------------------------------------------------
-------------------------------------------------------------------------------------------

**Description**
Write Access ---------------------------------------------------------------------------
-------------------------------------------------------------------------------------------

- wdt_counter: _( clk_i )_
clock enable tick
Watchdog Counter -----------------------------------------------------------------------
-------------------------------------------------------------------------------------------

**Description**
clock enable tick
Watchdog Counter -----------------------------------------------------------------------
-------------------------------------------------------------------------------------------

- reset_generator: _( rstn_i, clk_i )_
mode 1: RESET
Reset Generator & Action Cause Indicator -----------------------------------------------
-------------------------------------------------------------------------------------------

**Description**
mode 1: RESET
Reset Generator & Action Cause Indicator -----------------------------------------------
-------------------------------------------------------------------------------------------

- read_access: _( clk_i )_
Read Access ----------------------------------------------------------------------------
-------------------------------------------------------------------------------------------

**Description**
Read Access ----------------------------------------------------------------------------
-------------------------------------------------------------------------------------------

