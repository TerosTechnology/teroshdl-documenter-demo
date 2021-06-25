# Entity: arith_counter_ring
## Diagram
![Diagram](arith_counter_ring.svg "Diagram")
## Generics
| Generic name    | Type     | Value | Description |
| --------------- | -------- | ----- | ----------- |
| BITS            | positive |       |             |
| INVERT_FEEDBACK | boolean  | FALSE |             |
## Ports
| Port name | Direction | Type                                | Description |
| --------- | --------- | ----------------------------------- | ----------- |
| Clock     | in        | std_logic                           |             |
| Reset     | in        | std_logic                           |             |
| seed      | in        | std_logic_vector(BITS - 1 downto 0) |             |
| inc       | in        | std_logic                           |             |
| dec       | in        | std_logic                           |             |
| value     | out       | std_logic_vector(BITS - 1 downto 0) |             |
## Signals
| Name    | Type                                | Description |
| ------- | ----------------------------------- | ----------- |
| Counter | std_logic_vector(BITS - 1 downto 0) |             |
## Constants
| Name   | Type      | Value                   | Description |
| ------ | --------- | ----------------------- | ----------- |
| invert | std_logic |  to_sl(INVERT_FEEDBACK) |             |
## Processes
- unnamed: _( Clock )_

