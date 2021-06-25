# Entity: stat_Histogram
## Diagram
![Diagram](stat_Histogram.svg "Diagram")
## Generics
| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| DATA_BITS    | positive | 16    |             |
| COUNTER_BITS | positive | 16    |             |
## Ports
| Port name | Direction | Type                                                        | Description |
| --------- | --------- | ----------------------------------------------------------- | ----------- |
| Clock     | in        | std_logic                                                   |             |
| Reset     | in        | std_logic                                                   |             |
| Enable    | in        | std_logic                                                   |             |
| DataIn    | in        | std_logic_vector(DATA_BITS - 1 downto 0)                    |             |
| Histogram | out       | T_SLM(2**DATA_BITS - 1 downto 0, COUNTER_BITS - 1 downto 0) |             |
## Signals
| Name            | Type                                          | Description |
| --------------- | --------------------------------------------- | ----------- |
| HistogramMemory | T_HISTOGRAM_MEMORY(2**DATA_BITS - 1 downto 0) |             |
## Types
| Name               | Type | Description |
| ------------------ | ---- | ----------- |
| T_HISTOGRAM_MEMORY |      |             |
## Functions
- to_slm <font id="function_arguments">(usv : T_HISTOGRAM_MEMORY)</font> <font id="function_return">return T_SLM</font>
## Processes
- unnamed: _( Clock )_

