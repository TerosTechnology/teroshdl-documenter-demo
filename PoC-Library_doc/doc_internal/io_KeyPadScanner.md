# Entity: io_KeyPadScanner

- **File**: io_KeyPadScanner.vhdl
## Diagram

![Diagram](io_KeyPadScanner.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:				 	Patrick Lehmann
Entity:				 	Keypad button matrix scanner
Description:
-------------------------------------
This module drives a one-hot encoded column vector to read back a rows
vector. By scanning column-by-column it's possible to extract the current
button state of the whole keypad. The scanner uses high-active logic. The
keypad size and scan frequency can be configured. The outputed signal
matrix is not debounced.
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

| Generic name            | Type     | Value   | Description |
| ----------------------- | -------- | ------- | ----------- |
| CLOCK_FREQ              | FREQ     | 100 MHz |             |
| SCAN_FREQ               | FREQ     | 1 kHz   |             |
| ROWS                    | positive | 4       |             |
| COLUMNS                 | positive | 4       |             |
| ADD_INPUT_SYNCHRONIZERS | boolean  | TRUE    |             |
## Ports

| Port name    | Direction | Type                                           | Description      |
| ------------ | --------- | ---------------------------------------------- | ---------------- |
| Clock        | in        | std_logic                                      |                  |
| Reset        | in        | std_logic                                      |                  |
| KeyPadMatrix | out       | T_SLM(COLUMNS - 1 downto 0, ROWS - 1 downto 0) | Matrix interface |
| ColumnVector | out       | std_logic_vector(COLUMNS - 1 downto 0)         | KeyPad interface |
| RowVector    | in        | std_logic_vector(ROWS - 1 downto 0)            |                  |
## Signals

| Name            | Type                                                                               | Description |
| --------------- | ---------------------------------------------------------------------------------- | ----------- |
| ColumnTimer_rst | std_logic                                                                          |             |
| ColumnTimer_s   | signed(COLUMNTIMER_BITS - 1 downto 0)                                              |             |
| ColumnSelect_en | std_logic                                                                          |             |
| ColumnSelect_d  | std_logic_vector(COLUMNS - 1 downto 0)                                             |             |
| Rows_sync       | std_logic_vector(ROWS - 1 downto 0)                                                |             |
| KeyPadMatrix_r  | T_SLM(COLUMNS - 1 downto 0,<br><span style="padding-left:20px"> ROWS - 1 downto 0) |             |
## Constants

| Name             | Type     | Value                                                                                    | Description |
| ---------------- | -------- | ---------------------------------------------------------------------------------------- | ----------- |
| SHIFT_FREQ       | FREQ     |  SCAN_FREQ * COLUMNS                                                                     |             |
| COLUMNTIMER_MAX  | positive |  TimingToCycles(to_time(SHIFT_FREQ),<br><span style="padding-left:20px"> CLOCK_FREQ) - 1 |             |
| COLUMNTIMER_BITS | positive |  log2ceilnz(COLUMNTIMER_MAX) + 1                                                         |             |
