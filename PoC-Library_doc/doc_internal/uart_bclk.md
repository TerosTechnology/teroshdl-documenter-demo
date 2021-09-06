# Entity: uart_bclk

- **File**: uart_bclk.vhdl
## Diagram

![Diagram](uart_bclk.svg "Diagram")
## Description

 EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
 vim: tabstop=2:shiftwidth=2:noexpandtab
 kate: tab-width 2; replace-tabs off; indent-width 2;
 =============================================================================
 Authors:				 	Martin Zabel
									Patrick Lehmann

 Entity:				 	UART bit clock / baud rate generator

 Description:
 -------------------------------------
 .. TODO:: No documentation available.

 old comments:
   :abbr:`UART (Universal Asynchronous Receiver Transmitter)` BAUD rate generator
   bclk_r    = bit clock is rising
   bclk_x8_r = bit clock times 8 is rising


 License:
 =============================================================================
 Copyright 2008-2015 Technische Universitaet Dresden - Germany
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

| Generic name | Type | Value     | Description |
| ------------ | ---- | --------- | ----------- |
| CLOCK_FREQ   | FREQ | 100 MHz   |             |
| BAUDRATE     | BAUD | 115200 Bd |             |
## Ports

| Port name | Direction | Type      | Description |
| --------- | --------- | --------- | ----------- |
| clk       | in        | std_logic |             |
| rst       | in        | std_logic |             |
| bclk      | out       | std_logic |             |
| bclk_x8   | out       | std_logic |             |
## Signals

| Name        | Type                                         | Description       |
| ----------- | -------------------------------------------- | ----------------- |
| x8_cnt      | unsigned(BAUDRATE_COUNTER_BITS - 1 downto 0) |  registers        |
| x1_cnt      | unsigned(2 downto 0)                         |                   |
| x8_cnt_done | std_logic                                    |  control signals  |
| x1_cnt_done | std_logic                                    |                   |
| bclk_r      | std_logic                                    |                   |
| bclk_x8_r   | std_logic                                    |                   |
## Constants

| Name                   | Type     | Value                                                                                                 | Description |
| ---------------------- | -------- | ----------------------------------------------------------------------------------------------------- | ----------- |
| UART_OVERSAMPLING_RATE | positive |  8                                                                                                    |             |
| TIME_UNIT_INTERVAL     | time     |  1 sec / (to_real(BAUDRATE,<br><span style="padding-left:20px"> 1 Bd) * real(UART_OVERSAMPLING_RATE)) |             |
| BAUDRATE_COUNTER_MAX   | positive |  TimingToCycles(TIME_UNIT_INTERVAL,<br><span style="padding-left:20px"> CLOCK_FREQ)                   |             |
| BAUDRATE_COUNTER_BITS  | positive |  log2ceilnz(BAUDRATE_COUNTER_MAX + 1)                                                                 |             |
