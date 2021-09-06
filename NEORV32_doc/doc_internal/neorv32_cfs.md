# Entity: neorv32_cfs

- **File**: neorv32_cfs.vhd
## Diagram

![Diagram](neorv32_cfs.svg "Diagram")
## Description

 #################################################################################################
 # << NEORV32 - Custom Functions Subsystem (CFS) >>                                              #
 # ********************************************************************************************* #
 # For tightly-coupled custom co-processors. Provides 32x32-bit memory-mapped registers.         #
 # This is just an "example/illustrating template". Modify this file to implement your custom    #
 # design logic.                                                                                 #
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

| Generic name | Type                           | Value | Description                         |
| ------------ | ------------------------------ | ----- | ----------------------------------- |
| CFS_CONFIG   | std_ulogic_vector(31 downto 0) |       |  custom CFS configuration generic   |
| CFS_IN_SIZE  | positive                       |       |  size of CFS input conduit in bits  |
| CFS_OUT_SIZE | positive                       |       |  size of CFS output conduit in bits |
## Ports

| Port name   | Direction | Type                                       | Description                                  |
| ----------- | --------- | ------------------------------------------ | -------------------------------------------- |
| clk_i       | in        | std_ulogic                                 |  global clock line                           |
| rstn_i      | in        | std_ulogic                                 |  global reset line, low-active, use as async |
| addr_i      | in        | std_ulogic_vector(31 downto 0)             |  address                                     |
| rden_i      | in        | std_ulogic                                 |  read enable                                 |
| wren_i      | in        | std_ulogic                                 |  word write enable                           |
| data_i      | in        | std_ulogic_vector(31 downto 0)             |  data in                                     |
| data_o      | out       | std_ulogic_vector(31 downto 0)             |  data out                                    |
| ack_o       | out       | std_ulogic                                 |  transfer acknowledge                        |
| clkgen_en_o | out       | std_ulogic                                 |  enable clock generator                      |
| clkgen_i    | in        | std_ulogic_vector(07 downto 0)             |  "clock" inputs                              |
| sleep_i     | in        | std_ulogic                                 |  set if cpu is in sleep mode                 |
| irq_o       | out       | std_ulogic                                 |  interrupt request                           |
| cfs_in_i    | in        | std_ulogic_vector(CFS_IN_SIZE-1 downto 0)  |  custom inputs                               |
| cfs_out_o   | out       | std_ulogic_vector(CFS_OUT_SIZE-1 downto 0) |  custom outputs                              |
## Signals

| Name       | Type                           | Description                             |
| ---------- | ------------------------------ | --------------------------------------- |
| acc_en     | std_ulogic                     |  module access enable                   |
| addr       | std_ulogic_vector(31 downto 0) |  access address                         |
| wren       | std_ulogic                     |  word write enable                      |
| rden       | std_ulogic                     |  read enable                            |
| cfs_reg_wr | cfs_regs_t                     |  interface registers for WRITE accesses |
| cfs_reg_rd | cfs_regs_t                     |                                         |
## Constants

| Name     | Type    | Value                      | Description                |
| -------- | ------- | -------------------------- | -------------------------- |
| hi_abb_c | natural |  index_size_f(io_size_c)-1 |  high address boundary bit |
| lo_abb_c | natural |  index_size_f(cfs_size_c)  |  low address boundary bit  |
## Types

| Name       | Type | Description                                  |
| ---------- | ---- | -------------------------------------------- |
| cfs_regs_t |      |  just implement 4 registers for this example |
## Processes
- host_access: ( clk_i )
**Description**
 not used for this minimal example  Read/Write Access ----------------------------------------------------------------------  -------------------------------------------------------------------------------------------  Here we are reading/writing from/to the interface registers of the module. Please note that the peripheral/IO  modules of the NEORV32 can only be written in full word mode (32-bit). Any other write access (half-word or byte)  will trigger a store bus access fault exception.<br>  The CFS provides up to 32 memory-mapped 32-bit interface register. For instance, these could be used to provide  a <control register> for global control of the unit, a <data register> for reading/writing from/to a data FIFO, a <command register>  for issuing commands and a <status register> for status information.<br>  Following the interface protocol, each read or write access has to be acknowledged in the following cycle using the ack_o signal (or even later  if the module needs additional time; the maximum latency until an unacknowledged access will trigger a bus exception is defined via the package's  global "bus_timeout_c" constant). If no ACK is generated, the bus access will time out and cause a store bus access fault exception.  Host access: Read and write access to the interface registers + bus transfer acknowledge.  This example only implements four physical r/w register (the four lowest CF register). The remaining addresses of the CFS are not  associated with any writable or readable register - an access to those is simply ignored but still acknowledged. 
- cfs_core: ( cfs_reg_wr )
**Description**
 CFS Function Core ----------------------------------------------------------------------  -------------------------------------------------------------------------------------------  This is where the actual functionality can be implemented.  In this example we are just implementing four r/w registers that invert any value written to them. 
