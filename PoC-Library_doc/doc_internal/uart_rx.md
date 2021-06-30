# Entity: uart_rx

## Diagram

![Diagram](uart_rx.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:        Thomas B. Preusser
Entity:				 Universal Asynchronous Receiver Transmitter (UART) - Receiver
Description:
-------------------------------------
:abbr:`UART (Universal Asynchronous Receiver Transmitter)` Receiver:
1 Start + 8 Data + 1 Stop
License:
=============================================================================
Copyright 2008-2016 Technische Universitaet Dresden - Germany
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

| Generic name | Type    | Value | Description                               |
| ------------ | ------- | ----- | ----------------------------------------- |
| SYNC_DEPTH   | natural | 2     | use zero for already clock-synchronous rx |
## Ports

| Port name | Direction | Type                         | Description                             |
| --------- | --------- | ---------------------------- | --------------------------------------- |
| clk       | in        | std_logic                    | Global Control                          |
| rst       | in        | std_logic                    |                                         |
| bclk_x8   | in        | std_logic                    | bit clock, eight strobes per bit length |
| rx        | in        | std_logic                    |                                         |
| do        | out       | std_logic_vector(7 downto 0) | Byte Stream Output                      |
| stb       | out       | std_logic                    |                                         |
## Signals

| Name | Type                         | Description                                                                                                                                                                                                                                                                               |
| ---- | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| rxs  | std_logic                    |                                                                                                                                                                                                                                                                                           |
| Buf  | std_logic_vector(9 downto 0) |                Buf        Cnt  Vld  Idle     "---------0"    X    0  Start    "0111111111"  5->16  0   -- 1.5 bit length after start of start bit  Recv     "dcba011111"  9->16  0   -- shifting left to right (LSB first)  Done     "1hgfedcba0"    X    1   -- Output strobeData buffer |
| Cnt  | unsigned(4 downto 0)         | Bit clock counter: 8 ticks per bit                                                                                                                                                                                                                                                        |
| Vld  | std_logic                    | Output strobe                                                                                                                                                                                                                                                                             |
## Processes
- unnamed: ( clk )
**Description**
Reception state

## Instantiations

- sync: PoC.sync_Bits
