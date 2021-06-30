# Entity: gearbox_up_dc

## Diagram

![Diagram](gearbox_up_dc.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:				 	Patrick Lehmann
Entity:				 	An upscaling gearbox module with a dependent clock (dc) interface.
Description:
-------------------------------------
This module provides a upscaling gearbox with a dependent clock (dc)
interface. It perfoems a 'byte' to 'word' collection. The default order is
LITTLE_ENDIAN (starting at byte(0)). Input "In_Data" is of clock domain
"Clock1"; output "Out_Data" is of clock domain "Clock2". The "In_Align"
is required to mark the starting byte in the word. An optional input
register can be added by enabling (ADD_INPUT_REGISTERS = TRUE).
Assertions:
===========
- Clock periods of Clock1 and Clock2 MUST be multiples of each other.
- Clock1 and Clock2 MUST be phase aligned (related) to each other.
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

| Generic name        | Type        | Value     | Description                                                |
| ------------------- | ----------- | --------- | ---------------------------------------------------------- |
| INPUT_BITS          | positive    | 8         | input bit width                                            |
| INPUT_ORDER         | T_BIT_ORDER | LSB_FIRST | LSB_FIRST: start at byte(0), MSB_FIRST: start at byte(n-1) |
| OUTPUT_BITS         | positive    | 32        | output bit width                                           |
| ADD_INPUT_REGISTERS | boolean     | FALSE     | add input register @Clock1                                 |
## Ports

| Port name | Direction | Type                                       | Description                         |
| --------- | --------- | ------------------------------------------ | ----------------------------------- |
| Clock1    | in        | std_logic                                  | input clock domain                  |
| Clock2    | in        | std_logic                                  | output clock domain                 |
| In_Align  | in        | std_logic                                  | align word (one cycle high impulse) |
| In_Data   | in        | std_logic_vector(INPUT_BITS - 1 downto 0)  | input word                          |
| Out_Data  | out       | std_logic_vector(OUTPUT_BITS - 1 downto 0) | output word                         |
| Out_Valid | out       | std_logic                                  | output is valid                     |
## Signals

| Name              | Type                                       | Description |
| ----------------- | ------------------------------------------ | ----------- |
| Counter_us        | unsigned(COUNTER_BITS - 1 downto 0)        |             |
| Select_us         | unsigned(COUNTER_BITS - 1 downto 0)        |             |
| In_Data_d         | std_logic_vector(INPUT_BITS - 1 downto 0)  |             |
| In_Align_d        | std_logic                                  |             |
| Data_d            | T_CHUNK_VECTOR(INPUT_CHUNKS - 2 downto 0)  |             |
| Collected         | std_logic_vector(OUTPUT_BITS - 1 downto 0) |             |
| Collected_swapped | std_logic_vector(OUTPUT_BITS - 1 downto 0) |             |
| Collected_en      | std_logic                                  |             |
| Collected_d       | std_logic_vector(OUTPUT_BITS - 1 downto 0) |             |
| DataOut_d         | std_logic_vector(OUTPUT_BITS - 1 downto 0) |             |
| Valid_r           | std_logic                                  |             |
| Valid_d           | std_logic                                  |             |
## Constants

| Name           | Type     | Value                                 | Description |
| -------------- | -------- | ------------------------------------- | ----------- |
| BIT_RATIO      | REAL     |  real(OUTPUT_BITS) / real(INPUT_BITS) |             |
| INPUT_CHUNKS   | positive |  integer(BIT_RATIO)                   |             |
| BITS_PER_CHUNK | positive |  INPUT_BITS                           |             |
| COUNTER_MAX    | positive |  INPUT_CHUNKS - 1                     |             |
| COUNTER_BITS   | positive |  log2ceil(COUNTER_MAX + 1)            |             |
## Types

| Name           | Type | Description |
| -------------- | ---- | ----------- |
| T_CHUNK_VECTOR |      |             |
## Functions
- to_slv <font id="function_arguments">(slvv : T_CHUNK_VECTOR) </font> <font id="function_return">return std_logic_vector </font>
**Description**
convert chunk-vector to flatten vector
## Processes
- unnamed: ( Clock1 )
**Description**
byte alignment counter @Clock1

- unnamed: ( Clock1 )
**Description**
delay registers @Clock1

