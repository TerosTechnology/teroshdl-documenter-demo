# Entity: fifo_glue
## Diagram
![Diagram](fifo_glue.svg "Diagram")
## Description
EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:					Thomas B. Preusser
Entity:					Minimal FIFO, common clock (cc), pipelined interface, first-word-fall-through mode
Description:
-------------------------------------
Its primary use is the decoupling of enable domains in a processing
pipeline. Data storage is limited to two words only so as to allow both
the ``ful``  and the ``vld`` indicators to be driven by registers.
License:
=============================================================================
Copyright 2007-2015 Technische Universitaet Dresden - Germany
                    Chair of VLSI-Design, Diagnostics and Architecture
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
| D_BITS       | positive |       | Data Width  |
## Ports
| Port name | Direction | Type                                | Description       |
| --------- | --------- | ----------------------------------- | ----------------- |
| clk       | in        | std_logic                           | Clock             |
| rst       | in        | std_logic                           | Synchronous Reset |
| put       | in        | std_logic                           | Put Value         |
| di        | in        | std_logic_vector(D_BITS-1 downto 0) | Data Input        |
| ful       | out       | std_logic                           | Full              |
| vld       | out       | std_logic                           | Data Available    |
| do        | out       | std_logic_vector(D_BITS-1 downto 0) | Data Output       |
| got       | in        | std_logic                           | Data Consumed     |
## Signals
| Name   | Type                                | Description     |
| ------ | ----------------------------------- | --------------- |
| A      | std_logic_vector(D_BITS-1 downto 0) |                 |
|  B     | std_logic_vector(D_BITS-1 downto 0) |                 |
| Full   | std_logic                           | State Registers |
|  Avail | std_logic                           | State Registers |
## Processes
- unnamed: _( clk )_

