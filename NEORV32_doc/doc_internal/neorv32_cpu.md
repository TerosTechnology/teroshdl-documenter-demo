# Entity: neorv32_cpu

- **File**: neorv32_cpu.vhd
## Diagram

![Diagram](neorv32_cpu.svg "Diagram")
## Description

#################################################################################################
# << NEORV32 - CPU Top Entity >>                                                                #
# ********************************************************************************************* #
# NEORV32 CPU:                                                                                  #
# * neorv32_cpu.vhd                   - CPU top entity                                          #
#   * neorv32_cpu_alu.vhd             - Arithmetic/logic unit                                   #
#   * neorv32_cpu_bus.vhd             - Instruction and data bus interface unit                 #
#   * neorv32_cpu_cp_bitmanip.vhd     - Bit-manipulation co-processor ('B')                     #
#   * neorv32_cpu_cp_fpu.vhd          - Single-precision FPU co-processor ('Zfinx')             #
#   * neorv32_cpu_cp_muldiv.vhd       - Integer multiplier/divider co-processor ('M')           #
#   * neorv32_cpu_ctrl.vhd            - CPU control and CSR system                              #
#     * neorv32_cpu_decompressor.vhd  - Compressed instructions decoder                         #
#   * neorv32_cpu_regfile.vhd         - Data register file                                      #
# * neorv32_package.vhd               - Main CPU & Processor package file                       #
#                                                                                               #
# Check out the processor's data sheet for more information: docs/NEORV32.pdf                   #
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

| Generic name                 | Type                           | Value       | Description                                                              |
| ---------------------------- | ------------------------------ | ----------- | ------------------------------------------------------------------------ |
| HW_THREAD_ID                 | natural                        | 0           | hardware thread id (32-bit)                                              |
| CPU_BOOT_ADDR                | std_ulogic_vector(31 downto 0) | x"00000000" | cpu boot address                                                         |
| CPU_DEBUG_ADDR               | std_ulogic_vector(31 downto 0) | x"00000000" | cpu debug mode start address                                             |
| CPU_EXTENSION_RISCV_A        | boolean                        | false       | implement atomic extension?                                              |
| CPU_EXTENSION_RISCV_C        | boolean                        | false       | implement compressed extension?                                          |
| CPU_EXTENSION_RISCV_E        | boolean                        | false       | implement embedded RF extension?                                         |
| CPU_EXTENSION_RISCV_M        | boolean                        | false       | implement muld/div extension?                                            |
| CPU_EXTENSION_RISCV_U        | boolean                        | false       | implement user mode extension?                                           |
| CPU_EXTENSION_RISCV_Zfinx    | boolean                        | false       | implement 32-bit floating-point extension (using INT reg!)               |
| CPU_EXTENSION_RISCV_Zicsr    | boolean                        | true        | implement CSR system?                                                    |
| CPU_EXTENSION_RISCV_Zifencei | boolean                        | false       | implement instruction stream sync.?                                      |
| CPU_EXTENSION_RISCV_Zmmul    | boolean                        | false       | implement multiply-only M sub-extension?                                 |
| CPU_EXTENSION_RISCV_DEBUG    | boolean                        | false       | implement CPU debug mode?                                                |
| FAST_MUL_EN                  | boolean                        | false       | use DSPs for M extension's multiplier                                    |
| FAST_SHIFT_EN                | boolean                        | false       | use barrel shifter for shift operations                                  |
| CPU_CNT_WIDTH                | natural                        | 64          | total width of CPU cycle and instret counters (0..64)                    |
| CPU_IPB_ENTRIES              | natural                        | 2           | entries is instruction prefetch buffer, has to be a power of 2           |
| PMP_NUM_REGIONS              | natural                        | 0           | number of regions (0..64)                                                |
| PMP_MIN_GRANULARITY          | natural                        | 64*1024     | minimal region granularity in bytes, has to be a power of 2, min 8 bytes |
| HPM_NUM_CNTS                 | natural                        | 0           | number of implemented HPM counters (0..29)                               |
| HPM_CNT_WIDTH                | natural                        | 40          | total size of HPM counters (0..64)                                       |
## Ports

