# Entity: stream_Mux
## Diagram
![Diagram](stream_Mux.svg "Diagram")
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
| In_Valid     | in        | std_logic_vector(PORTS - 1 downto 0)                  |             |
| In_Data      | in        | T_SLM(PORTS - 1 downto 0, DATA_BITS - 1 downto 0)     |             |
| In_Meta      | in        | T_SLM(PORTS - 1 downto 0, META_BITS - 1 downto 0)     |             |
| In_Meta_rev  | out       | T_SLM(PORTS - 1 downto 0, META_REV_BITS - 1 downto 0) |             |
| In_SOF       | in        | std_logic_vector(PORTS - 1 downto 0)                  |             |
| In_EOF       | in        | std_logic_vector(PORTS - 1 downto 0)                  |             |
| In_Ack       | out       | std_logic_vector(PORTS - 1 downto 0)                  |             |
| Out_Valid    | out       | std_logic                                             |             |
| Out_Data     | out       | std_logic_vector(DATA_BITS - 1 downto 0)              |             |
| Out_Meta     | out       | std_logic_vector(META_BITS - 1 downto 0)              |             |
| Out_Meta_rev | in        | std_logic_vector(META_REV_BITS - 1 downto 0)          |             |
| Out_SOF      | out       | std_logic                                             |             |
| Out_EOF      | out       | std_logic                                             |             |
| Out_Ack      | in        | std_logic                                             |             |
## Signals
| Name               | Type                                     | Description |
| ------------------ | ---------------------------------------- | ----------- |
| State              | T_STATE                                  |             |
| NextState          | T_STATE                                  |             |
| FSM_Dataflow_en    | std_logic                                |             |
| RequestVector      | std_logic_vector(PORTS - 1 downto 0)     |             |
| RequestWithSelf    | std_logic                                |             |
| RequestWithoutSelf | std_logic                                |             |
| RequestLeft        | unsigned(PORTS - 1 downto 0)             |             |
| SelectLeft         | unsigned(PORTS - 1 downto 0)             |             |
| SelectRight        | unsigned(PORTS - 1 downto 0)             |             |
| ChannelPointer_en  | std_logic                                |             |
| ChannelPointer     | std_logic_vector(PORTS - 1 downto 0)     |             |
| ChannelPointer_d   | std_logic_vector(PORTS - 1 downto 0)     |             |
| ChannelPointer_nxt | std_logic_vector(PORTS - 1 downto 0)     |             |
| ChannelPointer_bin | unsigned(log2ceilnz(PORTS) - 1 downto 0) |             |
| idx                | T_CHANNEL_INDEX                          |             |
| Out_EOF_i          | std_logic                                |             |
## Types
| Name    | Type                   | Description |
| ------- | ---------------------- | ----------- |
| T_STATE | (ST_IDLE, ST_DATAFLOW) |             |
## Processes
- unnamed: _( Clock )_

- unnamed: _( State, RequestWithSelf, RequestWithoutSelf, Out_Ack, Out_EOF_i, ChannelPointer_d, ChannelPointer_nxt )_

- unnamed: _( Clock )_

