# Entity: dstruct_deque

- **File**: dstruct_deque.vhdl
## Diagram

![Diagram](dstruct_deque.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:     Jens Voss
Entity:      Double-ended queue
Description:
-------------------------------------
Implements a deque (double-ended queue). This data structure allows two
acting entities to queue data elements for the consumption by the other while
still being able to unqueue untaken ones in LIFO fashion.
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

| Generic name | Type     | Value | Description         |
| ------------ | -------- | ----- | ------------------- |
| D_BITS       | positive |       | Data Width          |
| MIN_DEPTH    | positive |       | Minimum Deque Depth |
## Ports

| Port name | Direction | Type                                | Description  |
| --------- | --------- | ----------------------------------- | ------------ |
| clk       | in        | std_logic                           | Shared Ports |
| rst       | in        | std_logic                           | Shared Ports |
| dinA      | in        | std_logic_vector(D_BITS-1 downto 0) | DataA Input  |
| putA      | in        | std_logic                           |              |
| gotA      | in        | std_logic                           |              |
| doutA     | out       | std_logic_vector(D_BITS-1 downto 0) | DataA Output |
| validA    | out       | std_logic                           |              |
| fullA     | out       | std_logic                           |              |
| dinB      | in        | std_logic_vector(D_BITS-1 downto 0) | DataB Input  |
| putB      | in        | std_logic                           |              |
| gotB      | in        | std_logic                           |              |
| doutB     | out       | std_logic_vector(D_BITS-1 downto 0) |              |
| validB    | out       | std_logic                           |              |
| fullB     | out       | std_logic                           |              |
## Signals

| Name           | Type                         | Description                                                                                                                                                           |
| -------------- | ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| combined       | std_logic_vector(3 downto 0) | MEMORY variabletype memory_t is array ((2**A_BITS)-1 downto 0) of std_logic_vector(D_BITS-1 downto 0);signal memory : memory_t := (others => (others => '0'));Signals |
| ctrl           | std_logic_vector(1 downto 0) |                                                                                                                                                                       |
| sub            | unsigned(A_BITS-1 downto 0)  |                                                                                                                                                                       |
| last_operation | std_logic                    | save last operation 0 -> read, 1 -> write                                                                                                                             |
| last_op_ctrl   | last_op_ctrl_t               |                                                                                                                                                                       |
| delayed_valid  | std_logic                    |                                                                                                                                                                       |
| delay          | std_logic                    |                                                                                                                                                                       |
| stackpointerA  | unsigned (A_BITS-1 downto 0) | signal s_validA : std_logic := '0';signal s_validB : std_logic := '0';StackpointerA                                                                                   |
| weA            | std_logic                    | signal reA : std_logic := '0';                                                                                                                                        |
| stackpointerB  | unsigned (A_BITS-1 downto 0) | B                                                                                                                                                                     |
| weB            | std_logic                    | signal reB : std_logic := '0';                                                                                                                                        |
| ctrlA          | ctrl_t                       |                                                                                                                                                                       |
| ctrlB          | ctrl_t                       |                                                                                                                                                                       |
| adrA           | unsigned(A_BITS-1 downto 0)  | RAM Signals                                                                                                                                                           |
| adrB           | unsigned(A_BITS-1 downto 0)  |                                                                                                                                                                       |
## Constants

| Name   | Type    | Value                | Description |
| ------ | ------- | -------------------- | ----------- |
| A_BITS | natural |  log2ceil(MIN_DEPTH) |             |
## Types

| Name           | Type                                                                                        | Description                             |
| -------------- | ------------------------------------------------------------------------------------------- | --------------------------------------- |
| last_op_ctrl_t | (IDLE,<br><span style="padding-left:20px"> SET,<br><span style="padding-left:20px"> UNSET)  |                                         |
| ctrl_t         | (PUSH,<br><span style="padding-left:20px"> POP,<br><span style="padding-left:20px"> IDLE)   | ctrl signal for stackpointer operations |
## Processes
- unnamed: ( combined, stackpointerA, stackpointerB, last_operation, ctrl )
- unnamed: ( clk )
- unnamed: ( clk )
- unnamed: ( clk )
**Description**
stackpointerB operations

- unnamed: ( clk )
**Description**
delayed_valid register

- unnamed: ( sub, last_operation, delayed_valid )
**Description**
sub of B and A

## Instantiations

- ram: poc.ocram_tdp_wf
