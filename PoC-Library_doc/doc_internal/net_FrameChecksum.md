# Entity: net_FrameChecksum
## Diagram
![Diagram](net_FrameChecksum.svg "Diagram")
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
| Generic name     | Type     | Value     | Description |
| ---------------- | -------- | --------- | ----------- |
| MAX_FRAMES       | positive | 8         |             |
| MAX_FRAME_LENGTH | positive | 2048      |             |
| META_BITS        | T_POSVEC | (0 => 8)  |             |
| META_FIFO_DEPTH  | T_POSVEC | (0 => 16) |             |
## Ports
| Port name         | Direction | Type                                            | Description |
| ----------------- | --------- | ----------------------------------------------- | ----------- |
| Clock             | in        | std_logic                                       |             |
| Reset             | in        | std_logic                                       |             |
| In_Valid          | in        | std_logic                                       | IN port     |
| In_Data           | in        | T_SLV_8                                         |             |
| In_SOF            | in        | std_logic                                       |             |
| In_EOF            | in        | std_logic                                       |             |
| In_Ack            | out       | std_logic                                       |             |
| In_Meta_rst       | out       | std_logic                                       |             |
| In_Meta_nxt       | out       | std_logic_vector(META_BITS'length - 1 downto 0) |             |
| In_Meta_Data      | in        | std_logic_vector(isum(META_BITS) - 1 downto 0)  |             |
| Out_Valid         | out       | std_logic                                       | OUT port    |
| Out_Data          | out       | T_SLV_8                                         |             |
| Out_SOF           | out       | std_logic                                       |             |
| Out_EOF           | out       | std_logic                                       |             |
| Out_Ack           | in        | std_logic                                       |             |
| Out_Meta_rst      | in        | std_logic                                       |             |
| Out_Meta_nxt      | in        | std_logic_vector(META_BITS'length - 1 downto 0) |             |
| Out_Meta_Data     | out       | std_logic_vector(isum(META_BITS) - 1 downto 0)  |             |
| Out_Meta_Length   | out       | T_SLV_16                                        |             |
| Out_Meta_Checksum | out       | T_SLV_16                                        |             |
## Signals
| Name                  | Type                                              | Description |
| --------------------- | ------------------------------------------------- | ----------- |
| Writer_State          | T_WRITER_STATE                                    |             |
| Writer_NextState      | T_WRITER_STATE                                    |             |
| MetaWriter_State      | T_METAWRITER_STATE                                |             |
| MetaWriter_NextState  | T_METAWRITER_STATE                                |             |
| Reader_State          | T_READER_STATE                                    |             |
| Reader_NextState      | T_READER_STATE                                    |             |
| Checksum_rst          | std_logic                                         |             |
| Checksum_en           | std_logic                                         |             |
| Checksum_Data_us      | unsigned(In_Data'range)                           |             |
| Checksum0_nxt_us      | unsigned(In_Data'length downto 0)                 |             |
| Checksum0_d_us        | unsigned(In_Data'length downto 0)                 |             |
| Checksum0_nxt_cy      | std_logic                                         |             |
| Checksum1_nxt_us      | unsigned(In_Data'range)                           |             |
| Checksum1_d_us        | unsigned(In_Data'range)                           |             |
| Checksum              | T_SLV_16                                          |             |
| WordCounter_rst       | std_logic                                         |             |
| WordCounter_en        | std_logic                                         |             |
| WordCounter_us        | unsigned(WORDCOUNTER_BITS - 1 downto 0)           |             |
| WordCount             | std_logic_vector(WORDCOUNTER_BITS + 15 downto 16) |             |
| FrameCommit           | std_logic                                         |             |
| DataFIFO_put          | std_logic                                         |             |
| DataFIFO_DataIn       | std_logic_vector(DATA_BITS downto 0)              |             |
| DataFIFO_Full         | std_logic                                         |             |
| DataFIFO_got          | std_logic                                         |             |
| DataFIFO_DataOut      | std_logic_vector(DATA_BITS downto 0)              |             |
| DataFIFO_Valid        | std_logic                                         |             |
| MetaFIFO_Misc_put     | std_logic                                         |             |
| MetaFIFO_Misc_DataIn  | std_logic_vector(META_MISC_BITS - 1 downto 0)     |             |
| MetaFIFO_Misc_Full    | std_logic                                         |             |
| MetaFIFO_Misc_got     | std_logic                                         |             |
| MetaFIFO_Misc_DataOut | std_logic_vector(META_MISC_BITS - 1 downto 0)     |             |
| MetaFIFO_Misc_Valid   | std_logic                                         |             |
| Meta_rst              | std_logic_vector(META_BITS'length - 1 downto 0)   |             |
## Constants
| Name             | Type     | Value                               | Description |
| ---------------- | -------- | ----------------------------------- | ----------- |
| WORDCOUNTER_BITS | positive |  log2ceilnz(MAX_FRAME_LENGTH)       |             |
| DATA_BITS        | positive |  8                                  |             |
| EOF_BIT          | natural  |  DATA_BITS                          |             |
| META_MISC_BITS   | positive |  Checksum'length + WordCount'length |             |
## Types
| Name               | Type                                        | Description |
| ------------------ | ------------------------------------------- | ----------- |
| T_WRITER_STATE     | (ST_IDLE, ST_FRAME, ST_CARRY_1, ST_CARRY_2) |             |
| T_METAWRITER_STATE | (ST_IDLE, ST_METADATA)                      |             |
| T_READER_STATE     | (ST_IDLE, ST_FRAME)                         |             |
## Processes
- unnamed: _( Clock )_

- unnamed: _( Writer_State,
					In_Valid, In_SOF, In_EOF, In_Data,
					WordCounter_us, Checksum0_nxt_cy,
					DataFIFO_Full, MetaFIFO_Misc_Full )_

- unnamed: _( Reader_State,
					Out_Ack,
					DataFIFO_Valid, DataFIFO_DataOut,
					MetaFIFO_Misc_Valid, MetaFIFO_Misc_DataOut )_

- unnamed: _( Clock )_

- unnamed: _( Clock )_

## Instantiations
- DataFIFO: PoC.fifo_cc_got
- MetaFIFO_Misc: PoC.fifo_cc_got
