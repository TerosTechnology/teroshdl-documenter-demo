# Entity: misc_Delay

- **File**: misc_Delay.vhdl
## Diagram

![Diagram](misc_Delay.svg "Diagram")
## Description

 EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
 vim: tabstop=2:shiftwidth=2:noexpandtab
 kate: tab-width 2; replace-tabs off; indent-width 2;
 =============================================================================
 Authors:					Patrick Lehmann

 Entity:					TODO

 Description:
 -------------------------------------
 .. TODO:: No documentation available.

 License:
 =============================================================================
 Copyright 2007-2015 Technische Universitaet Dresden - Germany
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

| Generic name | Type     | Value | Description                              |
| ------------ | -------- | ----- | ---------------------------------------- |
| BITS         | positive |       |                                          |
| TAPS         | T_NATVEC |       |  select one or multiple delay tap points |
## Ports

| Port name | Direction | Type                                               | Description                                     |
| --------- | --------- | -------------------------------------------------- | ----------------------------------------------- |
| Clock     | in        | std_logic                                          |  clock                                          |
| Reset     | in        | std_logic                                          |  reset; avoid reset to enable SRL16/SRL32 usage |
| Enable    | in        | std_logic                                          |  enable                                         |
| DataIn    | in        | std_logic_vector(BITS - 1 downto 0)                |  data to delay                                  |
| DataOut   | out       | T_SLM(TAPS'length - 1 downto 0, BITS - 1 downto 0) |  delayed ouputs, tapped at TAPS(i)              |
## Signals

| Name        | Type                                                                                   | Description |
| ----------- | -------------------------------------------------------------------------------------- | ----------- |
| Shifter_nxt | T_DELAY_VECTOR(MAX_DELAY downto 0)                                                     |             |
| Shifter_d   | T_DELAY_VECTOR(MAX_DELAY - 1 downto 0)                                                 |             |
| DataOut_i   | T_SLM(TAPS'length - 1 downto 0,<br><span style="padding-left:20px"> BITS - 1 downto 0) |             |
## Constants

| Name      | Type    | Value       | Description |
| --------- | ------- | ----------- | ----------- |
| MAX_DELAY | natural |  imax(TAPS) |             |
## Types

| Name           | Type                                                             | Description |
| -------------- | ---------------------------------------------------------------- | ----------- |
| T_DELAY_VECTOR | array (natural range <>) of std_logic_vector(BITS - 1 downto 0)  |             |
## Processes
- unnamed: ( Clock )
