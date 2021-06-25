# Entity: gearbox_up_dc
## Diagram
![Diagram](gearbox_up_dc.svg "Diagram")
## Generics
| Generic name        | Type        | Value     | Description |
| ------------------- | ----------- | --------- | ----------- |
| INPUT_BITS          | positive    | 8         |             |
| INPUT_ORDER         | T_BIT_ORDER | LSB_FIRST |             |
| OUTPUT_BITS         | positive    | 32        |             |
| ADD_INPUT_REGISTERS | boolean     | FALSE     |             |
## Ports
| Port name | Direction | Type                                       | Description |
| --------- | --------- | ------------------------------------------ | ----------- |
| Clock1    | in        | std_logic                                  |             |
| Clock2    | in        | std_logic                                  |             |
| In_Align  | in        | std_logic                                  |             |
| In_Data   | in        | std_logic_vector(INPUT_BITS - 1 downto 0)  |             |
| Out_Data  | out       | std_logic_vector(OUTPUT_BITS - 1 downto 0) |             |
| Out_Valid | out       | std_logic                                  |             |
## Signals
| Name              | Type                                       | Description |
| ----------------- | ------------------------------------------ | ----------- |
| Counter_us        | unsigned(COUNTER_BITS - 1 downto 0)        |             |
| Select_us         | unsigned(COUNTER_BITS - 1 downto 0)        |             |
| In_Data_d         | std_logic_vector(INPUT_BITS - 1 downto 0)  |             |
| In_Align_d        | std_logic                                  |             |
| Data_d            | T_CHUNK_VECTOR(INPUT_CHUNKS - 2 downto 0)  |             |
| Collected         | std_logic_vector(OUTPUT_BITS - 1 downto 0) |             |
| Collected_swapped | std_logic_vector(OUTPUT_BITS - 1 downto 0) |             |
| Collected_en      | std_logic                                  |             |
| Collected_d       | std_logic_vector(OUTPUT_BITS - 1 downto 0) |             |
| DataOut_d         | std_logic_vector(OUTPUT_BITS - 1 downto 0) |             |
| Valid_r           | std_logic                                  |             |
| Valid_d           | std_logic                                  |             |
## Constants
| Name           | Type     | Value                                 | Description |
| -------------- | -------- | ------------------------------------- | ----------- |
| BIT_RATIO      | REAL     |  real(OUTPUT_BITS) / real(INPUT_BITS) |             |
| INPUT_CHUNKS   | positive |  integer(BIT_RATIO)                   |             |
| BITS_PER_CHUNK | positive |  INPUT_BITS                           |             |
| COUNTER_MAX    | positive |  INPUT_CHUNKS - 1                     |             |
| COUNTER_BITS   | positive |  log2ceil(COUNTER_MAX + 1)            |             |
## Types
| Name           | Type | Description |
| -------------- | ---- | ----------- |
| T_CHUNK_VECTOR |      |             |
## Functions
- to_slv <font id="function_arguments">(slvv : T_CHUNK_VECTOR)</font> <font id="function_return">return std_logic_vector</font>
## Processes
- unnamed: _( Clock1 )_

- unnamed: _( Clock1 )_

