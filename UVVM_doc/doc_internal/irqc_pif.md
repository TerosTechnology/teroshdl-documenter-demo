# Entity: irqc_pif
## Diagram
![Diagram](irqc_pif.svg "Diagram")
## Ports
| Port name | Direction | Type                         | Description |
| --------- | --------- | ---------------------------- | ----------- |
| arst      | in        | std_logic                    |             |
| clk       | in        | std_logic                    |             |
| cs        | in        | std_logic                    |             |
| addr      | in        | unsigned                     |             |
| wr        | in        | std_logic                    |             |
| rd        | in        | std_logic                    |             |
| din       | in        | std_logic_vector(7 downto 0) |             |
| dout      | out       | std_logic_vector(7 downto 0) |             |
| p2c       | out       | t_p2c                        |             |
| c2p       | in        | t_c2p                        |             |
## Signals
| Name   | Type                         | Description |
| ------ | ---------------------------- | ----------- |
| p2c_i  | t_p2c                        |             |
| dout_i | std_logic_vector(7 downto 0) |             |
## Processes
- p_read_reg: _( cs, addr, rd, c2p, p2c_i )_

- p_write_reg: _( clk, arst )_

- p_aux: _( wr, addr, din )_

