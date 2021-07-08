# Entity: neorv32_cpu_cp_shifter

## Diagram

![Diagram](neorv32_cpu_cp_shifter.svg "Diagram")
## Description

#################################################################################################
# << NEORV32 - CPU Co-Processor: Shifter (CPU Core ISA) >>                                      #
# ********************************************************************************************* #
# Bit-shift unit for base ISA.                                                                  #
# FAST_SHIFT_EN = false (default): Use bit-serial shifter architecture (small but slow)         #
# FAST_SHIFT_EN = true: Use barrel shifter architecture (large but fast)                        #
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
| FAST_SHIFT_EN | boolean | false | use barrel shifter for shift operations |
## Ports

| Port name | Direction | Type                                       | Description                     |
| --------- | --------- | ------------------------------------------ | ------------------------------- |
| clk_i     | in        | std_ulogic                                 | global clock, rising edge       |
| rstn_i    | in        | std_ulogic                                 | global reset, low-active, async |
| ctrl_i    | in        | std_ulogic_vector(ctrl_width_c-1 downto 0) | main control bus                |
| start_i   | in        | std_ulogic                                 | trigger operation               |
| rs1_i     | in        | std_ulogic_vector(data_width_c-1 downto 0) | rf source 1                     |
| rs2_i     | in        | std_ulogic_vector(data_width_c-1 downto 0) | rf source 2                     |
| imm_i     | in        | std_ulogic_vector(data_width_c-1 downto 0) | immediate                       |
| res_o     | out       | std_ulogic_vector(data_width_c-1 downto 0) | operation result                |
| valid_o   | out       | std_ulogic                                 | data output valid               |
## Signals

| Name         | Type                                                     | Description |
| ------------ | -------------------------------------------------------- | ----------- |
| shift_amount | std_ulogic_vector(index_size_f(data_width_c)-1 downto 0) |             |
| shifter      | shifter_t                                                |             |
| bs_level     | bs_level_t                                               |             |
| bs_result    | std_ulogic_vector(data_width_c-1 downto 0)               |             |
## Types

| Name       | Type | Description       |
| ---------- | ---- | ----------------- |
| shifter_t  |      | serial shifter -- |
| bs_level_t |      | barrel shifter -- |
