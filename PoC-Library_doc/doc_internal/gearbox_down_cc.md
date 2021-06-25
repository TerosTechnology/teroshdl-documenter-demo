# Entity: gearbox_down_cc
## Diagram
![Diagram](gearbox_down_cc.svg "Diagram")
## Generics
| Generic name         | Type     | Value | Description |
| -------------------- | -------- | ----- | ----------- |
| INPUT_BITS           | positive | 32    |             |
| OUTPUT_BITS          | positive | 24    |             |
| META_BITS            | natural  | 0     |             |
| ADD_INPUT_REGISTERS  | boolean  | FALSE |             |
| ADD_OUTPUT_REGISTERS | boolean  | FALSE |             |
## Ports
| Port name | Direction | Type                                       | Description |
| --------- | --------- | ------------------------------------------ | ----------- |
| Clock     | in        | std_logic                                  |             |
| In_Sync   | in        | std_logic                                  |             |
| In_Valid  | in        | std_logic                                  |             |
| In_Next   | out       | std_logic                                  |             |
| In_Data   | in        | std_logic_vector(INPUT_BITS - 1 downto 0)  |             |
| In_Meta   | in        | std_logic_vector(META_BITS - 1 downto 0)   |             |
| Out_Sync  | out       | std_logic                                  |             |
| Out_Valid | out       | std_logic                                  |             |
| Out_Data  | out       | std_logic_vector(OUTPUT_BITS - 1 downto 0) |             |
| Out_Meta  | out       | std_logic_vector(META_BITS - 1 downto 0)   |             |
| Out_First | out       | std_logic                                  |             |
| Out_Last  | out       | std_logic                                  |             |
## Signals
| Name             | Type                                            | Description |
| ---------------- | ----------------------------------------------- | ----------- |
| In_Sync_d        | std_logic                                       |             |
| In_Data_d        | std_logic_vector(INPUT_BITS - 1 downto 0)       |             |
| In_Meta_d        | std_logic_vector(META_BITS - 1 downto 0)        |             |
| In_Valid_d       | std_logic                                       |             |
| MuxSelect_rst    | std_logic                                       |             |
| MuxSelect_en     | std_logic                                       |             |
| MuxSelect_us     | unsigned(log2ceilnz(INPUT_CHUNKS) - 1 downto 0) |             |
| MuxSelect_ov     | std_logic                                       |             |
| Nxt              | std_logic                                       |             |
| AutoIncrement    | std_logic                                       |             |
| GearBoxInput     | T_CHUNK_VECTOR(INPUT_CHUNKS - 1 downto 0)       |             |
| GearBoxBuffer_en | std_logic                                       |             |
| GearBoxBuffer    | T_CHUNK_VECTOR(INPUT_CHUNKS - 1 downto 1)       |             |
| GearBoxOutput    | T_CHUNK_VECTOR(OUTPUT_CHUNKS - 1 downto 0)      |             |
| SyncOut          | std_logic                                       |             |
| ValidOut         | std_logic                                       |             |
| DataOut          | std_logic_vector(OUTPUT_BITS - 1 downto 0)      |             |
| MetaOut          | std_logic_vector(META_BITS - 1 downto 0)        |             |
| FirstOut         | std_logic                                       |             |
| LastOut          | std_logic                                       |             |
| Out_Sync_d       | std_logic                                       |             |
| Out_Valid_d      | std_logic                                       |             |
| Out_Data_d       | std_logic_vector(OUTPUT_BITS - 1 downto 0)      |             |
| Out_Meta_d       | std_logic_vector(META_BITS - 1 downto 0)        |             |
| Out_First_d      | std_logic                                       |             |
| Out_Last_d       | std_logic                                       |             |
## Constants
| Name                  | Type               | Value                                           | Description |
| --------------------- | ------------------ | ----------------------------------------------- | ----------- |
| C_VERBOSE             | boolean            |  FALSE                                          |             |
| BITS_PER_CHUNK        | positive           |  greatestCommonDivisor(INPUT_BITS, OUTPUT_BITS) |             |
| INPUT_CHUNKS          | positive           |  INPUT_BITS / BITS_PER_CHUNK                    |             |
| OUTPUT_CHUNKS         | positive           |  OUTPUT_BITS / BITS_PER_CHUNK                   |             |
| MUX_INPUT_TRANSLATION | T_MUX_DESCRIPTIONS |  genMuxDescription                              |             |
## Types
| Name               | Type | Description |
| ------------------ | ---- | ----------- |
| T_CHUNK_VECTOR     |      |             |
| T_MUX_INPUT        |      |             |
| T_MUX_INPUT_LIST   |      |             |
| T_MUX_INPUT_STRUCT |      |             |
| T_MUX_DESCRIPTIONS |      |             |
## Functions
- genMuxDescription <font id="function_arguments">()</font> <font id="function_return">return T_MUX_DESCRIPTIONS</font>
- to_chunkv <font id="function_arguments">(slv : std_logic_vector)</font> <font id="function_return">return T_CHUNK_VECTOR</font>
- to_slv <font id="function_arguments">(slvv : T_CHUNK_VECTOR)</font> <font id="function_return">return std_logic_vector</font>
## Processes
- unnamed: _( Clock )_

