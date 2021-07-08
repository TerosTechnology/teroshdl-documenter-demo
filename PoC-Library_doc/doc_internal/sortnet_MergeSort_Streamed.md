# Entity: sortnet_MergeSort_Streamed

## Diagram

![Diagram](sortnet_MergeSort_Streamed.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:					Patrick Lehmann
Entity:					Sorting Network: Streaming MergeSort
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
| FIFO_DEPTH   | positive | 32    |             |
| KEY_BITS     | positive | 32    |             |
| DATA_BITS    | positive | 32    |             |
## Ports

| Port name | Direction | Type                                     | Description |
| --------- | --------- | ---------------------------------------- | ----------- |
| Clock     | in        | std_logic                                |             |
| Reset     | in        | std_logic                                |             |
| Inverse   | in        | std_logic                                |             |
| In_Valid  | in        | std_logic                                |             |
| In_Data   | in        | std_logic_vector(DATA_BITS - 1 downto 0) |             |
| In_SOF    | in        | std_logic                                |             |
| In_IsKey  | in        | std_logic                                |             |
| In_EOF    | in        | std_logic                                |             |
| In_Ack    | out       | std_logic                                |             |
| Out_Sync  | out       | std_logic                                |             |
| Out_Valid | out       | std_logic                                |             |
| Out_Data  | out       | std_logic_vector(DATA_BITS - 1 downto 0) |             |
| Out_SOF   | out       | std_logic                                |             |
| Out_IsKey | out       | std_logic                                |             |
| Out_EOF   | out       | std_logic                                |             |
| Out_Ack   | in        | std_logic                                |             |
## Signals

| Name           | Type        | Description |
| -------------- | ----------- | ----------- |
| FIFO_sel_r     | std_logic   |             |
| FIFO_0_put     | std_logic   |             |
| FIFO_0_DataIn  | T_FIFO_DATA |             |
| FIFO_0_Full    | std_logic   |             |
| FIFO_0_got     | std_logic   |             |
| FIFO_0_DataOut | T_FIFO_DATA |             |
| FIFO_0_Valid   | std_logic   |             |
| FIFO_1_put     | std_logic   |             |
| FIFO_1_DataIn  | T_FIFO_DATA |             |
| FIFO_1_Full    | std_logic   |             |
| FIFO_1_got     | std_logic   |             |
| FIFO_1_DataOut | T_FIFO_DATA |             |
| FIFO_1_Valid   | std_logic   |             |
| Greater        | std_logic   |             |
| Switch_d       | std_logic   |             |
| Switch_en      | std_logic   |             |
| Switch_r       | std_logic   |             |
| Switch         | std_logic   |             |
| State          | T_STATE     |             |
| NextState      | T_STATE     |             |
## Constants

| Name           | Type     | Value          | Description |
| -------------- | -------- | -------------- | ----------- |
| DATA_SOF_BIT   | natural  |  DATA_BITS + 0 |             |
| DATA_ISKEY_BIT | natural  |  DATA_BITS + 1 |             |
| DATA_EOF_BIT   | natural  |  DATA_BITS + 2 |             |
| FIFO_BITS      | positive |  DATA_BITS + 3 |             |
## Types

| Name    | Type                                                                                                                                                               | Description |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| T_STATE | (ST_IDLE,<br><span style="padding-left:20px"> ST_MERGE,<br><span style="padding-left:20px"> ST_EMPTY_FIFO_0,<br><span style="padding-left:20px"> ST_EMPTY_FIFO_1)  |             |
## Processes
- unnamed: ( Clock )
- unnamed: ( State, FIFO_0_Valid, FIFO_0_DataOut, FIFO_1_Valid, FIFO_1_DataOut, Switch, Out_Ack )
## Instantiations

- FIFO_0: PoC.fifo_cc_got
- FIFO_1: PoC.fifo_cc_got
