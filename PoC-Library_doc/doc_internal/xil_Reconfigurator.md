# Entity: xil_Reconfigurator

## Diagram

![Diagram](xil_Reconfigurator.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:				 	Patrick Lehmann
Entity:				 	Reconfiguration engine for DRP enabled Xilinx primtives
Description:
-------------------------------------
Many complex primitives in a Xilinx device offer a Dynamic Reconfiguration
Port (DRP) to reconfigure a primitive at runtime without reconfiguring the
whole FPGA.
This module is a DRP master that can be pre-configured at compile time with
different configuration sets. The configuration sets are mapped into a ROM.
The user can select a stored configuration with ``ConfigSelect``. Sending a
strobe to ``Reconfig`` will start the reconfiguration process. The operation
completes with another strobe on ``ReconfigDone``.
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

| Generic name | Type                 | Value                                      | Description |
| ------------ | -------------------- | ------------------------------------------ | ----------- |
| DEBUG        | boolean              | FALSE                                      |             |
| CLOCK_FREQ   | FREQ                 | 100 MHz                                    |             |
| CONFIG_ROM   | T_XIL_DRP_CONFIG_ROM | (0 downto 0 => C_XIL_DRP_CONFIG_SET_EMPTY) |             |
## Ports

| Port name    | Direction | Type                                                         | Description |
| ------------ | --------- | ------------------------------------------------------------ | ----------- |
| Clock        | in        | std_logic                                                    |             |
| Reset        | in        | std_logic                                                    |             |
| Reconfig     | in        | std_logic                                                    |             |
| ReconfigDone | out       | std_logic                                                    |             |
| ConfigSelect | in        | std_logic_vector(log2ceilnz(CONFIG_ROM'length) - 1 downto 0) |             |
| DRP_en       | out       | std_logic                                                    |             |
| DRP_Address  | out       | T_XIL_DRP_ADDRESS                                            |             |
| DRP_we       | out       | std_logic                                                    |             |
| DRP_DataIn   | in        | T_XIL_DRP_DATA                                               |             |
| DRP_DataOut  | out       | T_XIL_DRP_DATA                                               |             |
| DRP_Ack      | in        | std_logic                                                    |             |
## Signals

| Name               | Type                                    | Description                      |
| ------------------ | --------------------------------------- | -------------------------------- |
| State              | T_STATE                                 | DualConfiguration - Statemachine |
| NextState          | T_STATE                                 |                                  |
| DataBuffer_en      | std_logic                               |                                  |
| DataBuffer_d       | T_XIL_DRP_DATA                          |                                  |
| ROM_Entry          | T_XIL_DRP_CONFIG                        |                                  |
| ROM_LastConfigWord | std_logic                               |                                  |
| ConfigSelect_d     | std_logic_vector(ConfigSelect'range)    |                                  |
| ConfigIndex_rst    | std_logic                               |                                  |
| ConfigIndex_en     | std_logic                               |                                  |
| ConfigIndex_us     | unsigned(CONFIGINDEX_BITS - 1 downto 0) |                                  |
## Constants

| Name             | Type     | Value                          | Description |
| ---------------- | -------- | ------------------------------ | ----------- |
| CONFIGINDEX_BITS | positive |  log2ceilnz(CONFIG_ROM'length) |             |
## Types

| Name    | Type                                                                              | Description |
| ------- | --------------------------------------------------------------------------------- | ----------- |
| T_STATE | ( ST_IDLE, ST_READ_BEGIN,	ST_READ_WAIT, ST_WRITE_BEGIN,	ST_WRITE_WAIT, ST_DONE )  |             |
## Processes
- unnamed: ( Clock )
**Description**
configuration index counter

- unnamed: ( Clock )
**Description**
data buffer for DRP configuration words

- unnamed: ( Clock )
**Description**
DRP read-modify-write statemachine

- unnamed: ( State, Reconfig, ROM_LastConfigWord, DRP_Ack )
