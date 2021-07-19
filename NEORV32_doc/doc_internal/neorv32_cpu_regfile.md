# Entity: neorv32_cpu_regfile

- **File**: neorv32_cpu_regfile.vhd
## Diagram

![Diagram](neorv32_cpu_regfile.svg "Diagram")
## Description

#################################################################################################
# << NEORV32 - CPU General Purpose Data Register File >>                                        #
# ********************************************************************************************* #
# General purpose data register file. 32 entries (= 1024 bit) for normal mode (RV32I),          #
# 16 entries (= 512 bit) for embedded mode (RV32E) when RISC-V "E" extension is enabled.        #
#                                                                                               #
# Register zero (r0/x0) is a "normal" physical reg that has to be initialized to zero by the    #
# CPU control system. For normal operations register zero cannot be written.                    #
#                                                                                               #
# The register file uses synchronous read accesses and a *single* (multiplexed) address port    #
# for writing and reading rs1 and a single read-only port for rs2. Therefore, the whole         #
# register file can be mapped to a single true dual-port block RAM.                             #
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

| Generic name          | Type    | Value | Description                      |
| --------------------- | ------- | ----- | -------------------------------- |
| CPU_EXTENSION_RISCV_E | boolean | false | implement embedded RF extension? |
## Ports

| Port name | Direction | Type                                       | Description               |
| --------- | --------- | ------------------------------------------ | ------------------------- |
| clk_i     | in        | std_ulogic                                 | global clock, rising edge |
| ctrl_i    | in        | std_ulogic_vector(ctrl_width_c-1 downto 0) | main control bus          |
| mem_i     | in        | std_ulogic_vector(data_width_c-1 downto 0) | memory read data          |
| alu_i     | in        | std_ulogic_vector(data_width_c-1 downto 0) | ALU result                |
| rs1_o     | out       | std_ulogic_vector(data_width_c-1 downto 0) | operand 1                 |
| rs2_o     | out       | std_ulogic_vector(data_width_c-1 downto 0) | operand 2                 |
| cmp_o     | out       | std_ulogic_vector(1 downto 0)              | comparator status         |
## Signals

| Name         | Type                                       | Description            |
| ------------ | ------------------------------------------ | ---------------------- |
| reg_file     | reg_file_t                                 |                        |
| reg_file_emb | reg_file_emb_t                             |                        |
| rf_wdata     | std_ulogic_vector(data_width_c-1 downto 0) | actual write-back data |
| rd_is_r0     | std_ulogic                                 | writing to r0?         |
| rf_we        | std_ulogic                                 |                        |
| dst_addr     | std_ulogic_vector(4 downto 0)              | destination address    |
| opa_addr     | std_ulogic_vector(4 downto 0)              | rs1/dst address        |
| opb_addr     | std_ulogic_vector(4 downto 0)              | rs2 address            |
| rs1          | std_ulogic_vector(data_width_c-1 downto 0) |                        |
|  rs2         | std_ulogic_vector(data_width_c-1 downto 0) |                        |
| cmp_opx      | std_ulogic_vector(data_width_c downto 0)   | comparator --          |
| cmp_opy      | std_ulogic_vector(data_width_c downto 0)   |                        |
## Types

| Name           | Type | Description |
| -------------- | ---- | ----------- |
| reg_file_t     |      |             |
| reg_file_emb_t |      |             |
## Processes
- rf_access: ( clk_i )
**Description**
Register File Access -------------------------------------------------------------------
-------------------------------------------------------------------------------------------

