# Entity: neorv32_cfs
## Diagram
![Diagram](neorv32_cfs.svg "Diagram")
## Generics
| Generic name | Type                           | Value | Description |
| ------------ | ------------------------------ | ----- | ----------- |
| CFS_CONFIG   | std_ulogic_vector(31 downto 0) |       |             |
| CFS_IN_SIZE  | positive                       | 32    |             |
| CFS_OUT_SIZE | positive                       | 32    |             |
## Ports
| Port name   | Direction | Type                                       | Description |
| ----------- | --------- | ------------------------------------------ | ----------- |
| clk_i       | in        | std_ulogic                                 |             |
| rstn_i      | in        | std_ulogic                                 |             |
| addr_i      | in        | std_ulogic_vector(31 downto 0)             |             |
| rden_i      | in        | std_ulogic                                 |             |
| wren_i      | in        | std_ulogic                                 |             |
| data_i      | in        | std_ulogic_vector(31 downto 0)             |             |
| data_o      | out       | std_ulogic_vector(31 downto 0)             |             |
| ack_o       | out       | std_ulogic                                 |             |
| clkgen_en_o | out       | std_ulogic                                 |             |
| clkgen_i    | in        | std_ulogic_vector(07 downto 0)             |             |
| sleep_i     | in        | std_ulogic                                 |             |
| irq_o       | out       | std_ulogic                                 |             |
| irq_ack_i   | in        | std_ulogic                                 |             |
| cfs_in_i    | in        | std_ulogic_vector(CFS_IN_SIZE-1 downto 0)  |             |
| cfs_out_o   | out       | std_ulogic_vector(CFS_OUT_SIZE-1 downto 0) |             |
## Signals
| Name       | Type                           | Description |
| ---------- | ------------------------------ | ----------- |
| acc_en     | std_ulogic                     |             |
| addr       | std_ulogic_vector(31 downto 0) |             |
| wren       | std_ulogic                     |             |
| rden       | std_ulogic                     |             |
| cfs_reg_wr | cfs_regs_t                     |             |
| cfs_reg_rd | cfs_regs_t                     |             |
## Constants
| Name     | Type    | Value                      | Description |
| -------- | ------- | -------------------------- | ----------- |
| hi_abb_c | natural |  index_size_f(io_size_c)-1 |             |
| lo_abb_c | natural |  index_size_f(cfs_size_c)  |             |
## Types
| Name       | Type | Description |
| ---------- | ---- | ----------- |
| cfs_regs_t |      |             |
## Processes
- host_access: _( clk_i )_

- cfs_core: _( cfs_reg_wr )_

