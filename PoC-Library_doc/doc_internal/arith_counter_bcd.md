# Entity: arith_counter_bcd
## Diagram
![Diagram](arith_counter_bcd.svg "Diagram")
## Generics
| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| DIGITS       | positive |       |             |
## Ports
| Port name | Direction | Type                            | Description |
| --------- | --------- | ------------------------------- | ----------- |
| clk       | in        | std_logic                       |             |
| rst       | in        | std_logic                       |             |
| inc       | in        | std_logic                       |             |
| val       | out       | T_BCD_VECTOR(DIGITS-1 downto 0) |             |
## Signals
| Name | Type                        | Description |
| ---- | --------------------------- | ----------- |
| p    | unsigned(DIGITS-1 downto 0) |             |
| c    | unsigned(DIGITS   downto 0) |             |
