# Entity: mac_TX_SrcMAC_Prepender
## Diagram
![Diagram](mac_TX_SrcMAC_Prepender.svg "Diagram")
## Generics
| Generic name  | Type                     | Value                          | Description |
| ------------- | ------------------------ | ------------------------------ | ----------- |
| DEBUG         | boolean                  | FALSE                          |             |
| MAC_ADDRESSES | T_NET_MAC_ADDRESS_VECTOR | (0 => C_NET_MAC_ADDRESS_EMPTY) |             |
## Ports
| Port name                    | Direction | Type                                                | Description |
| ---------------------------- | --------- | --------------------------------------------------- | ----------- |
| Clock                        | in        | std_logic                                           |             |
| Reset                        | in        | std_logic                                           |             |
| In_Valid                     | in        | std_logic_vector(MAC_ADDRESSES'length - 1 downto 0) |             |
| In_Data                      | in        | T_SLVV_8(MAC_ADDRESSES'length - 1 downto 0)         |             |
| In_SOF                       | in        | std_logic_vector(MAC_ADDRESSES'length - 1 downto 0) |             |
| In_EOF                       | in        | std_logic_vector(MAC_ADDRESSES'length - 1 downto 0) |             |
| In_Ack                       | out       | std_logic_vector(MAC_ADDRESSES'length - 1 downto 0) |             |
| In_Meta_rst                  | out       | std_logic_vector(MAC_ADDRESSES'length - 1 downto 0) |             |
| In_Meta_DestMACAddress_nxt   | out       | std_logic_vector(MAC_ADDRESSES'length - 1 downto 0) |             |
| In_Meta_DestMACAddress_Data  | in        | T_SLVV_8(MAC_ADDRESSES'length - 1 downto 0)         |             |
| Out_Valid                    | out       | std_logic                                           |             |
| Out_Data                     | out       | T_SLV_8                                             |             |
| Out_SOF                      | out       | std_logic                                           |             |
| Out_EOF                      | out       | std_logic                                           |             |
| Out_Ack                      | in        | std_logic                                           |             |
| Out_Meta_rst                 | in        | std_logic                                           |             |
| Out_Meta_DestMACAddress_nxt  | in        | std_logic                                           |             |
| Out_Meta_DestMACAddress_Data | out       | T_SLV_8                                             |             |
## Signals
| Name               | Type                                                  | Description |
| ------------------ | ----------------------------------------------------- | ----------- |
| State              | T_STATE                                               |             |
| NextState          | T_STATE                                               |             |
| LLMux_In_Valid     | std_logic_vector(PORTS - 1 downto 0)                  |             |
| LLMux_In_Data      | T_SLM(PORTS - 1 downto 0, T_SLV_8'range)              |             |
| LLMux_In_Meta      | T_SLM(PORTS - 1 downto 0, META_BITS - 1 downto 0)     |             |
| LLMux_In_Meta_rev  | T_SLM(PORTS - 1 downto 0, META_REV_BITS - 1 downto 0) |             |
| LLMux_In_SOF       | std_logic_vector(PORTS - 1 downto 0)                  |             |
| LLMux_In_EOF       | std_logic_vector(PORTS - 1 downto 0)                  |             |
| LLMux_In_Ack       | std_logic_vector(PORTS - 1 downto 0)                  |             |
| LLMux_Out_Valid    | std_logic                                             |             |
| LLMux_Out_Data     | T_SLV_8                                               |             |
| LLMux_Out_Meta     | std_logic_vector(META_BITS - 1 downto 0)              |             |
| LLMux_Out_Meta_rev | std_logic_vector(META_REV_BITS - 1 downto 0)          |             |
| LLMux_Out_SOF      | std_logic                                             |             |
| LLMux_Out_EOF      | std_logic                                             |             |
| LLMux_Out_Ack      | std_logic                                             |             |
| Is_DataFlow        | std_logic                                             |             |
| Is_SOF             | std_logic                                             |             |
| Is_EOF             | std_logic                                             |             |
## Constants
| Name              | Type     | Value                 | Description |
| ----------------- | -------- | --------------------- | ----------- |
| PORTS             | positive |  MAC_ADDRESSES'length |             |
| META_RST_BIT      | natural  |  0                    |             |
| META_DEST_NXT_BIT | natural  |  1                    |             |
| META_BITS         | positive |  56                   |             |
| META_REV_BITS     | positive |  2                    |             |
## Types
| Name    | Type                                                                                                                                                       | Description |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| T_STATE | ( 		ST_IDLE, 			ST_PREPEND_SRC_MAC_1, 			ST_PREPEND_SRC_MAC_2, 			ST_PREPEND_SRC_MAC_3, 			ST_PREPEND_SRC_MAC_4, 			ST_PREPEND_SRC_MAC_5, 			ST_PAYLOAD 	) |             |
## Processes
- unnamed: _( Clock )_

- unnamed: _( State, LLMux_Out_Valid, LLMux_Out_Data, LLMux_Out_Meta, LLMux_Out_EOF, Is_DataFlow, Is_SOF, Is_EOF, Out_Ack )_

## Instantiations
- LLMux: PoC.stream_Mux
