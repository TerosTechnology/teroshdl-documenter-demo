# Entity: stat_Maximum
## Diagram
![Diagram](stat_Maximum.svg "Diagram")
## Generics
| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| DEPTH        | positive | 8     |             |
| DATA_BITS    | positive | 16    |             |
| COUNTER_BITS | positive | 16    |             |
## Ports
| Port name | Direction | Type                                                 | Description |
| --------- | --------- | ---------------------------------------------------- | ----------- |
| Clock     | in        | std_logic                                            |             |
| Reset     | in        | std_logic                                            |             |
| Enable    | in        | std_logic                                            |             |
| DataIn    | in        | std_logic_vector(DATA_BITS - 1 downto 0)             |             |
| Valids    | out       | std_logic_vector(DEPTH - 1 downto 0)                 |             |
| Maximums  | out       | T_SLM(DEPTH - 1 downto 0, DATA_BITS - 1 downto 0)    |             |
| Counts    | out       | T_SLM(DEPTH - 1 downto 0, COUNTER_BITS - 1 downto 0) |             |
## Signals
| Name          | Type                                 | Description |
| ------------- | ------------------------------------ | ----------- |
| DataIn_us     | unsigned(DataIn'range)               |             |
| TagHit        | std_logic_vector(DEPTH - 1 downto 0) |             |
| MaximumHit    | std_logic_vector(DEPTH - 1 downto 0) |             |
| TagMemory     | T_TAG_MEMORY(DEPTH - 1 downto 0)     |             |
| CounterMemory | T_COUNTER_MEMORY(DEPTH - 1 downto 0) |             |
| MaximumIndex  | std_logic_vector(DEPTH - 1 downto 0) |             |
| ValidMemory   | std_logic_vector(DEPTH - 1 downto 0) |             |
## Types
| Name             | Type | Description |
| ---------------- | ---- | ----------- |
| T_TAG_MEMORY     |      |             |
| T_COUNTER_MEMORY |      |             |
## Functions
- to_slm <font id="function_arguments">(usv : T_TAG_MEMORY)</font> <font id="function_return">return T_SLM</font>
- to_slm <font id="function_arguments">(usv : T_COUNTER_MEMORY)</font> <font id="function_return">return T_SLM</font>
## Processes
- unnamed: _( Clock )_

