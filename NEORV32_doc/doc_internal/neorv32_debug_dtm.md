# Entity: neorv32_debug_dtm

- **File**: neorv32_debug_dtm.vhd
## Diagram

![Diagram](neorv32_debug_dtm.svg "Diagram")
## Description

 #################################################################################################
 # << NEORV32 - RISC-V Debug Transport Module (DTM) >>                                           #
 # ********************************************************************************************* #
 # Provides a JTAG-compatible TAP to access the DMI register interface.                          #
 # Compatible to the RISC-V debug specification.                                                 #
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
 # https://github.com/stnolting/riscv-debug-dtm                              (c) Stephan Nolting #
 #################################################################################################
## Generics

| Generic name   | Type                           | Value | Description      |
| -------------- | ------------------------------ | ----- | ---------------- |
| IDCODE_VERSION | std_ulogic_vector(03 downto 0) |       |  version         |
| IDCODE_PARTID  | std_ulogic_vector(15 downto 0) |       |  part number     |
| IDCODE_MANID   | std_ulogic_vector(10 downto 0) |       |  manufacturer id |
## Ports

| Port name        | Direction | Type                           | Description                                   |
| ---------------- | --------- | ------------------------------ | --------------------------------------------- |
| clk_i            | in        | std_ulogic                     |  global clock line                            |
| rstn_i           | in        | std_ulogic                     |  global reset line, low-active                |
| jtag_trst_i      | in        | std_ulogic                     | jtag connection --                            |
| jtag_tck_i       | in        | std_ulogic                     |                                               |
| jtag_tdi_i       | in        | std_ulogic                     |                                               |
| jtag_tdo_o       | out       | std_ulogic                     |                                               |
| jtag_tms_i       | in        | std_ulogic                     |                                               |
| dmi_rstn_o       | out       | std_ulogic                     | debug module interface (DMI) --               |
| dmi_req_valid_o  | out       | std_ulogic                     |                                               |
| dmi_req_ready_i  | in        | std_ulogic                     |  DMI is allowed to make new requests when set |
| dmi_req_addr_o   | out       | std_ulogic_vector(06 downto 0) |                                               |
| dmi_req_op_o     | out       | std_ulogic                     |  0=read, 1=write                              |
| dmi_req_data_o   | out       | std_ulogic_vector(31 downto 0) |                                               |
| dmi_resp_valid_i | in        | std_ulogic                     |  response valid when set                      |
| dmi_resp_ready_o | out       | std_ulogic                     |  ready to receive respond                     |
| dmi_resp_data_i  | in        | std_ulogic_vector(31 downto 0) |                                               |
| dmi_resp_err_i   | in        | std_ulogic                     |  0=ok, 1=error                                |
## Signals

| Name     | Type       | Description |
| -------- | ---------- | ----------- |
| tap_ctrl | tap_ctrl_t |             |
| tap_reg  | tap_reg_t  |             |
| dmi_ctrl | dmi_ctrl_t |             |
## Constants

| Name          | Type                           | Value     | Description                     |
| ------------- | ------------------------------ | --------- | ------------------------------- |
| dmi_idle_c    | std_ulogic_vector(02 downto 0) |  "010"    |  minimum number if idle cycles  |
| dmi_version_c | std_ulogic_vector(03 downto 0) |  "0001"   |  version (0.13)                 |
| dmi_abits_c   | std_ulogic_vector(05 downto 0) |  "000111" |  number of DMI address bits (7) |
## Types

| Name             | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Description                 |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------- |
| tap_ctrl_state_t | (LOGIC_RESET,<br><span style="padding-left:20px"> DR_SCAN,<br><span style="padding-left:20px"> DR_CAPTURE,<br><span style="padding-left:20px"> DR_SHIFT,<br><span style="padding-left:20px"> DR_EXIT1,<br><span style="padding-left:20px"> DR_PAUSE,<br><span style="padding-left:20px"> DR_EXIT2,<br><span style="padding-left:20px"> DR_UPDATE,<br><span style="padding-left:20px"> RUN_IDLE,<br><span style="padding-left:20px"> IR_SCAN,<br><span style="padding-left:20px"> IR_CAPTURE,<br><span style="padding-left:20px"> IR_SHIFT,<br><span style="padding-left:20px"> IR_EXIT1,<br><span style="padding-left:20px"> IR_PAUSE,<br><span style="padding-left:20px"> IR_EXIT2,<br><span style="padding-left:20px"> IR_UPDATE)  |  tap controller - fsm --    |
| tap_ctrl_t       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                             |
| tap_reg_t        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  tap registers --           |
| dmi_ctrl_state_t | (DMI_IDLE,<br><span style="padding-left:20px"> DMI_READ_WAIT,<br><span style="padding-left:20px"> DMI_READ,<br><span style="padding-left:20px"> DMI_READ_BUSY,<br><span style="padding-left:20px"> DMI_WRITE_WAIT,<br><span style="padding-left:20px"> DMI_WRITE,<br><span style="padding-left:20px"> DMI_WRITE_BUSY)                                                                                                                                                                                                                                                                                                                                                                                                                |  debug module interface --  |
| dmi_ctrl_t       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                             |
## Processes
- tap_control: ( rstn_i, clk_i )
- reg_access: ( clk_i )
</br>**Description**
 Tap Register Access --------------------------------------------------------------------  ------------------------------------------------------------------------------------------- 
- dmi_controller: ( rstn_i, clk_i )
</br>**Description**
 version  Debug Module Interface Access Register (dmi) -- 
