# Entity: sortnet_Transform

## Diagram

![Diagram](sortnet_Transform.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:					Patrick Lehmann
Entity:					Sorting Network: Data structure transformation
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
| ROWS         | positive | 16    |             |
| COLUMNS      | positive | 4     |             |
| DATA_BITS    | positive | 8     |             |
## Ports

| Port name | Direction | Type                                                | Description |
| --------- | --------- | --------------------------------------------------- | ----------- |
| Clock     | in        | std_logic                                           |             |
| Reset     | in        | std_logic                                           |             |
| In_Valid  | in        | std_logic                                           |             |
| In_Data   | in        | T_SLM(ROWS - 1 downto 0, DATA_BITS - 1 downto 0)    |             |
| In_SOF    | in        | std_logic                                           |             |
| In_EOF    | in        | std_logic                                           |             |
| Out_Valid | out       | std_logic                                           |             |
| Out_Data  | out       | T_SLM(COLUMNS - 1 downto 0, DATA_BITS - 1 downto 0) |             |
| Out_SOF   | out       | std_logic                                           |             |
| Out_EOF   | out       | std_logic                                           |             |
## Signals

| Name             | Type                                       | Description |
| ---------------- | ------------------------------------------ | ----------- |
| DataIn           | T_DATA_VECTOR(ROWS - 1 downto 0)           |             |
| ColumnWriter_rst | std_logic                                  |             |
| ColumnWriter_us  | unsigned(log2ceilnz(COLUMNS) - 1 downto 0) |             |
| ColumnWriter_ov  | std_logic                                  |             |
| InputBuffer      | T_DATA_MATRIX(COLUMNS - 1 downto 0)        |             |
| RowReader_en_r   | std_logic                                  |             |
| RowReader_rst    | std_logic                                  |             |
| RowReader_en     | std_logic                                  |             |
| RowReader_us     | unsigned(log2ceilnz(ROWS) - 1 downto 0)    |             |
| RowReader_ov     | std_logic                                  |             |
## Types

| Name          | Type | Description |
| ------------- | ---- | ----------- |
| T_DATA_VECTOR |      |             |
| T_DATA_MATRIX |      |             |
## Functions
- to_dv <font id="function_arguments">(slm : T_SLM) </font> <font id="function_return">return T_DATA_VECTOR </font>
## Processes
- unnamed: ( Clock )
- unnamed: ( InputBuffer, RowReader_us )
