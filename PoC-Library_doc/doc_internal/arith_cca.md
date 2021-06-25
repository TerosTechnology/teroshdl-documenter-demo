# Entity: arith_cca
## Diagram
![Diagram](arith_cca.svg "Diagram")
## Description
===================================================================================
EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Description: Carry-Compact Adder for Xilinx Virtex-5 architectures and newer.
  A carry-compact adder (CCA) utilizes the fast carry chain of contemporary
  FPGA devices to implement a fast and even compacted binary word addition.
  For wide operands, it accounts for the delay encountered even on this fast
  signal path and uses the associated time to perform a significantly
  shorter but effective LUT-based parallel computation that reduces the
  length of the internal ripple-carry adder without affecting the critical
  path length.
  The compaction performed by the CCA is performed hierarchical on
  potentially multiple levels. The number of levels may be restricted by the
  optional generic parameter X. A linear compaction on a single level may
  be of special interest as it typically does not increase the LUT demand
  in comparison to a standard RCA implementation.
  The parameter L is architecture-dependent and estimates the delay of a LUT
  stage in terms of carry-chain hops. It is a tuning parameter. Values
  around 20 are a good starting point.
  For a detailed description see:    http://dx.doi.org/10.1109/ARITH.2011.22
     Preusser, T.B.; Zabel, M.; Spallek, R.G.:
     "Accelerating Computations on FPGA Carry Chains by Operand Compaction",
     20th IEEE Symposium on Computer Arithmetic (ARITH), 2011.
Author:      Thomas B. Preusser
================================================================================
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
             http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
===================================================================================
## Generics
| Generic name | Type     | Value | Description                                        |
| ------------ | -------- | ----- | -------------------------------------------------- |
| N            | positive |       | bit width                                          |
| L            | natural  |       | CC length equivalent per LUT stage                 |
| X            | natural  | 0     | max expansion depth; default: zero (0) - unlimited |
## Ports
| Port name | Direction | Type                           | Description |
| --------- | --------- | ------------------------------ | ----------- |
| a         | in        | std_logic_vector(N-1 downto 0) |             |
| b         | in        | std_logic_vector(N-1 downto 0) |             |
| c         | in        | std_logic                      |             |
| s         | out       | std_logic_vector(N-1 downto 0) |             |
## Constants
| Name   | Type    | Value              | Description |
| ------ | ------- | ------------------ | ----------- |
| LEVELS | tLevels |  compact           |             |
| CCA    | boolean |  LEVELS'length > 1 |             |
## Types
| Name    | Type | Description |
| ------- | ---- | ----------- |
| tLevel  |      |             |
| tLevels |      |             |
## Functions
- compact <font id="function_arguments">()</font> <font id="function_return">return tLevels</font>
