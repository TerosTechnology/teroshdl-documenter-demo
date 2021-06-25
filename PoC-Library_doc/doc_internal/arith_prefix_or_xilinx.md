# Entity: arith_prefix_or_xilinx
## Diagram
![Diagram](arith_prefix_or_xilinx.svg "Diagram")
## Generics
| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| N            | positive |       |             |
## Ports
| Port name | Direction | Type                           | Description |
| --------- | --------- | ------------------------------ | ----------- |
| x         | in        | std_logic_vector(N-1 downto 0) |             |
| y         | out       | std_logic_vector(N-1 downto 0) |             |
## Signals
| Name | Type                           | Description |
| ---- | ------------------------------ | ----------- |
| c    | std_logic_vector(N-1 downto 0) |             |
## Constants
| Name | Type                           | Value                        | Description |
| ---- | ------------------------------ | ---------------------------- | ----------- |
| d    | std_logic_vector(N-2 downto 0) |  (N-2 downto 1 => '1') & '0' |             |
