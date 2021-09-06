# Entity: ocram_tdp_sim

- **File**: ocram_tdp_sim.vhdl
## Diagram

![Diagram](ocram_tdp_sim.svg "Diagram")
## Description

 EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
 vim: tabstop=2:shiftwidth=2:noexpandtab
 kate: tab-width 2; replace-tabs off; indent-width 2;
 =============================================================================
 Authors:				 	Martin Zabel

 Entity:				 	Simulation model for true dual-port memory.

 Description:
 -------------------------------------
 Simulation model for true dual-port memory, with:

 * dual clock, clock enable,
 * 2 read/write ports.

 The interface matches that of the IP core PoC.mem.ocram.tdp.
 But the implementation there is restricted to the description supported by
 various synthesis compilers. The implementation here also simulates the
 correct Mixed-Port Read-During-Write Behavior and handles X propagation.

 License:
 =============================================================================
 Copyright 2016-2016 Technische Universitaet Dresden - Germany
										 Chair for VLSI-Design, Diagnostics and Architecture

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

| Generic name | Type     | Value | Description                       |
| ------------ | -------- | ----- | --------------------------------- |
| A_BITS       | positive |       |  number of address bits           |
| D_BITS       | positive |       |  number of data bits              |
| FILENAME     | string   | ""    |  file-name for RAM initialization |
## Ports

| Port name | Direction | Type                                | Description                |
| --------- | --------- | ----------------------------------- | -------------------------- |
| clk1      | in        | std_logic                           |  clock for 1st port        |
| clk2      | in        | std_logic                           |  clock for 2nd port        |
| ce1       | in        | std_logic                           |  clock-enable for 1st port |
| ce2       | in        | std_logic                           |  clock-enable for 2nd port |
| we1       | in        | std_logic                           |  write-enable for 1st port |
| we2       | in        | std_logic                           |  write-enable for 2nd port |
| a1        | in        | unsigned(A_BITS-1 downto 0)         |  address for 1st port      |
| a2        | in        | unsigned(A_BITS-1 downto 0)         |  address for 2nd port      |
| d1        | in        | std_logic_vector(D_BITS-1 downto 0) |  write-data for 1st port   |
| d2        | in        | std_logic_vector(D_BITS-1 downto 0) |  write-data for 2nd port   |
| q1        | out       | std_logic_vector(D_BITS-1 downto 0) |  read-data from 1st port   |
| q2        | out       | std_logic_vector(D_BITS-1 downto 0) |  read-data from 2nd port   |
## Signals

| Name   | Type  | Description                                   |
| ------ | ----- | --------------------------------------------- |
| ram    | ram_t |                                               |
| write1 | X01   |  write to memory, 'X' means maybe write       |
| write2 | X01   |                                               |
| read1  | X01   |  read only from memory, 'X' means maybe read  |
| read2  | X01   |                                               |
## Constants

| Name  | Type     | Value      | Description |
| ----- | -------- | ---------- | ----------- |
| DEPTH | positive |  2**A_BITS |             |
## Types

| Name  | Type | Description |
| ----- | ---- | ----------- |
| ram_t |      |             |
## Functions
## Processes
- unnamed: ( clk1, clk2 )
