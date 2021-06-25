# Entity: random
## Diagram
![Diagram](fpga-random.svg "Diagram")
## Ports
| Port name | Direction | Type                           | Description |
| --------- | --------- | ------------------------------ | ----------- |
| clk       | in        | std_ulogic                     |             |
| data      | out       | std_ulogic_vector(63 downto 0) |             |
| raw       | out       | std_ulogic_vector(63 downto 0) |             |
| err       | out       | std_ulogic                     |             |
## Signals
| Name    | Type                           | Description |
| ------- | ------------------------------ | ----------- |
| ringosc | std_ulogic_vector(63 downto 0) |             |
| ro_reg  | std_ulogic_vector(63 downto 0) |             |
| lhca    | std_ulogic_vector(63 downto 0) |             |
## Constants
| Name      | Type                           | Value                | Description |
| --------- | ------------------------------ | -------------------- | ----------- |
| lhca_diag | std_ulogic_vector(63 downto 0) |  x"fffffffffffffffb" |             |
## Processes
- random_osc: _( all )_

- lhca_update: _( clk )_

