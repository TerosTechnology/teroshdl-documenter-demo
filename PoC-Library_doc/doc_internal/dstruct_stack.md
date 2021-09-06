# Entity: dstruct_stack

- **File**: dstruct_stack.vhdl
## Diagram

![Diagram](dstruct_stack.svg "Diagram")
## Description

 EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
 vim: tabstop=2:shiftwidth=2:noexpandtab
 kate: tab-width 2; replace-tabs off; indent-width 2;
 =============================================================================
 Authors:     Jens Voss

 Entity:      Stack (LIFO)

 Description:
 -------------------------------------
 Implements a stack, a LIFO storage abstraction.

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

| Generic name | Type     | Value | Description          |
| ------------ | -------- | ----- | -------------------- |
| D_BITS       | positive |       |  Data Width          |
| MIN_DEPTH    | positive |       |  Minimum Stack Depth |
## Ports

| Port name | Direction | Type                                | Description          |
| --------- | --------- | ----------------------------------- | -------------------- |
| clk       | in        | std_logic                           | INPUTS               |
| rst       | in        | std_logic                           | INPUTS               |
| din       | in        | std_logic_vector(D_BITS-1 downto 0) |  Data Input          |
| put       | in        | std_logic                           |  0 -> pop, 1 -> push |
| full      | out       | std_logic                           |                      |
| got       | in        | std_logic                           | Read Ports           |
| dout      | out       | std_logic_vector(D_BITS-1 downto 0) |                      |
| valid     | out       | std_logic                           |                      |
## Signals

| Name          | Type                                | Description |
| ------------- | ----------------------------------- | ----------- |
| stackpointer  | unsigned(A_BITS-1 downto 0)         |  Signals    |
| we            | std_logic                           |             |
| adr           | unsigned(A_BITS-1 downto 0)         |             |
| s_adr         | unsigned(A_BITS-1 downto 0)         |             |
| s_dout        | std_logic_vector(D_BITS-1 downto 0) |             |
| s_valid       | std_logic                           |             |
| s_din         | std_logic_vector(D_BITS-1 downto 0) |             |
| ctrl          | ctrl_t                              |             |
| current_state | state                               |             |
|  next_state   | state                               |             |
## Constants

| Name   | Type    | Value                | Description |
| ------ | ------- | -------------------- | ----------- |
| A_BITS | natural |  log2ceil(MIN_DEPTH) |             |
## Types

| Name   | Type                                                                                                                                           | Description                               |
| ------ | ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| ctrl_t | (PUSH,<br><span style="padding-left:20px"> POP,<br><span style="padding-left:20px"> IDLE)                                                      |  ctrl signal for stackpointer operations  |
| state  | (SEMPTY,<br><span style="padding-left:20px"> NOTFULL,<br><span style="padding-left:20px"> WAITING,<br><span style="padding-left:20px"> SFULL)  |                                           |
## Processes
- unnamed: ( clk )
- unnamed: ( current_state, put, stackpointer, got )
- unnamed: ( clk )
## Instantiations

- ram: poc.ocram_sp
