# Entity: arith_div
## Diagram
![Diagram](arith_div.svg "Diagram")
## Generics
| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| A_BITS       | positive |       |             |
| D_BITS       | positive |       |             |
| RAPOW        | positive | 1     |             |
| PIPELINED    | boolean  | false |             |
## Ports
| Port name | Direction | Type                                | Description |
| --------- | --------- | ----------------------------------- | ----------- |
| clk       | in        | std_logic                           |             |
| rst       | in        | std_logic                           |             |
| start     | in        | std_logic                           |             |
| ready     | out       | std_logic                           |             |
| A         | in        | std_logic_vector(A_BITS-1 downto 0) |             |
| D         | in        | std_logic_vector(D_BITS-1 downto 0) |             |
| Q         | out       | std_logic_vector(A_BITS-1 downto 0) |             |
| R         | out       | std_logic_vector(D_BITS-1 downto 0) |             |
| Z         | out       | std_logic                           |             |
## Signals
| Name | Type                       | Description |
| ---- | -------------------------- | ----------- |
| AR   | residue_vector(0 to DEPTH) |             |
| DR   | divisor_vector(0 to DEPTH) |             |
| ZR   | std_logic                  |             |
| exec | std_logic                  |             |
## Constants
| Name        | Type     | Value                     | Description |
| ----------- | -------- | ------------------------- | ----------- |
| STEPS       | positive |  (A_BITS+RAPOW-1)/RAPOW   |             |
| DEPTH       | natural  |  ite(PIPELINED, STEPS, 0) |             |
| TRUNK_BITS  | natural  |  (STEPS-1)*RAPOW          |             |
| ACTIVE_BITS | positive |  D_BITS + RAPOW           |             |
## Types
| Name           | Type | Description |
| -------------- | ---- | ----------- |
| residue_vector |      |             |
| divisor_vector |      |             |
## Functions
- div_step <font id="function_arguments">(av : residue; dv : divisor)</font> <font id="function_return">return residue</font>
## Processes
- unnamed: _( clk )_

