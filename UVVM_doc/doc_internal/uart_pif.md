# Entity: uart_pif
## Diagram
![Diagram](uart_pif.svg "Diagram")
## Ports
| Port name | Direction | Type                         | Description |
| --------- | --------- | ---------------------------- | ----------- |
| arst      | in        | std_logic                    |             |
| clk       | in        | std_logic                    |             |
| cs        | in        | std_logic                    |             |
| addr      | in        | unsigned                     |             |
| wr        | in        | std_logic                    |             |
| rd        | in        | std_logic                    |             |
| wdata     | in        | std_logic_vector(7 downto 0) |             |
| rdata     | out       | std_logic_vector(7 downto 0) |             |
| p2c       | out       | t_p2c                        |             |
| c2p       | in        | t_c2p                        |             |
## Signals
| Name    | Type                         | Description |
| ------- | ---------------------------- | ----------- |
| p2c_i   | t_p2c                        |             |
| rdata_i | std_logic_vector(7 downto 0) |             |
## Processes
- p_aux: _( wdata, addr, cs, wr, rd )_

- p_read_reg: _( cs, addr, rd, c2p, p2c_i )_

