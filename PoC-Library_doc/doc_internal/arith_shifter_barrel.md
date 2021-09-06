# Entity: arith_shifter_barrel

- **File**: arith_shifter_barrel.vhdl
## Diagram

![Diagram](arith_shifter_barrel.svg "Diagram")
## Description

 EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
 vim: tabstop=2:shiftwidth=2:noexpandtab
 kate: tab-width 2; replace-tabs off; indent-width 2;
 =============================================================================
 Authors:					Patrick Lehmann

 Entity:					Universal Barrel-Shifter

 Description:
 -------------------------------------
 This Barrel-Shifter supports:

 * shifting and rotating
 * right and left operations
 * arithmetic and logic mode (only valid for shift operations)

 This is equivalent to the CPU instructions: SLL, SLA, SRL, SRA, RL, RR

 License:
 =============================================================================
 Copyright 2007-2015 Technische Universitaet Dresden - Germany,
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

| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| BITS         | positive | 32    |             |
## Ports

| Port name       | Direction | Type                                            | Description |
| --------------- | --------- | ----------------------------------------------- | ----------- |
| Input           | in        | std_logic_vector(BITS - 1 downto 0)             |             |
| ShiftAmount     | in        | std_logic_vector(log2ceilnz(BITS) - 1 downto 0) |             |
| ShiftRotate     | in        | std_logic                                       |             |
| LeftRight       | in        | std_logic                                       |             |
| ArithmeticLogic | in        | std_logic                                       |             |
| Output          | out       | std_logic_vector(BITS - 1 downto 0)             |             |
## Signals

| Name                | Type                                   | Description |
| ------------------- | -------------------------------------- | ----------- |
| IntermediateResults | T_INTERMEDIATE_VECTOR(STAGES downto 0) |             |
## Constants

| Name   | Type     | Value             | Description |
| ------ | -------- | ----------------- | ----------- |
| STAGES | positive |  log2ceilnz(BITS) |             |
## Types

| Name                  | Type                                               | Description |
| --------------------- | -------------------------------------------------- | ----------- |
| T_INTERMEDIATE_VECTOR | array (natural range <>) of T_INTERMEDIATE_RESULT  |             |
