# Entity: arith_div
## Diagram
![Diagram](arith_div.svg "Diagram")
## Description
EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:					Thomas B. Preusser
Entity:					Multi-cycle Non-Performing Restoring Divider
Description:
-------------------------------------
Implementation of a Non-Performing restoring divider with a configurable radix.
The multi-cycle division is controlled by 'start' / 'rdy'. A new division is
started by asserting 'start'. The result Q = A/D is available when 'rdy'
returns to '1'. A division by zero is identified by output Z. The Q and R
outputs are undefined in this case.
License:
=============================================================================
Copyright 2007-2016 Technische Universität Dresden - Germany,
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
| Generic name | Type     | Value | Description                       |
| ------------ | -------- | ----- | --------------------------------- |
| A_BITS       | positive |       | Dividend Width                    |
| D_BITS       | positive |       | Divisor Width                     |
| RAPOW        | positive | 1     | Power of Compute Radix (2**RAPOW) |
| PIPELINED    | boolean  | false | Computation Pipeline              |
## Ports
| Port name | Direction | Type                                | Description        |
| --------- | --------- | ----------------------------------- | ------------------ |
| clk       | in        | std_logic                           | Global Reset/Clock |
| rst       | in        | std_logic                           |                    |
| start     | in        | std_logic                           | Ready / Start      |
| ready     | out       | std_logic                           |                    |
| A         | in        | std_logic_vector(A_BITS-1 downto 0) | Dividend           |
| D         | in        | std_logic_vector(D_BITS-1 downto 0) | Divisor            |
| Q         | out       | std_logic_vector(A_BITS-1 downto 0) | Quotient           |
| R         | out       | std_logic_vector(D_BITS-1 downto 0) | Remainder          |
| Z         | out       | std_logic                           | Division by Zero   |
## Signals
| Name | Type                       | Description                                |
| ---- | -------------------------- | ------------------------------------------ |
| AR   | residue_vector(0 to DEPTH) | Data Registers                             |
| DR   | divisor_vector(0 to DEPTH) |                                            |
| ZR   | std_logic                  | Zero Detection only in last pipeline stage |
| exec | std_logic                  |                                            |
## Constants
| Name        | Type     | Value                     | Description               |
| ----------- | -------- | ------------------------- | ------------------------- |
| STEPS       | positive |  (A_BITS+RAPOW-1)/RAPOW   | Number of Iteration Steps |
| DEPTH       | natural  |  ite(PIPELINED, STEPS, 0) | Physical Depth            |
| TRUNK_BITS  | natural  |  (STEPS-1)*RAPOW          |                           |
| ACTIVE_BITS | positive |  D_BITS + RAPOW           |                           |
## Types
| Name           | Type | Description |
| -------------- | ---- | ----------- |
| residue_vector |      |             |
| divisor_vector |      |             |
## Functions
- div_step <font id="function_arguments">(av : residue; dv : divisor)</font> <font id="function_return">return residue</font>
## Processes
- unnamed: _( clk )_
Registers

**Description**
Registers

