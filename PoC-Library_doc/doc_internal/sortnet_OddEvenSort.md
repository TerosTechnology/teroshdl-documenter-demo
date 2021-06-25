# Entity: sortnet_OddEvenSort
## Diagram
![Diagram](sortnet_OddEvenSort.svg "Diagram")
## Generics
| Generic name         | Type     | Value | Description |
| -------------------- | -------- | ----- | ----------- |
| INPUTS               | positive | 8     |             |
| KEY_BITS             | positive | 32    |             |
| DATA_BITS            | positive | 32    |             |
| META_BITS            | natural  | 2     |             |
| PIPELINE_STAGE_AFTER | natural  | 2     |             |
| ADD_INPUT_REGISTERS  | boolean  | FALSE |             |
| ADD_OUTPUT_REGISTERS | boolean  | TRUE  |             |
## Ports
| Port name | Direction | Type                                               | Description |
| --------- | --------- | -------------------------------------------------- | ----------- |
| Clock     | in        | std_logic                                          |             |
| Reset     | in        | std_logic                                          |             |
| Inverse   | in        | std_logic                                          |             |
| In_Valid  | in        | std_logic                                          |             |
| In_IsKey  | in        | std_logic                                          |             |
| In_Data   | in        | T_SLM(INPUTS - 1 downto 0, DATA_BITS - 1 downto 0) |             |
| In_Meta   | in        | std_logic_vector(META_BITS - 1 downto 0)           |             |
| Out_Valid | out       | std_logic                                          |             |
| Out_IsKey | out       | std_logic                                          |             |
| Out_Data  | out       | T_SLM(INPUTS - 1 downto 0, DATA_BITS - 1 downto 0) |             |
| Out_Meta  | out       | std_logic_vector(META_BITS - 1 downto 0)           |             |
## Signals
| Name          | Type                                               | Description |
| ------------- | -------------------------------------------------- | ----------- |
| In_Valid_d    | std_logic                                          |             |
| In_IsKey_d    | std_logic                                          |             |
| In_Data_d     | T_SLM(INPUTS - 1 downto 0, DATA_BITS - 1 downto 0) |             |
| In_Meta_d     | std_logic_vector(META_BITS - 1 downto 0)           |             |
| MetaVector    | T_META_VECTOR(STAGES downto 0)                     |             |
| DataMatrix    | T_DATA_MATRIX(STAGES downto 0)                     |             |
| MetaOutputs_d | T_META                                             |             |
| DataOutputs_d | T_SLM(INPUTS - 1 downto 0, DATA_BITS - 1 downto 0) |             |
## Constants
| Name             | Type     | Value                                                                                               | Description |
| ---------------- | -------- | --------------------------------------------------------------------------------------------------- | ----------- |
| C_VERBOSE        | boolean  |  POC_VERBOSE                                                                                        |             |
| STAGES           | positive |  INPUTS                                                                                             |             |
| DELAY            | positive |  (STAGES	/ PIPELINE_STAGE_AFTER) + ite(ADD_INPUT_REGISTERS, 1, 0) + ite(ADD_OUTPUT_REGISTERS, 1, 0) |             |
| META_VALID_BIT   | natural  |  0                                                                                                  |             |
| META_ISKEY_BIT   | natural  |  1                                                                                                  |             |
| META_VECTOR_BITS | positive |  META_BITS + 2                                                                                      |             |
## Types
| Name          | Type | Description |
| ------------- | ---- | ----------- |
| T_META_VECTOR |      |             |
| T_DATA_VECTOR |      |             |
| T_DATA_MATRIX |      |             |
## Functions
- to_dv <font id="function_arguments">(slm : T_SLM)</font> <font id="function_return">return T_DATA_VECTOR</font>
- to_slm <font id="function_arguments">(dv : T_DATA_VECTOR)</font> <font id="function_return">return T_SLM</font>
