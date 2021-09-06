# Entity: reconfig_icap_wrapper

- **File**: reconfig_icap_wrapper.vhdl
## Diagram

![Diagram](reconfig_icap_wrapper.svg "Diagram")
## Description

 EMACS settings: -*-  tab-width: 4; indent-tabs-mode: t -*-
 vim: tabstop=4:shiftwidth=4:noexpandtab
 kate: tab-width 4; replace-tabs off; indent-width 4;
 =============================================================================
 Authors:					Paul Genssler

 Entity:					Simple ICAP wrapper with a fifo interface and a few status signals

 Description:
 -------------------------------------
 This module was designed to connect the Xilinx "Internal Configuration Access Port" (ICAP)
 to a PCIe endpoint on a Dini board. Tested on:

 tbd

 License:
 =============================================================================
 Copyright 2007-2016 Technische Universitaet Dresden - Germany,
										 Chair of VLSI-Design, Diagnostics and Architecture

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

		http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 =============================================================================
## Generics

| Generic name  | Type     | Value | Description |
| ------------- | -------- | ----- | ----------- |
| MIN_DEPTH_OUT | positive | 256   |             |
| MIN_DEPTH_IN  | positive | 256   |             |
## Ports

| Port name        | Direction | Type                          | Description                                                    |
| ---------------- | --------- | ----------------------------- | -------------------------------------------------------------- |
| clk              | in        | std_logic                     |                                                                |
| reset            | in        | std_logic                     |                                                                |
| clk_icap         | in        | std_logic                     |  clock signal for ICAP, max 100 MHz (double check with manual) |
| icap_busy        | out       | std_logic                     |  the ICAP is processing the data                               |
| icap_readback    | out       | std_logic                     |  high during a readback                                        |
| icap_partial_res | out       | std_logic                     |  high during reconfiguration                                   |
| write_put        | in        | std_logic                     | data in                                                        |
| write_full       | out       | std_logic                     |                                                                |
| write_data       | in        | std_logic_vector(31 downto 0) |                                                                |
| write_done       | in        | std_logic                     |  high pulse/edge after all data was written                    |
| read_got         | in        | std_logic                     | data out                                                       |
| read_valid       | out       | std_logic                     |                                                                |
| read_data        | out       | std_logic_vector(31 downto 0) |                                                                |
## Signals

| Name                 | Type                                     | Description                                                 |
| -------------------- | ---------------------------------------- | ----------------------------------------------------------- |
| reset_icap           | std_logic                                |                                                             |
| write_done_d         | std_logic                                |                                                             |
| write_done_edge      | std_logic                                |                                                             |
| write_done_icapclk   | std_logic                                |                                                             |
| in_data_valid        | std_logic                                |                                                             |
| in_data_fill_state   | std_logic_vector(STATE_BITS -1 downto 0) |                                                             |
| in_data_rden         | std_logic                                |                                                             |
| in_data_start        | std_logic                                |  high after enough data was written into the pci->icap fifo |
| icap_rden            | std_logic                                |  icap wants some yummy data                                 |
| in_data              | std_logic_vector(31 downto 0)            |                                                             |
| out_data_full        | std_logic                                |                                                             |
| out_data_put         | std_logic                                |                                                             |
| out_data             | std_logic_vector(31 downto 0)            |                                                             |
| icap_data_config     | std_logic_vector(31 downto 0)            |                                                             |
| icap_data_readback   | std_logic_vector(31 downto 0)            |                                                             |
| icap_csb             | std_logic                                |                                                             |
| icap_rw              | std_logic                                |                                                             |
| icap_data_config_r   | std_logic_vector(31 downto 0)            |                                                             |
| icap_data_readback_r | std_logic_vector(31 downto 0)            |                                                             |
| icap_csb_r           | std_logic                                |                                                             |
| icap_rw_r            | std_logic                                |                                                             |
| fsm_status           | std_logic_vector(31 downto 0)            |                                                             |
| fsm_status_clk       | std_logic_vector(31 downto 0)            |                                                             |
| fsm_ready            | std_logic                                |                                                             |
| fsm_ready_d          | std_logic                                |                                                             |
## Constants

| Name              | Type                                     | Value                                                          | Description |
| ----------------- | ---------------------------------------- | -------------------------------------------------------------- | ----------- |
| STATE_BITS        | positive                                 |  2                                                             |             |
| state_almost_full | std_logic_vector(STATE_BITS -1 downto 0) |  (0 => '0',<br><span style="padding-left:20px"> others => '1') |             |
## Processes
- in_data_buffer_p: ( clk_icap )
</br>**Description**
 buffer some data before starting the icap, icap needs to be sync'ed before it can be paused 
- icap_reg_p: ( clk_icap )
</br>**Description**
 icap 
## Instantiations

- fifo_in: poc.fifo_ic_got
</br>**Description**
 sync the written pci data into the user clk
 writer: pci
 reader: core

- fifo_out: poc.fifo_ic_got
</br>**Description**
 sync data from this core to the pci bus
 writer: core
 reader: pci

- icap_fsm_inst: poc.reconfig_icap_fsm
- icap_inst: poc.xil_ICAP
- strobe_sync: poc.sync_Strobe
- reset_sync: poc.sync_Bits
- fsm_status_sync: poc.sync_vector
