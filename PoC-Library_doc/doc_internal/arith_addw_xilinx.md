# Entity: arith_addw_xilinx

## Diagram

![Diagram](arith_addw_xilinx.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:					Thomas B. Preusser
Entity:					arith_addw_xilinx
Description:
-------------------------------------
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

| Generic name | Type      | Value | Description       |
| ------------ | --------- | ----- | ----------------- |
| N            | positive  |       | Operand Width     |
| K            | positive  |       | Block Count       |
| ARCH         | tArch     | CAI   | Architecture      |
| BLOCKING     | tBlocking | DFLT  | Blocking Scheme   |
| SKIPPING     | tSkipping | CCC   | Carry Skip Scheme |
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

| Name             | Type                         | Value                                                                                                                                                           | Description |
| ---------------- | ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| DEFAULT_BLOCKING | tBlocking_vector             |  (AAM => ASC,<br><span style="padding-left:20px"> CAI => ASC,<br><span style="padding-left:20px"> PAI => DESC,<br><span style="padding-left:20px"> CCA => DESC) |             |
| BLOCKS           | integer_vector(K-1 downto 0) |  compute_blocks                                                                                                                                                 |             |
## Types

| Name             | Type                               | Description |
| ---------------- | ---------------------------------- | ----------- |
| tBlocking_vector |                                    |             |
| integer_vector   | array(natural range<>) of integer  |             |
## Functions
- compute_blocks <font id="function_arguments">()</font> <font id="function_return">return integer_vector </font>
