# Entity: FrameLoopback

- **File**: net_FrameLoopback.vhdl
## Diagram

![Diagram](net_FrameLoopback.svg "Diagram")
## Description

 EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
 vim: tabstop=2:shiftwidth=2:noexpandtab
 kate: tab-width 2; replace-tabs off; indent-width 2;
 =============================================================================
 Authors:				 	Patrick Lehmann

 Entity:				 	TODO

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
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 =============================================================================
## Generics

| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| DATA_BW      | positive | 8     |             |
| META_BW      | natural  | 0     |             |
## Ports

| Port name | Direction | Type                                   | Description |
| --------- | --------- | -------------------------------------- | ----------- |
| Clock     | in        | std_logic                              |             |
| Reset     | in        | std_logic                              |             |
| In_Valid  | in        | std_logic                              |             |
| In_Data   | in        | std_logic_vector(DATA_BW - 1 downto 0) |             |
| In_Meta   | in        | std_logic_vector(META_BW - 1 downto 0) |             |
| In_SOF    | in        | std_logic                              |             |
| In_EOF    | in        | std_logic                              |             |
| In_Ack    | out       | std_logic                              |             |
| Out_Valid | out       | std_logic                              |             |
| Out_Data  | out       | std_logic_vector(DATA_BW - 1 downto 0) |             |
| Out_Meta  | out       | std_logic_vector(META_BW - 1 downto 0) |             |
| Out_SOF   | out       | std_logic                              |             |
| Out_EOF   | out       | std_logic                              |             |
| Out_Ack   | in        | std_logic                              |             |
## Signals

| Name                          | Type                                                                              | Description |
| ----------------------------- | --------------------------------------------------------------------------------- | ----------- |
| Meta_rst                      | std_logic                                                                         |             |
| Meta_nxt                      | std_logic_vector(META_STREAMS - 1 downto 0)                                       |             |
| Pipe_DataOut                  | T_SLV_8                                                                           |             |
| Pipe_MetaIn                   | T_SLM(META_STREAMS - 1 downto 0,<br><span style="padding-left:20px"> 31 downto 0) |             |
| Pipe_MetaOut                  | T_SLM(META_STREAMS - 1 downto 0,<br><span style="padding-left:20px"> 31 downto 0) |             |
| Pipe_Meta_rst                 | std_logic                                                                         |             |
| Pipe_Meta_nxt                 | std_logic_vector(META_STREAMS - 1 downto 0)                                       |             |
| Pipe_Meta_SrcMACAddress_Data  | std_logic_vector(TX_Funnel_SrcIPv6Address_Data'range)                             |             |
| Pipe_Meta_DestMACAddress_Data | std_logic_vector(TX_Funnel_DestIPv6Address_Data'range)                            |             |
| Pipe_Meta_EthType             | std_logic_vector(TX_Funnel_Payload_Type'range)                                    |             |
## Constants

| Name               | Type     | Value | Description                |
| ------------------ | -------- | ----- | -------------------------- |
| META_STREAMID_SRC  | natural  |  0    |                            |
| META_STREAMID_DEST | natural  |  1    |                            |
| META_STREAMID_type | natural  |  2    |                            |
| META_STREAMS       | positive |  3    |  Source, Destination, Type |
## Instantiations

- Pipe: PoC.stream_Buffer
