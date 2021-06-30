# Package: axi_dma_regs_pkg

## Constants

| Name                       | Type                          | Value                                                        | Description |
| -------------------------- | ----------------------------- | ------------------------------------------------------------ | ----------- |
| command_reg_addr           | natural                       |  0                                                           |             |
| status_reg_addr            | natural                       |  4                                                           |             |
| src_address_reg_addr       | natural                       |  8                                                           |             |
| dst_address_reg_addr       | natural                       |  12                                                          |             |
| num_bytes_reg_addr         | natural                       |  16                                                          |             |
| start_transfer_command_bit | natural                       |  0                                                           |             |
| start_transfer_command     | std_logic_vector(31 downto 0) |  (     start_transfer_command_bit => '1',     others => '0') |             |
| transfer_done_status_bit   | natural                       |  0                                                           |             |
| transfer_done_status       | std_logic_vector(31 downto 0) |  (     transfer_done_status_bit => '1',     others => '0')   |             |
