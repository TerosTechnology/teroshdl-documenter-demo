# Entity: arith_addw
## Diagram
![Diagram](arith_addw.svg "Diagram")
## Description
EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:					Thomas B. Preusser
Entity:					arith_addw
Description:
-------------------------------------
Implements wide addition providing several options all based
on an adaptation of a carry-select approach.
References:
* Hong Diep Nguyen and Bogdan Pasca and Thomas B. Preusser:
  FPGA-Specific Arithmetic Optimizations of Short-Latency Adders,
  FPL 2011.
  -> ARCH:     AAM, CAI, CCA
  -> SKIPPING: CCC
* Marcin Rogawski, Kris Gaj and Ekawat Homsirikamol:
  A Novel Modular Adder for One Thousand Bits and More
  Using Fast Carry Chains of Modern FPGAs, FPL 2014.
  -> ARCH:		 PAI
  -> SKIPPING: PPN_KS, PPN_BK
License:
=============================================================================
Copyright 2007-2015 Technische Universitaet Dresden - Germany
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
| Generic name | Type      | Value | Description                       |
| ------------ | --------- | ----- | --------------------------------- |
| N            | positive  |       | Operand Width                     |
| K            | positive  |       | Block Count                       |
| ARCH         | tArch     | AAM   | Architecture                      |
| BLOCKING     | tBlocking | DFLT  | Blocking Scheme                   |
| SKIPPING     | tSkipping | CCC   | Carry Skip Scheme                 |
| P_INCLUSIVE  | boolean   | false | Use Inclusive Propagate, i.e. c^1 |
## Ports
| Port name | Direction | Type                           | Description |
| --------- | --------- | ------------------------------ | ----------- |
| a         | in        | std_logic_vector(N-1 downto 0) |             |
| b         | in        | std_logic_vector(N-1 downto 0) |             |
| cin       | in        | std_logic                      |             |
| s         | out       | std_logic_vector(N-1 downto 0) |             |
| cout      | out       | std_logic                      |             |
## Signals
| Name | Type                           | Description     |
| ---- | ------------------------------ | --------------- |
| g    | std_logic_vector(K-1 downto 1) | Block Generate  |
| p    | std_logic_vector(K-1 downto 1) | Block Propagate |
| c    | std_logic_vector(K-1 downto 1) |                 |
## Constants
| Name             | Type                         | Value                                                | Description |
| ---------------- | ---------------------------- | ---------------------------------------------------- | ----------- |
| DEFAULT_BLOCKING | tBlocking_vector             |  (AAM => ASC, CAI => DESC, PAI => DESC, CCA => DESC) |             |
| BLOCKS           | integer_vector(K-1 downto 0) |  compute_blocks                                      |             |
## Types
| Name             | Type | Description |
| ---------------- | ---- | ----------- |
| tBlocking_vector |      |             |
| integer_vector   |      |             |
## Functions
