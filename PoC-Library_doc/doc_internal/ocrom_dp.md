# Entity: ocrom_dp
## Diagram
![Diagram](ocrom_dp.svg "Diagram")
## Description
EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:				 	Martin Zabel
Entity:				 	True dual-port memory.
Description:
-------------------------------------
Inferring / instantiating dual-port read-only memory, with:
* dual clock, clock enable,
* 2 read ports.
The generalized behavior across Altera and Xilinx FPGAs since
Stratix/Cyclone and Spartan-3/Virtex-5, respectively, is as follows:
WARNING: The simulated behavior on RT-level is not correct.
TODO: add timing diagram
TODO: implement correct behavior for RT-level simulation
License:
=============================================================================
Copyright 2008-2015 Technische Universitaet Dresden - Germany
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
| A_BITS       | positive |       |             |
| D_BITS       | positive |       |             |
| FILENAME     | string   | ""    |             |
## Ports
| Port name | Direction | Type                                | Description |
| --------- | --------- | ----------------------------------- | ----------- |
| clk1      | in        | std_logic                           |             |
| clk2      | in        | std_logic                           |             |
| ce1       | in        | std_logic                           |             |
| ce2       | in        | std_logic                           |             |
| a1        | in        | unsigned(A_BITS-1 downto 0)         |             |
| a2        | in        | unsigned(A_BITS-1 downto 0)         |             |
| q1        | out       | std_logic_vector(D_BITS-1 downto 0) |             |
| q2        | out       | std_logic_vector(D_BITS-1 downto 0) |             |
## Constants
| Name  | Type     | Value      | Description |
| ----- | -------- | ---------- | ----------- |
| DEPTH | positive |  2**A_BITS |             |
