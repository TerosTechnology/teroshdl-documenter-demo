# Entity: stream_Mirror

## Diagram

![Diagram](stream_Mirror.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:				 	Patrick Lehmann
Entity:				 	A generic buffer module for the PoC.Stream protocol.
Description:
-------------------------------------
.. TODO:: No documentation available.
License:
=============================================================================
Copyright 2007-2015 Technische Universitaet Dresden - Germany
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS of ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
=============================================================================
## Generics

| Generic name | Type     | Value     | Description |
| ------------ | -------- | --------- | ----------- |
| PORTS        | positive | 2         |             |
| DATA_BITS    | positive | 8         |             |
| META_BITS    | T_POSVEC | (0 => 8)  |             |
| META_LENGTH  | T_POSVEC | (0 => 16) |             |
## Ports

| Port name     | Direction | Type                                                     | Description |
| ------------- | --------- | -------------------------------------------------------- | ----------- |
| Clock         | in        | std_logic                                                |             |
| Reset         | in        | std_logic                                                |             |
| In_Valid      | in        | std_logic                                                | IN Port     |
| In_Data       | in        | std_logic_vector(DATA_BITS - 1 downto 0)                 |             |
| In_SOF        | in        | std_logic                                                |             |
| In_EOF        | in        | std_logic                                                |             |
| In_Ack        | out       | std_logic                                                |             |
| In_Meta_rst   | out       | std_logic                                                |             |
| In_Meta_nxt   | out       | std_logic_vector(META_BITS'length - 1 downto 0)          |             |
| In_Meta_Data  | in        | std_logic_vector(isum(META_BITS) - 1 downto 0)           |             |
| Out_Valid     | out       | std_logic_vector(PORTS - 1 downto 0)                     | OUT Port    |
| Out_Data      | out       | T_SLM(PORTS - 1 downto 0, DATA_BITS - 1 downto 0)        |             |
| Out_SOF       | out       | std_logic_vector(PORTS - 1 downto 0)                     |             |
| Out_EOF       | out       | std_logic_vector(PORTS - 1 downto 0)                     |             |
| Out_Ack       | in        | std_logic_vector(PORTS - 1 downto 0)                     |             |
| Out_Meta_rst  | in        | std_logic_vector(PORTS - 1 downto 0)                     |             |
| Out_Meta_nxt  | in        | T_SLM(PORTS - 1 downto 0, META_BITS'length - 1 downto 0) |             |
| Out_Meta_Data | out       | T_SLM(PORTS - 1 downto 0, isum(META_BITS) - 1 downto 0)  |             |
## Signals

| Name             | Type                                                    | Description |
| ---------------- | ------------------------------------------------------- | ----------- |
| FIFOGlue_put     | std_logic                                               |             |
| FIFOGlue_DataIn  | std_logic_vector(DATA_BITS + 1 downto 0)                |             |
| FIFOGlue_Full    | std_logic                                               |             |
| FIFOGlue_Valid   | std_logic                                               |             |
| FIFOGlue_DataOut | std_logic_vector(DATA_BITS + 1 downto 0)                |             |
| FIFOGlue_got     | std_logic                                               |             |
| Ack_i            | std_logic                                               |             |
| Mask_r           | std_logic_vector(PORTS - 1 downto 0)                    |             |
| MetaOut_rst      | std_logic_vector(PORTS - 1 downto 0)                    |             |
| Out_Data_i       | T_SLM(PORTS - 1 downto 0, DATA_BITS - 1 downto 0)       |             |
| Out_Meta_Data_i  | T_SLM(PORTS - 1 downto 0, isum(META_BITS) - 1 downto 0) |             |
## Processes
- unnamed: ( Clock )
## Instantiations

- FIFOGlue: PoC.fifo_glue
