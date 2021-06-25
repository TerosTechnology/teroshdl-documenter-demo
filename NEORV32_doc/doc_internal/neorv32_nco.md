# Entity: neorv32_nco
## Diagram
![Diagram](neorv32_nco.svg "Diagram")
## Description
#################################################################################################
# << NEORV32 - Number-Controlled Oscillator (NCO) >>                                            #
# ********************************************************************************************* #
# Arbitrary frequency generator based on a number-controlled oscillator (NCO) core with three   #
# independent channels. The phase accumulators and the tuning words are 20-bit wide (+1 bit for #
# the accumulator to detect overflows). See data sheet for more information.                    #
#                                                                                               #
# Output frequency for channel i:                                                               #
# f_out(i) =  (f_cpu / clk_prsc(i)) * (tuning_word(i) / 2^21) * 0.5                             #
# f_cpu       := CPU/processors primary clock                                                   #
# clk_prsc    := 3-bit clock prescaler                                                          #
# tuning_word := channel's 20-bit tuning word                                                   #
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
| Port name   | Direction | Type                           | Description            |
| ----------- | --------- | ------------------------------ | ---------------------- |
| clk_i       | in        | std_ulogic                     | global clock line      |
| addr_i      | in        | std_ulogic_vector(31 downto 0) | address                |
| rden_i      | in        | std_ulogic                     | read enable            |
| wren_i      | in        | std_ulogic                     | write enable           |
| data_i      | in        | std_ulogic_vector(31 downto 0) | data in                |
| data_o      | out       | std_ulogic_vector(31 downto 0) | data out               |
| ack_o       | out       | std_ulogic                     | transfer acknowledge   |
| clkgen_en_o | out       | std_ulogic                     | enable clock generator |
| clkgen_i    | in        | std_ulogic_vector(07 downto 0) |                        |
| nco_o       | out       | std_ulogic_vector(02 downto 0) | NCO output --          |
## Signals
| Name        | Type                                      | Description                |
| ----------- | ----------------------------------------- | -------------------------- |
| acc_en      | std_ulogic                                | module access enable       |
| addr        | std_ulogic_vector(31 downto 0)            | access address             |
| wren        | std_ulogic                                | word write access          |
| rden        | std_ulogic                                | read access                |
| tuning_word | tuning_word_t                             | r/w: tuning word channel i |
| ctrl        | std_ulogic_vector(ctrl_size_c-1 downto 0) | r/w: control register      |
| nco         | nco_core_t                                |                            |
## Constants
| Name                | Type    | Value                              | Description                                             |
| ------------------- | ------- | ---------------------------------- | ------------------------------------------------------- |
| phase_accu_width_c  | natural |  20                                | bits, min=1, max=as much as you like, default=20        |
| num_channels_c      | natural |   3                                | NCO channels, max=3                                     |
| hi_abb_c            | natural |  index_size_f(io_size_c)-1         | high address boundary bit                               |
| lo_abb_c            | natural |  index_size_f(nco_size_c)          | low address boundary bit                                |
| ctrl_en_c           | natural |   0                                | r/w: global NCO enable                                  |
| ctrl_ch0_mode_c     | natural |   1                                | r/w: output mode (0=fixed 50% duty cycle; 1=pulse mode) |
| ctrl_ch0_idle_pol_c | natural |   2                                | r/w: output idle polarity (0=low, 1=high)               |
| ctrl_ch0_oe_c       | natural |   3                                | r/w: enable processor output pin                        |
| ctrl_ch0_output_c   | natural |   4                                | r/-: current channel output state                       |
| ctrl_ch0_prsc0_c    | natural |   5                                | r/w: clock prescaler select bit 0                       |
| ctrl_ch0_prsc1_c    | natural |   6                                | r/w: clock prescaler select bit 1                       |
| ctrl_ch0_prsc2_c    | natural |   7                                | r/w: clock prescaler select bit 2                       |
| ctrl_ch0_pulse0_c   | natural |   8                                | r/w: pulse length select bit 0                          |
| ctrl_ch0_pulse1_c   | natural |   9                                | r/w: pulse length select bit 1                          |
| ctrl_ch0_pulse2_c   | natural |  10                                | r/w: pulse length select bit 2                          |
| ctrl_ch1_mode_c     | natural |  21                                | r/w: output mode (0=fixed 50% duty cycle; 1=pulse mode) |
| ctrl_ch1_idle_pol_c | natural |  22                                | r/w: output idle polarity (0=low, 1=high)               |
| ctrl_ch1_oe_c       | natural |  23                                | r/w: enable processor output pin                        |
| ctrl_ch1_output_c   | natural |  24                                | r/-: current channel output state                       |
| ctrl_ch1_prsc0_c    | natural |  25                                | r/w: clock prescaler select bit 0                       |
| ctrl_ch1_prsc1_c    | natural |  26                                | r/w: clock prescaler select bit 1                       |
| ctrl_ch1_prsc2_c    | natural |  27                                | r/w: clock prescaler select bit 2                       |
| ctrl_ch1_pulse0_c   | natural |  28                                | r/w: pulse length select bit 0                          |
| ctrl_ch1_pulse1_c   | natural |  29                                | r/w: pulse length select bit 1                          |
| ctrl_ch1_pulse2_c   | natural |  20                                | r/w: pulse length select bit 2                          |
| ctrl_ch2_mode_c     | natural |  21                                | r/w: output mode (0=fixed 50% duty cycle; 1=pulse mode) |
| ctrl_ch2_idle_pol_c | natural |  22                                | r/w: output idle polarity (0=low, 1=high)               |
| ctrl_ch2_oe_c       | natural |  23                                | r/w: enable processor output pin                        |
| ctrl_ch2_output_c   | natural |  24                                | r/-: current channel output state                       |
| ctrl_ch2_prsc0_c    | natural |  25                                | r/w: clock prescaler select bit 0                       |
| ctrl_ch2_prsc1_c    | natural |  26                                | r/w: clock prescaler select bit 1                       |
| ctrl_ch2_prsc2_c    | natural |  27                                | r/w: clock prescaler select bit 2                       |
| ctrl_ch2_pulse0_c   | natural |  28                                | r/w: pulse length select bit 0                          |
| ctrl_ch2_pulse1_c   | natural |  29                                | r/w: pulse length select bit 1                          |
| ctrl_ch2_pulse2_c   | natural |  30                                | r/w: pulse length select bit 2                          |
| ctrl_ch_offset_c    | natural |  10                                | number of bits for each channel                         |
| ctrl_size_c         | natural |  num_channels_c*ctrl_ch_offset_c+1 | number of bits in primary control register              |
## Types
| Name          | Type | Description                   |
| ------------- | ---- | ----------------------------- |
| tuning_word_t |      | accessible regs --            |
| nco_sel_t     |      | nco core --                   |
| pulse_cnt_t   |      |                               |
| accu_t        |      | +1 bit for overflow detection |
| nco_core_t    |      |                               |
## Processes
- rw_access: _( clk_i )_
Read/Write Access ----------------------------------------------------------------------
-------------------------------------------------------------------------------------------

**Description**
Read/Write Access ----------------------------------------------------------------------
-------------------------------------------------------------------------------------------

- nco_core: _( clk_i )_
NCO Core -------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------

**Description**
NCO Core -------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------

- pulse_generator: _( clk_i )_
i
Pulse Generator ------------------------------------------------------------------------
-------------------------------------------------------------------------------------------

**Description**
i
Pulse Generator ------------------------------------------------------------------------
-------------------------------------------------------------------------------------------

- output_generator: _( clk_i )_
i
Output Configuration -------------------------------------------------------------------
-------------------------------------------------------------------------------------------

**Description**
i
Output Configuration -------------------------------------------------------------------
-------------------------------------------------------------------------------------------

