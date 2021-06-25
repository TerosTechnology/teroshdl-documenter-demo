# Entity: sort_lru_cache
## Diagram
![Diagram](sort_lru_cache.svg "Diagram")
## Generics
| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| ELEMENTS     | positive | 32    |             |
## Ports
| Port name | Direction | Type                                                | Description |
| --------- | --------- | --------------------------------------------------- | ----------- |
| Clock     | in        | std_logic                                           |             |
| Reset     | in        | std_logic                                           |             |
| Insert    | in        | std_logic                                           |             |
| Free      | in        | std_logic                                           |             |
| KeyIn     | in        | std_logic_vector(log2ceilnz(ELEMENTS) - 1 downto 0) |             |
| KeyOut    | out       | std_logic_vector(log2ceilnz(ELEMENTS) - 1 downto 0) |             |
## Signals
| Name             | Type                                  | Description |
| ---------------- | ------------------------------------- | ----------- |
| NewElement       | T_ELEMENT                             |             |
| ElementsUp       | T_ELEMENT_VECTOR(ELEMENTS downto 0)   |             |
| ElementsDown     | T_ELEMENT_VECTOR(ELEMENTS downto 0)   |             |
| MovesDown        | std_logic_vector(ELEMENTS downto 0)   |             |
| MovesUp          | std_logic_vector(ELEMENTS downto 0)   |             |
| UnEqual          | std_logic_vector(ELEMENTS-1 downto 0) |             |
| MovesUpCond      | std_logic_vector(ELEMENTS downto 0)   |             |
| MovesDownCond    | std_logic_vector(ELEMENTS downto 0)   |             |
| MovesDownCondRev | std_logic_vector(ELEMENTS downto 0)   |             |
| MovesDownRev     | std_logic_vector(ELEMENTS downto 0)   |             |
## Constants
| Name     | Type     | Value                 | Description |
| -------- | -------- | --------------------- | ----------- |
| KEY_BITS | positive |  log2ceilnz(ELEMENTS) |             |
## Types
| Name             | Type | Description |
| ---------------- | ---- | ----------- |
| T_ELEMENT_VECTOR |      |             |
## Instantiations
- MovesUpProp: poc.arith_prefix_and
- MovesDownProp: poc.arith_prefix_and
