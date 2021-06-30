# Entity: io_7SegmentMux_HEX

## Diagram

![Diagram](io_7SegmentMux_HEX.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:				 	Patrick Lehmann
Entity:				 	time multiplexed 7 Segment Display Controller for HEX chars
Description:
-------------------------------------
This module is a 7 segment display controller that uses time multiplexing
to control a common anode for each digit in the display. The shown characters
are HEX encoded. A dot per digit is optional.
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

| Generic name | Type     | Value   | Description |
| ------------ | -------- | ------- | ----------- |
| CLOCK_FREQ   | FREQ     | 100 MHz |             |
| REFRESH_RATE | FREQ     | 1 kHz   |             |
| DIGITS       | positive | 4       |             |
## Ports

| Port name      | Direction | Type                                  | Description |
| -------------- | --------- | ------------------------------------- | ----------- |
| Clock          | in        | std_logic                             |             |
| HexDigits      | in        | T_SLVV_4(DIGITS - 1 downto 0)         |             |
| HexDots        | in        | std_logic_vector(DIGITS - 1 downto 0) |             |
| SegmentControl | out       | std_logic_vector(7 downto 0)          |             |
| DigitControl   | out       | std_logic_vector(DIGITS - 1 downto 0) |             |
## Signals

| Name             | Type                                      | Description |
| ---------------- | ----------------------------------------- | ----------- |
| DigitCounter_rst | std_logic                                 |             |
| DigitCounter_en  | std_logic                                 |             |
| DigitCounter_us  | unsigned(log2ceilnz(DIGITS) - 1 downto 0) |             |
## Processes
- unnamed: ( HexDigits, HexDots, DigitCounter_us )
## Instantiations

- Strobe: PoC.misc_StrobeGenerator
