# Entity: arith_counter_gray

## Diagram

![Diagram](arith_counter_gray.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:				 	Thomas B. Preusser
Entity:				 	Gray-Code counter.
Description:
-------------------------------------
.. TODO:: No documentation available.
License:
=============================================================================
Copyright 2007-2014 Technische Universitaet Dresden - Germany
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

| Generic name | Type     | Value | Description                 |
| ------------ | -------- | ----- | --------------------------- |
| BITS         | positive |       | Bit width of the counter    |
| INIT         | natural  | 0     | Initial/reset counter value |
## Ports

| Port name | Direction | Type                              | Description         |
| --------- | --------- | --------------------------------- | ------------------- |
| clk       | in        | std_logic                         |                     |
| rst       | in        | std_logic                         | Reset to INIT value |
| inc       | in        | std_logic                         | Increment           |
| dec       | in        | std_logic                         | Decrement           |
| val       | out       | std_logic_vector(BITS-1 downto 0) | Value output        |
| cry       | out       | std_logic                         | Carry output        |
## Signals

| Name         | Type                      | Description |
| ------------ | ------------------------- | ----------- |
| gray_cnt_r   | unsigned(BITS-1 downto 0) |             |
| gray_cnt_nxt | unsigned(BITS-1 downto 0) |             |
| en           | std_logic                 |             |
## Constants

| Name      | Type                      | Value                                                        | Description      |
| --------- | ------------------------- | ------------------------------------------------------------ | ---------------- |
| INIT_GRAY | unsigned(BITS-1 downto 0) |  gray_encode(INIT,<br><span style="padding-left:20px"> BITS) | Counter Register |
## Functions
- gray_encode <font id="function_arguments">(val : natural;<br><span style="padding-left:20px"> len : positive) </font> <font id="function_return">return unsigned </font>
- parity <font id="function_arguments">(val : unsigned) </font> <font id="function_return">return std_logic </font>
**Description**
purpose: parity generation
## Processes
- unnamed: ( clk )
