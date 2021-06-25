# Entity: sort_lru_list
## Diagram
![Diagram](sort_lru_list.svg "Diagram")
## Generics
| Generic name     | Type             | Value                        | Description |
| ---------------- | ---------------- | ---------------------------- | ----------- |
| ELEMENTS         | positive         | 16                           |             |
| KEY_BITS         | positive         | 4                            |             |
| DATA_BITS        | positive         | 8                            |             |
| INITIAL_ELEMENTS | T_SLM            | (0 to 15 => (0 to 7 => '0')) |             |
| INITIAL_VALIDS   | std_logic_vector | (0 to 15 => '0')             |             |
## Ports
| Port name | Direction | Type                                     | Description |
| --------- | --------- | ---------------------------------------- | ----------- |
| Clock     | in        | std_logic                                |             |
| Reset     | in        | std_logic                                |             |
| Insert    | in        | std_logic                                |             |
| Remove    | in        | std_logic                                |             |
| DataIn    | in        | std_logic_vector(DATA_BITS - 1 downto 0) |             |
| Valid     | out       | std_logic                                |             |
| DataOut   | out       | std_logic_vector(DATA_BITS - 1 downto 0) |             |
## Signals
| Name             | Type                                  | Description |
| ---------------- | ------------------------------------- | ----------- |
| NewElementsUp    | T_ELEMENT_VECTOR(ELEMENTS downto 0)   |             |
| ElementsUp       | T_ELEMENT_VECTOR(ELEMENTS downto 0)   |             |
| ElementsDown     | T_ELEMENT_VECTOR(ELEMENTS downto 0)   |             |
| ValidsUp         | std_logic_vector(ELEMENTS downto 0)   |             |
| ValidsDown       | std_logic_vector(ELEMENTS downto 0)   |             |
| Unequal          | std_logic_vector(ELEMENTS-1 downto 0) |             |
| MovesDown        | std_logic_vector(ELEMENTS downto 0)   |             |
| MovesUp          | std_logic_vector(ELEMENTS downto 0)   |             |
| DataOutDown      | T_ELEMENT_VECTOR(ELEMENTS downto 0)   |             |
| MovesUpCond      | std_logic_vector(ELEMENTS downto 0)   |             |
| MovesDownCond    | std_logic_vector(ELEMENTS downto 0)   |             |
| MovesDownCondRev | std_logic_vector(ELEMENTS downto 0)   |             |
| MovesDownRev     | std_logic_vector(ELEMENTS downto 0)   |             |
## Types
| Name             | Type | Description |
| ---------------- | ---- | ----------- |
| T_ELEMENT_VECTOR |      |             |
## Instantiations
- MovesUpProp: poc.arith_prefix_and
- MovesDownProp: poc.arith_prefix_and
