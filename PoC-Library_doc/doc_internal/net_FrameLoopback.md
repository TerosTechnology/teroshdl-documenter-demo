# Entity: FrameLoopback
## Diagram
![Diagram](net_FrameLoopback.svg "Diagram")
## Generics
| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| DATA_BW      | positive | 8     |             |
| META_BW      | natural  | 0     |             |
## Ports
| Port name | Direction | Type                                   | Description |
| --------- | --------- | -------------------------------------- | ----------- |
| Clock     | in        | std_logic                              |             |
| Reset     | in        | std_logic                              |             |
| In_Valid  | in        | std_logic                              |             |
| In_Data   | in        | std_logic_vector(DATA_BW - 1 downto 0) |             |
| In_Meta   | in        | std_logic_vector(META_BW - 1 downto 0) |             |
| In_SOF    | in        | std_logic                              |             |
| In_EOF    | in        | std_logic                              |             |
| In_Ack    | out       | std_logic                              |             |
| Out_Valid | out       | std_logic                              |             |
| Out_Data  | out       | std_logic_vector(DATA_BW - 1 downto 0) |             |
| Out_Meta  | out       | std_logic_vector(META_BW - 1 downto 0) |             |
| Out_SOF   | out       | std_logic                              |             |
| Out_EOF   | out       | std_logic                              |             |
| Out_Ack   | in        | std_logic                              |             |
## Signals
| Name                          | Type                                                   | Description |
| ----------------------------- | ------------------------------------------------------ | ----------- |
| Meta_rst                      | std_logic                                              |             |
| Meta_nxt                      | std_logic_vector(META_STREAMS - 1 downto 0)            |             |
| Pipe_DataOut                  | T_SLV_8                                                |             |
| Pipe_MetaIn                   | T_SLM(META_STREAMS - 1 downto 0, 31 downto 0)          |             |
| Pipe_MetaOut                  | T_SLM(META_STREAMS - 1 downto 0, 31 downto 0)          |             |
| Pipe_Meta_rst                 | std_logic                                              |             |
| Pipe_Meta_nxt                 | std_logic_vector(META_STREAMS - 1 downto 0)            |             |
| Pipe_Meta_SrcMACAddress_Data  | std_logic_vector(TX_Funnel_SrcIPv6Address_Data'range)  |             |
| Pipe_Meta_DestMACAddress_Data | std_logic_vector(TX_Funnel_DestIPv6Address_Data'range) |             |
| Pipe_Meta_EthType             | std_logic_vector(TX_Funnel_Payload_Type'range)         |             |
## Constants
| Name               | Type     | Value | Description |
| ------------------ | -------- | ----- | ----------- |
| META_STREAMID_SRC  | natural  |  0    |             |
| META_STREAMID_DEST | natural  |  1    |             |
| META_STREAMID_type | natural  |  2    |             |
| META_STREAMS       | positive |  3    |             |
## Instantiations
- Pipe: PoC.stream_Buffer
