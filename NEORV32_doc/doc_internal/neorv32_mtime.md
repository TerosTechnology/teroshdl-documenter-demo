# Entity: neorv32_mtime
## Diagram
![Diagram](neorv32_mtime.svg "Diagram")
## Ports
| Port name | Direction | Type                           | Description |
| --------- | --------- | ------------------------------ | ----------- |
| clk_i     | in        | std_ulogic                     |             |
| addr_i    | in        | std_ulogic_vector(31 downto 0) |             |
| rden_i    | in        | std_ulogic                     |             |
| wren_i    | in        | std_ulogic                     |             |
| data_i    | in        | std_ulogic_vector(31 downto 0) |             |
| data_o    | out       | std_ulogic_vector(31 downto 0) |             |
| ack_o     | out       | std_ulogic                     |             |
| time_o    | out       | std_ulogic_vector(63 downto 0) |             |
| irq_o     | out       | std_ulogic                     |             |
## Signals
| Name          | Type                           | Description |
| ------------- | ------------------------------ | ----------- |
| acc_en        | std_ulogic                     |             |
| addr          | std_ulogic_vector(31 downto 0) |             |
| wren          | std_ulogic                     |             |
| mtime_lo_we   | std_ulogic                     |             |
| mtime_hi_we   | std_ulogic                     |             |
| mtimecmp_lo   | std_ulogic_vector(31 downto 0) |             |
| mtimecmp_hi   | std_ulogic_vector(31 downto 0) |             |
| mtime_lo      | std_ulogic_vector(31 downto 0) |             |
| mtime_lo_nxt  | std_ulogic_vector(32 downto 0) |             |
| mtime_lo_ovfl | std_ulogic_vector(00 downto 0) |             |
| mtime_hi      | std_ulogic_vector(31 downto 0) |             |
| cmp_lo        | std_ulogic                     |             |
| cmp_lo_ff     | std_ulogic                     |             |
| cmp_hi        | std_ulogic                     |             |
| cmp_match_ff  | std_ulogic                     |             |
## Constants
| Name     | Type    | Value                       | Description |
| -------- | ------- | --------------------------- | ----------- |
| hi_abb_c | natural |  index_size_f(io_size_c)-1  |             |
| lo_abb_c | natural |  index_size_f(mtime_size_c) |             |
## Processes
- wr_access: _( clk_i )_

- rd_access: _( clk_i )_

- cmp_sync: _( clk_i )_

