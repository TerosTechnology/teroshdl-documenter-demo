# Entity: neorv32_mtime

- **File**: neorv32_mtime.vhd
## Diagram

![Diagram](neorv32_mtime.svg "Diagram")
## Description

#################################################################################################
# << NEORV32 - Machine System Timer (MTIME) >>                                                  #
# ********************************************************************************************* #
# Compatible to RISC-V spec's 64-bit MACHINE system timer including "mtime[h]" & "mtimecmp[h]". #
# Note: The 64-bit counter and compare systems are de-coupled into two 32-bit systems.          #
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

| Port name | Direction | Type                           | Description          |
| --------- | --------- | ------------------------------ | -------------------- |
| clk_i     | in        | std_ulogic                     | global clock line    |
| addr_i    | in        | std_ulogic_vector(31 downto 0) | address              |
| rden_i    | in        | std_ulogic                     | read enable          |
| wren_i    | in        | std_ulogic                     | write enable         |
| data_i    | in        | std_ulogic_vector(31 downto 0) | data in              |
| data_o    | out       | std_ulogic_vector(31 downto 0) | data out             |
| ack_o     | out       | std_ulogic                     | transfer acknowledge |
| time_o    | out       | std_ulogic_vector(63 downto 0) | current system time  |
| irq_o     | out       | std_ulogic                     | interrupt request    |
## Signals

| Name          | Type                           | Description                   |
| ------------- | ------------------------------ | ----------------------------- |
| acc_en        | std_ulogic                     | module access enable          |
| addr          | std_ulogic_vector(31 downto 0) | access address                |
| wren          | std_ulogic                     | module access enable          |
| mtime_lo_we   | std_ulogic                     | time write access buffer --   |
| mtime_hi_we   | std_ulogic                     |                               |
| mtimecmp_lo   | std_ulogic_vector(31 downto 0) | accessible regs --            |
| mtimecmp_hi   | std_ulogic_vector(31 downto 0) |                               |
| mtime_lo      | std_ulogic_vector(31 downto 0) |                               |
| mtime_lo_nxt  | std_ulogic_vector(32 downto 0) |                               |
| mtime_lo_ovfl | std_ulogic_vector(00 downto 0) |                               |
| mtime_hi      | std_ulogic_vector(31 downto 0) |                               |
| cmp_lo        | std_ulogic                     | comparator and IRQ trigger -- |
| cmp_lo_ff     | std_ulogic                     |                               |
| cmp_hi        | std_ulogic                     |                               |
| cmp_match_ff  | std_ulogic                     |                               |
## Constants

| Name     | Type    | Value                       | Description               |
| -------- | ------- | --------------------------- | ------------------------- |
| hi_abb_c | natural |  index_size_f(io_size_c)-1  | high address boundary bit |
| lo_abb_c | natural |  index_size_f(mtime_size_c) | low address boundary bit  |
## Processes
- wr_access: ( clk_i )
**Description**
Write Access ---------------------------------------------------------------------------
-------------------------------------------------------------------------------------------

- rd_access: ( clk_i )
**Description**
Read Access ----------------------------------------------------------------------------
-------------------------------------------------------------------------------------------

- cmp_sync: ( clk_i )
**Description**
Comparator -----------------------------------------------------------------------------
-------------------------------------------------------------------------------------------

