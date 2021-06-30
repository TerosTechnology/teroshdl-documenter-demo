# Entity: stream_Mux

## Diagram

![Diagram](stream_Mux.svg "Diagram")
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

| Generic name  | Type     | Value | Description |
| ------------- | -------- | ----- | ----------- |
| PORTS         | positive | 2     |             |
| DATA_BITS     | positive | 8     |             |
| META_BITS     | natural  | 8     |             |
| META_REV_BITS | natural  | 2     |             |
## Ports

| Port name    | Direction | Type                                                  | Description |
| ------------ | --------- | ----------------------------------------------------- | ----------- |
| Clock        | in        | std_logic                                             |             |
| Reset        | in        | std_logic                                             |             |
| In_Valid     | in        | std_logic_vector(PORTS - 1 downto 0)                  | IN Ports    |
| In_Data      | in        | T_SLM(PORTS - 1 downto 0, DATA_BITS - 1 downto 0)     |             |
| In_Meta      | in        | T_SLM(PORTS - 1 downto 0, META_BITS - 1 downto 0)     |             |
| In_Meta_rev  | out       | T_SLM(PORTS - 1 downto 0, META_REV_BITS - 1 downto 0) |             |
| In_SOF       | in        | std_logic_vector(PORTS - 1 downto 0)                  |             |
| In_EOF       | in        | std_logic_vector(PORTS - 1 downto 0)                  |             |
| In_Ack       | out       | std_logic_vector(PORTS - 1 downto 0)                  |             |
| Out_Valid    | out       | std_logic                                             | OUT Port    |
| Out_Data     | out       | std_logic_vector(DATA_BITS - 1 downto 0)              |             |
| Out_Meta     | out       | std_logic_vector(META_BITS - 1 downto 0)              |             |
| Out_Meta_rev | in        | std_logic_vector(META_REV_BITS - 1 downto 0)          |             |
| Out_SOF      | out       | std_logic                                             |             |
| Out_EOF      | out       | std_logic                                             |             |
| Out_Ack      | in        | std_logic                                             |             |
## Signals

| Name               | Type                                     | Description |
| ------------------ | ---------------------------------------- | ----------- |
| State              | T_STATE                                  |             |
| NextState          | T_STATE                                  |             |
| FSM_Dataflow_en    | std_logic                                |             |
| RequestVector      | std_logic_vector(PORTS - 1 downto 0)     |             |
| RequestWithSelf    | std_logic                                |             |
| RequestWithoutSelf | std_logic                                |             |
| RequestLeft        | unsigned(PORTS - 1 downto 0)             |             |
| SelectLeft         | unsigned(PORTS - 1 downto 0)             |             |
| SelectRight        | unsigned(PORTS - 1 downto 0)             |             |
| ChannelPointer_en  | std_logic                                |             |
| ChannelPointer     | std_logic_vector(PORTS - 1 downto 0)     |             |
| ChannelPointer_d   | std_logic_vector(PORTS - 1 downto 0)     |             |
| ChannelPointer_nxt | std_logic_vector(PORTS - 1 downto 0)     |             |
| ChannelPointer_bin | unsigned(log2ceilnz(PORTS) - 1 downto 0) |             |
| idx                | T_CHANNEL_INDEX                          |             |
| Out_EOF_i          | std_logic                                |             |
## Types

| Name    | Type                    | Description |
| ------- | ----------------------- | ----------- |
| T_STATE | (ST_IDLE, ST_DATAFLOW)  |             |
## Processes
- unnamed: ( Clock )
- unnamed: ( State, RequestWithSelf, RequestWithoutSelf, Out_Ack, Out_EOF_i, ChannelPointer_d, ChannelPointer_nxt )
- unnamed: ( Clock )