| Port name     | Direction | Type                                       | Description                     |
| ------------- | --------- | ------------------------------------------ | ------------------------------- |
| clk_i         | in        | std_ulogic                                 | global clock, rising edge       |
| rstn_i        | in        | std_ulogic                                 | global reset, low-active, async |
| sleep_o       | out       | std_ulogic                                 | cpu is in sleep mode when set   |
| i_bus_addr_o  | out       | std_ulogic_vector(data_width_c-1 downto 0) | bus access address              |
| i_bus_rdata_i | in        | std_ulogic_vector(data_width_c-1 downto 0) | bus read data                   |
| i_bus_wdata_o | out       | std_ulogic_vector(data_width_c-1 downto 0) | bus write data                  |
| i_bus_ben_o   | out       | std_ulogic_vector(03 downto 0)             | byte enable                     |
| i_bus_we_o    | out       | std_ulogic                                 | write enable                    |
| i_bus_re_o    | out       | std_ulogic                                 | read enable                     |
| i_bus_lock_o  | out       | std_ulogic                                 | exclusive access request        |
| i_bus_ack_i   | in        | std_ulogic                                 | bus transfer acknowledge        |
| i_bus_err_i   | in        | std_ulogic                                 | bus transfer error              |
| i_bus_fence_o | out       | std_ulogic                                 | executed FENCEI operation       |
| i_bus_priv_o  | out       | std_ulogic_vector(1 downto 0)              | privilege level                 |
| d_bus_addr_o  | out       | std_ulogic_vector(data_width_c-1 downto 0) | bus access address              |
| d_bus_rdata_i | in        | std_ulogic_vector(data_width_c-1 downto 0) | bus read data                   |
| d_bus_wdata_o | out       | std_ulogic_vector(data_width_c-1 downto 0) | bus write data                  |
| d_bus_ben_o   | out       | std_ulogic_vector(03 downto 0)             | byte enable                     |
| d_bus_we_o    | out       | std_ulogic                                 | write enable                    |
| d_bus_re_o    | out       | std_ulogic                                 | read enable                     |
| d_bus_lock_o  | out       | std_ulogic                                 | exclusive access request        |
| d_bus_ack_i   | in        | std_ulogic                                 | bus transfer acknowledge        |
| d_bus_err_i   | in        | std_ulogic                                 | bus transfer error              |
| d_bus_fence_o | out       | std_ulogic                                 | executed FENCE operation        |
| d_bus_priv_o  | out       | std_ulogic_vector(1 downto 0)              | privilege level                 |
| time_i        | in        | std_ulogic_vector(63 downto 0)             | current system time             |
| nm_irq_i      | in        | std_ulogic                                 | NMI                             |
| msw_irq_i     | in        | std_ulogic                                 | machine software interrupt      |
| mext_irq_i    | in        | std_ulogic                                 | machine external interrupt      |
| mtime_irq_i   | in        | std_ulogic                                 | machine timer interrupt         |
| firq_i        | in        | std_ulogic_vector(15 downto 0)             | fast interrupts (custom) --     |
| db_halt_req_i | in        | std_ulogic                                 | debug mode (halt) request --    |
## Signals

| Name       | Type                                       | Description                                   |
| ---------- | ------------------------------------------ | --------------------------------------------- |
| ctrl       | std_ulogic_vector(ctrl_width_c-1 downto 0) | main control bus                              |
| comparator | std_ulogic_vector(1 downto 0)              | comparator result                             |
| imm        | std_ulogic_vector(data_width_c-1 downto 0) | immediate                                     |
| instr      | std_ulogic_vector(data_width_c-1 downto 0) | new instruction                               |
| rs1        | std_ulogic_vector(data_width_c-1 downto 0) | source registers                              |
|  rs2       | std_ulogic_vector(data_width_c-1 downto 0) | source registers                              |
| alu_res    | std_ulogic_vector(data_width_c-1 downto 0) | alu result                                    |
| alu_add    | std_ulogic_vector(data_width_c-1 downto 0) | alu address result                            |
| mem_rdata  | std_ulogic_vector(data_width_c-1 downto 0) | memory read data                              |
| alu_idone  | std_ulogic                                 | iterative alu operation done                  |
| bus_i_wait | std_ulogic                                 | wait for current bus instruction fetch        |
| bus_d_wait | std_ulogic                                 | wait for current bus data access              |
| csr_rdata  | std_ulogic_vector(data_width_c-1 downto 0) | csr read data                                 |
| mar        | std_ulogic_vector(data_width_c-1 downto 0) | current memory address register               |
| ma_instr   | std_ulogic                                 | misaligned instruction address                |
| ma_load    | std_ulogic                                 | misaligned load data address                  |
| ma_store   | std_ulogic                                 | misaligned store data address                 |
| excl_state | std_ulogic                                 | atomic/exclusive access lock status           |
| be_instr   | std_ulogic                                 | bus error on instruction access               |
| be_load    | std_ulogic                                 | bus error on load data access                 |
| be_store   | std_ulogic                                 | bus error on store data access                |
| fetch_pc   | std_ulogic_vector(data_width_c-1 downto 0) | pc for instruction fetch                      |
| curr_pc    | std_ulogic_vector(data_width_c-1 downto 0) | current pc (for current executed instruction) |
| fpu_flags  | std_ulogic_vector(4 downto 0)              | FPU exception flags                           |
| pmp_addr   | pmp_addr_if_t                              | pmp interface --                              |
| pmp_ctrl   | pmp_ctrl_if_t                              |                                               |
## Instantiations

- neorv32_cpu_control_inst: neorv32_cpu_control
**Description**
Control Unit ---------------------------------------------------------------------------
-------------------------------------------------------------------------------------------

- neorv32_cpu_regfile_inst: neorv32_cpu_regfile
**Description**
set when CPU is sleeping (after WFI)
Register File --------------------------------------------------------------------------
-------------------------------------------------------------------------------------------

- neorv32_cpu_alu_inst: neorv32_cpu_alu
**Description**
ALU ------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------

- neorv32_cpu_bus_inst: neorv32_cpu_bus
**Description**
Bus Interface Unit ---------------------------------------------------------------------
-------------------------------------------------------------------------------------------

