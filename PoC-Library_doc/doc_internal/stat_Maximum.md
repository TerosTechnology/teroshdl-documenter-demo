# Entity: stat_Maximum

- **File**: stat_Maximum.vhdl
## Diagram

![Diagram](stat_Maximum.svg "Diagram")
## Description

 EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
 vim: tabstop=2:shiftwidth=2:noexpandtab
 kate: tab-width 2; replace-tabs off; indent-width 2;
 =============================================================================
 Authors:					Patrick Lehmann

 Entity:					Counts the most significant data words

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

| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| DEPTH        | positive | 8     |             |
| DATA_BITS    | positive | 16    |             |
| COUNTER_BITS | positive | 16    |             |
## Ports

| Port name | Direction | Type                                                 | Description |
| --------- | --------- | ---------------------------------------------------- | ----------- |
| Clock     | in        | std_logic                                            |             |
| Reset     | in        | std_logic                                            |             |
| Enable    | in        | std_logic                                            |             |
| DataIn    | in        | std_logic_vector(DATA_BITS - 1 downto 0)             |             |
| Valids    | out       | std_logic_vector(DEPTH - 1 downto 0)                 |             |
| Maximums  | out       | T_SLM(DEPTH - 1 downto 0, DATA_BITS - 1 downto 0)    |             |
| Counts    | out       | T_SLM(DEPTH - 1 downto 0, COUNTER_BITS - 1 downto 0) |             |
## Signals

| Name          | Type                                 | Description                                                                                                                                                                        |
| ------------- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DataIn_us     | unsigned(DataIn'range)               |                                                                                                                                                                                    |
| TagHit        | std_logic_vector(DEPTH - 1 downto 0) |                                                                                                                                                                                    |
| MaximumHit    | std_logic_vector(DEPTH - 1 downto 0) |                                                                                                                                                                                    |
| TagMemory     | T_TAG_MEMORY(DEPTH - 1 downto 0)     |                                                                                                                                                                                    |
| CounterMemory | T_COUNTER_MEMORY(DEPTH - 1 downto 0) |                                                                                                                                                                                    |
| MaximumIndex  | std_logic_vector(DEPTH - 1 downto 0) | ((DEPTH - 1) => '1', others => '0'); -- WORKAROUND: GHDL says  not static choice exclude others choice;  non-locally static choice for an aggregate is allowed only if only choice |
| ValidMemory   | std_logic_vector(DEPTH - 1 downto 0) |                                                                                                                                                                                    |
## Types

| Name             | Type                                                            | Description |
| ---------------- | --------------------------------------------------------------- | ----------- |
| T_TAG_MEMORY     | array(natural range <>) of unsigned(DATA_BITS - 1 downto 0)     |             |
| T_COUNTER_MEMORY | array(natural range <>) of unsigned(COUNTER_BITS - 1 downto 0)  |             |
## Functions
- to_slm <font id="function_arguments">(usv : T_TAG_MEMORY) </font> <font id="function_return">return T_SLM </font>
**Description**
 create matrix from vector-vector

- to_slm <font id="function_arguments">(usv : T_COUNTER_MEMORY) </font> <font id="function_return">return T_SLM </font>
## Processes
- unnamed: ( Clock )
