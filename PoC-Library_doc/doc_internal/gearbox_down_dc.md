# Entity: gearbox_down_dc

## Diagram

![Diagram](gearbox_down_dc.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:				 	Patrick Lehmann
Entity:				 	A downscaling gearbox module with a dependent clock (dc) interface.
Description:
-------------------------------------
This module provides a downscaling gearbox with a dependent clock (dc)
interface. It perfoems a 'word' to 'byte' splitting. The default order is
LITTLE_ENDIAN (starting at byte(0)). Input "In_Data" is of clock domain
"Clock1"; output "Out_Data" is of clock domain "Clock2". Optional input and
output registers can be added by enabling (ADD_***PUT_REGISTERS = TRUE).
Assertions:
===========
- Clock periods of Clock1 and Clock2 MUST be multiples of each other.
- Clock1 and Clock2 MUST be phase aligned (related) to each other.
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

| Generic name         | Type        | Value     | Description                                                |
| -------------------- | ----------- | --------- | ---------------------------------------------------------- |
| INPUT_BITS           | positive    | 32        | input bits ('words')                                       |
| OUTPUT_BITS          | positive    | 8         | output bits ('byte')                                       |
| OUTPUT_ORDER         | T_BIT_ORDER | LSB_FIRST | LSB_FIRST: start at byte(0), MSB_FIRST: start at byte(n-1) |
| ADD_INPUT_REGISTERS  | boolean     | FALSE     | add input register @Clock1                                 |
| ADD_OUTPUT_REGISTERS | boolean     | FALSE     | add output register @Clock2                                |
## Ports

| Port name | Direction | Type                                       | Description         |
| --------- | --------- | ------------------------------------------ | ------------------- |
| Clock1    | in        | std_logic                                  | input clock domain  |
| Clock2    | in        | std_logic                                  | output clock domain |
| In_Data   | in        | std_logic_vector(INPUT_BITS - 1 downto 0)  | input word          |
| Out_Data  | out       | std_logic_vector(OUTPUT_BITS - 1 downto 0) | output word         |
## Signals

| Name           | Type                                       | Description |
| -------------- | ------------------------------------------ | ----------- |
| WordBoundary   | std_logic                                  |             |
| WordBoundary_d | std_logic                                  |             |
| Align          | std_logic                                  |             |
| Data_d         | std_logic_vector(INPUT_BITS - 1 downto 0)  |             |
| DataIn         | std_logic_vector(INPUT_BITS - 1 downto 0)  |             |
| DataOut_d      | std_logic_vector(OUTPUT_BITS - 1 downto 0) |             |
| MuxInput       | T_MUX_INPUT(2**COUNTER_BITS - 1 downto 0)  |             |
| MuxOutput      | std_logic_vector(OUTPUT_BITS - 1 downto 0) |             |
| MuxCounter_us  | unsigned(COUNTER_BITS - 1 downto 0)        |             |
| MuxSelect_us   | unsigned(COUNTER_BITS - 1 downto 0)        |             |
## Constants

| Name         | Type     | Value                                 | Description |
| ------------ | -------- | ------------------------------------- | ----------- |
| BIT_RATIO    | REAL     |  real(INPUT_BITS) / real(OUTPUT_BITS) |             |
| COUNTER_BITS | positive |  log2ceil(integer(BIT_RATIO))         |             |
## Types

| Name        | Type | Description |
| ----------- | ---- | ----------- |
| T_MUX_INPUT |      |             |
