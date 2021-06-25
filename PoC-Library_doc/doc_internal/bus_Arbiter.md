# Entity: bus_Arbiter
## Diagram
![Diagram](bus_Arbiter.svg "Diagram")
## Generics
| Generic name | Type     | Value    | Description |
| ------------ | -------- | -------- | ----------- |
| STRATEGY     | string   | "RR"     |             |
| PORTS        | positive | 1        |             |
| WEIGHTS      | T_INTVEC | (0 => 1) |             |
| OUTPUT_REG   | boolean  | TRUE     |             |
## Ports
| Port name      | Direction | Type                                             | Description |
| -------------- | --------- | ------------------------------------------------ | ----------- |
| Clock          | in        | std_logic                                        |             |
| Reset          | in        | std_logic                                        |             |
| Arbitrate      | in        | std_logic                                        |             |
| Request_Vector | in        | std_logic_vector(PORTS - 1 downto 0)             |             |
| Arbitrated     | out       | std_logic                                        |             |
| Grant_Vector   | out       | std_logic_vector(PORTS - 1 downto 0)             |             |
| Grant_Index    | out       | std_logic_vector(log2ceilnz(PORTS) - 1 downto 0) |             |
