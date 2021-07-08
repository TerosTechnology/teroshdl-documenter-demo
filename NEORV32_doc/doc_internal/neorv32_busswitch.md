# Entity: neorv32_busswitch

## Diagram

![Diagram](neorv32_busswitch.svg "Diagram")
## Description

#################################################################################################
# << NEORV32 - Bus Switch >>                                                                    #
# ********************************************************************************************* #
# Allows to access a single peripheral bus ("p_bus") by two controller busses. Controller port  #
# A ("ca_bus") has priority over controller port B ("cb_bus").                                  #
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

| Generic name      | Type    | Value | Description                           |
| ----------------- | ------- | ----- | ------------------------------------- |
| PORT_CA_READ_ONLY | boolean | false | set if controller port A is read-only |
| PORT_CB_READ_ONLY | boolean | false | set if controller port B is read-only |
## Ports

| Port name      | Direction | Type                                       | Description                     |
| -------------- | --------- | ------------------------------------------ | ------------------------------- |
| clk_i          | in        | std_ulogic                                 | global clock, rising edge       |
| rstn_i         | in        | std_ulogic                                 | global reset, low-active, async |
| ca_bus_addr_i  | in        | std_ulogic_vector(data_width_c-1 downto 0) | bus access address              |
| ca_bus_rdata_o | out       | std_ulogic_vector(data_width_c-1 downto 0) | bus read data                   |
| ca_bus_wdata_i | in        | std_ulogic_vector(data_width_c-1 downto 0) | bus write data                  |
| ca_bus_ben_i   | in        | std_ulogic_vector(03 downto 0)             | byte enable                     |
| ca_bus_we_i    | in        | std_ulogic                                 | write enable                    |
| ca_bus_re_i    | in        | std_ulogic                                 | read enable                     |
| ca_bus_lock_i  | in        | std_ulogic                                 | exclusive access request        |
| ca_bus_ack_o   | out       | std_ulogic                                 | bus transfer acknowledge        |
| ca_bus_err_o   | out       | std_ulogic                                 | bus transfer error              |
| cb_bus_addr_i  | in        | std_ulogic_vector(data_width_c-1 downto 0) | bus access address              |
| cb_bus_rdata_o | out       | std_ulogic_vector(data_width_c-1 downto 0) | bus read data                   |
| cb_bus_wdata_i | in        | std_ulogic_vector(data_width_c-1 downto 0) | bus write data                  |
| cb_bus_ben_i   | in        | std_ulogic_vector(03 downto 0)             | byte enable                     |
| cb_bus_we_i    | in        | std_ulogic                                 | write enable                    |
| cb_bus_re_i    | in        | std_ulogic                                 | read enable                     |
| cb_bus_lock_i  | in        | std_ulogic                                 | exclusive access request        |
| cb_bus_ack_o   | out       | std_ulogic                                 | bus transfer acknowledge        |
| cb_bus_err_o   | out       | std_ulogic                                 | bus transfer error              |
| p_bus_src_o    | out       | std_ulogic                                 | access source: 0 = A, 1 = B     |
| p_bus_addr_o   | out       | std_ulogic_vector(data_width_c-1 downto 0) | bus access address              |
| p_bus_rdata_i  | in        | std_ulogic_vector(data_width_c-1 downto 0) | bus read data                   |
| p_bus_wdata_o  | out       | std_ulogic_vector(data_width_c-1 downto 0) | bus write data                  |
| p_bus_ben_o    | out       | std_ulogic_vector(03 downto 0)             | byte enable                     |
| p_bus_we_o     | out       | std_ulogic                                 | write enable                    |
| p_bus_re_o     | out       | std_ulogic                                 | read enable                     |
| p_bus_lock_o   | out       | std_ulogic                                 | exclusive access request        |
| p_bus_ack_i    | in        | std_ulogic                                 | bus transfer acknowledge        |
| p_bus_err_i    | in        | std_ulogic                                 | bus transfer error              |
## Signals

| Name             | Type       | Description           |
| ---------------- | ---------- | --------------------- |
| ca_rd_req_buf    | std_ulogic |                       |
|   ca_wr_req_buf  | std_ulogic |                       |
| cb_rd_req_buf    | std_ulogic |                       |
|   cb_wr_req_buf  | std_ulogic |                       |
| ca_req_current   | std_ulogic |                       |
|  ca_req_buffered | std_ulogic |                       |
| cb_req_current   | std_ulogic |                       |
|  cb_req_buffered | std_ulogic |                       |
| ca_bus_ack       | std_ulogic | internal bus lines -- |
|  cb_bus_ack      | std_ulogic | internal bus lines -- |
| ca_bus_err       | std_ulogic |                       |
|  cb_bus_err      | std_ulogic |                       |
| p_bus_we         | std_ulogic |                       |
|    p_bus_re      | std_ulogic |                       |
| arbiter          | arbiter_t  |                       |
## Types

| Name            | Type                                                                                                                                                                                                  | Description       |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| arbiter_state_t | (IDLE,<br><span style="padding-left:20px"> BUSY,<br><span style="padding-left:20px"> RETIRE,<br><span style="padding-left:20px"> BUSY_SWITCHED,<br><span style="padding-left:20px"> RETIRE_SWITCHED)  | access arbiter -- |
| arbiter_t       |                                                                                                                                                                                                       |                   |
## Processes
- access_buffer: ( rstn_i, clk_i )
- arbiter_sync: ( rstn_i, clk_i )
**Description**
Access Arbiter Sync --------------------------------------------------------------------
-------------------------------------------------------------------------------------------
for registers that require a specific reset state --

- arbiter_comb: ( arbiter, ca_req_current, cb_req_current, ca_req_buffered, cb_req_buffered,
                        ca_rd_req_buf, ca_wr_req_buf, cb_rd_req_buf, cb_wr_req_buf, p_bus_ack_i, p_bus_err_i )
**Description**
Peripheral Bus Arbiter -----------------------------------------------------------------
-------------------------------------------------------------------------------------------

