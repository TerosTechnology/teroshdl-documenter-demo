# Entity: stream_FrameGenerator
## Diagram
![Diagram](stream_FrameGenerator.svg "Diagram")
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
| Generic name | Type                           | Value                              | Description |
| ------------ | ------------------------------ | ---------------------------------- | ----------- |
| DATA_BITS    | positive                       | 8                                  |             |
| WORD_BITS    | positive                       | 16                                 |             |
| APPEND       | T_FRAMEGEN_APPEND              | FRAMEGEN_APP_NONE                  |             |
| FRAMEGROUPS  | T_FRAMEGEN_FRAMEGROUP_VECTOR_8 | (0 => C_FRAMEGEN_FRAMEGROUP_EMPTY) |             |
## Ports
| Port name       | Direction | Type                                     | Description       |
| --------------- | --------- | ---------------------------------------- | ----------------- |
| Clock           | in        | std_logic                                |                   |
| Reset           | in        | std_logic                                |                   |
| Command         | in        | T_FRAMEGEN_COMMAND                       | CSE interface     |
| Status          | out       | T_FRAMEGEN_STATUS                        |                   |
| Pause           | in        | T_SLV_16                                 | Control interface |
| FrameGroupIndex | in        | T_SLV_8                                  |                   |
| FrameIndex      | in        | T_SLV_8                                  |                   |
| Sequences       | in        | T_SLV_16                                 |                   |
| FrameLength     | in        | T_SLV_16                                 |                   |
| Out_Valid       | out       | std_logic                                | OUT Port          |
| Out_Data        | out       | std_logic_vector(DATA_BITS - 1 downto 0) |                   |
| Out_SOF         | out       | std_logic                                |                   |
| Out_EOF         | out       | std_logic                                |                   |
| Out_Ack         | in        | std_logic                                |                   |
## Signals
| Name                   | Type                                     | Description |
| ---------------------- | ---------------------------------------- | ----------- |
| State                  | T_STATE                                  |             |
| NextState              | T_STATE                                  |             |
| FrameLengthCounter_rst | std_logic                                |             |
| FrameLengthCounter_en  | std_logic                                |             |
| FrameLengthCounter_us  | unsigned(15 downto 0)                    |             |
| SequencesCounter_rst   | std_logic                                |             |
| SequencesCounter_en    | std_logic                                |             |
| SequencesCounter_us    | unsigned(15 downto 0)                    |             |
| ContentCounter_rst     | std_logic                                |             |
| ContentCounter_en      | std_logic                                |             |
| ContentCounter_us      | unsigned(WORD_BITS - 1 downto 0)         |             |
| PRNG_rst               | std_logic                                |             |
| PRNG_got               | std_logic                                |             |
| PRNG_Data              | std_logic_vector(DATA_BITS - 1 downto 0) |             |
## Types
| Name    | Type                                                                                                                                 | Description |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| T_STATE | ( 		ST_IDLE, 			ST_SEQUENCE_SOF,	ST_SEQUENCE_DATA,	ST_SEQUENCE_EOF, 			ST_RANDOM_SOF,		ST_RANDOM_DATA,		ST_RANDOM_EOF, 		ST_ERROR 	) |             |
## Processes
- unnamed: _( Clock )_

- unnamed: _( State, Command, Out_Ack,
					Sequences, FrameLength,
					FrameLengthCounter_us,
					SequencesCounter_us, ContentCounter_us,
					PRNG_Data )_

- unnamed: _( Clock )_

- unnamed: _( Clock )_

- unnamed: _( Clock )_

## Instantiations
- PRNG: PoC.arith_prng
