# Entity: neorv32_sysinfo
## Diagram
![Diagram](neorv32_sysinfo.svg "Diagram")
## Generics
| Generic name         | Type                           | Value       | Description |
| -------------------- | ------------------------------ | ----------- | ----------- |
| CLOCK_FREQUENCY      | natural                        | 0           |             |
| INT_BOOTLOADER_EN    | boolean                        | true        |             |
| USER_CODE            | std_ulogic_vector(31 downto 0) | x"00000000" |             |
| MEM_INT_IMEM_EN      | boolean                        | true        |             |
| MEM_INT_IMEM_SIZE    | natural                        | 8*1024      |             |
| MEM_INT_DMEM_EN      | boolean                        | true        |             |
| MEM_INT_DMEM_SIZE    | natural                        | 4*1024      |             |
| ICACHE_EN            | boolean                        | true        |             |
| ICACHE_NUM_BLOCKS    | natural                        | 4           |             |
| ICACHE_BLOCK_SIZE    | natural                        | 64          |             |
| ICACHE_ASSOCIATIVITY | natural                        | 1           |             |
| MEM_EXT_EN           | boolean                        | false       |             |
| ON_CHIP_DEBUGGER_EN  | boolean                        | false       |             |
| IO_GPIO_EN           | boolean                        | true        |             |
| IO_MTIME_EN          | boolean                        | true        |             |
| IO_UART0_EN          | boolean                        | true        |             |
| IO_UART1_EN          | boolean                        | true        |             |
| IO_SPI_EN            | boolean                        | true        |             |
| IO_TWI_EN            | boolean                        | true        |             |
| IO_PWM_NUM_CH        | natural                        | 4           |             |
| IO_WDT_EN            | boolean                        | true        |             |
| IO_TRNG_EN           | boolean                        | true        |             |
| IO_CFS_EN            | boolean                        | true        |             |
| IO_NCO_EN            | boolean                        | true        |             |
| IO_NEOLED_EN         | boolean                        | true        |             |
## Ports
| Port name | Direction | Type                           | Description |
| --------- | --------- | ------------------------------ | ----------- |
| clk_i     | in        | std_ulogic                     |             |
| addr_i    | in        | std_ulogic_vector(31 downto 0) |             |
| rden_i    | in        | std_ulogic                     |             |
| data_o    | out       | std_ulogic_vector(31 downto 0) |             |
| ack_o     | out       | std_ulogic                     |             |
## Signals
| Name        | Type                           | Description |
| ----------- | ------------------------------ | ----------- |
| acc_en      | std_ulogic                     |             |
| addr        | std_ulogic_vector(31 downto 0) |             |
| rden        | std_ulogic                     |             |
| info_addr   | std_ulogic_vector(02 downto 0) |             |
| sysinfo_mem | info_mem_t                     |             |
## Constants
| Name     | Type    | Value                         | Description |
| -------- | ------- | ----------------------------- | ----------- |
| hi_abb_c | natural |  index_size_f(io_size_c)-1    |             |
| lo_abb_c | natural |  index_size_f(sysinfo_size_c) |             |
## Types
| Name       | Type | Description |
| ---------- | ---- | ----------- |
| info_mem_t |      |             |
## Processes
- read_access: _( clk_i )_

