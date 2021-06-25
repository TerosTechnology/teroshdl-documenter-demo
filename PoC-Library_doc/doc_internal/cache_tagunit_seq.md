# Entity: cache_tagunit_seq
## Diagram
![Diagram](cache_tagunit_seq.svg "Diagram")
## Description
EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:					Patrick Lehmann
Entity:					Tag-unit with sequential compare of tag.
Description:
-------------------------------------
.. TODO:: No documentation available.
License:
=============================================================================
Copyright 2007-2014 Technische Universitaet Dresden - Germany
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
| Generic name       | Type         | Value                                 | Description |
| ------------------ | ------------ | ------------------------------------- | ----------- |
| REPLACEMENT_POLICY | string       | "LRU"                                 |             |
| CACHE_LINES        | positive     | 32                                    |             |
| ASSOCIATIVITY      | positive     | 32                                    |             |
| TAG_BITS           | positive     | 128                                   |             |
| CHUNK_BITS         | positive     | 8                                     |             |
| TAG_BYTE_ORDER     | T_BYTE_ORDER | LITTLE_ENDIAN                         |             |
| USE_INITIAL_TAGS   | boolean      | false                                 |             |
| INITIAL_TAGS       | T_SLM        | (0 downto 0 => (127 downto 0 => '0')) |             |
## Ports
| Port name           | Direction | Type                                                   | Description |
| ------------------- | --------- | ------------------------------------------------------ | ----------- |
| Clock               | in        | std_logic                                              |             |
| Reset               | in        | std_logic                                              |             |
| Replace             | in        | std_logic                                              |             |
| Replaced            | out       | std_logic                                              |             |
| Replace_NewTag_rst  | out       | std_logic                                              |             |
| Replace_NewTag_rev  | out       | std_logic                                              |             |
| Replace_NewTag_nxt  | out       | std_logic                                              |             |
| Replace_NewTag_Data | in        | std_logic_vector(CHUNK_BITS - 1 downto 0)              |             |
| Replace_NewIndex    | out       | std_logic_vector(log2ceilnz(CACHE_LINES) - 1 downto 0) |             |
| Request             | in        | std_logic                                              |             |
| Request_ReadWrite   | in        | std_logic                                              |             |
| Request_Invalidate  | in        | std_logic                                              |             |
| Request_Tag_rst     | out       | std_logic                                              |             |
| Request_Tag_rev     | out       | std_logic                                              |             |
| Request_Tag_nxt     | out       | std_logic                                              |             |
| Request_Tag_Data    | in        | std_logic_vector(CHUNK_BITS - 1 downto 0)              |             |
| Request_Index       | out       | std_logic_vector(log2ceilnz(CACHE_LINES) - 1 downto 0) |             |
| Request_TagHit      | out       | std_logic                                              |             |
| Request_TagMiss     | out       | std_logic                                              |             |
## Constants
| Name | Type     | Value                        | Description |
| ---- | -------- | ---------------------------- | ----------- |
| SETS | positive |  CACHE_LINES / ASSOCIATIVITY |             |
