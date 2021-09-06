# Entity: ddr2_mem2mig_adapter_Spartan6

- **File**: ddr2_mem2mig_adapter_Spartan6.vhdl
## Diagram

![Diagram](ddr2_mem2mig_adapter_Spartan6.svg "Diagram")
## Description

 EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
 vim: tabstop=2:shiftwidth=2:noexpandtab
 kate: tab-width 2; replace-tabs off; indent-width 2;

 =============================================================================
 Authors:					Martin Zabel

 Module:					Adapter for the Xilinx MIG IP core on Spartan-6 FPGAs.

 Description:
 ------------------------------------
 Adapter between the :ref:`PoC.Mem <INT:PoC.Mem>`
 interface and the User Interface of the Xilinx MIG IP core for the
 Spartan-6 FPGA Memory Controller Block (MCB). The MCB can be configured to
 have multiple ports. One instance of this adapter is required for every
 port. The control signals for one port of the MIG IP core are prefixed by
 "cX_pY", meaning port Y on controller X.

 Simplifies the User Interface ("user") of the Xilinx MIG IP core (UG388).
 The PoC.Mem interface provides single-cycle fully pipelined read/write access
 to the memory. All accesses are word-aligned. Always all bytes of a word are
 written to the memory. More details can be found
 :ref:`here <INT:PoC.Mem>`.

 Generic parameters:

 * D_BITS: Data bus width of the PoC.Mem and MIG / MCBinterface. Also size of
   one word in bits.

 * MEM_A_BITS: Address bus width of the PoC.Mem interface.

 * APP_A_BTIS: Address bus width of the MIG / MCB interface.

 Containts only combinational logic.

 License:
 =============================================================================
 Copyright 2007-2016 Technische Universitaet Dresden - Germany
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

| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| D_BITS       | positive |       |             |
| MEM_A_BITS   | positive |       |             |
| APP_A_BITS   | positive |       |             |
## Ports

| Port name         | Direction | Type                                    | Description                  |
| ----------------- | --------- | --------------------------------------- | ---------------------------- |
| mem_req           | in        | std_logic                               | PoC.Mem interface            |
| mem_write         | in        | std_logic                               |                              |
| mem_addr          | in        | unsigned(MEM_A_BITS-1 downto 0)         |                              |
| mem_wdata         | in        | std_logic_vector(D_BITS-1 downto 0)     |                              |
| mem_wmask         | in        | std_logic_vector(D_BITS/8-1 downto 0)   |                              |
| mem_rdy           | out       | std_logic                               |                              |
| mem_rstb          | out       | std_logic                               |                              |
| mem_rdata         | out       | std_logic_vector(D_BITS-1 downto 0)     |                              |
| mig_calib_done    | in        | std_logic                               | Xilinx MIG IP Core interface |
| mig_cmd_full      | in        | std_logic                               |                              |
| mig_wr_full       | in        | std_logic                               |                              |
| mig_rd_empty      | in        | std_logic                               |                              |
| mig_rd_data       | in        | std_logic_vector((D_BITS)-1 downto 0)   |                              |
| mig_cmd_instr     | out       | std_logic_vector(2 downto 0)            |                              |
| mig_cmd_en        | out       | std_logic                               |                              |
| mig_cmd_bl        | out       | std_logic_vector(5 downto 0)            |                              |
| mig_cmd_byte_addr | out       | std_logic_vector(APP_A_BITS-1 downto 0) |                              |
| mig_wr_data       | out       | std_logic_vector((D_BITS)-1 downto 0)   |                              |
| mig_wr_mask       | out       | std_logic_vector((D_BITS)/8-1 downto 0) |                              |
| mig_wr_en         | out       | std_logic                               |                              |
| mig_rd_en         | out       | std_logic                               |                              |
## Signals

| Name      | Type      | Description |
| --------- | --------- | ----------- |
| mem_rdy_i | std_logic |             |
## Constants

| Name           | Type     | Value               | Description |
| -------------- | -------- | ------------------- | ----------- |
| BYTE_ADDR_BITS | positive |  log2ceil(D_BITS/8) |             |
## Processes
- unnamed: ( mem_addr )
</br>**Description**
 1 word of D_BITS  address 
