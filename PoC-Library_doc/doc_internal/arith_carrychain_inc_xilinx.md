# Entity: arith_carrychain_inc_xilinx
## Diagram
![Diagram](arith_carrychain_inc_xilinx.svg "Diagram")
## Description
EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:					Patrick Lehmann
Entity:					Carry-chain abstraction for increment by one operations
Description:
-------------------------------------
License:
=============================================================================
Copyright 2007-2016 Technische Universitaet Dresden - Germany,
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
| BITS         | positive |       |             |
## Ports
| Port name | Direction | Type                                | Description |
| --------- | --------- | ----------------------------------- | ----------- |
| X         | in        | std_logic_vector(BITS - 1 downto 0) |             |
| CIn       | in        | std_logic                           |             |
| Y         | out       | std_logic_vector(BITS - 1 downto 0) |             |
## Signals
| Name | Type                            | Description |
| ---- | ------------------------------- | ----------- |
| ci   | std_logic_vector(BITS downto 0) |             |
| co   | std_logic_vector(BITS downto 0) |             |
