# Entity: stream_Buffer

- **File**: stream_Buffer.vhdl
## Diagram

![Diagram](stream_Buffer.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:				 	Patrick Lehmann
Entity:				 	A generic buffer module for the PoC.Stream protocol.
Description:
-------------------------------------
This module implements a generic buffer (FIFO) for the
:doc:`PoC.Stream </Interfaces/Stream>` protocol. It is generic in
``DATA_BITS`` and in ``META_BITS`` as well as in FIFO depths for data and
meta information.
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

| Generic name    | Type     | Value     | Description |
| --------------- | -------- | --------- | ----------- |
| FRAMES          | positive | 2         |             |
| DATA_BITS       | positive | 8         |             |
| DATA_FIFO_DEPTH | positive | 8         |             |
| META_BITS       | T_POSVEC | (0 => 8)  |             |
| META_FIFO_DEPTH | T_POSVEC | (0 => 16) |             |
## Ports

| Port name     | Direction | Type                                            | Description |
| ------------- | --------- | ----------------------------------------------- | ----------- |
| Clock         | in        | std_logic                                       |             |
| Reset         | in        | std_logic                                       |             |
| In_Valid      | in        | std_logic                                       | IN Port     |
| In_Data       | in        | std_logic_vector(DATA_BITS - 1 downto 0)        |             |
| In_SOF        | in        | std_logic                                       |             |
| In_EOF        | in        | std_logic                                       |             |
| In_Ack        | out       | std_logic                                       |             |
| In_Meta_rst   | out       | std_logic                                       |             |
| In_Meta_nxt   | out       | std_logic_vector(META_BITS'length - 1 downto 0) |             |
| In_Meta_Data  | in        | std_logic_vector(isum(META_BITS) - 1 downto 0)  |             |
| Out_Valid     | out       | std_logic                                       | OUT Port    |
| Out_Data      | out       | std_logic_vector(DATA_BITS - 1 downto 0)        |             |
| Out_SOF       | out       | std_logic                                       |             |
| Out_EOF       | out       | std_logic                                       |             |
| Out_Ack       | in        | std_logic                                       |             |
| Out_Meta_rst  | in        | std_logic                                       |             |
| Out_Meta_nxt  | in        | std_logic_vector(META_BITS'length - 1 downto 0) |             |
| Out_Meta_Data | out       | std_logic_vector(isum(META_BITS) - 1 downto 0)  |             |
## Signals

| Name             | Type                                            | Description |
| ---------------- | ----------------------------------------------- | ----------- |
| Writer_State     | T_WRITER_STATE                                  |             |
| Writer_NextState | T_WRITER_STATE                                  |             |
| Reader_State     | T_READER_STATE                                  |             |
| Reader_NextState | T_READER_STATE                                  |             |
| DataFIFO_put     | std_logic                                       |             |
| DataFIFO_DataIn  | std_logic_vector(DATA_BITS downto 0)            |             |
| DataFIFO_Full    | std_logic                                       |             |
| DataFIFO_got     | std_logic                                       |             |
| DataFIFO_DataOut | std_logic_vector(DataFIFO_DataIn'range)         |             |
| DataFIFO_Valid   | std_logic                                       |             |
| FrameCommit      | std_logic                                       |             |
| Meta_rst         | std_logic_vector(META_BITS'length - 1 downto 0) |             |
## Constants

| Name         | Type     | Value             | Description |
| ------------ | -------- | ----------------- | ----------- |
| META_STREAMS | positive |  META_BITS'length |             |
| EOF_BIT      | natural  |  DATA_BITS        |             |
## Types

| Name           | Type                                                     | Description |
| -------------- | -------------------------------------------------------- | ----------- |
| T_WRITER_STATE | (ST_IDLE,<br><span style="padding-left:20px"> ST_FRAME)  |             |
| T_READER_STATE | (ST_IDLE,<br><span style="padding-left:20px"> ST_FRAME)  |             |
## Processes
- unnamed: ( Clock )
- unnamed: ( Writer_State,
					In_Valid, In_Data, In_SOF, In_EOF,
					DataFIFO_Full )
- unnamed: ( Reader_State,
					Out_Ack,
					DataFIFO_Valid, DataFIFO_DataOut )
## Instantiations

- DataFIFO: PoC.fifo_cc_got
