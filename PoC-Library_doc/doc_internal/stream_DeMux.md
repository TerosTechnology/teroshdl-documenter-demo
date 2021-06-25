# Entity: stream_DeMux
## Diagram
![Diagram](stream_DeMux.svg "Diagram")
## Generics
| Generic name  | Type     | Value | Description |
| ------------- | -------- | ----- | ----------- |
| PORTS         | positive | 2     |             |
| DATA_BITS     | positive | 8     |             |
| META_BITS     | natural  | 8     |             |
| META_REV_BITS | natural  | 2     |             |
## Ports
| Port name    | Direction | Type                                                  | Description |
| ------------ | --------- | ----------------------------------------------------- | ----------- |
| Clock        | in        | std_logic                                             |             |
| Reset        | in        | std_logic                                             |             |
| DeMuxControl | in        | std_logic_vector(PORTS - 1 downto 0)                  |             |
| In_Valid     | in        | std_logic                                             |             |
| In_Data      | in        | std_logic_vector(DATA_BITS - 1 downto 0)              |             |
| In_Meta      | in        | std_logic_vector(META_BITS - 1 downto 0)              |             |
| In_Meta_rev  | out       | std_logic_vector(META_REV_BITS - 1 downto 0)          |             |
| In_SOF       | in        | std_logic                                             |             |
| In_EOF       | in        | std_logic                                             |             |
| In_Ack       | out       | std_logic                                             |             |
| Out_Valid    | out       | std_logic_vector(PORTS - 1 downto 0)                  |             |
| Out_Data     | out       | T_SLM(PORTS - 1 downto 0, DATA_BITS - 1 downto 0)     |             |
| Out_Meta     | out       | T_SLM(PORTS - 1 downto 0, META_BITS - 1 downto 0)     |             |
| Out_Meta_rev | in        | T_SLM(PORTS - 1 downto 0, META_REV_BITS - 1 downto 0) |             |
| Out_SOF      | out       | std_logic_vector(PORTS - 1 downto 0)                  |             |
| Out_EOF      | out       | std_logic_vector(PORTS - 1 downto 0)                  |             |
| Out_Ack      | in        | std_logic_vector(PORTS - 1 downto 0)                  |             |
## Signals
| Name               | Type                                              | Description |
| ------------------ | ------------------------------------------------- | ----------- |
| State              | T_STATE                                           |             |
| NextState          | T_STATE                                           |             |
| Is_SOF             | std_logic                                         |             |
| Is_EOF             | std_logic                                         |             |
| In_Ack_i           | std_logic                                         |             |
| Out_Valid_i        | std_logic                                         |             |
| DiscardFrame       | std_logic                                         |             |
| ChannelPointer_rst | std_logic                                         |             |
| ChannelPointer_en  | std_logic                                         |             |
| ChannelPointer     | std_logic_vector(PORTS - 1 downto 0)              |             |
| ChannelPointer_d   | std_logic_vector(PORTS - 1 downto 0)              |             |
| ChannelPointer_bin | unsigned(log2ceilnz(PORTS) - 1 downto 0)          |             |
| idx                | T_CHANNEL_INDEX                                   |             |
| Out_Data_i         | T_SLM(PORTS - 1 downto 0, DATA_BITS - 1 downto 0) |             |
| Out_Meta_i         | T_SLM(PORTS - 1 downto 0, META_BITS - 1 downto 0) |             |
## Types
| Name    | Type                                     | Description |
| ------- | ---------------------------------------- | ----------- |
| T_STATE | (ST_IDLE, ST_DATAFLOW, ST_DISCARD_FRAME) |             |
## Processes
- unnamed: _( Clock )_

- unnamed: _( State, In_Ack_i, In_Valid, Is_SOF, Is_EOF, DiscardFrame, DeMuxControl, ChannelPointer_d )_

- unnamed: _( Clock )_

