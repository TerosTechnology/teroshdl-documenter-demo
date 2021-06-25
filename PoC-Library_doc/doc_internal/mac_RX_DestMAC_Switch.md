# Entity: mac_RX_DestMAC_Switch
## Diagram
![Diagram](mac_RX_DestMAC_Switch.svg "Diagram")
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
| Generic name       | Type                     | Value                          | Description |
| ------------------ | ------------------------ | ------------------------------ | ----------- |
| DEBUG              | boolean                  | FALSE                          |             |
| MAC_ADDRESSES      | T_NET_MAC_ADDRESS_VECTOR | (0 => C_NET_MAC_ADDRESS_EMPTY) |             |
| MAC_ADDRESSE_MASKS | T_NET_MAC_ADDRESS_VECTOR | (0 => C_NET_MAC_MASK_DEFAULT)  |             |
## Ports
| Port name                    | Direction | Type                                                | Description |
| ---------------------------- | --------- | --------------------------------------------------- | ----------- |
| Clock                        | in        | std_logic                                           |             |
| Reset                        | in        | std_logic                                           |             |
| In_Valid                     | in        | std_logic                                           |             |
| In_Data                      | in        | T_SLV_8                                             |             |
| In_SOF                       | in        | std_logic                                           |             |
| In_EOF                       | in        | std_logic                                           |             |
| In_Ack                       | out       | std_logic                                           |             |
| Out_Valid                    | out       | std_logic_vector(MAC_ADDRESSES'length - 1 downto 0) |             |
| Out_Data                     | out       | T_SLVV_8(MAC_ADDRESSES'length - 1 downto 0)         |             |
| Out_SOF                      | out       | std_logic_vector(MAC_ADDRESSES'length - 1 downto 0) |             |
| Out_EOF                      | out       | std_logic_vector(MAC_ADDRESSES'length - 1 downto 0) |             |
| Out_Ack                      | in        | std_logic_vector(MAC_ADDRESSES'length - 1 downto 0) |             |
| Out_Meta_DestMACAddress_rst  | in        | std_logic_vector(MAC_ADDRESSES'length - 1 downto 0) |             |
| Out_Meta_DestMACAddress_nxt  | in        | std_logic_vector(MAC_ADDRESSES'length - 1 downto 0) |             |
| Out_Meta_DestMACAddress_Data | out       | T_SLVV_8(MAC_ADDRESSES'length - 1 downto 0)         |             |
## Signals
| Name                          | Type                                       | Description |
| ----------------------------- | ------------------------------------------ | ----------- |
| State                         | T_STATE                                    |             |
| NextState                     | T_STATE                                    |             |
| In_Ack_i                      | std_logic                                  |             |
| Is_DataFlow                   | std_logic                                  |             |
| Is_SOF                        | std_logic                                  |             |
| Is_EOF                        | std_logic                                  |             |
| New_Valid_i                   | std_logic                                  |             |
| New_SOF_i                     | std_logic                                  |             |
| Out_Ack_i                     | std_logic                                  |             |
| MAC_ByteIndex                 | T_MAC_BYTEINDEX                            |             |
| CompareRegister_rst           | std_logic                                  |             |
| CompareRegister_init          | std_logic                                  |             |
| CompareRegister_clear         | std_logic                                  |             |
| CompareRegister_en            | std_logic                                  |             |
| CompareRegister_d             | std_logic_vector(PORTS - 1 downto 0)       |             |
| NoHits                        | std_logic                                  |             |
| Reader_Counter_rst            | std_logic                                  |             |
| Reader_Counter_en             | std_logic                                  |             |
| Reader_Counter_us             | unsigned(READER_COUNTER_BITS - 1 downto 0) |             |
| DestinationMAC_rst            | std_logic                                  |             |
| DestinationMAC_en             | std_logic                                  |             |
| DestinationMAC_sel            | T_MAC_BYTEINDEX                            |             |
| DestinationMAC_d              | T_NET_MAC_ADDRESS                          |             |
| Out_Meta_DestMACAddress_rst_i | std_logic                                  |             |
| Out_Meta_DestMACAddress_nxt_i | std_logic                                  |             |
## Constants
| Name                 | Type                                     | Value                           | Description    |
| -------------------- | ---------------------------------------- | ------------------------------- | -------------- |
| PORTS                | positive                                 |  MAC_ADDRESSES'length           |                |
| MAC_ADDRESSES_I      | T_NET_MAC_ADDRESS_VECTOR(0 to PORTS - 1) |  MAC_ADDRESSES                  |                |
| MAC_ADDRESSE_MASKS_I | T_NET_MAC_ADDRESS_VECTOR(0 to PORTS - 1) |  MAC_ADDRESSE_MASKS             |                |
| MAC_ADDRESS_LENGTH   | positive                                 |  6                              | MAC -> 6 bytes |
| READER_COUNTER_BITS  | positive                                 |  log2ceilnz(MAC_ADDRESS_LENGTH) |                |
## Types
| Name    | Type                                                                                                                                                           | Description |
| ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| T_STATE | ( 		ST_IDLE, 			ST_DEST_MAC_1, 			ST_DEST_MAC_2, 			ST_DEST_MAC_3, 			ST_DEST_MAC_4, 			ST_DEST_MAC_5, 			ST_PAYLOAD_1, 			ST_PAYLOAD_N, 		ST_DISCARD_FRAME 	) |             |
## Processes
- unnamed: _( Clock )_

- unnamed: _( State, Is_DataFlow, Is_SOF, Is_EOF, In_Valid, NoHits, Out_Ack_i )_

- unnamed: _( Clock )_

- unnamed: _( Clock )_

