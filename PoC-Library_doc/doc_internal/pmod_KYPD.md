# Entity: pmod_KYPD

- **File**: pmod_KYPD.vhdl
## Diagram

![Diagram](pmod_KYPD.svg "Diagram")
## Description

 EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
 vim: tabstop=2:shiftwidth=2:noexpandtab
 kate: tab-width 2; replace-tabs off; indent-width 2;
 =============================================================================
 Authors:				 	Patrick Lehmann

 Entity:				 	Digilent Peripherial Module: 4x4 Keypad (Pmod_KYPD)

 Description:
 -------------------------------------
 This module drives a 4-bit one-cold encoded column vector to read back a
 4-bit rows vector. By scanning column-by-column it's possible to extract
 the current button state of the whole keypad. This wrapper converts the
 high-active signals from :doc:`PoC.io.KeypadScanner <../io_KeyPadScanner>`
 to low-active signals for the pmod. An additional debounce circuit filters
 the button signals. The scan frequency and bounce time can be configured.

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
## Generics

| Generic name | Type | Value   | Description |
| ------------ | ---- | ------- | ----------- |
| CLOCK_FREQ   | FREQ | 100 MHz |             |
| SCAN_FREQ    | FREQ | 1 kHz   |             |
| BOUNCE_TIME  | time | 10 ms   |             |
## Ports

| Port name | Direction | Type                         | Description      |
| --------- | --------- | ---------------------------- | ---------------- |
| Clock     | in        | std_logic                    |                  |
| Reset     | in        | std_logic                    |                  |
| Keys      | out       | T_PMOD_KYPD_KEYPAD           | Matrix interface |
| Columns_n | out       | std_logic_vector(3 downto 0) | KeyPad interface |
| Rows_n    | in        | std_logic_vector(3 downto 0) |                  |
## Signals

| Name             | Type                                                              | Description |
| ---------------- | ----------------------------------------------------------------- | ----------- |
| ColumnVector     | std_logic_vector(3 downto 0)                                      |             |
| RowVector        | std_logic_vector(3 downto 0)                                      |             |
| KeyPadMatrix     | T_SLM(3 downto 0,<br><span style="padding-left:20px"> 3 downto 0) |             |
| KeyPadMatrix_slv | std_logic_vector(15 downto 0)                                     |             |
| KeyPadVector     | std_logic_vector(15 downto 0)                                     |             |
| KeyPad           | T_SLM(3 downto 0,<br><span style="padding-left:20px"> 3 downto 0) |             |
## Instantiations

- scanner: PoC.io_KeyPadScanner
**Description**
 initialize a 4x4 matrix scanner

- debounce: PoC.io_Debounce
