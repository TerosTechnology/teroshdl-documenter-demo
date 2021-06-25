# Entity: pp_fifo
## Diagram
![Diagram](pp_fifo.svg "Diagram")
## Generics
| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| DEPTH        | natural | 64    |             |
| WIDTH        | natural | 32    |             |
## Ports
| Port name | Direction | Type                                 | Description |
| --------- | --------- | ------------------------------------ | ----------- |
| clk       | in        | std_logic                            |             |
| reset     | in        | std_logic                            |             |
| full      | out       | std_logic                            |             |
| empty     | out       | std_logic                            |             |
| data_in   | in        | std_logic_vector(WIDTH - 1 downto 0) |             |
| data_out  | out       | std_logic_vector(WIDTH - 1 downto 0) |             |
| push      | in        | std_logic                            |             |
| pop       | in        | std_logic                            |             |
## Signals
| Name    | Type         | Description |
| ------- | ------------ | ----------- |
| memory  | memory_array |             |
| top     | index_type   |             |
|  bottom | index_type   |             |
| prev_op | fifo_op      |             |
## Types
| Name         | Type                  | Description |
| ------------ | --------------------- | ----------- |
| memory_array |                       |             |
| fifo_op      | (FIFO_POP, FIFO_PUSH) |             |
## Processes
- read: _( clk )_

- write: _( clk )_

- set_prev_op: _( clk )_

