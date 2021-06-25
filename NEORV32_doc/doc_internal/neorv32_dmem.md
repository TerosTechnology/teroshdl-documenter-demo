# Entity: neorv32_dmem
## Diagram
![Diagram](neorv32_dmem.svg "Diagram")
## Generics
| Generic name | Type                           | Value       | Description |
| ------------ | ------------------------------ | ----------- | ----------- |
| DMEM_BASE    | std_ulogic_vector(31 downto 0) | x"80000000" |             |
| DMEM_SIZE    | natural                        | 4*1024      |             |
## Ports
| Port name | Direction | Type                           | Description |
| --------- | --------- | ------------------------------ | ----------- |
| clk_i     | in        | std_ulogic                     |             |
| rden_i    | in        | std_ulogic                     |             |
| wren_i    | in        | std_ulogic                     |             |
| ben_i     | in        | std_ulogic_vector(03 downto 0) |             |
| addr_i    | in        | std_ulogic_vector(31 downto 0) |             |
| data_i    | in        | std_ulogic_vector(31 downto 0) |             |
| data_o    | out       | std_ulogic_vector(31 downto 0) |             |
| ack_o     | out       | std_ulogic                     |             |
## Signals
| Name           | Type                                                    | Description |
| -------------- | ------------------------------------------------------- | ----------- |
| acc_en         | std_ulogic                                              |             |
| rdata          | std_ulogic_vector(31 downto 0)                          |             |
| rden           | std_ulogic                                              |             |
| addr           | std_ulogic_vector(index_size_f(DMEM_SIZE/4)-1 downto 0) |             |
| mem_ram_b0     | mem8_t(0 to DMEM_SIZE/4-1)                              |             |
| mem_ram_b1     | mem8_t(0 to DMEM_SIZE/4-1)                              |             |
| mem_ram_b2     | mem8_t(0 to DMEM_SIZE/4-1)                              |             |
| mem_ram_b3     | mem8_t(0 to DMEM_SIZE/4-1)                              |             |
| mem_ram_b0_rd  | std_ulogic_vector(7 downto 0)                           |             |
|  mem_ram_b1_rd | std_ulogic_vector(7 downto 0)                           |             |
|  mem_ram_b2_rd | std_ulogic_vector(7 downto 0)                           |             |
|  mem_ram_b3_rd | std_ulogic_vector(7 downto 0)                           |             |
## Constants
| Name     | Type    | Value                    | Description |
| -------- | ------- | ------------------------ | ----------- |
| hi_abb_c | natural |  31                      |             |
| lo_abb_c | natural |  index_size_f(DMEM_SIZE) |             |
## Processes
- mem_access: _( clk_i )_

- bus_feedback: _( clk_i )_

