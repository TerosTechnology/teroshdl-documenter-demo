# Entity: neorv32_ProcessorTop_Test

## Diagram

![Diagram](neorv32_ProcessorTop_Test.svg "Diagram")
## Description

#################################################################################################
# << NEORV32 - Simple Test Setup >>                                                             #
# ********************************************************************************************* #
# This test setup instantiates the NEORV32 processor with a rather small configuration and only #
# propagates the UART and GPIO.out signals to the outer world.                                  #
# Only internal memories are used and the address space for instructions/data is constrained to #
# these memories.                                                                               #
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

| Port name   | Direction | Type                          | Description                     |
| ----------- | --------- | ----------------------------- | ------------------------------- |
| clk_i       | in        | std_ulogic                    | global clock, rising edge       |
| rstn_i      | in        | std_ulogic                    | global reset, low-active, async |
| gpio_o      | out       | std_ulogic_vector(7 downto 0) | parallel output                 |
| uart0_txd_o | out       | std_ulogic                    | UART0 send data                 |
| uart0_rxd_i | in        | std_ulogic                    | UART0 receive data              |
## Signals

| Name     | Type                           | Description |
| -------- | ------------------------------ | ----------- |
| gpio_out | std_ulogic_vector(63 downto 0) |             |
## Instantiations

- neorv32_top_inst: neorv32_top
