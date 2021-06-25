# Entity: arith_carrychain_inc
## Diagram
![Diagram](arith_carrychain_inc.svg "Diagram")
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
## Constants
| Name                    | Type    | Value                                                         | Description |
| ----------------------- | ------- | ------------------------------------------------------------- | ----------- |
| XILINX_FORCE_CARRYCHAIN | boolean |  (not SIMULATION) and (VENDOR = VENDOR_XILINX) and (BITS > 4) |             |
