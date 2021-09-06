# Entity: ethernet_mac

- **File**: ethernet_mac.vhd
## Diagram

![Diagram](ethernet_mac.svg "Diagram")
## Description

================================================================================================================================
 Copyright 2020 Bitvis
 Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.
 You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 and in the provided LICENSE.TXT.

 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
 an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and limitations under the License.
================================================================================================================================
 Note : Any functionality not explicitly described in the documentation is subject to change at any time
--------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------
 Description : See library quick reference (under 'doc') and README-file(s)
-------------------------------------------------------------------------------------------
## Ports

| Port name | Direction | Type                         | Description              |
| --------- | --------- | ---------------------------- | ------------------------ |
| clk       | in        | std_logic                    | SBI interface            |
| sbi_cs    | in        | std_logic                    |                          |
| sbi_addr  | in        | unsigned(7 downto 0)         |                          |
| sbi_rena  | in        | std_logic                    |                          |
| sbi_wena  | in        | std_logic                    |                          |
| sbi_wdata | in        | std_logic_vector(7 downto 0) |                          |
| sbi_ready | out       | std_logic                    |                          |
| sbi_rdata | out       | std_logic_vector(7 downto 0) |                          |
| gtxclk    | out       | std_logic                    | GMII interface (only TX) |
| txd       | out       | std_logic_vector(7 downto 0) |                          |
| txen      | out       | std_logic                    |                          |
## Signals

| Name            | Type                                      | Description |
| --------------- | ----------------------------------------- | ----------- |
| mac_dest_addr   | std_logic_vector(47 downto 0)             |             |
| mac_src_addr    | std_logic_vector(47 downto 0)             |             |
| payload_len     | std_logic_vector(15 downto 0)             |             |
| payload_len_int | integer                                   |             |
| payload         | t_byte_array(0 to C_MAX_PAYLOAD_LENGTH-1) |             |
| dummy_reg       | std_logic_vector(7 downto 0)              |             |
| frame_ready     | std_logic                                 |             |
| frame_sent      | std_logic                                 |             |
| read_ready      | std_logic                                 |             |
| fsm_tx          | t_state                                   |             |
## Types

| Name    | Type                                                      | Description |
| ------- | --------------------------------------------------------- | ----------- |
| t_state | (s_idle,<br><span style="padding-left:20px"> s_send_pkt)  |             |
## Processes
- p_sbi_write_regs: ( clk )
- p_sbi_read_regs: ( sbi_cs, sbi_rena, sbi_addr )
</br>**Description**
 Read the Ethernet MAC dummy register 
- p_gmii_send_frame: ( clk )
</br>**Description**
----------------------------------------------------------------------------------  GMII interface ----------------------------------------------------------------------------------  Send Ethernet frames once they have been completely stored in the internal registers. 
## State machines

- ----------------------------------------------------------------------------------

 GMII interface

----------------------------------------------------------------------------------

 Send Ethernet frames once they have been completely stored in the internal registers.

![Diagram_state_machine_0]( stm_ethernet_mac_00.svg "Diagram")