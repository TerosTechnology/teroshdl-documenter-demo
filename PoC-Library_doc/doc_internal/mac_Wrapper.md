# Entity: mac_Wrapper
## Diagram
![Diagram](mac_Wrapper.svg "Diagram")
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
| Generic name | Type                           | Value | Description |
| ------------ | ------------------------------ | ----- | ----------- |
| DEBUG        | boolean                        | FALSE |             |
| MAC_CONFIG   | T_NET_MAC_CONFIGURATION_VECTOR |       |             |
## Ports
| Port name                   | Direction | Type                                                                 | Description |
| --------------------------- | --------- | -------------------------------------------------------------------- | ----------- |
| Clock                       | in        | std_logic                                                            |             |
| Reset                       | in        | std_logic                                                            |             |
| Eth_TX_Valid                | out       | std_logic                                                            |             |
| Eth_TX_Data                 | out       | T_SLV_8                                                              |             |
| Eth_TX_SOF                  | out       | std_logic                                                            |             |
| Eth_TX_EOF                  | out       | std_logic                                                            |             |
| Eth_TX_Ack                  | in        | std_logic                                                            |             |
| Eth_RX_Valid                | in        | std_logic                                                            |             |
| Eth_RX_Data                 | in        | T_SLV_8                                                              |             |
| Eth_RX_SOF                  | in        | std_logic                                                            |             |
| Eth_RX_EOF                  | in        | std_logic                                                            |             |
| Eth_RX_Ack                  | out       | std_logic                                                            |             |
| TX_Valid                    | in        | std_logic_vector(getPortCount(MAC_CONFIG) - 1 downto 0)              |             |
| TX_Data                     | in        | T_SLVV_8(getPortCount(MAC_CONFIG) - 1 downto 0)                      |             |
| TX_SOF                      | in        | std_logic_vector(getPortCount(MAC_CONFIG) - 1 downto 0)              |             |
| TX_EOF                      | in        | std_logic_vector(getPortCount(MAC_CONFIG) - 1 downto 0)              |             |
| TX_Ack                      | out       | std_logic_vector(getPortCount(MAC_CONFIG) - 1 downto 0)              |             |
| TX_Meta_rst                 | out       | std_logic_vector(getPortCount(MAC_CONFIG) - 1 downto 0)              |             |
| TX_Meta_DestMACAddress_nxt  | out       | std_logic_vector(getPortCount(MAC_CONFIG) - 1 downto 0)              |             |
| TX_Meta_DestMACAddress_Data | in        | T_SLVV_8(getPortCount(MAC_CONFIG) - 1 downto 0)                      |             |
| RX_Valid                    | out       | std_logic_vector(getPortCount(MAC_CONFIG) - 1 downto 0)              |             |
| RX_Data                     | out       | T_SLVV_8(getPortCount(MAC_CONFIG) - 1 downto 0)                      |             |
| RX_SOF                      | out       | std_logic_vector(getPortCount(MAC_CONFIG) - 1 downto 0)              |             |
| RX_EOF                      | out       | std_logic_vector(getPortCount(MAC_CONFIG) - 1 downto 0)              |             |
| RX_Ack                      | in        | std_logic_vector(getPortCount(MAC_CONFIG) - 1 downto 0)              |             |
| RX_Meta_rst                 | in        | std_logic_vector(getPortCount(MAC_CONFIG) - 1 downto 0)              |             |
| RX_Meta_SrcMACAddress_nxt   | in        | std_logic_vector(getPortCount(MAC_CONFIG) - 1 downto 0)              |             |
| RX_Meta_SrcMACAddress_Data  | out       | T_SLVV_8(getPortCount(MAC_CONFIG) - 1 downto 0)                      |             |
| RX_Meta_DestMACAddress_nxt  | in        | std_logic_vector(getPortCount(MAC_CONFIG) - 1 downto 0)              |             |
| RX_Meta_DestMACAddress_Data | out       | T_SLVV_8(getPortCount(MAC_CONFIG) - 1 downto 0)                      |             |
| RX_Meta_EthType             | out       | T_NET_MAC_ETHERNETTYPE_VECTOR(getPortCount(MAC_CONFIG) - 1 downto 0) |             |
## Signals
| Name                                | Type                                           | Description |
| ----------------------------------- | ---------------------------------------------- | ----------- |
| DestEth_RX_Valid                    | std_logic_vector(INTERFACE_COUNT - 1 downto 0) |             |
| DestEth_RX_Data                     | T_SLVV_8(INTERFACE_COUNT - 1 downto 0)         |             |
| DestEth_RX_SOF                      | std_logic_vector(INTERFACE_COUNT - 1 downto 0) |             |
| DestEth_RX_EOF                      | std_logic_vector(INTERFACE_COUNT - 1 downto 0) |             |
| DestEth_RX_Meta_DestMACAddress_Data | T_SLVV_8(INTERFACE_COUNT - 1 downto 0)         |             |
| SrcEth_RX_Ack                       | std_logic_vector(INTERFACE_COUNT - 1 downto 0) |             |
| SrcEth_RX_Meta_rst                  | std_logic_vector(INTERFACE_COUNT - 1 downto 0) |             |
| SrcEth_RX_Meta_DestMACAddress_nxt   | std_logic_vector(INTERFACE_COUNT - 1 downto 0) |             |
| EthType_TX_Valid                    | std_logic_vector(INTERFACE_COUNT - 1 downto 0) |             |
| EthType_TX_Data                     | T_SLVV_8(INTERFACE_COUNT - 1 downto 0)         |             |
| EthType_TX_SOF                      | std_logic_vector(INTERFACE_COUNT - 1 downto 0) |             |
| EthType_TX_EOF                      | std_logic_vector(INTERFACE_COUNT - 1 downto 0) |             |
| EthType_TX_Meta_DestMACAddress_Data | T_SLVV_8(INTERFACE_COUNT - 1 downto 0)         |             |
| SrcEth_TX_Valid                     | std_logic                                      |             |
| SrcEth_TX_Data                      | T_SLV_8                                        |             |
| SrcEth_TX_SOF                       | std_logic                                      |             |
| SrcEth_TX_EOF                       | std_logic                                      |             |
| SrcEth_TX_Ack                       | std_logic_vector(INTERFACE_COUNT - 1 downto 0) |             |
| SrcEth_TX_Meta_rst                  | std_logic_vector(INTERFACE_COUNT - 1 downto 0) |             |
| SrcEth_TX_Meta_DestMACAddress_nxt   | std_logic_vector(INTERFACE_COUNT - 1 downto 0) |             |
| SrcEth_TX_Meta_DestMACAddress_Data  | T_SLV_8                                        |             |
| DestEth_TX_Ack                      | std_logic                                      |             |
| DestEth_TX_Meta_rst                 | std_logic                                      |             |
| DestEth_TX_Meta_DestMACAddress_nxt  | std_logic                                      |             |
## Constants
| Name                | Type                     | Value                              | Description |
| ------------------- | ------------------------ | ---------------------------------- | ----------- |
| PORTS               | positive                 |  getPortCount(MAC_CONFIG)          |             |
| INTERFACE_COUNT     | positive                 |  MAC_CONFIG'length                 |             |
| INTERFACE_ADDRESSES | T_NET_MAC_ADDRESS_VECTOR |  getInterfaceAddresses(MAC_CONFIG) |             |
| INTERFACE_MASKS     | T_NET_MAC_ADDRESS_VECTOR |  getInterfaceMasks(MAC_CONFIG)     |             |
## Functions
- getInterfaceAddresses <font id="function_arguments">(MAC_CONFIG : T_NET_MAC_CONFIGURATION_VECTOR)</font> <font id="function_return">return T_NET_MAC_ADDRESS_VECTOR</font>
- getInterfaceMasks <font id="function_arguments">(MAC_CONFIG : T_NET_MAC_CONFIGURATION_VECTOR)</font> <font id="function_return">return T_NET_MAC_ADDRESS_VECTOR</font>
- getSourceFilterCount <font id="function_arguments">(Interfaces : T_NET_MAC_INTERFACE_VECTOR)</font> <font id="function_return">return natural</font>
- getSourceFilterAddresses <font id="function_arguments">(Interfaces : T_NET_MAC_INTERFACE_VECTOR)</font> <font id="function_return">return T_NET_MAC_ADDRESS_VECTOR</font>
- getSourceFilterMasks <font id="function_arguments">(Interfaces : T_NET_MAC_INTERFACE_VECTOR)</font> <font id="function_return">return T_NET_MAC_ADDRESS_VECTOR</font>
- getTypeSwitchCount <font id="function_arguments">(Types : T_NET_MAC_ETHERNETTYPE_VECTOR)</font> <font id="function_return">return natural</font>
- calcPortIndex <font id="function_arguments">(MAC_CONFIG : T_NET_MAC_CONFIGURATION_VECTOR; CurrentInterfaceID : natural)</font> <font id="function_return">return natural</font>
## Instantiations
- RX_DestMAC: PoC.mac_RX_DestMAC_Switch
- TX_SrcMAC: PoC.mac_TX_SrcMAC_Prepender
**Description**
Ethernet SourceMAC prepender

- TX_DestMAC: PoC.mac_TX_DestMAC_Prepender
**Description**
Ethernet SourceMAC prepender

