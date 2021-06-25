# Entity: stream_Buffer
## Diagram
![Diagram](stream_Buffer.svg "Diagram")
## Generics
| Generic name    | Type     | Value     | Description |
| --------------- | -------- | --------- | ----------- |
| FRAMES          | positive | 2         |             |
| DATA_BITS       | positive | 8         |             |
| DATA_FIFO_DEPTH | positive | 8         |             |
| META_BITS       | T_POSVEC | (0 => 8)  |             |
| META_FIFO_DEPTH | T_POSVEC | (0 => 16) |             |
## Ports
| Port name     | Direction | Type                                            | Description |
| ------------- | --------- | ----------------------------------------------- | ----------- |
| Clock         | in        | std_logic                                       |             |
| Reset         | in        | std_logic                                       |             |
| In_Valid      | in        | std_logic                                       |             |
| In_Data       | in        | std_logic_vector(DATA_BITS - 1 downto 0)        |             |
| In_SOF        | in        | std_logic                                       |             |
| In_EOF        | in        | std_logic                                       |             |
| In_Ack        | out       | std_logic                                       |             |
| In_Meta_rst   | out       | std_logic                                       |             |
| In_Meta_nxt   | out       | std_logic_vector(META_BITS'length - 1 downto 0) |             |
| In_Meta_Data  | in        | std_logic_vector(isum(META_BITS) - 1 downto 0)  |             |
| Out_Valid     | out       | std_logic                                       |             |
| Out_Data      | out       | std_logic_vector(DATA_BITS - 1 downto 0)        |             |
| Out_SOF       | out       | std_logic                                       |             |
| Out_EOF       | out       | std_logic                                       |             |
| Out_Ack       | in        | std_logic                                       |             |
| Out_Meta_rst  | in        | std_logic                                       |             |
| Out_Meta_nxt  | in        | std_logic_vector(META_BITS'length - 1 downto 0) |             |
| Out_Meta_Data | out       | std_logic_vector(isum(META_BITS) - 1 downto 0)  |             |
## Signals
| Name             | Type                                            | Description |
| ---------------- | ----------------------------------------------- | ----------- |
| Writer_State     | T_WRITER_STATE                                  |             |
| Writer_NextState | T_WRITER_STATE                                  |             |
| Reader_State     | T_READER_STATE                                  |             |
| Reader_NextState | T_READER_STATE                                  |             |
| DataFIFO_put     | std_logic                                       |             |
| DataFIFO_DataIn  | std_logic_vector(DATA_BITS downto 0)            |             |
| DataFIFO_Full    | std_logic                                       |             |
| DataFIFO_got     | std_logic                                       |             |
| DataFIFO_DataOut | std_logic_vector(DataFIFO_DataIn'range)         |             |
| DataFIFO_Valid   | std_logic                                       |             |
| FrameCommit      | std_logic                                       |             |
| Meta_rst         | std_logic_vector(META_BITS'length - 1 downto 0) |             |
## Constants
| Name         | Type     | Value             | Description |
| ------------ | -------- | ----------------- | ----------- |
| META_STREAMS | positive |  META_BITS'length |             |
| EOF_BIT      | natural  |  DATA_BITS        |             |
## Types
| Name           | Type                | Description |
| -------------- | ------------------- | ----------- |
| T_WRITER_STATE | (ST_IDLE, ST_FRAME) |             |
| T_READER_STATE | (ST_IDLE, ST_FRAME) |             |
## Processes
- unnamed: _( Clock )_

- unnamed: _( Writer_State,
					In_Valid, In_Data, In_SOF, In_EOF,
					DataFIFO_Full )_

- unnamed: _( Reader_State,
					Out_Ack,
					DataFIFO_Valid, DataFIFO_DataOut )_

## Instantiations
- DataFIFO: PoC.fifo_cc_got
