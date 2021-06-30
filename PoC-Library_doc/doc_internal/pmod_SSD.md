# Entity: pmod_SSD

## Diagram

![Diagram](pmod_SSD.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:				 	Patrick Lehmann
Entity:				 	Digilent Peritherial Module: Pmod_SSD
Description:
-------------------------------------
This module drives a dual-digit 7-segment display (Pmod_SSD). The module
expects two binary encoded 4-bit ``Digit<i>`` signals and drives a 2x6 bit
Pmod connector (7 anode bits, 1 cathode bit).
.. code-block:: none
   Segment Pos./ Index
      AAA      |   000
     F   B     |  5   1
     F   B     |  5   1
      GGG      |   666
     E   C     |  4   2
     E   C     |  4   2
      DDD  DOT |   333  7
License:
=============================================================================
Copyright 2007-2016 Technische Universitaet Dresden - Germany
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

| Generic name | Type | Value   | Description |
| ------------ | ---- | ------- | ----------- |
| CLOCK_FREQ   | FREQ | 100 MHz |             |
| REFRESH_RATE | FREQ | 1 kHz   |             |
## Ports

| Port name | Direction | Type                         | Description |
| --------- | --------- | ---------------------------- | ----------- |
| Clock     | in        | std_logic                    |             |
| Digit0    | in        | std_logic_vector(3 downto 0) |             |
| Digit1    | in        | std_logic_vector(3 downto 0) |             |
| SSD       | out       | T_PMOD_SSD_PINS              |             |
## Signals

| Name             | Type                                   | Description |
| ---------------- | -------------------------------------- | ----------- |
| RefreshTimer_rst | std_logic                              |             |
| RefreshTimer_s   | signed(REFRESHTIMER_BITS - 1 downto 0) |             |
| CathodeSelect_en | std_logic                              |             |
| CathodeSelect_r  | std_logic                              |             |
| Digit            | std_logic_vector(3 downto 0)           |             |
| Segments         | std_logic_vector(6 downto 0)           |             |
## Constants

| Name              | Type     | Value                                                  | Description |
| ----------------- | -------- | ------------------------------------------------------ | ----------- |
| REFRESHTIMER_MAX  | positive |  TimingToCycles(to_time(REFRESH_RATE), CLOCK_FREQ) - 1 |             |
| REFRESHTIMER_BITS | positive |  log2ceilnz(REFRESHTIMER_MAX) + 1                      |             |
