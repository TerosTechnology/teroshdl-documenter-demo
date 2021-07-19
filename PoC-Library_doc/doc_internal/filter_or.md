# Entity: filter_or

- **File**: filter_or.vhdl
## Diagram

![Diagram](filter_or.svg "Diagram")
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
Copyright 2007-2014 Technische Universitaet Dresden - Germany
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

| Generic name   | Type      | Value | Description |
| -------------- | --------- | ----- | ----------- |
| TAPS           | positive  | 4     |             |
| INIT           | std_logic | '1'   |             |
| ADD_OUTPUT_REG | boolean   | FALSE |             |
## Ports

| Port name | Direction | Type      | Description     |
| --------- | --------- | --------- | --------------- |
| Clock     | in        | std_logic | clock           |
| DataIn    | in        | std_logic | data to filter  |
| DataOut   | out       | std_logic | filtered signal |
## Signals

| Name      | Type                                | Description |
| --------- | ----------------------------------- | ----------- |
| Delays    | std_logic_vector(TAPS - 1 downto 0) |             |
| FilterOut | std_logic                           |             |
