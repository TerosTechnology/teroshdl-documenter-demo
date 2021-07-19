# Entity: sort_lru_list

- **File**: sort_lru_list.vhdl
## Diagram

![Diagram](sort_lru_list.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:          Patrick Lehmann
                  Martin Zabel
Entity:           List storing key-value pairs in recently-used order.
Description:
-------------------------------------
List storing ``(key, value)`` pairs. The least-recently inserted pair is
outputed on ``DataOut`` if ``Valid = '1'``. If ``Valid = '0'``, then the list
empty.
The inputs ``Insert``, ``Remove``, ``DataIn``, and ``Reset`` are synchronous
to the rising-edge of the clock ``clock``. All control signals are high-active.
Supported operations:
 * **Insert:** Insert ``DataIn`` as  recently used ``(key, value)`` pair. If
   key is already within the list, then the corresponding value is updated and
   the pair is moved to the recently used position.
 * **Remove:** Remove ``(key, value)`` pair with the given key. The list is not
   modified if key is not within the list.
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

| Generic name     | Type             | Value                        | Description |
| ---------------- | ---------------- | ---------------------------- | ----------- |
| ELEMENTS         | positive         | 16                           |             |
| KEY_BITS         | positive         | 4                            |             |
| DATA_BITS        | positive         | 8                            |             |
| INITIAL_ELEMENTS | T_SLM            | (0 to 15 => (0 to 7 => '0')) |             |
| INITIAL_VALIDS   | std_logic_vector | (0 to 15 => '0')             |             |
## Ports

| Port name | Direction | Type                                     | Description |
| --------- | --------- | ---------------------------------------- | ----------- |
| Clock     | in        | std_logic                                |             |
| Reset     | in        | std_logic                                |             |
| Insert    | in        | std_logic                                |             |
| Remove    | in        | std_logic                                |             |
| DataIn    | in        | std_logic_vector(DATA_BITS - 1 downto 0) |             |
| Valid     | out       | std_logic                                |             |
| DataOut   | out       | std_logic_vector(DATA_BITS - 1 downto 0) |             |
## Signals

| Name             | Type                                  | Description |
| ---------------- | ------------------------------------- | ----------- |
| NewElementsUp    | T_ELEMENT_VECTOR(ELEMENTS downto 0)   |             |
| ElementsUp       | T_ELEMENT_VECTOR(ELEMENTS downto 0)   |             |
| ElementsDown     | T_ELEMENT_VECTOR(ELEMENTS downto 0)   |             |
| ValidsUp         | std_logic_vector(ELEMENTS downto 0)   |             |
| ValidsDown       | std_logic_vector(ELEMENTS downto 0)   |             |
| Unequal          | std_logic_vector(ELEMENTS-1 downto 0) |             |
| MovesDown        | std_logic_vector(ELEMENTS downto 0)   |             |
| MovesUp          | std_logic_vector(ELEMENTS downto 0)   |             |
| DataOutDown      | T_ELEMENT_VECTOR(ELEMENTS downto 0)   |             |
| MovesUpCond      | std_logic_vector(ELEMENTS downto 0)   |             |
| MovesDownCond    | std_logic_vector(ELEMENTS downto 0)   |             |
| MovesDownCondRev | std_logic_vector(ELEMENTS downto 0)   |             |
| MovesDownRev     | std_logic_vector(ELEMENTS downto 0)   |             |
## Types

| Name             | Type                                   | Description |
| ---------------- | -------------------------------------- | ----------- |
| T_ELEMENT_VECTOR | array (natural range <>) of T_ELEMENT  |             |
## Instantiations

- MovesUpProp: poc.arith_prefix_and
- MovesDownProp: poc.arith_prefix_and
