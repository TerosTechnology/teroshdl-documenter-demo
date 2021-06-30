# Entity: io_TimingCounter

## Diagram

![Diagram](io_TimingCounter.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:				 	Patrick Lehmann
Entity:				 	optimized down-counter to control timings for low speed signals
Description:
-------------------------------------
This down-counter can be configured with a ``TIMING_TABLE`` (a ROM), from which
the initial counter value is loaded. The table index can be selected by
``Slot``. ``Timeout`` is a registered output. Up to 16 values fit into one ROM
consisting of ``log2ceilnz(imax(TIMING_TABLE)) + 1`` 6-input LUTs.
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

| Generic name | Type     | Value | Description  |
| ------------ | -------- | ----- | ------------ |
| TIMING_TABLE | T_NATVEC |       | timing table |
## Ports

| Port name | Direction | Type                                         | Description                                          |
| --------- | --------- | -------------------------------------------- | ---------------------------------------------------- |
| Clock     | in        | std_logic                                    | clock                                                |
| Enable    | in        | std_logic                                    | enable counter                                       |
| Load      | in        | std_logic                                    | load Timing Value from TIMING_TABLE selected by slot |
| Slot      | in        | natural range 0 to (TIMING_TABLE'length - 1) |                                                      |
| Timeout   | out       | std_logic                                    | timing reached                                       |
## Signals

| Name      | Type                          | Description |
| --------- | ----------------------------- | ----------- |
| Counter_s | signed(COUNTER_BITS downto 0) |             |
## Constants

| Name          | Type     | Value                       | Description |
| ------------- | -------- | --------------------------- | ----------- |
| TIMING_TABLE2 | T_INTVEC |  transform(TIMING_TABLE)    |             |
| TIMING_MAX    | natural  |  imax(TIMING_TABLE2)        |             |
| COUNTER_BITS  | natural  |  log2ceilnz(TIMING_MAX + 1) |             |
## Functions
- transform <font id="function_arguments">(vec : T_NATVEC) </font> <font id="function_return">return T_INTVEC </font>
## Processes
- unnamed: ( Clock )
