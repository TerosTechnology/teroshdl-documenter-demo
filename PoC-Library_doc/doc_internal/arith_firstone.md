# Entity: arith_firstone
## Diagram
![Diagram](arith_firstone.svg "Diagram")
## Generics
| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| N            | positive |       |             |
## Ports
| Port name | Direction | Type                                     | Description |
| --------- | --------- | ---------------------------------------- | ----------- |
| tin       | in        | std_logic                                |             |
| rqst      | in        | std_logic_vector(N-1 downto 0)           |             |
| grnt      | out       | std_logic_vector(N-1 downto 0)           |             |
| tout      | out       | std_logic                                |             |
| bin       | out       | std_logic_vector(log2ceil(N)-1 downto 0) |             |
