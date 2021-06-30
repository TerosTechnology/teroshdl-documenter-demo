# Entity: io_PulseWidthModulation

## Diagram

![Diagram](io_PulseWidthModulation.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:				 	Patrick Lehmann
Entity:				 	Pulse Width Modulated (PWM) signal generator
Description:
-------------------------------------
This module generates a pulse width modulated signal, that can be configured
in frequency (``PWM_FREQ``) and modulation granularity (``PWM_RESOLUTION``).
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

| Generic name   | Type     | Value   | Description |
| -------------- | -------- | ------- | ----------- |
| CLOCK_FREQ     | FREQ     | 100 MHz |             |
| PWM_FREQ       | FREQ     | 1 kHz   |             |
| PWM_RESOLUTION | positive | 8       |             |
## Ports

| Port name | Direction | Type                                          | Description |
| --------- | --------- | --------------------------------------------- | ----------- |
| Clock     | in        | std_logic                                     |             |
| Reset     | in        | std_logic                                     |             |
| PWMIn     | in        | std_logic_vector(PWM_RESOLUTION - 1 downto 0) |             |
| PWMOut    | out       | std_logic                                     |             |
## Signals

| Name                    | Type                                         | Description |
| ----------------------- | -------------------------------------------- | ----------- |
| PWM_FrequencyCounter_us | unsigned(PWM_FREQUENCYCOUNTER_BITS downto 0) |             |
| PWM_FrequencyCounter_ov | std_logic                                    |             |
| PWM_PulseCounter_us     | unsigned(PWM_RESOLUTION - 1 downto 0)        |             |
| PWM_PulseCounter_ov     | std_logic                                    |             |
## Constants

| Name                      | Type     | Value                                            | Description            |
| ------------------------- | -------- | ------------------------------------------------ | ---------------------- |
| PWM_STEPS                 | positive |  2**PWM_RESOLUTION                               |                        |
| PWM_STEP_FREQ             | FREQ     |  PWM_FREQ * (PWM_STEPS - 1)                      |                        |
| PWM_FREQUENCYCOUNTER_MAX  | positive |  (CLOCK_FREQ+PWM_STEP_FREQ-1 Hz) / PWM_STEP_FREQ | division with round-up |
| PWM_FREQUENCYCOUNTER_BITS | positive |  log2ceilnz(PWM_FREQUENCYCOUNTER_MAX)            |                        |
## Processes
- unnamed: ( Clock )
- unnamed: ( Clock )
