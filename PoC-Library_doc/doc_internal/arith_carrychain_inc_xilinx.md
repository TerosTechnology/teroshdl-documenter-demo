# Entity: arith_carrychain_inc_xilinx
## Diagram
![Diagram](arith_carrychain_inc_xilinx.svg "Diagram")
## Generics
| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| BITS         | positive |       |             |
## Ports
| Port name | Direction | Type                                | Description |
| --------- | --------- | ----------------------------------- | ----------- |
| X         | in        | std_logic_vector(BITS - 1 downto 0) |             |
| CIn       | in        | std_logic                           |             |
| Y         | out       | std_logic_vector(BITS - 1 downto 0) |             |
## Signals
| Name | Type                            | Description |
| ---- | ------------------------------- | ----------- |
| ci   | std_logic_vector(BITS downto 0) |             |
| co   | std_logic_vector(BITS downto 0) |             |
