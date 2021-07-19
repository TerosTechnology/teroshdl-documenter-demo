# Entity: uart_tx

- **File**: uart_tx.vhdl
## Diagram

![Diagram](uart_tx.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:					Thomas B. Preusser
Entity:					Universal Asynchronous Receiver Transmitter (UART) - Transmitter
Description:
-------------------------------------
:abbr:`UART (Universal Asynchronous Receiver Transmitter)` Transmitter:
1 Start + 8 Data + 1 Stop
License:
=============================================================================
Copyright 2007-2015 Technische Universitaet Dresden - Germany
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
## Ports

| Port name | Direction | Type                         | Description                           |
| --------- | --------- | ---------------------------- | ------------------------------------- |
| clk       | in        | std_logic                    | Global Control                        |
| rst       | in        | std_logic                    |                                       |
| bclk      | in        | std_logic                    | bit clock, one strobe each bit length |
| tx        | out       | std_logic                    |                                       |
| di        | in        | std_logic_vector(7 downto 0) | Byte Stream Input                     |
| put       | in        | std_logic                    |                                       |
| ful       | out       | std_logic                    |                                       |
## Signals

| Name | Type                         | Description |
| ---- | ---------------------------- | ----------- |
| Buf  | std_logic_vector(9 downto 0) |             |
| Cnt  | signed(4 downto 0)           |             |
## Processes
- unnamed: ( clk )
