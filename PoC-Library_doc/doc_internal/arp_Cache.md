# Entity: arp_Cache

- **File**: arp_Cache.vhdl
## Diagram

![Diagram](arp_Cache.svg "Diagram")
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

| Generic name          | Type                      | Value      | Description |
| --------------------- | ------------------------- | ---------- | ----------- |
| CLOCK_FREQ            | FREQ                      | 125 MHz    |             |
| REPLACEMENT_POLICY    | string                    | "LRU"      |             |
| TAG_BYTE_ORDER        | T_BYTE_ORDER              | BIG_ENDIAN |             |
| DATA_BYTE_ORDER       | T_BYTE_ORDER              | BIG_ENDIAN |             |
| INITIAL_CACHE_CONTENT | T_NET_ARP_ARPCACHE_VECTOR |            |             |
## Ports

| Port name           | Direction | Type                       | Description |
| ------------------- | --------- | -------------------------- | ----------- |
| Clock               | in        | std_logic                  |             |
| Reset               | in        | std_logic                  |             |
| Command             | in        | T_NET_ARP_ARPCACHE_COMMAND |             |
| Status              | out       | T_NET_ARP_ARPCACHE_STATUS  |             |
| NewIPv4Address_rst  | out       | std_logic                  |             |
| NewIPv4Address_nxt  | out       | std_logic                  |             |
| NewIPv4Address_Data | in        | T_SLV_8                    |             |
| NewMACAddress_rst   | out       | std_logic                  |             |
| NewMACAddress_nxt   | out       | std_logic                  |             |
| NewMACAddress_Data  | in        | T_SLV_8                    |             |
| Lookup              | in        | std_logic                  |             |
| IPv4Address_rst     | out       | std_logic                  |             |
| IPv4Address_nxt     | out       | std_logic                  |             |
| IPv4Address_Data    | in        | T_SLV_8                    |             |
| CacheResult         | out       | T_CACHE_RESULT             |             |
| MACAddress_rst      | in        | std_logic                  |             |
| MACAddress_nxt      | in        | std_logic                  |             |
| MACAddress_Data     | out       | T_SLV_8                    |             |
## Signals

