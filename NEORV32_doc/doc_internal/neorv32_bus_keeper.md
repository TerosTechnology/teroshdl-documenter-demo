# Entity: neorv32_bus_keeper
## Diagram
![Diagram](neorv32_bus_keeper.svg "Diagram")
## Generics
| Generic name      | Type    | Value  | Description |
| ----------------- | ------- | ------ | ----------- |
| MEM_EXT_EN        | boolean | false  |             |
| MEM_INT_IMEM_EN   | boolean | true   |             |
| MEM_INT_IMEM_SIZE | natural | 8*1024 |             |
| MEM_INT_DMEM_EN   | boolean | true   |             |
| MEM_INT_DMEM_SIZE | natural | 8*1024 |             |
## Ports
| Port name | Direction | Type                           | Description |
| --------- | --------- | ------------------------------ | ----------- |
| clk_i     | in        | std_ulogic                     |             |
| rstn_i    | in        | std_ulogic                     |             |
| addr_i    | in        | std_ulogic_vector(31 downto 0) |             |
| rden_i    | in        | std_ulogic                     |             |
| wren_i    | in        | std_ulogic                     |             |
| ack_i     | in        | std_ulogic                     |             |
| err_i     | in        | std_ulogic                     |             |
| err_o     | out       | std_ulogic                     |             |
## Signals
| Name         | Type           | Description |
| ------------ | -------------- | ----------- |
| access_check | access_check_t |             |
| control      | control_t      |             |
## Types
| Name           | Type | Description |
| -------------- | ---- | ----------- |
| access_check_t |      |             |
| control_t      |      |             |
## Processes
- keeper_control: _( rstn_i, clk_i )_

