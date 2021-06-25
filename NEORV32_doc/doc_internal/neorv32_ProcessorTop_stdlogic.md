# Entity: neorv32_ProcessorTop_stdlogic
## Diagram
![Diagram](neorv32_ProcessorTop_stdlogic.svg "Diagram")
## Generics
| Generic name                 | Type                           | Value       | Description |
| ---------------------------- | ------------------------------ | ----------- | ----------- |
| CLOCK_FREQUENCY              | natural                        | 0           |             |
| INT_BOOTLOADER_EN            | boolean                        | true        |             |
| USER_CODE                    | std_logic_vector(31 downto 0)  | x"00000000" |             |
| HW_THREAD_ID                 | natural                        | 0           |             |
| ON_CHIP_DEBUGGER_EN          | boolean                        | false       |             |
| CPU_EXTENSION_RISCV_A        | boolean                        | false       |             |
| CPU_EXTENSION_RISCV_C        | boolean                        | false       |             |
| CPU_EXTENSION_RISCV_E        | boolean                        | false       |             |
| CPU_EXTENSION_RISCV_M        | boolean                        | false       |             |
| CPU_EXTENSION_RISCV_U        | boolean                        | false       |             |
| CPU_EXTENSION_RISCV_Zfinx    | boolean                        | false       |             |
| CPU_EXTENSION_RISCV_Zicsr    | boolean                        | true        |             |
| CPU_EXTENSION_RISCV_Zifencei | boolean                        | false       |             |
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
| IO_CFS_CONFIG                | std_ulogic_vector(31 downto 0) |             |             |
| IO_CFS_IN_SIZE               | positive                       | 32          |             |
| IO_CFS_OUT_SIZE              | positive                       | 32          |             |
| IO_NCO_EN                    | boolean                        | true        |             |
| IO_NEOLED_EN                 | boolean                        | true        |             |
## Ports
| Port name   | Direction | Type                                         | Description |
| ----------- | --------- | -------------------------------------------- | ----------- |
| clk_i       | in        | std_logic                                    |             |
| rstn_i      | in        | std_logic                                    |             |
| jtag_trst_i | in        | std_logic                                    |             |
| jtag_tck_i  | in        | std_logic                                    |             |
| jtag_tdi_i  | in        | std_logic                                    |             |
| jtag_tdo_o  | out       | std_logic                                    |             |
| jtag_tms_i  | in        | std_logic                                    |             |
| wb_tag_o    | out       | std_logic_vector(02 downto 0)                |             |
| wb_adr_o    | out       | std_logic_vector(31 downto 0)                |             |
| wb_dat_i    | in        | std_logic_vector(31 downto 0)                |             |
| wb_dat_o    | out       | std_logic_vector(31 downto 0)                |             |
| wb_we_o     | out       | std_logic                                    |             |
| wb_sel_o    | out       | std_logic_vector(03 downto 0)                |             |
| wb_stb_o    | out       | std_logic                                    |             |
| wb_cyc_o    | out       | std_logic                                    |             |
| wb_lock_o   | out       | std_logic                                    |             |
| wb_ack_i    | in        | std_logic                                    |             |
| wb_err_i    | in        | std_logic                                    |             |
| fence_o     | out       | std_logic                                    |             |
| fencei_o    | out       | std_logic                                    |             |
| gpio_o      | out       | std_logic_vector(31 downto 0)                |             |
| gpio_i      | in        | std_logic_vector(31 downto 0)                |             |
| uart0_txd_o | out       | std_logic                                    |             |
| uart0_rxd_i | in        | std_logic                                    |             |
| uart0_rts_o | out       | std_logic                                    |             |
| uart0_cts_i | in        | std_logic                                    |             |
| uart1_txd_o | out       | std_logic                                    |             |
| uart1_rxd_i | in        | std_logic                                    |             |
| uart1_rts_o | out       | std_logic                                    |             |
| uart1_cts_i | in        | std_logic                                    |             |
| spi_sck_o   | out       | std_logic                                    |             |
| spi_sdo_o   | out       | std_logic                                    |             |
| spi_sdi_i   | in        | std_logic                                    |             |
| spi_csn_o   | out       | std_logic_vector(07 downto 0)                |             |
| twi_sda_io  | inout     | std_logic                                    |             |
| twi_scl_io  | inout     | std_logic                                    |             |
| pwm_o       | out       | std_logic_vector(IO_PWM_NUM_CH-1 downto 0)   |             |
| cfs_in_i    | in        | std_logic_vector(IO_CFS_IN_SIZE-1  downto 0) |             |
| cfs_out_o   | out       | std_logic_vector(IO_CFS_OUT_SIZE-1 downto 0) |             |
| nco_o       | out       | std_logic_vector(02 downto 0)                |             |
| neoled_o    | out       | std_logic                                    |             |
| mtime_i     | in        | std_logic_vector(63 downto 0)                |             |
| mtime_o     | out       | std_logic_vector(63 downto 0)                |             |
| nm_irq_i    | in        | std_logic                                    |             |
| soc_firq_i  | in        | std_logic_vector(5 downto 0)                 |             |
| mtime_irq_i | in        | std_logic                                    |             |
| msw_irq_i   | in        | std_logic                                    |             |
| mext_irq_i  | in        | std_logic                                    |             |
## Signals
| Name            | Type                                          | Description |
| --------------- | --------------------------------------------- | ----------- |
| clk_i_int       | std_ulogic                                    |             |
| rstn_i_int      | std_ulogic                                    |             |
| jtag_trst_i_int | std_ulogic                                    |             |
| jtag_tck_i_int  | std_ulogic                                    |             |
| jtag_tdi_i_int  | std_ulogic                                    |             |
| jtag_tdo_o_int  | std_ulogic                                    |             |
| jtag_tms_i_int  | std_ulogic                                    |             |
| wb_tag_o_int    | std_ulogic_vector(02 downto 0)                |             |
| wb_adr_o_int    | std_ulogic_vector(31 downto 0)                |             |
| wb_dat_i_int    | std_ulogic_vector(31 downto 0)                |             |
| wb_dat_o_int    | std_ulogic_vector(31 downto 0)                |             |
| wb_we_o_int     | std_ulogic                                    |             |
| wb_sel_o_int    | std_ulogic_vector(03 downto 0)                |             |
| wb_stb_o_int    | std_ulogic                                    |             |
| wb_cyc_o_int    | std_ulogic                                    |             |
| wb_lock_o_int   | std_ulogic                                    |             |
| wb_ack_i_int    | std_ulogic                                    |             |
| wb_err_i_int    | std_ulogic                                    |             |
| fence_o_int     | std_ulogic                                    |             |
| fencei_o_int    | std_ulogic                                    |             |
| gpio_o_int      | std_ulogic_vector(31 downto 0)                |             |
| gpio_i_int      | std_ulogic_vector(31 downto 0)                |             |
| uart0_txd_o_int | std_ulogic                                    |             |
| uart0_rxd_i_int | std_ulogic                                    |             |
| uart0_rts_o_int | std_ulogic                                    |             |
| uart0_cts_i_int | std_ulogic                                    |             |
| uart1_txd_o_int | std_ulogic                                    |             |
| uart1_rxd_i_int | std_ulogic                                    |             |
| uart1_rts_o_int | std_ulogic                                    |             |
| uart1_cts_i_int | std_ulogic                                    |             |
| spi_sck_o_int   | std_ulogic                                    |             |
| spi_sdo_o_int   | std_ulogic                                    |             |
| spi_sdi_i_int   | std_ulogic                                    |             |
| spi_csn_o_int   | std_ulogic_vector(07 downto 0)                |             |
| pwm_o_int       | std_ulogic_vector(IO_PWM_NUM_CH-1 downto 0)   |             |
| cfs_in_i_int    | std_ulogic_vector(IO_CFS_IN_SIZE-1  downto 0) |             |
| cfs_out_o_int   | std_ulogic_vector(IO_CFS_OUT_SIZE-1 downto 0) |             |
| nco_o_int       | std_ulogic_vector(02 downto 0)                |             |
| neoled_o_int    | std_ulogic                                    |             |
| mtime_i_int     | std_ulogic_vector(63 downto 0)                |             |
| mtime_o_int     | std_ulogic_vector(63 downto 0)                |             |
| nm_irq_i_int    | std_ulogic                                    |             |
| soc_firq_i_int  | std_ulogic_vector(05 downto 0)                |             |
| mtime_irq_i_int | std_ulogic                                    |             |
| msw_irq_i_int   | std_ulogic                                    |             |
| mext_irq_i_int  | std_ulogic                                    |             |
## Constants
| Name              | Type                           | Value                             | Description |
| ----------------- | ------------------------------ | --------------------------------- | ----------- |
| USER_CODE_INT     | std_ulogic_vector(31 downto 0) |  std_ulogic_vector(USER_CODE)     |             |
| IO_CFS_CONFIG_INT | std_ulogic_vector(31 downto 0) |  std_ulogic_vector(IO_CFS_CONFIG) |             |
## Instantiations
- neorv32_top_inst: neorv32_top
