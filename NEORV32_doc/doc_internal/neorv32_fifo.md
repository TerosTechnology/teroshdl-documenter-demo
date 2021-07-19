# Entity: neorv32_fifo

- **File**: neorv32_fifo.vhd
## Diagram

![Diagram](neorv32_fifo.svg "Diagram")
## Description

#################################################################################################
# << NEORV32 - General Purpose FIFO Component >>                                                #
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

| Generic name | Type    | Value | Description                                             |
| ------------ | ------- | ----- | ------------------------------------------------------- |
| FIFO_DEPTH   | natural | 4     | number of fifo entries; has to be a power of two; min 1 |
| FIFO_WIDTH   | natural | 32    | size of data elements in fifo                           |
| FIFO_RSYNC   | boolean | false | false = async read; true = sync read                    |
| FIFO_SAFE    | boolean | false | true = allow read/write only if entry available         |
## Ports

| Port name | Direction | Type                                                 | Description                         |
| --------- | --------- | ---------------------------------------------------- | ----------------------------------- |
| clk_i     | in        | std_ulogic                                           | clock, rising edge                  |
| rstn_i    | in        | std_ulogic                                           | async reset, low-active             |
| clear_i   | in        | std_ulogic                                           | sync reset, high-active             |
| level_o   | out       | std_ulogic_vector(index_size_f(FIFO_DEPTH) downto 0) | fill level                          |
| wdata_i   | in        | std_ulogic_vector(FIFO_WIDTH-1 downto 0)             | write data                          |
| we_i      | in        | std_ulogic                                           | write enable                        |
| free_o    | out       | std_ulogic                                           | at least one entry is free when set |
| re_i      | in        | std_ulogic                                           | read enable                         |
| rdata_o   | out       | std_ulogic_vector(FIFO_WIDTH-1 downto 0)             | read data                           |
| avail_o   | out       | std_ulogic                                           | data available when set             |
## Signals

| Name | Type   | Description |
| ---- | ------ | ----------- |
| fifo | fifo_t |             |
## Types

| Name        | Type | Description |
| ----------- | ---- | ----------- |
| fifo_data_t |      |             |
| fifo_t      |      |             |
## Processes
- fifo_control: ( rstn_i, clk_i )
**Description**
FIFO Control ---------------------------------------------------------------------------
-------------------------------------------------------------------------------------------

- fifo_memory_write: ( clk_i )
**Description**
FIFO Memory ----------------------------------------------------------------------------
-------------------------------------------------------------------------------------------

