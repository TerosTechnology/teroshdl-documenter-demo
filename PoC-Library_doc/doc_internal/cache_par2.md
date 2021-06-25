# Entity: cache_par2
## Diagram
![Diagram](cache_par2.svg "Diagram")
## Generics
| Generic name       | Type     | Value | Description |
| ------------------ | -------- | ----- | ----------- |
| REPLACEMENT_POLICY | string   | "LRU" |             |
| CACHE_LINES        | positive | 32    |             |
| ASSOCIATIVITY      | positive | 32    |             |
| ADDR_BITS          | positive | 8     |             |
| DATA_BITS          | positive | 8     |             |
| HIT_MISS_REG       | boolean  | true  |             |
## Ports
| Port name    | Direction | Type                                       | Description |
| ------------ | --------- | ------------------------------------------ | ----------- |
| Clock        | in        | std_logic                                  |             |
| Reset        | in        | std_logic                                  |             |
| Request      | in        | std_logic                                  |             |
| ReadWrite    | in        | std_logic                                  |             |
| WriteMask    | in        | std_logic_vector(DATA_BITS/8 - 1 downto 0) |             |
| Invalidate   | in        | std_logic                                  |             |
| Replace      | in        | std_logic                                  |             |
| Address      | in        | std_logic_vector(ADDR_BITS-1 downto 0)     |             |
| CacheLineIn  | in        | std_logic_vector(DATA_BITS - 1 downto 0)   |             |
| CacheLineOut | out       | std_logic_vector(DATA_BITS - 1 downto 0)   |             |
| CacheHit     | out       | std_logic                                  |             |
| CacheMiss    | out       | std_logic                                  |             |
| OldAddress   | out       | std_logic_vector(ADDR_BITS-1 downto 0)     |             |
## Signals
| Name                | Type                                           | Description |
| ------------------- | ---------------------------------------------- | ----------- |
| TU_LineIndex        | std_logic_vector(LINE_INDEX_BITS - 1 downto 0) |             |
| TU_TagHit           | std_logic                                      |             |
| TU_TagMiss          | std_logic                                      |             |
| ReplaceWrite        | std_logic                                      |             |
| TU_ReplaceLineIndex | std_logic_vector(LINE_INDEX_BITS - 1 downto 0) |             |
| TU_OldAddress       | std_logic_vector(OldAddress'range)             |             |
| MemoryIndex_us      | unsigned(LINE_INDEX_BITS - 1 downto 0)         |             |
| MemoryAccess        | std_logic                                      |             |
## Constants
| Name            | Type     | Value                    | Description |
| --------------- | -------- | ------------------------ | ----------- |
| LINE_INDEX_BITS | positive |  log2ceilnz(CACHE_LINES) |             |
## Types
| Name                | Type | Description |
| ------------------- | ---- | ----------- |
| T_CACHE_LINE_VECTOR |      |             |
## Instantiations
- TU: PoC.cache_tagunit_par
