# Entity: xil_SystemMonitor

## Diagram

![Diagram](xil_SystemMonitor.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:				 	Patrick Lehmann
Entity:				 	SysMon wrapper for temperature supervision applications
Description:
-------------------------------------
This module wraps a SYSMON or XADC to report if preconfigured temperature values
are overrun. The XADC was formerly known as "System Monitor".
.. rubric:: Temperature Curve
.. code-block:: none
                   |                      /-----\
   Temp_ov   on=80 | - - - - - - /-------/       \
                   |            /        |        \
   Temp_ov  off=60 | - - - - - / - - - - | - - - - \----\
                   |          /          |              |\
                   |         /           |              | \
   Temp_us   on=35 | -  /---/            |              |  \
   Temp_us  off=30 | - / - -|- - - - - - |- - - - - - - |- -\------\
                   |  /     |            |              |           \
   ----------------|--------|------------|--------------|-----------|--------
   pwm =           |   min  |  medium    |   max        |   medium  |  min
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
## Ports

| Port name      | Direction | Type      | Description                                       |
| -------------- | --------- | --------- | ------------------------------------------------- |
| Reset          | in        | std_logic | Reset signal for the System Monitor control logic |
| Alarm_UserTemp | out       | std_logic | Temperature-sensor alarm output                   |
| Alarm_OverTemp | out       | std_logic | Over-Temperature alarm output                     |
| Alarm          | out       | std_logic | OR'ed output of all the Alarms                    |
| VP             | in        | std_logic | Dedicated Analog Input Pair                       |
| VN             | in        | std_logic |                                                   |
## Signals

| Name          | Type                          | Description |
| ------------- | ----------------------------- | ----------- |
| aux_channel_p | std_logic_vector(15 downto 0) |             |
| aux_channel_n | std_logic_vector(15 downto 0) |             |
