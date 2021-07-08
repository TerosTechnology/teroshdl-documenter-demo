# Entity: stat_Average

## Diagram

![Diagram](stat_Average.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:					Patrick Lehmann
Entity:					Computes the overall average value of all data words
Description:
-------------------------------------
.. TODO:: No documentation available.
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

| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| DATA_BITS    | positive | 8     |             |
| COUNTER_BITS | positive | 16    |             |
## Ports

| Port name | Direction | Type                                        | Description |
| --------- | --------- | ------------------------------------------- | ----------- |
| Clock     | in        | std_logic                                   |             |
| Reset     | in        | std_logic                                   |             |
| Enable    | in        | std_logic                                   |             |
| DataIn    | in        | std_logic_vector(DATA_BITS - 1 downto 0)    |             |
| Count     | out       | std_logic_vector(COUNTER_BITS - 1 downto 0) |             |
| Sum       | out       | std_logic_vector(COUNTER_BITS - 1 downto 0) |             |
| Average   | out       | std_logic_vector(COUNTER_BITS - 1 downto 0) |             |
| Valid     | out       | std_logic                                   |             |
## Signals

| Name       | Type                                        | Description |
| ---------- | ------------------------------------------- | ----------- |
| DataIn_us  | unsigned(DataIn'range)                      |             |
| Counter_i  | std_logic_vector(COUNTER_BITS - 1 downto 0) |             |
| Counter_us | unsigned(COUNTER_BITS - 1 downto 0)         |             |
| Sum_i      | std_logic_vector(COUNTER_BITS - 1 downto 0) |             |
| Sum_us     | unsigned(COUNTER_BITS - 1 downto 0)         |             |
| Quotient   | std_logic_vector(COUNTER_BITS - 1 downto 0) |             |
| Valid_i    | std_logic                                   |             |
| Count_d    | T_COUNT_VECTOR(DELAY downto 0)              |             |
| Sum_d      | T_SUM_VECTOR(DELAY downto 0)                |             |
## Constants

| Name  | Type     | Value             | Description |
| ----- | -------- | ----------------- | ----------- |
| DELAY | positive |  COUNTER_BITS - 1 |             |
## Types

| Name           | Type                                                                    | Description |
| -------------- | ----------------------------------------------------------------------- | ----------- |
| T_SUM_VECTOR   | array(natural range <>) of std_logic_vector(COUNTER_BITS - 1 downto 0)  |             |
| T_COUNT_VECTOR | array(natural range <>) of std_logic_vector(COUNTER_BITS - 1 downto 0)  |             |
## Processes
- unnamed: ( Clock )
## Instantiations

- div: PoC.arith_div
