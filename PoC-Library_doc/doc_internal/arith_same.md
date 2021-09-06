# Entity: arith_same

- **File**: arith_same.vhdl
## Diagram

![Diagram](arith_same.svg "Diagram")
## Description

 EMACS settings: -*-	tab-width: 2; indent-tabs-mode: t -*-
 vim: tabstop=2:shiftwidth=2:noexpandtab
 kate: tab-width 2; replace-tabs off; indent-width 2;
 =============================================================================
 Authors:					Thomas B. Preusser

 Entity:					This module detects whether all bit positions of a std_logic_vector have the same value.

 Description:
 -------------------------------------
 This circuit may, for instance, be used to detect the first sign change
 and, thus, the range of a two's complement number.

 These components may be chained by using the output of the predecessor as
 guard input. This chaining allows to have intermediate results available
 while still ensuring the use of a fast carry chain on supporting FPGA
 architectures. When chaining, make sure to overlap both vector slices by one
 bit position as to avoid an undetected sign change between the slices.

 License:
 =============================================================================
 Copyright 2007-2015 Technische Universität Dresden - Germany,
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

| Generic name | Type     | Value | Description  |
| ------------ | -------- | ----- | ------------ |
| N            | positive |       |  Input width |
## Ports

| Port name | Direction | Type                           | Description             |
| --------- | --------- | ------------------------------ | ----------------------- |
| g         | in        | std_logic                      |  Guard Input (!g => !y) |
| x         | in        | std_logic_vector(N-1 downto 0) |  Input Vector           |
| y         | out       | std_logic                      |  All-same Output        |
## Signals

| Name | Type                           | Description |
| ---- | ------------------------------ | ----------- |
| p    | std_logic_vector(M-1 downto 0) |             |
## Constants

| Name     | Type          | Value                | Description           |
| -------- | ------------- | -------------------- | --------------------- |
| DEV_INFO | T_DEVICE_INFO |  DEVICE_INFO         |                       |
| K        | positive      |  DEV_INFO.LUT_FanIn  |  LUT Fanin            |
| M        | positive      |  (N-2+1/N)/(K-1) + 1 |  Required Stage Count |