| Name                     | Type                                                                   | Description                                                                |
| ------------------------ | ---------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| ReadWrite                | std_logic                                                              |                                                                            |
| FSMReplace_State         | T_FSMREPLACE_STATE                                                     |                                                                            |
| FSMReplace_NextState     | T_FSMREPLACE_STATE                                                     |                                                                            |
| Insert                   | std_logic                                                              |                                                                            |
| TU_NewTag_rst            | std_logic                                                              |                                                                            |
| TU_NewTag_nxt            | std_logic                                                              |                                                                            |
| NewTag_Data              | T_SLV_8                                                                |                                                                            |
| NewCacheLine_Data        | T_SLV_8                                                                |                                                                            |
| TU_Tag_rst               | std_logic                                                              |                                                                            |
| TU_Tag_nxt               | std_logic                                                              |                                                                            |
| TU_Tag_Data              | T_SLV_8                                                                |                                                                            |
| CacheHit                 | std_logic                                                              |                                                                            |
| CacheMiss                | std_logic                                                              |                                                                            |
| TU_Index                 | std_logic_vector(CACHEMEMORY_INDEX_BITS - 1 downto 0)                  |                                                                            |
| TU_Index_d               | std_logic_vector(CACHEMEMORY_INDEX_BITS - 1 downto 0)                  |                                                                            |
| TU_NewIndex              | std_logic_vector(CACHEMEMORY_INDEX_BITS - 1 downto 0)                  | 	signal TU_Index_us						: UNSIGNED(CACHEMEMORY_INDEX_BITS - 1 downto 0);  |
| TU_Replaced              | std_logic                                                              |                                                                            |
| TU_TagHit                | std_logic                                                              |                                                                            |
| TU_TagMiss               | std_logic                                                              |                                                                            |
| TickCounter_s            | signed(TICKCOUNTER_BITS downto 0)                                      |                                                                            |
| Tick                     | std_logic                                                              |                                                                            |
| Exp_Expired              | std_logic                                                              |                                                                            |
| Exp_KeyOut               | std_logic_vector(CACHEMEMORY_INDEX_BITS - 1 downto 0)                  |                                                                            |
| DataChunkIndex_us        | unsigned((CACHEMEMORY_INDEX_BITS + DATACHUNK_INDEX_BITS) - 1 downto 0) |                                                                            |
| DataChunkIndex_l_us      | unsigned((CACHEMEMORY_INDEX_BITS + DATACHUNK_INDEX_BITS) - 1 downto 0) |                                                                            |
| NewDataChunkIndex_en     | std_logic                                                              |                                                                            |
| NewDataChunkIndex_us     | unsigned((CACHEMEMORY_INDEX_BITS + DATACHUNK_INDEX_BITS) - 1 downto 0) |                                                                            |
| NewDataChunkIndex_max_us | unsigned((CACHEMEMORY_INDEX_BITS + DATACHUNK_INDEX_BITS) - 1 downto 0) |                                                                            |
| CacheMemory_we           | std_logic                                                              |                                                                            |
| CacheMemory              | T_SLVV_8((CACHE_LINES * T_NET_MAC_ADDRESS'length) - 1 downto 0)        |                                                                            |
| Memory_ReadWrite         | std_logic                                                              |                                                                            |
## Constants

| Name                   | Type     | Value                                                                            | Description   |
| ---------------------- | -------- | -------------------------------------------------------------------------------- | ------------- |
| CACHE_LINES            | positive |  8                                                                               |               |
| TAG_BITS               | positive |  32                                                                              |  IPv4 address |
| DATA_BITS              | positive |  48                                                                              |  MAC address  |
| TAGCHUNK_BITS          | positive |  8                                                                               |               |
| DATACHUNK_BITS         | positive |  8                                                                               |               |
| DATACHUNKS             | positive |  div_ceil(DATA_BITS,<br><span style="padding-left:20px"> DATACHUNK_BITS)         |               |
| DATACHUNK_INDEX_BITS   | positive |  log2ceilnz(DATACHUNKS)                                                          |               |
| CACHEMEMORY_INDEX_BITS | positive |  log2ceilnz(CACHE_LINES)                                                         |               |
| INITIAL_TAGS           | T_SLM    |  to_TagData(INITIAL_CACHE_CONTENT)                                               |               |
| INITIAL_DATALINES      | T_SLVV_8 |  to_CacheMemory(INITIAL_CACHE_CONTENT)                                           |               |
| TICKCOUNTER_RES        | time     |  10 ms                                                                           |               |
| TICKCOUNTER_MAX        | positive |  TimingToCycles(TICKCOUNTER_RES,<br><span style="padding-left:20px"> CLOCK_FREQ) |               |
| TICKCOUNTER_BITS       | positive |  log2ceilnz(TICKCOUNTER_MAX)                                                     |               |
## Types

| Name               | Type                                                       | Description |
| ------------------ | ---------------------------------------------------------- | ----------- |
| T_FSMREPLACE_STATE | (ST_IDLE,<br><span style="padding-left:20px"> ST_REPLACE)  |             |
## Functions
- to_TagData <font id="function_arguments">(CacheContent : T_NET_ARP_ARPCACHE_VECTOR) </font> <font id="function_return">return T_SLM </font>
- to_CacheData_slvv_48 <font id="function_arguments">(CacheContent : T_NET_ARP_ARPCACHE_VECTOR) </font> <font id="function_return">return T_SLVV_48 </font>
- to_CacheMemory <font id="function_arguments">(CacheContent : T_NET_ARP_ARPCACHE_VECTOR) </font> <font id="function_return">return T_SLVV_8 </font>
## Processes
- unnamed: ( Clock )
- unnamed: ( FSMReplace_State, Command, TU_Replaced, TU_NewTag_rst, TU_NewTag_nxt, NewDataChunkIndex_us, NewDataChunkIndex_max_us )
- unnamed: ( Clock )
</br>**Description**
 expiration time tick generator 
- unnamed: ( Clock )
</br>**Description**
 latch TU_Index on TagHit 	TU_Index_us		<= unsigned(TU_Index) when rising_edge(Clock) AND (TU_TagHit = '1');  NewDataChunkIndex counter 
- unnamed: ( Clock, TU_Index )
</br>**Description**
 DataChunkIndex counter 
- unnamed: ( Clock )
## Instantiations

- TU: PoC.cache_TagUnit_seq
</br>**Description**
 Cache TagUnit
	TU : entity PoC.Cache_TagUnit_seq

- Exp: PoC.list_expire
</br>**Description**
	Exp : entity PoC.list_expire

