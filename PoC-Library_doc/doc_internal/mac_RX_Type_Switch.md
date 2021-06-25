# Entity: mac_RX_Type_Switch
## Diagram
![Diagram](mac_RX_Type_Switch.svg "Diagram")
## Generics
| Generic name   | Type                          | Value                               | Description |
| -------------- | ----------------------------- | ----------------------------------- | ----------- |
| DEBUG          | boolean                       | FALSE                               |             |
| ETHERNET_TYPES | T_NET_MAC_ETHERNETTYPE_VECTOR | (0 => C_NET_MAC_ETHERNETTYPE_EMPTY) |             |
## Ports
| Port name                    | Direction | Type                                                              | Description |
| ---------------------------- | --------- | ----------------------------------------------------------------- | ----------- |
| Clock                        | in        | std_logic                                                         |             |
| Reset                        | in        | std_logic                                                         |             |
| In_Valid                     | in        | std_logic                                                         |             |
| In_Data                      | in        | T_SLV_8                                                           |             |
| In_SOF                       | in        | std_logic                                                         |             |
| In_EOF                       | in        | std_logic                                                         |             |
| In_Ack                       | out       | std_logic                                                         |             |
| In_Meta_rst                  | out       | std_logic                                                         |             |
| In_Meta_SrcMACAddress_nxt    | out       | std_logic                                                         |             |
| In_Meta_SrcMACAddress_Data   | in        | T_SLV_8                                                           |             |
| In_Meta_DestMACAddress_nxt   | out       | std_logic                                                         |             |
| In_Meta_DestMACAddress_Data  | in        | T_SLV_8                                                           |             |
| Out_Valid                    | out       | std_logic_vector(ETHERNET_TYPES'length - 1 downto 0)              |             |
| Out_Data                     | out       | T_SLVV_8(ETHERNET_TYPES'length - 1 downto 0)                      |             |
| Out_SOF                      | out       | std_logic_vector(ETHERNET_TYPES'length - 1 downto 0)              |             |
| Out_EOF                      | out       | std_logic_vector(ETHERNET_TYPES'length - 1 downto 0)              |             |
| Out_Ack                      | in        | std_logic_vector(ETHERNET_TYPES'length - 1 downto 0)              |             |
| Out_Meta_rst                 | in        | std_logic_vector(ETHERNET_TYPES'length - 1 downto 0)              |             |
| Out_Meta_SrcMACAddress_nxt   | in        | std_logic_vector(ETHERNET_TYPES'length - 1 downto 0)              |             |
| Out_Meta_SrcMACAddress_Data  | out       | T_SLVV_8(ETHERNET_TYPES'length - 1 downto 0)                      |             |
| Out_Meta_DestMACAddress_nxt  | in        | std_logic_vector(ETHERNET_TYPES'length - 1 downto 0)              |             |
| Out_Meta_DestMACAddress_Data | out       | T_SLVV_8(ETHERNET_TYPES'length - 1 downto 0)                      |             |
| Out_Meta_EthType             | out       | T_NET_MAC_ETHERNETTYPE_VECTOR(ETHERNET_TYPES'length - 1 downto 0) |             |
## Signals
| Name                      | Type                                 | Description |
| ------------------------- | ------------------------------------ | ----------- |
| State                     | T_STATE                              |             |
| NextState                 | T_STATE                              |             |
| In_Ack_i                  | std_logic                            |             |
| Is_DataFlow               | std_logic                            |             |
| Is_SOF                    | std_logic                            |             |
| Is_EOF                    | std_logic                            |             |
| New_Valid_i               | std_logic                            |             |
| New_SOF_i                 | std_logic                            |             |
| Out_Ack_i                 | std_logic                            |             |
| EthernetType_CompareIndex | T_ETHERNETTYPE_BYTEINDEX             |             |
| CompareRegister_rst       | std_logic                            |             |
| CompareRegister_init      | std_logic                            |             |
| CompareRegister_clear     | std_logic                            |             |
| CompareRegister_en        | std_logic                            |             |
| CompareRegister_d         | std_logic_vector(PORTS - 1 downto 0) |             |
| NoHits                    | std_logic                            |             |
| EthernetType_rst          | std_logic                            |             |
| EthernetType_en           | std_logic                            |             |
| EthernetType_sel          | T_ETHERNETTYPE_BYTEINDEX             |             |
| EthernetType_d            | T_NET_MAC_ETHERNETTYPE               |             |
## Constants
| Name             | Type                                          | Value                  | Description |
| ---------------- | --------------------------------------------- | ---------------------- | ----------- |
| PORTS            | positive                                      |  ETHERNET_TYPES'length |             |
| ETHERNET_TYPES_I | T_NET_MAC_ETHERNETTYPE_VECTOR(0 to PORTS - 1) |  ETHERNET_TYPES        |             |
## Types
| Name    | Type                                                                               | Description |
| ------- | ---------------------------------------------------------------------------------- | ----------- |
| T_STATE | ( 		ST_IDLE, 			ST_TYPE_1, 			ST_PAYLOAD_1, 			ST_PAYLOAD_N, 		ST_DISCARD_FRAME 	) |             |
## Processes
- unnamed: _( Clock )_

- unnamed: _( State, Is_DataFlow, Is_SOF, Is_EOF, In_Valid, NoHits, Out_Ack_i )_

