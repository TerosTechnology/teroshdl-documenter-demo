# Entity: stat_Average
## Diagram
![Diagram](stat_Average.svg "Diagram")
## Generics
| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| DATA_BITS    | positive | 8     |             |
| COUNTER_BITS | positive | 16    |             |
## Ports
| Port name | Direction | Type                                        | Description |
| --------- | --------- | ------------------------------------------- | ----------- |
| Clock     | in        | std_logic                                   |             |
| Reset     | in        | std_logic                                   |             |
| Enable    | in        | std_logic                                   |             |
| DataIn    | in        | std_logic_vector(DATA_BITS - 1 downto 0)    |             |
| Count     | out       | std_logic_vector(COUNTER_BITS - 1 downto 0) |             |
| Sum       | out       | std_logic_vector(COUNTER_BITS - 1 downto 0) |             |
| Average   | out       | std_logic_vector(COUNTER_BITS - 1 downto 0) |             |
| Valid     | out       | std_logic                                   |             |
## Signals
| Name       | Type                                        | Description |
| ---------- | ------------------------------------------- | ----------- |
| DataIn_us  | unsigned(DataIn'range)                      |             |
| Counter_i  | std_logic_vector(COUNTER_BITS - 1 downto 0) |             |
| Counter_us | unsigned(COUNTER_BITS - 1 downto 0)         |             |
| Sum_i      | std_logic_vector(COUNTER_BITS - 1 downto 0) |             |
| Sum_us     | unsigned(COUNTER_BITS - 1 downto 0)         |             |
| Quotient   | std_logic_vector(COUNTER_BITS - 1 downto 0) |             |
| Valid_i    | std_logic                                   |             |
| Count_d    | T_COUNT_VECTOR(DELAY downto 0)              |             |
| Sum_d      | T_SUM_VECTOR(DELAY downto 0)                |             |
## Constants
| Name  | Type     | Value             | Description |
| ----- | -------- | ----------------- | ----------- |
| DELAY | positive |  COUNTER_BITS - 1 |             |
## Types
| Name           | Type | Description |
| -------------- | ---- | ----------- |
| T_SUM_VECTOR   |      |             |
| T_COUNT_VECTOR |      |             |
## Processes
- unnamed: _( Clock )_

## Instantiations
- div: PoC.arith_div
