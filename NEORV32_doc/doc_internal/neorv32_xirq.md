# Entity: neorv32_xirq

- **File**: neorv32_xirq.vhd
## Diagram

![Diagram](neorv32_xirq.svg "Diagram")
## Description

 #################################################################################################
 # << NEORV32 - External Interrupt Controller (XIRQ) >>                                          #
 # ********************************************************************************************* #
 # Simple interrupt controller for platform (processor-external) interrupts. Up to 32 channels   #
 # are supported that get (optionally) prioritized into a single CPU interrupt.                  #
 #                                                                                               #
 # The actual trigger configuration has to be done before synthesis using the XIRQ_TRIGGER_TYPE  #
 # and XIRQ_TRIGGER_POLARITY generics. These allow to configure channel-independent low-level,   #
 # high-level, falling-edge and rising-edge triggers.                                            #
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

| Generic name          | Type                           | Value | Description                                                           |
| --------------------- | ------------------------------ | ----- | --------------------------------------------------------------------- |
| XIRQ_NUM_CH           | natural                        |       |  number of external IRQ channels (0..32)                              |
| XIRQ_TRIGGER_TYPE     | std_ulogic_vector(31 downto 0) |       |  trigger type: 0=level, 1=edge                                        |
| XIRQ_TRIGGER_POLARITY | std_ulogic_vector(31 downto 0) |       |  trigger polarity: 0=low-level/falling-edge, 1=high-level/rising-edge |
## Ports

| Port name | Direction | Type                                      | Description                 |
| --------- | --------- | ----------------------------------------- | --------------------------- |
| clk_i     | in        | std_ulogic                                |  global clock line          |
| addr_i    | in        | std_ulogic_vector(31 downto 0)            |  address                    |
| rden_i    | in        | std_ulogic                                |  read enable                |
| wren_i    | in        | std_ulogic                                |  write enable               |
| data_i    | in        | std_ulogic_vector(31 downto 0)            |  data in                    |
| data_o    | out       | std_ulogic_vector(31 downto 0)            |  data out                   |
| ack_o     | out       | std_ulogic                                |  transfer acknowledge       |
| xirq_i    | in        | std_ulogic_vector(XIRQ_NUM_CH-1 downto 0) | external interrupt lines -- |
| cpu_irq_o | out       | std_ulogic                                | CPU interrupt --            |
## Signals

| Name         | Type                                      | Description                    |
| ------------ | ----------------------------------------- | ------------------------------ |
| acc_en       | std_ulogic                                |  module access enable          |
| addr         | std_ulogic_vector(31 downto 0)            |  access address                |
| irq_enable   | std_ulogic_vector(XIRQ_NUM_CH-1 downto 0) |  r/w: interrupt enable         |
| clr_pending  | std_ulogic_vector(XIRQ_NUM_CH-1 downto 0) |  (r)/w: clear/ack pending IRQs |
| irq_sync     | std_ulogic_vector(XIRQ_NUM_CH-1 downto 0) |  interrupt trigger --          |
| irq_sync2    | std_ulogic_vector(XIRQ_NUM_CH-1 downto 0) |                                |
| irq_trig     | std_ulogic_vector(XIRQ_NUM_CH-1 downto 0) |                                |
| irq_buf      | std_ulogic_vector(XIRQ_NUM_CH-1 downto 0) |  interrupt buffer --           |
| irq_fire     | std_ulogic                                |                                |
| irq_src      | std_ulogic_vector(04 downto 0)            |  interrupt source --           |
|  irq_src_nxt | std_ulogic_vector(04 downto 0)            |  interrupt source --           |
| irq_run      | std_ulogic                                |  arbiter --                    |
| irq_run_ff   | std_ulogic                                |                                |
| host_ack     | std_ulogic                                |                                |
## Constants

| Name     | Type    | Value                      | Description                |
| -------- | ------- | -------------------------- | -------------------------- |
| hi_abb_c | natural |  index_size_f(io_size_c)-1 |  high address boundary bit |
| lo_abb_c | natural |  index_size_f(xirq_size_c) |  low address boundary bit  |
## Processes
- rw_access: ( clk_i )
</br>**Description**
 word aligned  Read/Write Access ----------------------------------------------------------------------  ------------------------------------------------------------------------------------------- 
- irq_trigger: ( clk_i )
</br>**Description**
 IRQ Trigger --------------------------------------------------------------  ----------------------------------------------------------------------------- 
- irq_trigger_comb: ( irq_sync, irq_sync2 )
- irq_buffer: ( clk_i )
</br>**Description**
 IRQ Buffer ---------------------------------------------------------------  ----------------------------------------------------------------------------- 
- irq_priority: ( irq_buf )
</br>**Description**
 IRQ Priority Encoder -----------------------------------------------------  ----------------------------------------------------------------------------- 
- irq_arbiter: ( clk_i )
</br>**Description**
 IRQ Arbiter --------------------------------------------------------------  ----------------------------------------------------------------------------- 
