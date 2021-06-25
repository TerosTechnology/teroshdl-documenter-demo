# Entity: top
## Diagram
![Diagram](top.svg "Diagram")
## Ports
| Port name | Direction | Type                         | Description |
| --------- | --------- | ---------------------------- | ----------- |
| clk       | in        | std_logic                    |             |
| rstn      | in        | std_logic                    |             |
| in_valid  | in        | std_logic                    |             |
| in_ready  | out       | std_logic                    |             |
| in_data   | in        | std_logic_vector(7 downto 0) |             |
| out_valid | out       | std_logic                    |             |
| out_ready | in        | std_logic                    |             |
| out_data  | out       | std_logic_vector(7 downto 0) |             |
## Instantiations
- fifo_8b_32w_inst: component fifo_8b_32w
