# Entity: stream_DeMux

- **File**: stream_DeMux.vhdl
## Diagram

![Diagram](stream_DeMux.svg "Diagram")
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
										 Chair of VLSI-Design, Diagnostics and Architecture

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

		http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS of ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 =============================================================================
## Generics

| Generic name  | Type     | Value | Description |
| ------------- | -------- | ----- | ----------- |
| PORTS         | positive | 2     |             |
| DATA_BITS     | positive | 8     |             |
| META_BITS     | natural  | 8     |             |
| META_REV_BITS | natural  | 2     |             |
## Ports

| Port name    | Direction | Type                                                  | Description       |
| ------------ | --------- | ----------------------------------------------------- | ----------------- |
| Clock        | in        | std_logic                                             |                   |
| Reset        | in        | std_logic                                             |                   |
| DeMuxControl | in        | std_logic_vector(PORTS - 1 downto 0)                  | Control interface |
| In_Valid     | in        | std_logic                                             | IN Port           |
| In_Data      | in        | std_logic_vector(DATA_BITS - 1 downto 0)              |                   |
| In_Meta      | in        | std_logic_vector(META_BITS - 1 downto 0)              |                   |
| In_Meta_rev  | out       | std_logic_vector(META_REV_BITS - 1 downto 0)          |                   |
| In_SOF       | in        | std_logic                                             |                   |
| In_EOF       | in        | std_logic                                             |                   |
| In_Ack       | out       | std_logic                                             |                   |
| Out_Valid    | out       | std_logic_vector(PORTS - 1 downto 0)                  | OUT Ports         |
| Out_Data     | out       | T_SLM(PORTS - 1 downto 0, DATA_BITS - 1 downto 0)     |                   |
| Out_Meta     | out       | T_SLM(PORTS - 1 downto 0, META_BITS - 1 downto 0)     |                   |
| Out_Meta_rev | in        | T_SLM(PORTS - 1 downto 0, META_REV_BITS - 1 downto 0) |                   |
| Out_SOF      | out       | std_logic_vector(PORTS - 1 downto 0)                  |                   |
| Out_EOF      | out       | std_logic_vector(PORTS - 1 downto 0)                  |                   |
| Out_Ack      | in        | std_logic_vector(PORTS - 1 downto 0)                  |                   |
## Signals

| Name               | Type                                                                                  | Description                                                                                    |
| ------------------ | ------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| State              | T_STATE                                                                               |                                                                                                |
| NextState          | T_STATE                                                                               |                                                                                                |
| Is_SOF             | std_logic                                                                             |                                                                                                |
| Is_EOF             | std_logic                                                                             |                                                                                                |
| In_Ack_i           | std_logic                                                                             |                                                                                                |
| Out_Valid_i        | std_logic                                                                             |                                                                                                |
| DiscardFrame       | std_logic                                                                             |                                                                                                |
| ChannelPointer_rst | std_logic                                                                             |                                                                                                |
| ChannelPointer_en  | std_logic                                                                             |                                                                                                |
| ChannelPointer     | std_logic_vector(PORTS - 1 downto 0)                                                  |                                                                                                |
| ChannelPointer_d   | std_logic_vector(PORTS - 1 downto 0)                                                  |                                                                                                |
| ChannelPointer_bin | unsigned(log2ceilnz(PORTS) - 1 downto 0)                                              |                                                                                                |
| idx                | T_CHANNEL_INDEX                                                                       |                                                                                                |
| Out_Data_i         | T_SLM(PORTS - 1 downto 0,<br><span style="padding-left:20px"> DATA_BITS - 1 downto 0) |  necessary default assignment 'Z' to get correct simulation results (iSIM, vSIM, ghdl/gtkwave) |
| Out_Meta_i         | T_SLM(PORTS - 1 downto 0,<br><span style="padding-left:20px"> META_BITS - 1 downto 0) |                                                                                                |
## Types

| Name    | Type                                                                                                              | Description |
| ------- | ----------------------------------------------------------------------------------------------------------------- | ----------- |
| T_STATE | (ST_IDLE,<br><span style="padding-left:20px"> ST_DATAFLOW,<br><span style="padding-left:20px"> ST_DISCARD_FRAME)  |             |
## Processes
- unnamed: ( Clock )
- unnamed: ( State, In_Ack_i, In_Valid, Is_SOF, Is_EOF, DiscardFrame, DeMuxControl, ChannelPointer_d )
- unnamed: ( Clock )
