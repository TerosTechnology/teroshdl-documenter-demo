# Entity: arith_sqrt

- **File**: arith_sqrt.vhdl
## Diagram

![Diagram](arith_sqrt.svg "Diagram")
## Description

EMACS settings: -*-	tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:					Thomas B. Preußer
Entity:					Iterative Square Root Extractor.
Description:
-------------------------------------
Iterative Square Root Extractor.
Its computation requires (N+1)/2 steps for an argument bit width of N.
License:
=============================================================================
Copyright 2007-2014 Technische Universität Dresden - Germany,
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

| Generic name | Type     | Value | Description                            |
| ------------ | -------- | ----- | -------------------------------------- |
| N            | positive |       | := 8									 -- Bit Width of Argument |
## Ports

| Port name | Direction | Type                               | Description         |
| --------- | --------- | ---------------------------------- | ------------------- |
| rst       | in        | std_logic                          | Reset (synchronous) |
| clk       | in        | std_logic                          | Clock               |
| arg       | in        | std_logic_vector(N-1 downto 0)     | Radicand            |
| start     | in        | std_logic                          | Start Strobe        |
| sqrt      | out       | std_logic_vector((N-1)/2 downto 0) | Result              |
| rdy       | out       | std_logic                          | Ready / Done        |
## Signals

| Name | Type                         | Description          |
| ---- | ---------------------------- | -------------------- |
| Rmd  | unsigned(N+STEPS-1 downto 0) | Remainder / Result   |
| Vld  | unsigned(STEPS-1 downto 0)   | Result Flags         |
| Res  | unsigned(STEPS-1 downto 0)   | Extracted Result     |
| diff | unsigned(STEPS+1 downto 0)   | Tentative Difference |
## Constants

| Name  | Type     | Value    | Description |
| ----- | -------- | -------- | ----------- |
| STEPS | positive |  (N+1)/2 |             |
## Processes
- unnamed: ( clk )
