# Entity: neorv32_pwm

- **File**: neorv32_pwm.vhd
## Diagram

![Diagram](neorv32_pwm.svg "Diagram")
## Description

 #################################################################################################
 # << NEORV32 - Pulse Width Modulation Controller (PWM) >>                                       #
 # ********************************************************************************************* #
 # Simple PWM controller with 8 bit resolution for the duty cycle and programmable base          #
 # frequency. The controller supports up to 60 PWM channels.                                     #
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

| Generic name | Type    | Value | Description                     |
| ------------ | ------- | ----- | ------------------------------- |
| NUM_CHANNELS | natural |       |  number of PWM channels (0..60) |
## Ports

| Port name   | Direction | Type                                       | Description             |
| ----------- | --------- | ------------------------------------------ | ----------------------- |
| clk_i       | in        | std_ulogic                                 |  global clock line      |
| addr_i      | in        | std_ulogic_vector(31 downto 0)             |  address                |
| rden_i      | in        | std_ulogic                                 |  read enable            |
| wren_i      | in        | std_ulogic                                 |  write enable           |
| data_i      | in        | std_ulogic_vector(31 downto 0)             |  data in                |
| data_o      | out       | std_ulogic_vector(31 downto 0)             |  data out               |
| ack_o       | out       | std_ulogic                                 |  transfer acknowledge   |
| clkgen_en_o | out       | std_ulogic                                 |  enable clock generator |
| clkgen_i    | in        | std_ulogic_vector(07 downto 0)             |                         |
| pwm_o       | out       | std_ulogic_vector(NUM_CHANNELS-1 downto 0) | pwm output channels --  |
## Signals

| Name      | Type                           | Description                    |
| --------- | ------------------------------ | ------------------------------ |
| acc_en    | std_ulogic                     |  module access enable          |
| addr      | std_ulogic_vector(31 downto 0) |  access address                |
| wren      | std_ulogic                     |  write enable                  |
| rden      | std_ulogic                     |  read enable                   |
| pwm_ch    | pwm_ch_t                       |  duty cycle (r/w)              |
| enable    | std_ulogic                     |  enable unit (r/w)             |
| prsc      | std_ulogic_vector(2 downto 0)  |  clock prescaler (r/w)         |
| pwm_ch_rd | pwm_ch_rd_t                    |  duty cycle read-back          |
| prsc_tick | std_ulogic                     |  prescaler clock generator --  |
| pwm_cnt   | std_ulogic_vector(7 downto 0)  |  pwm core counter --           |
## Constants

| Name             | Type    | Value                      | Description                  |
| ---------------- | ------- | -------------------------- | ---------------------------- |
| hi_abb_c         | natural |  index_size_f(io_size_c)-1 |  high address boundary bit   |
| lo_abb_c         | natural |  index_size_f(pwm_size_c)  |  low address boundary bit    |
| ctrl_enable_c    | natural |  0                         |  r/w: PWM enable             |
| ctrl_prsc0_bit_c | natural |  1                         |  r/w: prescaler select bit 0 |
| ctrl_prsc1_bit_c | natural |  2                         |  r/w: prescaler select bit 1 |
| ctrl_prsc2_bit_c | natural |  3                         |  r/w: prescaler select bit 2 |
## Types

| Name        | Type | Description          |
| ----------- | ---- | -------------------- |
| pwm_ch_t    |      |  accessible regs --  |
| pwm_ch_rd_t |      |                      |
## Processes
- wr_access: ( clk_i )
</br>**Description**
 Write access ---------------------------------------------------------------------------  ------------------------------------------------------------------------------------------- 
- pwm_dc_rd_gen: ( pwm_ch )
</br>**Description**
 duty cycle read-back -- 
- pwm_core: ( clk_i )
</br>**Description**
 PWM Core -------------------------------------------------------------------------------  ------------------------------------------------------------------------------------------- 
