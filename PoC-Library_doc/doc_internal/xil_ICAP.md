# Entity: xil_ICAP

## Diagram

![Diagram](xil_ICAP.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 4; indent-tabs-mode: t -*-
vim: tabstop=4:shiftwidth=4:noexpandtab
kate: tab-width 4; replace-tabs off; indent-width 4;
=============================================================================
Authors:					Paul Genssler
Entity:					ICAP Wrapper
Description:
-------------------------------------
This module wraps Xilinx "Internal Configuration Access Port" (ICAP) primitives in a generic
module. |br|
Supported devices are:
 * Spartan-6
 * Virtex-4, Virtex-5, Virtex-6
 * Series-7 (Artix-7, Kintex-7, Virtex-7, Zynq-7000)
License:
=============================================================================
Copyright 2007-2016 Technische Universitaet Dresden - Germany,
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

| Generic name      | Type       | Value      | Description                                                   |
| ----------------- | ---------- | ---------- | ------------------------------------------------------------- |
| ICAP_WIDTH        | string     | "X32"      | Specifies the input and output data width to be used          |
| DEVICE_ID         | bit_vector | X"1234567" | pre-programmed Device ID value for simulation                 |
| SIM_CFG_FILE_NAME | string     | "NONE"     | Raw Bitstream (RBT) file to be parsed by the simulation model |
## Ports

| Port name | Direction | Type                          | Description                                    |
| --------- | --------- | ----------------------------- | ---------------------------------------------- |
| clk       | in        | std_logic                     | up to 100 MHz (Virtex-6 and above, Virtex-5??) |
| disable   | in        | std_logic                     | low active enable -> high active disable       |
| rd_wr     | in        | std_logic                     | 0 - write, 1 - read                            |
| busy      | out       | std_logic                     | on Series-7 devices always '0'                 |
| data_in   | in        | std_logic_vector(31 downto 0) | on Spartan-6 only 15 downto 0                  |
| data_out  | out       | std_logic_vector(31 downto 0) | on Spartan-6 only 15 downto 0                  |
## Constants

| Name     | Type          | Value        | Description |
| -------- | ------------- | ------------ | ----------- |
| DEV_INFO | T_DEVICE_INFO |  DEVICE_INFO |             |
