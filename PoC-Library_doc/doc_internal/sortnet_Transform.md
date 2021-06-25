# Entity: sortnet_Transform
## Diagram
![Diagram](sortnet_Transform.svg "Diagram")
## Generics
| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| ROWS         | positive | 16    |             |
| COLUMNS      | positive | 4     |             |
| DATA_BITS    | positive | 8     |             |
## Ports
| Port name | Direction | Type                                                | Description |
| --------- | --------- | --------------------------------------------------- | ----------- |
| Clock     | in        | std_logic                                           |             |
| Reset     | in        | std_logic                                           |             |
| In_Valid  | in        | std_logic                                           |             |
| In_Data   | in        | T_SLM(ROWS - 1 downto 0, DATA_BITS - 1 downto 0)    |             |
| In_SOF    | in        | std_logic                                           |             |
| In_EOF    | in        | std_logic                                           |             |
| Out_Valid | out       | std_logic                                           |             |
| Out_Data  | out       | T_SLM(COLUMNS - 1 downto 0, DATA_BITS - 1 downto 0) |             |
| Out_SOF   | out       | std_logic                                           |             |
| Out_EOF   | out       | std_logic                                           |             |
## Signals
| Name             | Type                                       | Description |
| ---------------- | ------------------------------------------ | ----------- |
| DataIn           | T_DATA_VECTOR(ROWS - 1 downto 0)           |             |
| ColumnWriter_rst | std_logic                                  |             |
| ColumnWriter_us  | unsigned(log2ceilnz(COLUMNS) - 1 downto 0) |             |
| ColumnWriter_ov  | std_logic                                  |             |
| InputBuffer      | T_DATA_MATRIX(COLUMNS - 1 downto 0)        |             |
| RowReader_en_r   | std_logic                                  |             |
| RowReader_rst    | std_logic                                  |             |
| RowReader_en     | std_logic                                  |             |
| RowReader_us     | unsigned(log2ceilnz(ROWS) - 1 downto 0)    |             |
| RowReader_ov     | std_logic                                  |             |
## Types
| Name          | Type | Description |
| ------------- | ---- | ----------- |
| T_DATA_VECTOR |      |             |
| T_DATA_MATRIX |      |             |
## Functions
- to_dv <font id="function_arguments">(slm : T_SLM)</font> <font id="function_return">return T_DATA_VECTOR</font>
## Processes
- unnamed: _( Clock )_

- unnamed: _( InputBuffer, RowReader_us )_

