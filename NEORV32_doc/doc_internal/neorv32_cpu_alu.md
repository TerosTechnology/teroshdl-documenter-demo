# Entity: neorv32_cpu_alu

- **File**: neorv32_cpu_alu.vhd
## Diagram

![Diagram](neorv32_cpu_alu.svg "Diagram")
## Description

#################################################################################################
# << NEORV32 - Arithmetical/Logical Unit >>                                                     #
# ********************************************************************************************* #
# Main data and address ALU and co-processor interface/arbiter.                                 #
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

| Generic name              | Type    | Value | Description                                                |
| ------------------------- | ------- | ----- | ---------------------------------------------------------- |
| CPU_EXTENSION_RISCV_M     | boolean | false | implement mul/div extension?                               |
| CPU_EXTENSION_RISCV_Zmmul | boolean | false | implement multiply-only M sub-extension?                   |
| CPU_EXTENSION_RISCV_Zfinx | boolean | false | implement 32-bit floating-point extension (using INT reg!) |
| FAST_MUL_EN               | boolean | false | use DSPs for M extension's multiplier                      |
| FAST_SHIFT_EN             | boolean | false | use barrel shifter for shift operations                    |
## Ports

| Port name   | Direction | Type                                       | Description                      |
| ----------- | --------- | ------------------------------------------ | -------------------------------- |
| clk_i       | in        | std_ulogic                                 | global clock, rising edge        |
| rstn_i      | in        | std_ulogic                                 | global reset, low-active, async  |
| ctrl_i      | in        | std_ulogic_vector(ctrl_width_c-1 downto 0) | main control bus                 |
| rs1_i       | in        | std_ulogic_vector(data_width_c-1 downto 0) | rf source 1                      |
| rs2_i       | in        | std_ulogic_vector(data_width_c-1 downto 0) | rf source 2                      |
| pc2_i       | in        | std_ulogic_vector(data_width_c-1 downto 0) | delayed PC                       |
| imm_i       | in        | std_ulogic_vector(data_width_c-1 downto 0) | immediate                        |
| csr_i       | in        | std_ulogic_vector(data_width_c-1 downto 0) | CSR read data                    |
| cmp_i       | in        | std_ulogic_vector(1 downto 0)              | comparator status                |
| res_o       | out       | std_ulogic_vector(data_width_c-1 downto 0) | ALU result                       |
| add_o       | out       | std_ulogic_vector(data_width_c-1 downto 0) | address computation result       |
| fpu_flags_o | out       | std_ulogic_vector(4 downto 0)              | FPU exception flags              |
| idone_o     | out       | std_ulogic                                 | iterative processing units done? |
## Signals

| Name       | Type                                       | Description            |
| ---------- | ------------------------------------------ | ---------------------- |
| opa        | std_ulogic_vector(data_width_c-1 downto 0) |                        |
|  opb       | std_ulogic_vector(data_width_c-1 downto 0) |                        |
| addsub_res | std_ulogic_vector(data_width_c downto 0)   | results --             |
| cp_res     | std_ulogic_vector(data_width_c-1 downto 0) |                        |
| arith_res  | std_ulogic_vector(data_width_c-1 downto 0) |                        |
| logic_res  | std_ulogic_vector(data_width_c-1 downto 0) |                        |
| cp_ctrl    | cp_ctrl_t                                  |                        |
| cp_start   | std_ulogic_vector(3 downto 0)              | trigger co-processor i |
| cp_valid   | std_ulogic_vector(3 downto 0)              | co-processor i done    |
| cp_result  | cp_data_if_t                               |                        |
## Types

| Name      | Type | Description                           |
| --------- | ---- | ------------------------------------- |
| cp_ctrl_t |      | co-processor arbiter and interface -- |
## Processes
- binary_arithmetic_core: ( ctrl_i, opa, opb )
**Description**
operand b (second ALU input operand)
Binary Adder/Subtracter ----------------------------------------------------------------
-------------------------------------------------------------------------------------------

- arithmetic_core: ( ctrl_i, addsub_res )
**Description**
ALU arithmetic logic core --

- cp_arbiter: ( rstn_i, clk_i )
**Description**
Co-Processor Arbiter -------------------------------------------------------------------
-------------------------------------------------------------------------------------------
Interface:
Co-processor "valid" signal has to be asserted (for one cycle) one cycle before asserting output data
Co-processor "output data" has to be always zero unless co-processor was explicitly triggered

- alu_logic_core: ( ctrl_i, rs1_i, opb )
**Description**
ALU Logic Core -------------------------------------------------------------------------
-------------------------------------------------------------------------------------------

- alu_function_mux: ( ctrl_i, arith_res, logic_res, csr_i, cp_res )
**Description**
ALU Function Select --------------------------------------------------------------------
-------------------------------------------------------------------------------------------

## Instantiations

- neorv32_cpu_cp_shifter_inst: neorv32_cpu_cp_shifter
**Description**
**************************************************************************************************************************
Co-Processors
**************************************************************************************************************************
Co-Processor 0: Shifter (CPU Core ISA) --------------------------------------------------
-------------------------------------------------------------------------------------------

