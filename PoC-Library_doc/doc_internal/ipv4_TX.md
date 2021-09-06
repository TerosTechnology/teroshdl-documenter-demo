# Entity: ipv4_TX

- **File**: ipv4_TX.vhdl
## Diagram

![Diagram](ipv4_TX.svg "Diagram")
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

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| DEBUG        | boolean | FALSE |             |
## Ports

| Port name                    | Direction | Type      | Description |
| ---------------------------- | --------- | --------- | ----------- |
| Clock                        | in        | std_logic |             |
| Reset                        | in        | std_logic |             |
| In_Valid                     | in        | std_logic | IN port     |
| In_Data                      | in        | T_SLV_8   |             |
| In_SOF                       | in        | std_logic |             |
| In_EOF                       | in        | std_logic |             |
| In_Ack                       | out       | std_logic |             |
| In_Meta_rst                  | out       | std_logic |             |
| In_Meta_SrcIPv4Address_nxt   | out       | std_logic |             |
| In_Meta_SrcIPv4Address_Data  | in        | T_SLV_8   |             |
| In_Meta_DestIPv4Address_nxt  | out       | std_logic |             |
| In_Meta_DestIPv4Address_Data | in        | T_SLV_8   |             |
| In_Meta_Length               | in        | T_SLV_16  |             |
| In_Meta_Protocol             | in        | T_SLV_8   |             |
| ARP_IPCache_Query            | out       | std_logic | ARP port    |
| ARP_IPCache_IPv4Address_rst  | in        | std_logic |             |
| ARP_IPCache_IPv4Address_nxt  | in        | std_logic |             |
| ARP_IPCache_IPv4Address_Data | out       | T_SLV_8   |             |
| ARP_IPCache_Valid            | in        | std_logic |             |
| ARP_IPCache_MACAddress_rst   | out       | std_logic |             |
| ARP_IPCache_MACAddress_nxt   | out       | std_logic |             |
| ARP_IPCache_MACAddress_Data  | in        | T_SLV_8   |             |
| Out_Valid                    | out       | std_logic | OUT port    |
| Out_Data                     | out       | T_SLV_8   |             |
| Out_SOF                      | out       | std_logic |             |
| Out_EOF                      | out       | std_logic |             |
| Out_Ack                      | in        | std_logic |             |
| Out_Meta_rst                 | in        | std_logic |             |
| Out_Meta_DestMACAddress_nxt  | in        | std_logic |             |
| Out_Meta_DestMACAddress_Data | out       | T_SLV_8   |             |
## Signals

