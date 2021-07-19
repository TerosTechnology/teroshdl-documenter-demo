# Entity: bus_Arbiter

- **File**: bus_Arbiter.vhdl
## Diagram

![Diagram](bus_Arbiter.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:				 	Patrick Lehmann
Entity:				 	Generic arbiter
Description:
-------------------------------------
This module implements a generic arbiter. It currently supports the
following arbitration strategies:
* Round Robin (RR)
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

| Generic name | Type     | Value    | Description |
| ------------ | -------- | -------- | ----------- |
| STRATEGY     | string   | "RR"     | RR, LOT     |
| PORTS        | positive | 1        |             |
| WEIGHTS      | T_INTVEC | (0 => 1) |             |
| OUTPUT_REG   | boolean  | TRUE     |             |
## Ports

| Port name      | Direction | Type                                             | Description |
| -------------- | --------- | ------------------------------------------------ | ----------- |
| Clock          | in        | std_logic                                        |             |
| Reset          | in        | std_logic                                        |             |
| Arbitrate      | in        | std_logic                                        |             |
| Request_Vector | in        | std_logic_vector(PORTS - 1 downto 0)             |             |
| Arbitrated     | out       | std_logic                                        |             |
| Grant_Vector   | out       | std_logic_vector(PORTS - 1 downto 0)             |             |
| Grant_Index    | out       | std_logic_vector(log2ceilnz(PORTS) - 1 downto 0) |             |
