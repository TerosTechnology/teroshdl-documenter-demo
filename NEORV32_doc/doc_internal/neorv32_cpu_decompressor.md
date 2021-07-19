# Entity: neorv32_cpu_decompressor

- **File**: neorv32_cpu_decompressor.vhd
## Diagram

![Diagram](neorv32_cpu_decompressor.svg "Diagram")
## Description

#################################################################################################
# << NEORV32 - CPU: Compressed Instructions Decoder (RISC-V "C" Extension) >>                   #
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

| Port name    | Direction | Type                           | Description                          |
| ------------ | --------- | ------------------------------ | ------------------------------------ |
| ci_instr16_i | in        | std_ulogic_vector(15 downto 0) | compressed instruction input         |
| ci_illegal_o | out       | std_ulogic                     | is an illegal compressed instruction |
| ci_instr32_o | out       | std_ulogic_vector(31 downto 0) | 32-bit decompressed instruction      |
## Constants

| Name            | Type    | Value | Description |
| --------------- | ------- | ----- | ----------- |
| ci_opcode_lsb_c | natural |   0   |             |
| ci_opcode_msb_c | natural |   1   |             |
| ci_rd_3_lsb_c   | natural |   2   |             |
| ci_rd_3_msb_c   | natural |   4   |             |
| ci_rd_5_lsb_c   | natural |   7   |             |
| ci_rd_5_msb_c   | natural |  11   |             |
| ci_rs1_3_lsb_c  | natural |   7   |             |
| ci_rs1_3_msb_c  | natural |   9   |             |
| ci_rs1_5_lsb_c  | natural |   7   |             |
| ci_rs1_5_msb_c  | natural |  11   |             |
| ci_rs2_3_lsb_c  | natural |   2   |             |
| ci_rs2_3_msb_c  | natural |   4   |             |
| ci_rs2_5_lsb_c  | natural |   2   |             |
| ci_rs2_5_msb_c  | natural |   6   |             |
| ci_funct3_lsb_c | natural |  13   |             |
| ci_funct3_msb_c | natural |  15   |             |
## Processes
- decompressor: ( ci_instr16_i )
