# Entity: neorv32_top
## Diagram
![Diagram](neorv32_top.svg "Diagram")
## Generics
| Generic name                 | Type                           | Value       | Description |
| ---------------------------- | ------------------------------ | ----------- | ----------- |
| CLOCK_FREQUENCY              | natural                        | 0           |             |
| USER_CODE                    | std_ulogic_vector(31 downto 0) | x"00000000" |             |
| HW_THREAD_ID                 | natural                        | 0           |             |
| INT_BOOTLOADER_EN            | boolean                        | true        |             |
| ON_CHIP_DEBUGGER_EN          | boolean                        | false       |             |
| CPU_EXTENSION_RISCV_A        | boolean                        | false       |             |
| CPU_EXTENSION_RISCV_C        | boolean                        | false       |             |
| CPU_EXTENSION_RISCV_E        | boolean                        | false       |             |
| CPU_EXTENSION_RISCV_M        | boolean                        | false       |             |
| CPU_EXTENSION_RISCV_U        | boolean                        | false       |             |
| CPU_EXTENSION_RISCV_Zfinx    | boolean                        | false       |             |
| CPU_EXTENSION_RISCV_Zicsr    | boolean                        | true        |             |
| CPU_EXTENSION_RISCV_Zifencei | boolean                        | false       |             |
| CPU_EXTENSION_RISCV_Zmmul    | boolean                        | false       |             |
| FAST_MUL_EN                  | boolean                        | false       |             |
| FAST_SHIFT_EN                | boolean                        | false       |             |
| CPU_CNT_WIDTH                | natural                        | 64          |             |
| PMP_NUM_REGIONS              | natural                        | 0           |             |
| PMP_MIN_GRANULARITY          | natural                        | 64*1024     |             |
| HPM_NUM_CNTS                 | natural                        | 0           |             |
| HPM_CNT_WIDTH                | natural                        | 40          |             |
| MEM_INT_IMEM_EN              | boolean                        | true        |             |
| MEM_INT_IMEM_SIZE            | natural                        | 16*1024     |             |
| MEM_INT_DMEM_EN              | boolean                        | true        |             |
| MEM_INT_DMEM_SIZE            | natural                        | 8*1024      |             |
| ICACHE_EN                    | boolean                        | false       |             |
| ICACHE_NUM_BLOCKS            | natural                        | 4           |             |
| ICACHE_BLOCK_SIZE            | natural                        | 64          |             |
| ICACHE_ASSOCIATIVITY         | natural                        | 1           |             |
| MEM_EXT_EN                   | boolean                        | false       |             |
| MEM_EXT_TIMEOUT              | natural                        | 255         |             |
| IO_GPIO_EN                   | boolean                        | true        |             |
| IO_MTIME_EN                  | boolean                        | true        |             |
| IO_UART0_EN                  | boolean                        | true        |             |
| IO_UART1_EN                  | boolean                        | true        |             |
| IO_SPI_EN                    | boolean                        | true        |             |
| IO_TWI_EN                    | boolean                        | true        |             |
| IO_PWM_NUM_CH                | natural                        | 4           |             |
| IO_WDT_EN                    | boolean                        | true        |             |
| IO_TRNG_EN                   | boolean                        | false       |             |
| IO_CFS_EN                    | boolean                        | false       |             |
| IO_CFS_CONFIG                | std_ulogic_vector(31 downto 0) | x"00000000" |             |
| IO_CFS_IN_SIZE               | positive                       | 32          |             |
| IO_CFS_OUT_SIZE              | positive                       | 32          |             |
| IO_NCO_EN                    | boolean                        | true        |             |
| IO_NEOLED_EN                 | boolean                        | true        |             |
## Ports
| Port name   | Direction | Type                                          | Description |
| ----------- | --------- | --------------------------------------------- | ----------- |
| clk_i       | in        | std_ulogic                                    |             |
| rstn_i      | in        | std_ulogic                                    |             |
| jtag_trst_i | in        | std_ulogic                                    |             |
| jtag_tck_i  | in        | std_ulogic                                    |             |
| jtag_tdi_i  | in        | std_ulogic                                    |             |
| jtag_tdo_o  | out       | std_ulogic                                    |             |
| jtag_tms_i  | in        | std_ulogic                                    |             |
| wb_tag_o    | out       | std_ulogic_vector(02 downto 0)                |             |
| wb_adr_o    | out       | std_ulogic_vector(31 downto 0)                |             |
| wb_dat_i    | in        | std_ulogic_vector(31 downto 0)                |             |
| wb_dat_o    | out       | std_ulogic_vector(31 downto 0)                |             |
| wb_we_o     | out       | std_ulogic                                    |             |
| wb_sel_o    | out       | std_ulogic_vector(03 downto 0)                |             |
| wb_stb_o    | out       | std_ulogic                                    |             |
| wb_cyc_o    | out       | std_ulogic                                    |             |
| wb_lock_o   | out       | std_ulogic                                    |             |
| wb_ack_i    | in        | std_ulogic                                    |             |
| wb_err_i    | in        | std_ulogic                                    |             |
| fence_o     | out       | std_ulogic                                    |             |
| fencei_o    | out       | std_ulogic                                    |             |
| gpio_o      | out       | std_ulogic_vector(31 downto 0)                |             |
| gpio_i      | in        | std_ulogic_vector(31 downto 0)                |             |
| uart0_txd_o | out       | std_ulogic                                    |             |
| uart0_rxd_i | in        | std_ulogic                                    |             |
| uart0_rts_o | out       | std_ulogic                                    |             |
| uart0_cts_i | in        | std_ulogic                                    |             |
| uart1_txd_o | out       | std_ulogic                                    |             |
| uart1_rxd_i | in        | std_ulogic                                    |             |
| uart1_rts_o | out       | std_ulogic                                    |             |
| uart1_cts_i | in        | std_ulogic                                    |             |
| spi_sck_o   | out       | std_ulogic                                    |             |
| spi_sdo_o   | out       | std_ulogic                                    |             |
| spi_sdi_i   | in        | std_ulogic                                    |             |
| spi_csn_o   | out       | std_ulogic_vector(07 downto 0)                |             |
| twi_sda_io  | inout     | std_logic                                     |             |
| twi_scl_io  | inout     | std_logic                                     |             |
| pwm_o       | out       | std_ulogic_vector(IO_PWM_NUM_CH-1 downto 0)   |             |
| cfs_in_i    | in        | std_ulogic_vector(IO_CFS_IN_SIZE-1  downto 0) |             |
| cfs_out_o   | out       | std_ulogic_vector(IO_CFS_OUT_SIZE-1 downto 0) |             |
| nco_o       | out       | std_ulogic_vector(02 downto 0)                |             |
| neoled_o    | out       | std_ulogic                                    |             |
| mtime_i     | in        | std_ulogic_vector(63 downto 0)                |             |
| mtime_o     | out       | std_ulogic_vector(63 downto 0)                |             |
| nm_irq_i    | in        | std_ulogic                                    |             |
| soc_firq_i  | in        | std_ulogic_vector(5 downto 0)                 |             |
| mtime_irq_i | in        | std_ulogic                                    |             |
| msw_irq_i   | in        | std_ulogic                                    |             |
| mext_irq_i  | in        | std_ulogic                                    |             |
## Signals
| Name           | Type                           | Description |
| -------------- | ------------------------------ | ----------- |
| rstn_gen       | std_ulogic_vector(7 downto 0)  |             |
| ext_rstn       | std_ulogic                     |             |
| sys_rstn       | std_ulogic                     |             |
| wdt_rstn       | std_ulogic                     |             |
| clk_div        | std_ulogic_vector(11 downto 0) |             |
| clk_div_ff     | std_ulogic_vector(11 downto 0) |             |
| clk_gen        | std_ulogic_vector(07 downto 0) |             |
| clk_gen_en     | std_ulogic_vector(08 downto 0) |             |
| wdt_cg_en      | std_ulogic                     |             |
| uart0_cg_en    | std_ulogic                     |             |
| uart1_cg_en    | std_ulogic                     |             |
| spi_cg_en      | std_ulogic                     |             |
| twi_cg_en      | std_ulogic                     |             |
| pwm_cg_en      | std_ulogic                     |             |
| cfs_cg_en      | std_ulogic                     |             |
| nco_cg_en      | std_ulogic                     |             |
| neoled_cg_en   | std_ulogic                     |             |
| cpu_i          | bus_interface_t                |             |
|  i_cache       | bus_interface_t                |             |
|  cpu_d         | bus_interface_t                |             |
|  p_bus         | bus_interface_t                |             |
| dci_ndmrstn    | std_ulogic                     |             |
| dci_halt_req   | std_ulogic                     |             |
| dmi            | dmi_t                          |             |
| io_acc         | std_ulogic                     |             |
| io_rden        | std_ulogic                     |             |
| io_wren        | std_ulogic                     |             |
| resp_bus       | resp_bus_t                     |             |
| fast_irq       | std_ulogic_vector(15 downto 0) |             |
| fast_irq_ack   | std_ulogic_vector(15 downto 0) |             |
| mtime_irq      | std_ulogic                     |             |
| gpio_irq       | std_ulogic                     |             |
| wdt_irq        | std_ulogic                     |             |
| uart0_rxd_irq  | std_ulogic                     |             |
| uart0_txd_irq  | std_ulogic                     |             |
| uart1_rxd_irq  | std_ulogic                     |             |
| uart1_txd_irq  | std_ulogic                     |             |
| spi_irq        | std_ulogic                     |             |
| twi_irq        | std_ulogic                     |             |
| cfs_irq        | std_ulogic                     |             |
| cfs_irq_ack    | std_ulogic                     |             |
| neoled_irq     | std_ulogic                     |             |
| mtime_time     | std_ulogic_vector(63 downto 0) |             |
| cpu_sleep      | std_ulogic                     |             |
| bus_keeper_err | std_ulogic                     |             |
## Constants
| Name                       | Type                                                          | Value                                                                          | Description |
| -------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------------ | ----------- |
| cpu_boot_addr_c            | std_ulogic_vector(31 downto 0)                                |  cond_sel_stdulogicvector_f(INT_BOOTLOADER_EN, boot_rom_base_c, ispace_base_c) |             |
| imem_align_check_c         | std_ulogic_vector(index_size_f(MEM_INT_IMEM_SIZE)-1 downto 0) |  (others => '0')                                                               |             |
| dmem_align_check_c         | std_ulogic_vector(index_size_f(MEM_INT_DMEM_SIZE)-1 downto 0) |  (others => '0')                                                               |             |
| resp_bus_entry_terminate_c | resp_bus_entry_t                                              |  (rdata => (others => '0'), ack => '0', err => '0')                            |             |
## Types
| Name             | Type                                                                                                                                                                                                                                    | Description |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| bus_interface_t  |                                                                                                                                                                                                                                         |             |
| dmi_t            |                                                                                                                                                                                                                                         |             |
| resp_bus_entry_t |                                                                                                                                                                                                                                         |             |
| resp_bus_id_t    | (RESP_IMEM, RESP_DMEM, RESP_BOOTROM, RESP_WISHBONE, RESP_GPIO, RESP_MTIME, RESP_UART0, RESP_UART1, RESP_SPI,                          RESP_TWI, RESP_PWM, RESP_WDT, RESP_TRNG, RESP_CFS, RESP_NCO, RESP_NEOLED, RESP_SYSINFO, RESP_OCD) |             |
| resp_bus_t       |                                                                                                                                                                                                                                         |             |
## Processes
- reset_generator: _( rstn_i, clk_i )_

- clock_generator: _( sys_rstn, clk_i )_

- soc_firq_sync: _( clk_i )_

- bus_response: _( resp_bus, bus_keeper_err )_

- mtime_sync: _( clk_i )_

## Instantiations
- neorv32_cpu_inst: neorv32_cpu
- neorv32_busswitch_inst: neorv32_busswitch
- neorv32_bus_keeper_inst: neorv32_bus_keeper
- neorv32_sysinfo_inst: neorv32_sysinfo