| Name                   | Type                                | Description |
| ---------------------- | ----------------------------------- | ----------- |
| State                  | T_STATE                             |             |
| NextState              | T_STATE                             |             |
| In_Ack_i               | std_logic                           |             |
| UpperLayerPacketLength | std_logic_vector(15 downto 0)       |             |
| InternetHeaderLength   | T_SLV_4                             |             |
| TypeOfService          | T_NET_IPV4_TYPE_OF_SERVICE          |             |
| TotalLength            | T_SLV_16                            |             |
| Identification         | T_SLV_16                            |             |
| Flag_DontFragment      | std_logic                           |             |
| Flag_MoreFragments     | std_logic                           |             |
| FragmentOffset         | std_logic_vector(12 downto 0)       |             |
| TimeToLive             | T_SLV_8                             |             |
| Protocol               | T_SLV_8                             |             |
| HeaderChecksum         | T_SLV_16                            |             |
| IPv4SeqCounter_rst     | std_logic                           |             |
| IPv4SeqCounter_en      | std_logic                           |             |
| IPv4SeqCounter_us      | unsigned(1 downto 0)                |             |
| Checksum_rst           | std_logic                           |             |
| Checksum_en            | std_logic                           |             |
| Checksum_Addend0_us    | unsigned(T_SLV_8'range)             |             |
| Checksum_Addend1_us    | unsigned(T_SLV_8'range)             |             |
| Checksum0_nxt0_us      | unsigned(T_SLV_8'high + 1 downto 0) |             |
| Checksum0_nxt1_us      | unsigned(T_SLV_8'high + 1 downto 0) |             |
| Checksum0_d_us         | unsigned(T_SLV_8'high downto 0)     |             |
| Checksum0_cy           | unsigned(T_SLV_2'range)             |             |
| Checksum1_nxt_us       | unsigned(T_SLV_8'range)             |             |
| Checksum1_d_us         | unsigned(T_SLV_8'range)             |             |
| Checksum0_cy0          | std_logic                           |             |
| Checksum0_cy0_d        | std_logic                           |             |
| Checksum0_cy1          | std_logic                           |             |
| Checksum0_cy1_d        | std_logic                           |             |
| Checksum_i             | T_SLV_16                            |             |
| Checksum               | T_SLV_16                            |             |
| Checksum_mux_rst       | std_logic                           |             |
| Checksum_mux_set       | std_logic                           |             |
| Checksum_mux_r         | std_logic                           |             |
## Types

| Name    | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Description |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| T_STATE | ( ST_IDLE,<br><span style="padding-left:20px"> ST_ARP_QUERY,<br><span style="padding-left:20px">									ST_ARP_QUERY_WAIT,<br><span style="padding-left:20px"> ST_CHECKSUM_IPV4_ADDRESSES,<br><span style="padding-left:20px"> ST_CHECKSUM_IPVERSION_LENGTH_0,<br><span style="padding-left:20px">							ST_CHECKSUM_TYPE_OF_SERVICE_LENGTH_1,<br><span style="padding-left:20px"> ST_CHECKSUM_IDENTIFICAION_FRAGMENTOFFSET_0,<br><span style="padding-left:20px">	ST_CHECKSUM_IDENTIFICAION_FRAGMENTOFFSET_1,<br><span style="padding-left:20px"> ST_CHECKSUM_TIME_TO_LIVE,<br><span style="padding-left:20px">				ST_CHECKSUM_PROTOCOL,<br><span style="padding-left:20px"> ST_CARRY_0,<br><span style="padding-left:20px"> ST_CARRY_1,<br><span style="padding-left:20px"> ST_SEND_VERSION,<br><span style="padding-left:20px">							ST_SEND_TYPE_OF_SERVICE,<br><span style="padding-left:20px">	ST_SEND_TOTAL_LENGTH_0,<br><span style="padding-left:20px">			ST_SEND_TOTAL_LENGTH_1,<br><span style="padding-left:20px"> ST_SEND_IDENTIFICATION_0,<br><span style="padding-left:20px">			ST_SEND_IDENTIFICATION_1,<br><span style="padding-left:20px">	ST_SEND_FLAGS,<br><span style="padding-left:20px">							ST_SEND_FRAGMENT_OFFSET,<br><span style="padding-left:20px"> ST_SEND_TIME_TO_LIVE,<br><span style="padding-left:20px">					ST_SEND_PROTOCOL,<br><span style="padding-left:20px">					ST_SEND_HEADER_CHECKSUM_0,<br><span style="padding-left:20px">	ST_SEND_HEADER_CHECKSUM_1,<br><span style="padding-left:20px"> ST_SEND_SOURCE_ADDRESS,<br><span style="padding-left:20px"> ST_SEND_DESTINATION_ADDRESS,<br><span style="padding-left:20px"> ST_SEND_DATA,<br><span style="padding-left:20px"> ST_DISCARD_FRAME,<br><span style="padding-left:20px"> ST_ERROR )  |             |
## Processes
- unnamed: ( Clock )
- unnamed: ( State, In_Valid, In_SOF, In_EOF, In_Data,
					In_Meta_Length,
					Out_Ack, Out_Meta_rst, Out_Meta_DestMACAddress_nxt,
					ARP_IPCache_Valid, ARP_IPCache_IPv4Address_rst, ARP_IPCache_IPv4Address_nxt, ARP_IPCache_MACAddress_Data,
					In_Meta_DestIPv4Address_Data, In_Meta_SrcIPv4Address_Data, In_Meta_Protocol,
					InternetHeaderLength, UpperLayerPacketLength, TypeOfService, Flag_DontFragment, Flag_MoreFragments,
					Identification, FragmentOffset, TimeToLive, Protocol,
					IPv4SeqCounter_us, Checksum0_cy, Checksum )
- unnamed: ( Clock )
- unnamed: ( Clock )
- unnamed: ( Clock )
