# Entity: dstruct_deque
## Diagram
![Diagram](dstruct_deque.svg "Diagram")
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
| dinA      | in        | std_logic_vector(D_BITS-1 downto 0) |             |
| putA      | in        | std_logic                           |             |
| gotA      | in        | std_logic                           |             |
| doutA     | out       | std_logic_vector(D_BITS-1 downto 0) |             |
| validA    | out       | std_logic                           |             |
| fullA     | out       | std_logic                           |             |
| dinB      | in        | std_logic_vector(D_BITS-1 downto 0) |             |
| putB      | in        | std_logic                           |             |
| gotB      | in        | std_logic                           |             |
| doutB     | out       | std_logic_vector(D_BITS-1 downto 0) |             |
| validB    | out       | std_logic                           |             |
| fullB     | out       | std_logic                           |             |
## Signals
| Name           | Type                         | Description |
| -------------- | ---------------------------- | ----------- |
| combined       | std_logic_vector(3 downto 0) |             |
| ctrl           | std_logic_vector(1 downto 0) |             |
| sub            | unsigned(A_BITS-1 downto 0)  |             |
| last_operation | std_logic                    |             |
| last_op_ctrl   | last_op_ctrl_t               |             |
| delayed_valid  | std_logic                    |             |
| delay          | std_logic                    |             |
| stackpointerA  | unsigned (A_BITS-1 downto 0) |             |
| weA            | std_logic                    |             |
| stackpointerB  | unsigned (A_BITS-1 downto 0) |             |
| weB            | std_logic                    |             |
| ctrlA          | ctrl_t                       |             |
| ctrlB          | ctrl_t                       |             |
| adrA           | unsigned(A_BITS-1 downto 0)  |             |
| adrB           | unsigned(A_BITS-1 downto 0)  |             |
## Constants
| Name   | Type    | Value                | Description |
| ------ | ------- | -------------------- | ----------- |
| A_BITS | natural |  log2ceil(MIN_DEPTH) |             |
## Types
| Name           | Type               | Description |
| -------------- | ------------------ | ----------- |
| last_op_ctrl_t | (IDLE, SET, UNSET) |             |
| ctrl_t         | (PUSH, POP, IDLE)  |             |
## Processes
- unnamed: _( combined, stackpointerA, stackpointerB, last_operation, ctrl )_

- unnamed: _( clk )_

- unnamed: _( clk )_

- unnamed: _( clk )_

- unnamed: _( clk )_

- unnamed: _( sub, last_operation, delayed_valid )_

## Instantiations
- ram: poc.ocram_tdp_wf
