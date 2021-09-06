# Entity: sortnet_OddEvenMergeSort

- **File**: sortnet_OddEvenMergeSort.vhdl
## Diagram

![Diagram](sortnet_OddEvenMergeSort.svg "Diagram")
## Description

 EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
 vim: tabstop=2:shiftwidth=2:noexpandtab
 kate: tab-width 2; replace-tabs off; indent-width 2;
 =============================================================================
 Authors:					Patrick Lehmann

 Entity:					Sorting Network: Odd-Even-Merge-Sort

 Description:
 -------------------------------------
 .. TODO:: No documentation available.

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

| Generic name         | Type     | Value | Description                                                        |
| -------------------- | -------- | ----- | ------------------------------------------------------------------ |
| INPUTS               | positive | 128   |  input count                                                       |
| KEY_BITS             | positive | 32    |  the first KEY_BITS of In_Data are used as a sorting critera (key) |
| DATA_BITS            | positive | 32    |  inclusive KEY_BITS                                                |
| META_BITS            | natural  | 2     |  additional bits, not sorted but delayed as long as In_Data        |
| PIPELINE_STAGE_AFTER | natural  | 2     |  add a pipline stage after n sorting stages                        |
| ADD_INPUT_REGISTERS  | boolean  | FALSE |                                                                    |
| ADD_OUTPUT_REGISTERS | boolean  | TRUE  |                                                                    |
## Ports

| Port name | Direction | Type                                               | Description |
| --------- | --------- | -------------------------------------------------- | ----------- |
| Clock     | in        | std_logic                                          |             |
| Reset     | in        | std_logic                                          |             |
| Inverse   | in        | std_logic                                          |             |
| In_Valid  | in        | std_logic                                          |             |
| In_IsKey  | in        | std_logic                                          |             |
| In_Data   | in        | T_SLM(INPUTS - 1 downto 0, DATA_BITS - 1 downto 0) |             |
| In_Meta   | in        | std_logic_vector(META_BITS - 1 downto 0)           |             |
| Out_Valid | out       | std_logic                                          |             |
| Out_IsKey | out       | std_logic                                          |             |
| Out_Data  | out       | T_SLM(INPUTS - 1 downto 0, DATA_BITS - 1 downto 0) |             |
| Out_Meta  | out       | std_logic_vector(META_BITS - 1 downto 0)           |             |
## Signals

| Name          | Type                                                                                   | Description |
| ------------- | -------------------------------------------------------------------------------------- | ----------- |
| In_Valid_d    | std_logic                                                                              |             |
| In_IsKey_d    | std_logic                                                                              |             |
| In_Data_d     | T_SLM(INPUTS - 1 downto 0,<br><span style="padding-left:20px"> DATA_BITS - 1 downto 0) |             |
| In_Meta_d     | std_logic_vector(META_BITS - 1 downto 0)                                               |             |
| MetaVector    | T_META_VECTOR(STAGES downto 0)                                                         |             |
| DataMatrix    | T_DATA_MATRIX(STAGES downto 0)                                                         |             |
| MetaOutputs_d | T_META                                                                                 |             |
| DataOutputs_d | T_SLM(INPUTS - 1 downto 0,<br><span style="padding-left:20px"> DATA_BITS - 1 downto 0) |             |
## Constants

| Name             | Type     | Value                     | Description |
| ---------------- | -------- | ------------------------- | ----------- |
| C_VERBOSE        | boolean  |  POC_VERBOSE              |             |
| BLOCKS           | positive |  log2ceil(INPUTS)         |             |
| STAGES           | positive |  triangularNumber(BLOCKS) |             |
| META_VALID_BIT   | natural  |  0                        |             |
| META_ISKEY_BIT   | natural  |  1                        |             |
| META_VECTOR_BITS | positive |  META_BITS + 2            |             |
## Types

| Name          | Type                                                           | Description |
| ------------- | -------------------------------------------------------------- | ----------- |
| T_META_VECTOR | array(natural range <>) of T_META                              |             |
| T_DATA_VECTOR | array(natural range <>) of T_DATA                              |             |
| T_DATA_MATRIX | array(natural range <>) of T_DATA_VECTOR(INPUTS - 1 downto 0)  |             |
## Functions
- to_dv <font id="function_arguments">(slm : T_SLM) </font> <font id="function_return">return T_DATA_VECTOR </font>
- to_slm <font id="function_arguments">(dv : T_DATA_VECTOR) </font> <font id="function_return">return T_SLM </font>
