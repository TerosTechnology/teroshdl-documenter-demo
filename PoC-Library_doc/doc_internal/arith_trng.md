# Entity: arith_trng
## Diagram
![Diagram](arith_trng.svg "Diagram")
## Generics
| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| BITS         | positive |       |             |
## Ports
| Port name | Direction | Type                              | Description |
| --------- | --------- | --------------------------------- | ----------- |
| clk       | in        | std_logic                         |             |
| rnd       | out       | std_logic_vector(BITS-1 downto 0) |             |
## Signals
| Name | Type                              | Description |
| ---- | --------------------------------- | ----------- |
| osc  | std_logic_vector(BITS-1 downto 0) |             |
## Instantiations
- sync_i: sync_Bits
