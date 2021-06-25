# Entity: stream_Mirror
## Diagram
![Diagram](stream_Mirror.svg "Diagram")
## Generics
| Generic name | Type     | Value     | Description |
| ------------ | -------- | --------- | ----------- |
| PORTS        | positive | 2         |             |
| DATA_BITS    | positive | 8         |             |
| META_BITS    | T_POSVEC | (0 => 8)  |             |
| META_LENGTH  | T_POSVEC | (0 => 16) |             |
## Ports
| Port name     | Direction | Type                                                     | Description |
| ------------- | --------- | -------------------------------------------------------- | ----------- |
| Clock         | in        | std_logic                                                |             |
| Reset         | in        | std_logic                                                |             |
| In_Valid      | in        | std_logic                                                |             |
| In_Data       | in        | std_logic_vector(DATA_BITS - 1 downto 0)                 |             |
| In_SOF        | in        | std_logic                                                |             |
| In_EOF        | in        | std_logic                                                |             |
| In_Ack        | out       | std_logic                                                |             |
| In_Meta_rst   | out       | std_logic                                                |             |
| In_Meta_nxt   | out       | std_logic_vector(META_BITS'length - 1 downto 0)          |             |
| In_Meta_Data  | in        | std_logic_vector(isum(META_BITS) - 1 downto 0)           |             |
| Out_Valid     | out       | std_logic_vector(PORTS - 1 downto 0)                     |             |
| Out_Data      | out       | T_SLM(PORTS - 1 downto 0, DATA_BITS - 1 downto 0)        |             |
| Out_SOF       | out       | std_logic_vector(PORTS - 1 downto 0)                     |             |
| Out_EOF       | out       | std_logic_vector(PORTS - 1 downto 0)                     |             |
| Out_Ack       | in        | std_logic_vector(PORTS - 1 downto 0)                     |             |
| Out_Meta_rst  | in        | std_logic_vector(PORTS - 1 downto 0)                     |             |
| Out_Meta_nxt  | in        | T_SLM(PORTS - 1 downto 0, META_BITS'length - 1 downto 0) |             |
| Out_Meta_Data | out       | T_SLM(PORTS - 1 downto 0, isum(META_BITS) - 1 downto 0)  |             |
## Signals
| Name             | Type                                                    | Description |
| ---------------- | ------------------------------------------------------- | ----------- |
| FIFOGlue_put     | std_logic                                               |             |
| FIFOGlue_DataIn  | std_logic_vector(DATA_BITS + 1 downto 0)                |             |
| FIFOGlue_Full    | std_logic                                               |             |
| FIFOGlue_Valid   | std_logic                                               |             |
| FIFOGlue_DataOut | std_logic_vector(DATA_BITS + 1 downto 0)                |             |
| FIFOGlue_got     | std_logic                                               |             |
| Ack_i            | std_logic                                               |             |
| Mask_r           | std_logic_vector(PORTS - 1 downto 0)                    |             |
| MetaOut_rst      | std_logic_vector(PORTS - 1 downto 0)                    |             |
| Out_Data_i       | T_SLM(PORTS - 1 downto 0, DATA_BITS - 1 downto 0)       |             |
| Out_Meta_Data_i  | T_SLM(PORTS - 1 downto 0, isum(META_BITS) - 1 downto 0) |             |
## Processes
- unnamed: _( Clock )_

## Instantiations
- FIFOGlue: PoC.fifo_glue
