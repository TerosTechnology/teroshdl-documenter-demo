# Entity: neorv32_boot_rom
## Diagram
![Diagram](neorv32_boot_rom.svg "Diagram")
## Generics
| Generic name | Type                           | Value       | Description |
| ------------ | ------------------------------ | ----------- | ----------- |
| BOOTROM_BASE | std_ulogic_vector(31 downto 0) | x"FFFF0000" |             |
## Ports
| Port name | Direction | Type                           | Description |
| --------- | --------- | ------------------------------ | ----------- |
| clk_i     | in        | std_ulogic                     |             |
| rden_i    | in        | std_ulogic                     |             |
| addr_i    | in        | std_ulogic_vector(31 downto 0) |             |
| data_o    | out       | std_ulogic_vector(31 downto 0) |             |
| ack_o     | out       | std_ulogic                     |             |
## Signals
| Name   | Type                                                | Description |
| ------ | --------------------------------------------------- | ----------- |
| acc_en | std_ulogic                                          |             |
| rden   | std_ulogic                                          |             |
| rdata  | std_ulogic_vector(31 downto 0)                      |             |
| addr   | std_ulogic_vector(boot_rom_size_index_c-1 downto 0) |             |
## Constants
| Name                  | Type                              | Value                                                   | Description |
| --------------------- | --------------------------------- | ------------------------------------------------------- | ----------- |
| boot_rom_size_index_c | natural                           |  index_size_f((bootloader_init_image'length))           |             |
| boot_rom_size_c       | natural                           |  (2**boot_rom_size_index_c)*4                           |             |
| hi_abb_c              | natural                           |  31                                                     |             |
| lo_abb_c              | natural                           |  index_size_f(boot_rom_max_size_c)                      |             |
| mem_rom               | mem32_t(0 to boot_rom_size_c/4-1) |  mem32_init_f(bootloader_init_image, boot_rom_size_c/4) |             |
## Processes
- mem_file_access: _( clk_i )_

