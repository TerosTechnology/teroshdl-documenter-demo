# Entity: arith_counter_free

- **File**: arith_counter_free.vhdl
## Diagram

![Diagram](arith_counter_free.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:				 	Thomas B. Preusser
Entity:				 	Poc.arith_counter_free
Description:
-------------------------------------
Implements a free-running counter that generates a strobe signal every
DIVIDER-th cycle the increment input was asserted. There is deliberately no
output or specification of the counter value so as to allow an implementation
to optimize as much as possible.
The implementation guarantees a strobe output directly from a register. It is
asserted exactly for one clock after DIVIDER cycles of an asserted increment
input have been observed.
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

| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| DIVIDER      | positive |       |             |
## Ports

| Port name | Direction | Type      | Description          |
| --------- | --------- | --------- | -------------------- |
| clk       | in        | std_logic | Global Control       |
| rst       | in        | std_logic |                      |
| inc       | in        | std_logic |                      |
| stb       | out       | std_logic | End-of-Period Strobe |
