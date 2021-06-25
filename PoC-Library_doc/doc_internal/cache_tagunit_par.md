# Entity: cache_tagunit_par
## Diagram
![Diagram](cache_tagunit_par.svg "Diagram")
## Generics
| Generic name       | Type     | Value | Description |
| ------------------ | -------- | ----- | ----------- |
| REPLACEMENT_POLICY | string   | "LRU" |             |
| CACHE_LINES        | positive | 32    |             |
| ASSOCIATIVITY      | positive | 32    |             |
| ADDRESS_BITS       | positive | 8     |             |
## Ports
| Port name        | Direction | Type                                                   | Description |
| ---------------- | --------- | ------------------------------------------------------ | ----------- |
| Clock            | in        | std_logic                                              |             |
| Reset            | in        | std_logic                                              |             |
| Replace          | in        | std_logic                                              |             |
| ReplaceLineIndex | out       | std_logic_vector(log2ceilnz(CACHE_LINES) - 1 downto 0) |             |
| OldAddress       | out       | std_logic_vector(ADDRESS_BITS - 1 downto 0)            |             |
| Request          | in        | std_logic                                              |             |
| ReadWrite        | in        | std_logic                                              |             |
| Invalidate       | in        | std_logic                                              |             |
| Address          | in        | std_logic_vector(ADDRESS_BITS - 1 downto 0)            |             |
| LineIndex        | out       | std_logic_vector(log2ceilnz(CACHE_LINES) - 1 downto 0) |             |
| TagHit           | out       | std_logic                                              |             |
| TagMiss          | out       | std_logic                                              |             |
## Constants
| Name | Type     | Value                        | Description |
| ---- | -------- | ---------------------------- | ----------- |
| SETS | positive |  CACHE_LINES / ASSOCIATIVITY |             |
## Functions
- contains_x <font id="function_arguments">(value : unsigned)</font> <font id="function_return">return boolean</font>
