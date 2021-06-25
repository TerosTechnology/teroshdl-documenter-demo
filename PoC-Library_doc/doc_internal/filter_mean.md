# Entity: filter_mean
## Diagram
![Diagram](filter_mean.svg "Diagram")
## Generics
| Generic name   | Type      | Value | Description |
| -------------- | --------- | ----- | ----------- |
| TAPS           | positive  | 4     |             |
| INIT           | std_logic | '1'   |             |
| ADD_OUTPUT_REG | boolean   | FALSE |             |
## Ports
| Port name | Direction | Type      | Description |
| --------- | --------- | --------- | ----------- |
| Clock     | in        | std_logic |             |
| DataIn    | in        | std_logic |             |
| DataOut   | out       | std_logic |             |
## Signals
| Name      | Type                                | Description |
| --------- | ----------------------------------- | ----------- |
| Delays    | std_logic_vector(TAPS - 1 downto 0) |             |
| FilterOut | std_logic                           |             |
## Processes
- unnamed: _( Delays )_

