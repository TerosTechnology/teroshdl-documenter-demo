# Entity: neorv32_spi
## Diagram
![Diagram](neorv32_spi.svg "Diagram")
## Ports
| Port name   | Direction | Type                           | Description |
| ----------- | --------- | ------------------------------ | ----------- |
| clk_i       | in        | std_ulogic                     |             |
| addr_i      | in        | std_ulogic_vector(31 downto 0) |             |
| rden_i      | in        | std_ulogic                     |             |
| wren_i      | in        | std_ulogic                     |             |
| data_i      | in        | std_ulogic_vector(31 downto 0) |             |
| data_o      | out       | std_ulogic_vector(31 downto 0) |             |
| ack_o       | out       | std_ulogic                     |             |
| clkgen_en_o | out       | std_ulogic                     |             |
| clkgen_i    | in        | std_ulogic_vector(07 downto 0) |             |
| spi_sck_o   | out       | std_ulogic                     |             |
| spi_sdo_o   | out       | std_ulogic                     |             |
| spi_sdi_i   | in        | std_ulogic                     |             |
| spi_csn_o   | out       | std_ulogic_vector(07 downto 0) |             |
| irq_o       | out       | std_ulogic                     |             |
## Signals
| Name           | Type                           | Description |
| -------------- | ------------------------------ | ----------- |
| acc_en         | std_ulogic                     |             |
| addr           | std_ulogic_vector(31 downto 0) |             |
| wren           | std_ulogic                     |             |
| rden           | std_ulogic                     |             |
| ctrl           | std_ulogic_vector(14 downto 0) |             |
| tx_data_reg    | std_ulogic_vector(31 downto 0) |             |
| rx_data        | std_ulogic_vector(31 downto 0) |             |
| spi_clk        | std_ulogic                     |             |
| spi_start      | std_ulogic                     |             |
| spi_busy       | std_ulogic                     |             |
| spi_state0     | std_ulogic                     |             |
| spi_state1     | std_ulogic                     |             |
| spi_rtx_sreg   | std_ulogic_vector(31 downto 0) |             |
| spi_rx_data    | std_ulogic_vector(31 downto 0) |             |
| spi_bitcnt     | std_ulogic_vector(05 downto 0) |             |
| spi_bitcnt_max | std_ulogic_vector(05 downto 0) |             |
| spi_sdi_ff0    | std_ulogic                     |             |
| spi_sdi_ff1    | std_ulogic                     |             |
## Constants
| Name             | Type    | Value                      | Description |
| ---------------- | ------- | -------------------------- | ----------- |
| hi_abb_c         | natural |  index_size_f(io_size_c)-1 |             |
| lo_abb_c         | natural |  index_size_f(spi_size_c)  |             |
| ctrl_spi_cs0_c   | natural |   0                        |             |
| ctrl_spi_cs1_c   | natural |   1                        |             |
| ctrl_spi_cs2_c   | natural |   2                        |             |
| ctrl_spi_cs3_c   | natural |   3                        |             |
| ctrl_spi_cs4_c   | natural |   4                        |             |
| ctrl_spi_cs5_c   | natural |   5                        |             |
| ctrl_spi_cs6_c   | natural |   6                        |             |
| ctrl_spi_cs7_c   | natural |   7                        |             |
| ctrl_spi_en_c    | natural |   8                        |             |
| ctrl_spi_cpha_c  | natural |   9                        |             |
| ctrl_spi_prsc0_c | natural |  10                        |             |
| ctrl_spi_prsc1_c | natural |  11                        |             |
| ctrl_spi_prsc2_c | natural |  12                        |             |
| ctrl_spi_size0_c | natural |  13                        |             |
| ctrl_spi_size1_c | natural |  14                        |             |
| ctrl_spi_busy_c  | natural |  31                        |             |
## Processes
- rw_access: _( clk_i )_

- spi_rtx_unit: _( clk_i )_

- data_size: _( ctrl )_

- rx_mapping: _( ctrl, spi_rtx_sreg )_

