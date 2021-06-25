# Entity: arith_sqrt
## Diagram
![Diagram](arith_sqrt.svg "Diagram")
## Generics
| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| N            | positive |       |             |
## Ports
| Port name | Direction | Type                               | Description |
| --------- | --------- | ---------------------------------- | ----------- |
| rst       | in        | std_logic                          |             |
| clk       | in        | std_logic                          |             |
| arg       | in        | std_logic_vector(N-1 downto 0)     |             |
| start     | in        | std_logic                          |             |
| sqrt      | out       | std_logic_vector((N-1)/2 downto 0) |             |
| rdy       | out       | std_logic                          |             |
## Signals
| Name | Type                         | Description |
| ---- | ---------------------------- | ----------- |
| Rmd  | unsigned(N+STEPS-1 downto 0) |             |
| Vld  | unsigned(STEPS-1 downto 0)   |             |
| Res  | unsigned(STEPS-1 downto 0)   |             |
| diff | unsigned(STEPS+1 downto 0)   |             |
## Constants
| Name  | Type     | Value    | Description |
| ----- | -------- | -------- | ----------- |
| STEPS | positive |  (N+1)/2 |             |
## Processes
- unnamed: _( clk )_

