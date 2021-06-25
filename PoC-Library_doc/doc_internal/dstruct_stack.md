# Entity: dstruct_stack
## Diagram
![Diagram](dstruct_stack.svg "Diagram")
## Generics
| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| D_BITS       | positive |       |             |
| MIN_DEPTH    | positive |       |             |
## Ports
| Port name | Direction | Type                                | Description |
| --------- | --------- | ----------------------------------- | ----------- |
| clk       | in        | std_logic                           |             |
| rst       | in        | std_logic                           |             |
| din       | in        | std_logic_vector(D_BITS-1 downto 0) |             |
| put       | in        | std_logic                           |             |
| full      | out       | std_logic                           |             |
| got       | in        | std_logic                           |             |
| dout      | out       | std_logic_vector(D_BITS-1 downto 0) |             |
| valid     | out       | std_logic                           |             |
## Signals
| Name          | Type                                | Description |
| ------------- | ----------------------------------- | ----------- |
| stackpointer  | unsigned(A_BITS-1 downto 0)         |             |
| we            | std_logic                           |             |
| adr           | unsigned(A_BITS-1 downto 0)         |             |
| s_adr         | unsigned(A_BITS-1 downto 0)         |             |
| s_dout        | std_logic_vector(D_BITS-1 downto 0) |             |
| s_valid       | std_logic                           |             |
| s_din         | std_logic_vector(D_BITS-1 downto 0) |             |
| ctrl          | ctrl_t                              |             |
| current_state | state                               |             |
|  next_state   | state                               |             |
## Constants
| Name   | Type    | Value                | Description |
| ------ | ------- | -------------------- | ----------- |
| A_BITS | natural |  log2ceil(MIN_DEPTH) |             |
## Types
| Name   | Type                              | Description |
| ------ | --------------------------------- | ----------- |
| ctrl_t | (PUSH, POP, IDLE)                 |             |
| state  | (SEMPTY, NOTFULL, WAITING, SFULL) |             |
## Processes
- unnamed: _( clk )_

- unnamed: _( current_state, put, stackpointer, got )_

- unnamed: _( clk )_

## Instantiations
- ram: poc.ocram_sp
