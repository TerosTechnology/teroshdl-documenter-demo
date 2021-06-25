# Entity: arith_counter_gray
## Diagram
![Diagram](arith_counter_gray.svg "Diagram")
## Generics
| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| BITS         | positive |       |             |
| INIT         | natural  | 0     |             |
## Ports
| Port name | Direction | Type                              | Description |
| --------- | --------- | --------------------------------- | ----------- |
| clk       | in        | std_logic                         |             |
| rst       | in        | std_logic                         |             |
| inc       | in        | std_logic                         |             |
| dec       | in        | std_logic                         |             |
| val       | out       | std_logic_vector(BITS-1 downto 0) |             |
| cry       | out       | std_logic                         |             |
## Signals
| Name         | Type                      | Description |
| ------------ | ------------------------- | ----------- |
| gray_cnt_r   | unsigned(BITS-1 downto 0) |             |
| gray_cnt_nxt | unsigned(BITS-1 downto 0) |             |
| en           | std_logic                 |             |
## Constants
| Name      | Type                      | Value                    | Description |
| --------- | ------------------------- | ------------------------ | ----------- |
| INIT_GRAY | unsigned(BITS-1 downto 0) |  gray_encode(INIT, BITS) |             |
## Functions
- gray_encode <font id="function_arguments">(val : natural; len : positive)</font> <font id="function_return">return unsigned</font>
- parity <font id="function_arguments">(val : unsigned)</font> <font id="function_return">return std_logic</font>
## Processes
- unnamed: _( clk )_

