# Entity: sync_Command

- **File**: sync_Command.vhdl
## Diagram

![Diagram](sync_Command.svg "Diagram")
## Description

 EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
 vim: tabstop=2:shiftwidth=2:noexpandtab
 kate: tab-width 2; replace-tabs off; indent-width 2;
 =============================================================================
 Authors:         Patrick Lehmann
                  Steffen Koehler

 Entity:          Synchronizes a command signal across clock-domain boundaries

 Description:
 -------------------------------------
 This module synchronizes a vector of bits from clock-domain ``Clock1`` to
 clock-domain ``Clock2``. The clock-domain boundary crossing is done by a
 change comparator, a T-FF, two synchronizer D-FFs and a reconstructive
 XOR indicating a value change on the input. This changed signal is used
 to capture the input for the new output. A busy flag is additionally
 calculated for the input clock-domain. The output has strobe character
 and is reset to it's ``INIT`` value after one clock cycle.

 Constraints:
   This module uses sub modules which need to be constrained. Please
   attend to the notes of the instantiated sub modules.

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

| Generic name | Type              | Value                 | Description                                  |
| ------------ | ----------------- | --------------------- | -------------------------------------------- |
| BITS         | positive          | 8                     |  number of bit to be synchronized            |
| INIT         | std_logic_vector  | x"00000000"           |                                              |
| SYNC_DEPTH   | T_MISC_SYNC_DEPTH | T_MISC_SYNC_DEPTH'low |  generate SYNC_DEPTH many stages, at least 2 |
## Ports

| Port name | Direction | Type                                | Description             |
| --------- | --------- | ----------------------------------- | ----------------------- |
| Clock1    | in        | std_logic                           |  <Clock>  input clock   |
| Clock2    | in        | std_logic                           |  <Clock>  output clock  |
| Input     | in        | std_logic_vector(BITS - 1 downto 0) |  @Clock1: input vector  |
| Output    | out       | std_logic_vector(BITS - 1 downto 0) |  @Clock2: output vector |
| Busy      | out       | std_logic                           |  @Clock1: busy bit      |
| Changed   | out       | std_logic                           |  @Clock2: changed bit   |
## Signals

| Name           | Type                                | Description |
| -------------- | ----------------------------------- | ----------- |
| D0             | std_logic                           |             |
| D1             | std_logic_vector(BITS - 1 downto 0) |             |
| T2             | std_logic                           |             |
| D3             | std_logic                           |             |
| D4             | std_logic                           |             |
| D5             | std_logic_vector(BITS - 1 downto 0) |             |
| IsCommand_Clk1 | std_logic                           |             |
| Changed_Clk1   | std_logic                           |             |
| Changed_Clk2   | std_logic                           |             |
| Busy_i         | std_logic                           |             |
| syncClk1_In    | std_logic                           |             |
| syncClk1_Out   | std_logic                           |             |
| syncClk2_In    | std_logic                           |             |
| syncClk2_Out   | std_logic                           |             |
## Constants

| Name   | Type             | Value                             | Description |
| ------ | ---------------- | --------------------------------- | ----------- |
| INIT_I | std_logic_vector |  descend(INIT)(BITS - 1 downto 0) |             |
## Processes
- unnamed: ( Clock1 )
- unnamed: ( Clock2 )
**Description**
 D-FF for level change detection (both edges) 
## Instantiations

- syncClk2: PoC.sync_Bits
- syncClk1: PoC.sync_Bits
