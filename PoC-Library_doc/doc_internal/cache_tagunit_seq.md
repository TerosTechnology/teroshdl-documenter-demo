# Entity: cache_tagunit_seq
## Diagram
![Diagram](cache_tagunit_seq.svg "Diagram")
## Generics
| Generic name       | Type         | Value                                 | Description |
| ------------------ | ------------ | ------------------------------------- | ----------- |
| REPLACEMENT_POLICY | string       | "LRU"                                 |             |
| CACHE_LINES        | positive     | 32                                    |             |
| ASSOCIATIVITY      | positive     | 32                                    |             |
| TAG_BITS           | positive     | 128                                   |             |
| CHUNK_BITS         | positive     | 8                                     |             |
| TAG_BYTE_ORDER     | T_BYTE_ORDER | LITTLE_ENDIAN                         |             |
| USE_INITIAL_TAGS   | boolean      | false                                 |             |
| INITIAL_TAGS       | T_SLM        | (0 downto 0 => (127 downto 0 => '0')) |             |
## Ports
| Port name           | Direction | Type                                                   | Description |
| ------------------- | --------- | ------------------------------------------------------ | ----------- |
| Clock               | in        | std_logic                                              |             |
| Reset               | in        | std_logic                                              |             |
| Replace             | in        | std_logic                                              |             |
| Replaced            | out       | std_logic                                              |             |
| Replace_NewTag_rst  | out       | std_logic                                              |             |
| Replace_NewTag_rev  | out       | std_logic                                              |             |
| Replace_NewTag_nxt  | out       | std_logic                                              |             |
| Replace_NewTag_Data | in        | std_logic_vector(CHUNK_BITS - 1 downto 0)              |             |
| Replace_NewIndex    | out       | std_logic_vector(log2ceilnz(CACHE_LINES) - 1 downto 0) |             |
| Request             | in        | std_logic                                              |             |
| Request_ReadWrite   | in        | std_logic                                              |             |
| Request_Invalidate  | in        | std_logic                                              |             |
| Request_Tag_rst     | out       | std_logic                                              |             |
| Request_Tag_rev     | out       | std_logic                                              |             |
| Request_Tag_nxt     | out       | std_logic                                              |             |
| Request_Tag_Data    | in        | std_logic_vector(CHUNK_BITS - 1 downto 0)              |             |
| Request_Index       | out       | std_logic_vector(log2ceilnz(CACHE_LINES) - 1 downto 0) |             |
| Request_TagHit      | out       | std_logic                                              |             |
| Request_TagMiss     | out       | std_logic                                              |             |
## Constants
| Name | Type     | Value                        | Description |
| ---- | -------- | ---------------------------- | ----------- |
| SETS | positive |  CACHE_LINES / ASSOCIATIVITY |             |
