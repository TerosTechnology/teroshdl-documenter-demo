# Entity: ddr3_mem2mig_adapter_Series7

## Diagram

![Diagram](ddr3_mem2mig_adapter_Series7.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:					Martin Zabel
Module:					Adapter for the Xilinx MIG IP core on 7-Series FPGAs.
Description:
------------------------------------
Adapter between the :ref:`PoC.Mem <INT:PoC.Mem>` interface and the
application interface ("app") of the Xilinx MIG IP core for 7-Series	FPGAs.
Simplifies the application interface ("app") of the Xilinx MIG IP core.
The PoC.Mem interface provides single-cycle fully pipelined read/write access
to the memory. All accesses are word-aligned. Always all bytes of a word are
written to the memory. More details can be found
:ref:`here <INT:PoC.Mem>`.
Generic parameters:
* D_BITS: Data bus width of the PoC.Mem and "app" interface. Also size of one
  word in bits.
* DQ_BITS: Size of data bus between memory controller and external memory
  (DIMM, SoDIMM).
* MEM_A_BITS: Address bus width of the PoC.Mem interface.
* APP_A_BTIS: Address bus width of the "app" interface.
Containts only combinational logic.
License:
=============================================================================
Copyright 2007-2016 Technische Universitaet Dresden - Germany
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
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
| DQ_BITS      | positive |       |             |
| MEM_A_BITS   | positive |       |             |
| APP_A_BITS   | positive |       |             |
## Ports

| Port name           | Direction | Type                                    | Description                  |
| ------------------- | --------- | --------------------------------------- | ---------------------------- |
| mem_req             | in        | std_logic                               | PoC.Mem interface            |
| mem_write           | in        | std_logic                               |                              |
| mem_addr            | in        | unsigned(MEM_A_BITS-1 downto 0)         |                              |
| mem_wdata           | in        | std_logic_vector(D_BITS-1 downto 0)     |                              |
| mem_wmask           | in        | std_logic_vector(D_BITS/8-1 downto 0)   |                              |
| mem_rdy             | out       | std_logic                               |                              |
| mem_rstb            | out       | std_logic                               |                              |
| mem_rdata           | out       | std_logic_vector(D_BITS-1 downto 0)     |                              |
| init_calib_complete | in        | std_logic                               | Xilinx MIG IP Core interface |
| app_rd_data         | in        | std_logic_vector((D_BITS)-1 downto 0)   |                              |
| app_rd_data_end     | in        | std_logic                               |                              |
| app_rd_data_valid   | in        | std_logic                               |                              |
| app_rdy             | in        | std_logic                               |                              |
| app_wdf_rdy         | in        | std_logic                               |                              |
| app_addr            | out       | std_logic_vector(APP_A_BITS-1 downto 0) |                              |
| app_cmd             | out       | std_logic_vector(2 downto 0)            |                              |
| app_en              | out       | std_logic                               |                              |
| app_wdf_data        | out       | std_logic_vector((D_BITS)-1 downto 0)   |                              |
| app_wdf_end         | out       | std_logic                               |                              |
| app_wdf_mask        | out       | std_logic_vector((D_BITS)/8-1 downto 0) |                              |
| app_wdf_wren        | out       | std_logic                               |                              |
## Signals

| Name      | Type      | Description |
| --------- | --------- | ----------- |
| mem_rdy_i | std_logic |             |
## Constants

| Name    | Type     | Value             | Description |
| ------- | -------- | ----------------- | ----------- |
| BL      | positive |  D_BITS / DQ_BITS |             |
| BL_BITS | natural  |  log2ceil(BL)     |             |
## Processes
- unnamed: ( mem_addr )
**Description**
address

