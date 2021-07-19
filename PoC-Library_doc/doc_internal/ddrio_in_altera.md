# Entity: ddrio_in_altera

- **File**: ddrio_in_altera.vhdl
## Diagram

![Diagram](ddrio_in_altera.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:					Martin Zabel
Entity:					Instantiates Chip-Specific DDR Input Registers for Altera FPGAs.
Description:
-------------------------------------
License:
=============================================================================
Copyright 2007-2015 Technische Universitaet Dresden - Germany,
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

| Generic name | Type       | Value       | Description |
| ------------ | ---------- | ----------- | ----------- |
| BITS         | positive   |             |             |
| INIT_VALUE   | bit_vector | x"FFFFFFFF" |             |
## Ports

| Port name   | Direction | Type                                | Description |
| ----------- | --------- | ----------------------------------- | ----------- |
| Clock       | in        | std_logic                           |             |
| ClockEnable | in        | std_logic                           |             |
| DataIn_high | out       | std_logic_vector(BITS - 1 downto 0) |             |
| DataIn_low  | out       | std_logic_vector(BITS - 1 downto 0) |             |
| Pad         | in        | std_logic_vector(BITS - 1 downto 0) |             |
