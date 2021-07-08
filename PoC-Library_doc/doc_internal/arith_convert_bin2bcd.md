# Entity: arith_convert_bin2bcd

## Diagram

![Diagram](arith_convert_bin2bcd.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:					Patrick Lehmann
Entity:					Converter binary numbers to BCD encoded numbers.
Description:
-------------------------------------
.. TODO:: No documentation available.
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

| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| BITS         | positive | 8     |             |
| DIGITS       | positive | 3     |             |
| RADIX        | positive | 2     |             |
## Ports

| Port name | Direction | Type                                | Description |
| --------- | --------- | ----------------------------------- | ----------- |
| Clock     | in        | std_logic                           |             |
| Reset     | in        | std_logic                           |             |
| Start     | in        | std_logic                           |             |
| Busy      | out       | std_logic                           |             |
| Binary    | in        | std_logic_vector(BITS - 1 downto 0) |             |
| IsSigned  | in        | std_logic                           |             |
| BCDDigits | out       | T_BCD_VECTOR(DIGITS - 1 downto 0)   |             |
| Sign      | out       | std_logic                           |             |
## Signals

| Name            | Type                                       | Description |
| --------------- | ------------------------------------------ | ----------- |
| Digit_Shift_rst | std_logic                                  |             |
| Digit_Shift_en  | std_logic                                  |             |
| Digit_Shift_in  | T_CARRY_VECTOR(DIGITS downto 0)            |             |
| Binary_en       | std_logic                                  |             |
| Binary_rl       | std_logic                                  |             |
| Binary_d        | std_logic_vector(BINARY_BITS - 1 downto 0) |             |
| Sign_d          | std_logic                                  |             |
| DelayShifter    | std_logic_vector(BINARY_SHIFTS downto 0)   |             |
## Constants

| Name          | Type     | Value                                                           | Description |
| ------------- | -------- | --------------------------------------------------------------- | ----------- |
| RADIX_BITS    | positive |  log2ceil(RADIX)                                                |             |
| BINARY_SHIFTS | positive |  div_ceil(BITS,<br><span style="padding-left:20px"> RADIX_BITS) |             |
| BINARY_BITS   | positive |  BINARY_SHIFTS * RADIX_BITS                                     |             |
## Types

| Name           | Type                                | Description |
| -------------- | ----------------------------------- | ----------- |
| T_CARRY_VECTOR | array(natural range <>) of T_CARRY  |             |
## Functions
- nextBCD <font id="function_arguments">(Value : unsigned(4 downto 0)) </font> <font id="function_return">return unsigned </font>
## Processes
- unnamed: ( Clock )
