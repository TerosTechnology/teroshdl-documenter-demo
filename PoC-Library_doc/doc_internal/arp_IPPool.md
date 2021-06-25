# Entity: arp_IPPool
## Diagram
![Diagram](arp_IPPool.svg "Diagram")
## Generics
| Generic name          | Type                      | Value                                | Description |
| --------------------- | ------------------------- | ------------------------------------ | ----------- |
| IPPOOL_SIZE           | positive                  |                                      |             |
| INITIAL_IPV4ADDRESSES | T_NET_IPV4_ADDRESS_VECTOR | (0 to 7 => C_NET_IPV4_ADDRESS_EMPTY) |             |
## Ports
| Port name        | Direction | Type           | Description |
| ---------------- | --------- | -------------- | ----------- |
| Clock            | in        | std_logic      |             |
| Reset            | in        | std_logic      |             |
| Lookup           | in        | std_logic      |             |
| IPv4Address_rst  | out       | std_logic      |             |
| IPv4Address_nxt  | out       | std_logic      |             |
| IPv4Address_Data | in        | T_SLV_8        |             |
| PoolResult       | out       | T_CACHE_RESULT |             |
## Signals
| Name          | Type                                                  | Description |
| ------------- | ----------------------------------------------------- | ----------- |
| ReadWrite     | std_logic                                             |             |
| Insert        | std_logic                                             |             |
| TU_NewTag_rst | std_logic                                             |             |
| TU_NewTag_nxt | std_logic                                             |             |
| NewTag_Data   | T_SLV_8                                               |             |
| TU_Tag_rst    | std_logic                                             |             |
| TU_Tag_nxt    | std_logic                                             |             |
| TU_Tag_Data   | T_SLV_8                                               |             |
| CacheHit      | std_logic                                             |             |
| CacheMiss     | std_logic                                             |             |
| TU_Index      | std_logic_vector(CACHEMEMORY_INDEX_BITS - 1 downto 0) |             |
| TU_Index_d    | std_logic_vector(CACHEMEMORY_INDEX_BITS - 1 downto 0) |             |
| TU_Index_us   | unsigned(CACHEMEMORY_INDEX_BITS - 1 downto 0)         |             |
| TU_NewIndex   | std_logic_vector(CACHEMEMORY_INDEX_BITS - 1 downto 0) |             |
| TU_Replace    | std_logic                                             |             |
| TU_TagHit     | std_logic                                             |             |
| TU_TagMiss    | std_logic                                             |             |
## Constants
| Name                   | Type     | Value                                            | Description |
| ---------------------- | -------- | ------------------------------------------------ | ----------- |
| CACHE_LINES            | positive |  imax(IPPOOL_SIZE, INITIAL_IPV4ADDRESSES'length) |             |
| TAG_BITS               | positive |  32                                              |             |
| TAGCHUNK_BITS          | positive |  8                                               |             |
| CACHEMEMORY_INDEX_BITS | positive |  log2ceilnz(CACHE_LINES)                         |             |
| INITIAL_TAGS           | T_SLM    |  to_TagData(INITIAL_IPV4ADDRESSES)               |             |
## Functions
- to_TagData <font id="function_arguments">(CacheContent : T_NET_IPV4_ADDRESS_VECTOR)</font> <font id="function_return">return T_SLM</font>
## Instantiations
- TU: PoC.cache_TagUnit_seq
