# Entity: sort_lru_cache

- **File**: sort_lru_cache.vhdl
## Diagram

![Diagram](sort_lru_cache.svg "Diagram")
## Description

 EMACS settings: -*-	tab-width: 2; indent-tabs-mode: t -*-
 vim: tabstop=2:shiftwidth=2:noexpandtab
 kate: tab-width 2; replace-tabs off; indent-width 2;
 =============================================================================
 Authors:         Patrick Lehmann
                  Martin Zabel

 Entity:          Optimized LRU list implementation for Caches.

 Description:
 -------------------------------------
 This is an optimized implementation of ``sort_lru_list`` to be used for caches.
 Only keys are stored within this list, and these keys are the index of the
 cache lines. The list initially contains all indizes from 0 to ELEMENTS-1.
 The least-recently used index ``KeyOut`` is always valid.

 The first outputed least-recently used index will be ELEMENTS-1.

 The inputs ``Insert``, ``Free``, ``KeyIn``, and ``Reset`` are synchronous to the
 rising-edge of the clock ``clock``. All control signals are high-active.

 Supported operations:
  * **Insert:** Mark index ``KeyIn`` as recently used, e.g., when a cache-line
    was accessed.
  * **Free:** Mark index ``KeyIn`` as least-recently used. Apply this operation,
    when a cache-line gets invalidated.

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
| ELEMENTS     | positive | 32    |             |
## Ports

| Port name | Direction | Type                                                | Description |
| --------- | --------- | --------------------------------------------------- | ----------- |
| Clock     | in        | std_logic                                           |             |
| Reset     | in        | std_logic                                           |             |
| Insert    | in        | std_logic                                           |             |
| Free      | in        | std_logic                                           |             |
| KeyIn     | in        | std_logic_vector(log2ceilnz(ELEMENTS) - 1 downto 0) |             |
| KeyOut    | out       | std_logic_vector(log2ceilnz(ELEMENTS) - 1 downto 0) |             |
## Signals

| Name             | Type                                  | Description |
| ---------------- | ------------------------------------- | ----------- |
| NewElement       | T_ELEMENT                             |             |
| ElementsUp       | T_ELEMENT_VECTOR(ELEMENTS downto 0)   |             |
| ElementsDown     | T_ELEMENT_VECTOR(ELEMENTS downto 0)   |             |
| MovesDown        | std_logic_vector(ELEMENTS downto 0)   |             |
| MovesUp          | std_logic_vector(ELEMENTS downto 0)   |             |
| UnEqual          | std_logic_vector(ELEMENTS-1 downto 0) |             |
| MovesUpCond      | std_logic_vector(ELEMENTS downto 0)   |             |
| MovesDownCond    | std_logic_vector(ELEMENTS downto 0)   |             |
| MovesDownCondRev | std_logic_vector(ELEMENTS downto 0)   |             |
| MovesDownRev     | std_logic_vector(ELEMENTS downto 0)   |             |
## Constants

| Name     | Type     | Value                 | Description |
| -------- | -------- | --------------------- | ----------- |
| KEY_BITS | positive |  log2ceilnz(ELEMENTS) |             |
## Types

| Name             | Type                                   | Description |
| ---------------- | -------------------------------------- | ----------- |
| T_ELEMENT_VECTOR | array (natural range <>) of T_ELEMENT  |             |
## Instantiations

- MovesUpProp: poc.arith_prefix_and
- MovesDownProp: poc.arith_prefix_and
