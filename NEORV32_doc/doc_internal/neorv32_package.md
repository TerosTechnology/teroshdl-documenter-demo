# Package: neorv32_package
## Constants
| Name                         | Type                                       | Value                                              | Description |
| ---------------------------- | ------------------------------------------ | -------------------------------------------------- | ----------- |
| ispace_base_c                | std_ulogic_vector(31 downto 0)             |  x"00000000"                                       |             |
| dspace_base_c                | std_ulogic_vector(31 downto 0)             |  x"80000000"                                       |             |
| wb_pipe_mode_c               | boolean                                    |  false                                             |             |
| wb_big_endian_c              | boolean                                    |  false                                             |             |
| wb_rx_buffer_c               | boolean                                    |  true                                              |             |
| ipb_entries_c                | natural                                    |  4                                                 |             |
| cp_timeout_en_c              | boolean                                    |  false                                             |             |
| dedicated_reset_c            | boolean                                    |  false                                             |             |
| pmp_num_regions_critical_c   | natural                                    |  8                                                 |             |
| max_proc_int_response_time_c | natural                                    |  15                                                |             |
| jtag_tap_idcode_version_c    | std_ulogic_vector(03 downto 0)             |  x"0"                                              |             |
| jtag_tap_idcode_partid_c     | std_ulogic_vector(15 downto 0)             |  x"cafe"                                           |             |
| jtag_tap_idcode_manid_c      | std_ulogic_vector(10 downto 0)             |  "00000000000"                                     |             |
| data_width_c                 | natural                                    |  32                                                |             |
| hw_version_c                 | std_ulogic_vector(31 downto 0)             |  x"01050702"                                       |             |
| archid_c                     | natural                                    |  19                                                |             |
| rf_r0_is_reg_c               | boolean                                    |  true                                              |             |
| def_rst_val_c                | std_ulogic                                 |  cond_sel_stdulogic_f(dedicated_reset_c, '0', '-') |             |
| imem_base_c                  | std_ulogic_vector(data_width_c-1 downto 0) |  ispace_base_c                                     |             |
| dmem_base_c                  | std_ulogic_vector(data_width_c-1 downto 0) |  dspace_base_c                                     |             |
| boot_rom_base_c              | std_ulogic_vector(data_width_c-1 downto 0) |  x"ffff0000"                                       |             |
| boot_rom_max_size_c          | natural                                    |  32*1024                                           |             |
| dm_base_c                    | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffff800"                                       |             |
| dm_size_c                    | natural                                    |  4*32*4                                            |             |
| dm_code_base_c               | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffff800"                                       |             |
| dm_pbuf_base_c               | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffff880"                                       |             |
| dm_data_base_c               | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffff900"                                       |             |
| dm_sreg_base_c               | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffff980"                                       |             |
| io_base_c                    | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe00"                                       |             |
| io_size_c                    | natural                                    |  512                                               |             |
| cfs_base_c                   | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe00"                                       |             |
| cfs_size_c                   | natural                                    |  64*4                                              |             |
| cfs_reg0_addr_c              | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe00"                                       |             |
| cfs_reg1_addr_c              | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe04"                                       |             |
| cfs_reg2_addr_c              | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe08"                                       |             |
| cfs_reg3_addr_c              | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe0c"                                       |             |
| cfs_reg4_addr_c              | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe10"                                       |             |
| cfs_reg5_addr_c              | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe14"                                       |             |
| cfs_reg6_addr_c              | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe18"                                       |             |
| cfs_reg7_addr_c              | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe1c"                                       |             |
| cfs_reg8_addr_c              | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe20"                                       |             |
| cfs_reg9_addr_c              | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe24"                                       |             |
| cfs_reg10_addr_c             | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe28"                                       |             |
| cfs_reg11_addr_c             | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe2c"                                       |             |
| cfs_reg12_addr_c             | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe30"                                       |             |
| cfs_reg13_addr_c             | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe34"                                       |             |
| cfs_reg14_addr_c             | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe38"                                       |             |
| cfs_reg15_addr_c             | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe3c"                                       |             |
| cfs_reg16_addr_c             | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe40"                                       |             |
| cfs_reg17_addr_c             | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe44"                                       |             |
| cfs_reg18_addr_c             | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe48"                                       |             |
| cfs_reg19_addr_c             | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe4c"                                       |             |
| cfs_reg20_addr_c             | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe50"                                       |             |
| cfs_reg21_addr_c             | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe54"                                       |             |
| cfs_reg22_addr_c             | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe58"                                       |             |
| cfs_reg23_addr_c             | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe5c"                                       |             |
| cfs_reg24_addr_c             | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe60"                                       |             |
| cfs_reg25_addr_c             | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe64"                                       |             |
| cfs_reg26_addr_c             | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe68"                                       |             |
| cfs_reg27_addr_c             | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe6c"                                       |             |
| cfs_reg28_addr_c             | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe70"                                       |             |
| cfs_reg29_addr_c             | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe74"                                       |             |
| cfs_reg30_addr_c             | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe78"                                       |             |
| cfs_reg31_addr_c             | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe7c"                                       |             |
| pwm_base_c                   | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe80"                                       |             |
| pwm_size_c                   | natural                                    |  16*4                                              |             |
| pwm_ctrl_addr_c              | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe80"                                       |             |
| pwm_duty0_addr_c             | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe84"                                       |             |
| pwm_duty1_addr_c             | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe88"                                       |             |
| pwm_duty2_addr_c             | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe8c"                                       |             |
| pwm_duty3_addr_c             | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe90"                                       |             |
| pwm_duty4_addr_c             | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe94"                                       |             |
| pwm_duty5_addr_c             | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe98"                                       |             |
| pwm_duty6_addr_c             | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffe9c"                                       |             |
| pwm_duty7_addr_c             | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffea0"                                       |             |
| pwm_duty8_addr_c             | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffea4"                                       |             |
| pwm_duty9_addr_c             | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffea8"                                       |             |
| pwm_duty10_addr_c            | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffeac"                                       |             |
| pwm_duty11_addr_c            | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffeb0"                                       |             |
| pwm_duty12_addr_c            | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffeb4"                                       |             |
| pwm_duty13_addr_c            | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffeb8"                                       |             |
| pwm_duty14_addr_c            | std_ulogic_vector(data_width_c-1 downto 0) |  x"fffffebc"                                       |             |
| gpio_base_c                  | std_ulogic_vector(data_width_c-1 downto 0) |  x"ffffff80"                                       |             |
| gpio_size_c                  | natural                                    |  2*4                                               |             |
| gpio_in_addr_c               | std_ulogic_vector(data_width_c-1 downto 0) |  x"ffffff80"                                       |             |
| gpio_out_addr_c              | std_ulogic_vector(data_width_c-1 downto 0) |  x"ffffff84"                                       |             |
| trng_base_c                  | std_ulogic_vector(data_width_c-1 downto 0) |  x"ffffff88"                                       |             |
| trng_size_c                  | natural                                    |  1*4                                               |             |
| trng_ctrl_addr_c             | std_ulogic_vector(data_width_c-1 downto 0) |  x"ffffff88"                                       |             |
| wdt_base_c                   | std_ulogic_vector(data_width_c-1 downto 0) |  x"ffffff8c"                                       |             |
| wdt_size_c                   | natural                                    |  1*4                                               |             |
| wdt_ctrl_addr_c              | std_ulogic_vector(data_width_c-1 downto 0) |  x"ffffff8c"                                       |             |
| mtime_base_c                 | std_ulogic_vector(data_width_c-1 downto 0) |  x"ffffff90"                                       |             |
| mtime_size_c                 | natural                                    |  4*4                                               |             |
| mtime_time_lo_addr_c         | std_ulogic_vector(data_width_c-1 downto 0) |  x"ffffff90"                                       |             |
| mtime_time_hi_addr_c         | std_ulogic_vector(data_width_c-1 downto 0) |  x"ffffff94"                                       |             |
| mtime_cmp_lo_addr_c          | std_ulogic_vector(data_width_c-1 downto 0) |  x"ffffff98"                                       |             |
| mtime_cmp_hi_addr_c          | std_ulogic_vector(data_width_c-1 downto 0) |  x"ffffff9c"                                       |             |
| uart0_base_c                 | std_ulogic_vector(data_width_c-1 downto 0) |  x"ffffffa0"                                       |             |
| uart0_size_c                 | natural                                    |  2*4                                               |             |
| uart0_ctrl_addr_c            | std_ulogic_vector(data_width_c-1 downto 0) |  x"ffffffa0"                                       |             |
| uart0_rtx_addr_c             | std_ulogic_vector(data_width_c-1 downto 0) |  x"ffffffa4"                                       |             |
| spi_base_c                   | std_ulogic_vector(data_width_c-1 downto 0) |  x"ffffffa8"                                       |             |
| spi_size_c                   | natural                                    |  2*4                                               |             |
| spi_ctrl_addr_c              | std_ulogic_vector(data_width_c-1 downto 0) |  x"ffffffa8"                                       |             |
| spi_rtx_addr_c               | std_ulogic_vector(data_width_c-1 downto 0) |  x"ffffffac"                                       |             |
| twi_base_c                   | std_ulogic_vector(data_width_c-1 downto 0) |  x"ffffffb0"                                       |             |
| twi_size_c                   | natural                                    |  2*4                                               |             |
| twi_ctrl_addr_c              | std_ulogic_vector(data_width_c-1 downto 0) |  x"ffffffb0"                                       |             |
| twi_rtx_addr_c               | std_ulogic_vector(data_width_c-1 downto 0) |  x"ffffffb4"                                       |             |
| nco_base_c                   | std_ulogic_vector(data_width_c-1 downto 0) |  x"ffffffc0"                                       |             |
| nco_size_c                   | natural                                    |  4*4                                               |             |
| nco_ctrl_addr_c              | std_ulogic_vector(data_width_c-1 downto 0) |  x"ffffffc0"                                       |             |
| nco_ch0_addr_c               | std_ulogic_vector(data_width_c-1 downto 0) |  x"ffffffc4"                                       |             |
| nco_ch1_addr_c               | std_ulogic_vector(data_width_c-1 downto 0) |  x"ffffffc8"                                       |             |
| nco_ch2_addr_c               | std_ulogic_vector(data_width_c-1 downto 0) |  x"ffffffcc"                                       |             |
| uart1_base_c                 | std_ulogic_vector(data_width_c-1 downto 0) |  x"ffffffd0"                                       |             |
| uart1_size_c                 | natural                                    |  2*4                                               |             |
| uart1_ctrl_addr_c            | std_ulogic_vector(data_width_c-1 downto 0) |  x"ffffffd0"                                       |             |
| uart1_rtx_addr_c             | std_ulogic_vector(data_width_c-1 downto 0) |  x"ffffffd4"                                       |             |
| neoled_base_c                | std_ulogic_vector(data_width_c-1 downto 0) |  x"ffffffd8"                                       |             |
| neoled_size_c                | natural                                    |  2*4                                               |             |
| neoled_ctrl_addr_c           | std_ulogic_vector(data_width_c-1 downto 0) |  x"ffffffd8"                                       |             |
| neoled_data_addr_c           | std_ulogic_vector(data_width_c-1 downto 0) |  x"ffffffdc"                                       |             |
| sysinfo_base_c               | std_ulogic_vector(data_width_c-1 downto 0) |  x"ffffffe0"                                       |             |
| sysinfo_size_c               | natural                                    |  8*4                                               |             |
| ctrl_rf_in_mux_c             | natural                                    |   0                                                |             |
| ctrl_rf_rs1_adr0_c           | natural                                    |   1                                                |             |
| ctrl_rf_rs1_adr1_c           | natural                                    |   2                                                |             |
| ctrl_rf_rs1_adr2_c           | natural                                    |   3                                                |             |
| ctrl_rf_rs1_adr3_c           | natural                                    |   4                                                |             |
| ctrl_rf_rs1_adr4_c           | natural                                    |   5                                                |             |
| ctrl_rf_rs2_adr0_c           | natural                                    |   6                                                |             |
| ctrl_rf_rs2_adr1_c           | natural                                    |   7                                                |             |
| ctrl_rf_rs2_adr2_c           | natural                                    |   8                                                |             |
| ctrl_rf_rs2_adr3_c           | natural                                    |   9                                                |             |
| ctrl_rf_rs2_adr4_c           | natural                                    |  10                                                |             |
| ctrl_rf_rd_adr0_c            | natural                                    |  11                                                |             |
| ctrl_rf_rd_adr1_c            | natural                                    |  12                                                |             |
| ctrl_rf_rd_adr2_c            | natural                                    |  13                                                |             |
| ctrl_rf_rd_adr3_c            | natural                                    |  14                                                |             |
| ctrl_rf_rd_adr4_c            | natural                                    |  15                                                |             |
| ctrl_rf_wb_en_c              | natural                                    |  16                                                |             |
| ctrl_rf_r0_we_c              | natural                                    |  17                                                |             |
| ctrl_alu_arith_c             | natural                                    |  18                                                |             |
| ctrl_alu_logic0_c            | natural                                    |  19                                                |             |
| ctrl_alu_logic1_c            | natural                                    |  20                                                |             |
| ctrl_alu_func0_c             | natural                                    |  21                                                |             |
| ctrl_alu_func1_c             | natural                                    |  22                                                |             |
| ctrl_alu_addsub_c            | natural                                    |  23                                                |             |
| ctrl_alu_opa_mux_c           | natural                                    |  24                                                |             |
| ctrl_alu_opb_mux_c           | natural                                    |  25                                                |             |
| ctrl_alu_unsigned_c          | natural                                    |  26                                                |             |
| ctrl_alu_shift_dir_c         | natural                                    |  27                                                |             |
| ctrl_alu_shift_ar_c          | natural                                    |  28                                                |             |
| ctrl_alu_frm0_c              | natural                                    |  29                                                |             |
| ctrl_alu_frm1_c              | natural                                    |  30                                                |             |
| ctrl_alu_frm2_c              | natural                                    |  31                                                |             |
| ctrl_bus_size_lsb_c          | natural                                    |  32                                                |             |
| ctrl_bus_size_msb_c          | natural                                    |  33                                                |             |
| ctrl_bus_rd_c                | natural                                    |  34                                                |             |
| ctrl_bus_wr_c                | natural                                    |  35                                                |             |
| ctrl_bus_if_c                | natural                                    |  36                                                |             |
| ctrl_bus_mo_we_c             | natural                                    |  37                                                |             |
| ctrl_bus_mi_we_c             | natural                                    |  38                                                |             |
| ctrl_bus_unsigned_c          | natural                                    |  39                                                |             |
| ctrl_bus_ierr_ack_c          | natural                                    |  40                                                |             |
| ctrl_bus_derr_ack_c          | natural                                    |  41                                                |             |
| ctrl_bus_fence_c             | natural                                    |  42                                                |             |
| ctrl_bus_fencei_c            | natural                                    |  43                                                |             |
| ctrl_bus_lock_c              | natural                                    |  44                                                |             |
| ctrl_bus_de_lock_c           | natural                                    |  45                                                |             |
| ctrl_bus_ch_lock_c           | natural                                    |  46                                                |             |
| ctrl_cp_id_lsb_c             | natural                                    |  47                                                |             |
| ctrl_cp_id_msb_c             | natural                                    |  48                                                |             |
| ctrl_ir_funct3_0_c           | natural                                    |  49                                                |             |
| ctrl_ir_funct3_1_c           | natural                                    |  50                                                |             |
| ctrl_ir_funct3_2_c           | natural                                    |  51                                                |             |
| ctrl_ir_funct12_0_c          | natural                                    |  52                                                |             |
| ctrl_ir_funct12_1_c          | natural                                    |  53                                                |             |
| ctrl_ir_funct12_2_c          | natural                                    |  54                                                |             |
| ctrl_ir_funct12_3_c          | natural                                    |  55                                                |             |
| ctrl_ir_funct12_4_c          | natural                                    |  56                                                |             |
| ctrl_ir_funct12_5_c          | natural                                    |  57                                                |             |
| ctrl_ir_funct12_6_c          | natural                                    |  58                                                |             |
| ctrl_ir_funct12_7_c          | natural                                    |  59                                                |             |
| ctrl_ir_funct12_8_c          | natural                                    |  60                                                |             |
| ctrl_ir_funct12_9_c          | natural                                    |  61                                                |             |
| ctrl_ir_funct12_10_c         | natural                                    |  62                                                |             |
| ctrl_ir_funct12_11_c         | natural                                    |  63                                                |             |
| ctrl_ir_opcode7_0_c          | natural                                    |  64                                                |             |
| ctrl_ir_opcode7_1_c          | natural                                    |  65                                                |             |
| ctrl_ir_opcode7_2_c          | natural                                    |  66                                                |             |
| ctrl_ir_opcode7_3_c          | natural                                    |  67                                                |             |
| ctrl_ir_opcode7_4_c          | natural                                    |  68                                                |             |
| ctrl_ir_opcode7_5_c          | natural                                    |  69                                                |             |
| ctrl_ir_opcode7_6_c          | natural                                    |  70                                                |             |
| ctrl_priv_lvl_lsb_c          | natural                                    |  71                                                |             |
| ctrl_priv_lvl_msb_c          | natural                                    |  72                                                |             |
| ctrl_sleep_c                 | natural                                    |  73                                                |             |
| ctrl_trap_c                  | natural                                    |  74                                                |             |
| ctrl_debug_running_c         | natural                                    |  75                                                |             |
| ctrl_width_c                 | natural                                    |  76                                                |             |
| cmp_equal_c                  | natural                                    |  0                                                 |             |
| cmp_less_c                   | natural                                    |  1                                                 |             |
| instr_opcode_lsb_c           | natural                                    |   0                                                |             |
| instr_opcode_msb_c           | natural                                    |   6                                                |             |
| instr_rd_lsb_c               | natural                                    |   7                                                |             |
| instr_rd_msb_c               | natural                                    |  11                                                |             |
| instr_funct3_lsb_c           | natural                                    |  12                                                |             |
| instr_funct3_msb_c           | natural                                    |  14                                                |             |
| instr_rs1_lsb_c              | natural                                    |  15                                                |             |
| instr_rs1_msb_c              | natural                                    |  19                                                |             |
| instr_rs2_lsb_c              | natural                                    |  20                                                |             |
| instr_rs2_msb_c              | natural                                    |  24                                                |             |
| instr_funct7_lsb_c           | natural                                    |  25                                                |             |
| instr_funct7_msb_c           | natural                                    |  31                                                |             |
| instr_funct12_lsb_c          | natural                                    |  20                                                |             |
| instr_funct12_msb_c          | natural                                    |  31                                                |             |
| instr_imm12_lsb_c            | natural                                    |  20                                                |             |
| instr_imm12_msb_c            | natural                                    |  31                                                |             |
| instr_imm20_lsb_c            | natural                                    |  12                                                |             |
| instr_imm20_msb_c            | natural                                    |  31                                                |             |
| instr_csr_id_lsb_c           | natural                                    |  20                                                |             |
| instr_csr_id_msb_c           | natural                                    |  31                                                |             |
| instr_funct5_lsb_c           | natural                                    |  27                                                |             |
| instr_funct5_msb_c           | natural                                    |  31                                                |             |
| opcode_lui_c                 | std_ulogic_vector(6 downto 0)              |  "0110111"                                         |             |
| opcode_auipc_c               | std_ulogic_vector(6 downto 0)              |  "0010111"                                         |             |
| opcode_alui_c                | std_ulogic_vector(6 downto 0)              |  "0010011"                                         |             |
| opcode_alu_c                 | std_ulogic_vector(6 downto 0)              |  "0110011"                                         |             |
| opcode_jal_c                 | std_ulogic_vector(6 downto 0)              |  "1101111"                                         |             |
| opcode_jalr_c                | std_ulogic_vector(6 downto 0)              |  "1100111"                                         |             |
| opcode_branch_c              | std_ulogic_vector(6 downto 0)              |  "1100011"                                         |             |
| opcode_load_c                | std_ulogic_vector(6 downto 0)              |  "0000011"                                         |             |
| opcode_store_c               | std_ulogic_vector(6 downto 0)              |  "0100011"                                         |             |
| opcode_fence_c               | std_ulogic_vector(6 downto 0)              |  "0001111"                                         |             |
| opcode_syscsr_c              | std_ulogic_vector(6 downto 0)              |  "1110011"                                         |             |
| opcode_atomic_c              | std_ulogic_vector(6 downto 0)              |  "0101111"                                         |             |
| opcode_fop_c                 | std_ulogic_vector(6 downto 0)              |  "1010011"                                         |             |
| funct3_beq_c                 | std_ulogic_vector(2 downto 0)              |  "000"                                             |             |
| funct3_bne_c                 | std_ulogic_vector(2 downto 0)              |  "001"                                             |             |
| funct3_blt_c                 | std_ulogic_vector(2 downto 0)              |  "100"                                             |             |
| funct3_bge_c                 | std_ulogic_vector(2 downto 0)              |  "101"                                             |             |
| funct3_bltu_c                | std_ulogic_vector(2 downto 0)              |  "110"                                             |             |
| funct3_bgeu_c                | std_ulogic_vector(2 downto 0)              |  "111"                                             |             |
| funct3_lb_c                  | std_ulogic_vector(2 downto 0)              |  "000"                                             |             |
| funct3_lh_c                  | std_ulogic_vector(2 downto 0)              |  "001"                                             |             |
| funct3_lw_c                  | std_ulogic_vector(2 downto 0)              |  "010"                                             |             |
| funct3_lbu_c                 | std_ulogic_vector(2 downto 0)              |  "100"                                             |             |
| funct3_lhu_c                 | std_ulogic_vector(2 downto 0)              |  "101"                                             |             |
| funct3_sb_c                  | std_ulogic_vector(2 downto 0)              |  "000"                                             |             |
| funct3_sh_c                  | std_ulogic_vector(2 downto 0)              |  "001"                                             |             |
| funct3_sw_c                  | std_ulogic_vector(2 downto 0)              |  "010"                                             |             |
| funct3_subadd_c              | std_ulogic_vector(2 downto 0)              |  "000"                                             |             |
| funct3_sll_c                 | std_ulogic_vector(2 downto 0)              |  "001"                                             |             |
| funct3_slt_c                 | std_ulogic_vector(2 downto 0)              |  "010"                                             |             |
| funct3_sltu_c                | std_ulogic_vector(2 downto 0)              |  "011"                                             |             |
| funct3_xor_c                 | std_ulogic_vector(2 downto 0)              |  "100"                                             |             |
| funct3_sr_c                  | std_ulogic_vector(2 downto 0)              |  "101"                                             |             |
| funct3_or_c                  | std_ulogic_vector(2 downto 0)              |  "110"                                             |             |
| funct3_and_c                 | std_ulogic_vector(2 downto 0)              |  "111"                                             |             |
| funct3_env_c                 | std_ulogic_vector(2 downto 0)              |  "000"                                             |             |
| funct3_csrrw_c               | std_ulogic_vector(2 downto 0)              |  "001"                                             |             |
| funct3_csrrs_c               | std_ulogic_vector(2 downto 0)              |  "010"                                             |             |
| funct3_csrrc_c               | std_ulogic_vector(2 downto 0)              |  "011"                                             |             |
| funct3_csrrwi_c              | std_ulogic_vector(2 downto 0)              |  "101"                                             |             |
| funct3_csrrsi_c              | std_ulogic_vector(2 downto 0)              |  "110"                                             |             |
| funct3_csrrci_c              | std_ulogic_vector(2 downto 0)              |  "111"                                             |             |
| funct3_fence_c               | std_ulogic_vector(2 downto 0)              |  "000"                                             |             |
| funct3_fencei_c              | std_ulogic_vector(2 downto 0)              |  "001"                                             |             |
| funct12_ecall_c              | std_ulogic_vector(11 downto 0)             |  x"000"                                            |             |
| funct12_ebreak_c             | std_ulogic_vector(11 downto 0)             |  x"001"                                            |             |
| funct12_mret_c               | std_ulogic_vector(11 downto 0)             |  x"302"                                            |             |
| funct12_wfi_c                | std_ulogic_vector(11 downto 0)             |  x"105"                                            |             |
| funct12_dret_c               | std_ulogic_vector(11 downto 0)             |  x"7b2"                                            |             |
| funct5_a_lr_c                | std_ulogic_vector(4 downto 0)              |  "00010"                                           |             |
| funct5_a_sc_c                | std_ulogic_vector(4 downto 0)              |  "00011"                                           |             |
| float_single_c               | std_ulogic_vector(1 downto 0)              |  "00"                                              |             |
| float_double_c               | std_ulogic_vector(1 downto 0)              |  "01"                                              |             |
| float_half_c                 | std_ulogic_vector(1 downto 0)              |  "10"                                              |             |
| float_quad_c                 | std_ulogic_vector(1 downto 0)              |  "11"                                              |             |
| fp_class_neg_inf_c           | natural                                    |  0                                                 |             |
| fp_class_neg_norm_c          | natural                                    |  1                                                 |             |
| fp_class_neg_denorm_c        | natural                                    |  2                                                 |             |
| fp_class_neg_zero_c          | natural                                    |  3                                                 |             |
| fp_class_pos_zero_c          | natural                                    |  4                                                 |             |
| fp_class_pos_denorm_c        | natural                                    |  5                                                 |             |
| fp_class_pos_norm_c          | natural                                    |  6                                                 |             |
| fp_class_pos_inf_c           | natural                                    |  7                                                 |             |
| fp_class_snan_c              | natural                                    |  8                                                 |             |
| fp_class_qnan_c              | natural                                    |  9                                                 |             |
| fp_exc_nv_c                  | natural                                    |  0                                                 |             |
| fp_exc_dz_c                  | natural                                    |  1                                                 |             |
| fp_exc_of_c                  | natural                                    |  2                                                 |             |
| fp_exc_uf_c                  | natural                                    |  3                                                 |             |
| fp_exc_nx_c                  | natural                                    |  4                                                 |             |
| fp_single_qnan_c             | std_ulogic_vector(31 downto 0)             |  x"7fc00000"                                       |             |
| fp_single_snan_c             | std_ulogic_vector(31 downto 0)             |  x"7fa00000"                                       |             |
| fp_single_pos_inf_c          | std_ulogic_vector(31 downto 0)             |  x"7f800000"                                       |             |
| fp_single_neg_inf_c          | std_ulogic_vector(31 downto 0)             |  x"ff800000"                                       |             |
| fp_single_pos_zero_c         | std_ulogic_vector(31 downto 0)             |  x"00000000"                                       |             |
| fp_single_neg_zero_c         | std_ulogic_vector(31 downto 0)             |  x"80000000"                                       |             |
| csr_class_float_c            | std_ulogic_vector(07 downto 0)             |  x"00"                                             |             |
| csr_fflags_c                 | std_ulogic_vector(11 downto 0)             |  x"001"                                            |             |
| csr_frm_c                    | std_ulogic_vector(11 downto 0)             |  x"002"                                            |             |
| csr_fcsr_c                   | std_ulogic_vector(11 downto 0)             |  x"003"                                            |             |
| csr_class_setup_c            | std_ulogic_vector(07 downto 0)             |  x"30"                                             |             |
| csr_mstatus_c                | std_ulogic_vector(11 downto 0)             |  x"300"                                            |             |
| csr_misa_c                   | std_ulogic_vector(11 downto 0)             |  x"301"                                            |             |
| csr_mie_c                    | std_ulogic_vector(11 downto 0)             |  x"304"                                            |             |
| csr_mtvec_c                  | std_ulogic_vector(11 downto 0)             |  x"305"                                            |             |
| csr_mcounteren_c             | std_ulogic_vector(11 downto 0)             |  x"306"                                            |             |
| csr_cnt_setup_c              | std_ulogic_vector(06 downto 0)             |  x"3" & "001"                                      |             |
| csr_mcountinhibit_c          | std_ulogic_vector(11 downto 0)             |  x"320"                                            |             |
| csr_mhpmevent3_c             | std_ulogic_vector(11 downto 0)             |  x"323"                                            |             |
| csr_mhpmevent4_c             | std_ulogic_vector(11 downto 0)             |  x"324"                                            |             |
| csr_mhpmevent5_c             | std_ulogic_vector(11 downto 0)             |  x"325"                                            |             |
| csr_mhpmevent6_c             | std_ulogic_vector(11 downto 0)             |  x"326"                                            |             |
| csr_mhpmevent7_c             | std_ulogic_vector(11 downto 0)             |  x"327"                                            |             |
| csr_mhpmevent8_c             | std_ulogic_vector(11 downto 0)             |  x"328"                                            |             |
| csr_mhpmevent9_c             | std_ulogic_vector(11 downto 0)             |  x"329"                                            |             |
| csr_mhpmevent10_c            | std_ulogic_vector(11 downto 0)             |  x"32a"                                            |             |
| csr_mhpmevent11_c            | std_ulogic_vector(11 downto 0)             |  x"32b"                                            |             |
| csr_mhpmevent12_c            | std_ulogic_vector(11 downto 0)             |  x"32c"                                            |             |
| csr_mhpmevent13_c            | std_ulogic_vector(11 downto 0)             |  x"32d"                                            |             |
| csr_mhpmevent14_c            | std_ulogic_vector(11 downto 0)             |  x"32e"                                            |             |
| csr_mhpmevent15_c            | std_ulogic_vector(11 downto 0)             |  x"32f"                                            |             |
| csr_mhpmevent16_c            | std_ulogic_vector(11 downto 0)             |  x"330"                                            |             |
| csr_mhpmevent17_c            | std_ulogic_vector(11 downto 0)             |  x"331"                                            |             |
| csr_mhpmevent18_c            | std_ulogic_vector(11 downto 0)             |  x"332"                                            |             |
| csr_mhpmevent19_c            | std_ulogic_vector(11 downto 0)             |  x"333"                                            |             |
| csr_mhpmevent20_c            | std_ulogic_vector(11 downto 0)             |  x"334"                                            |             |
| csr_mhpmevent21_c            | std_ulogic_vector(11 downto 0)             |  x"335"                                            |             |
| csr_mhpmevent22_c            | std_ulogic_vector(11 downto 0)             |  x"336"                                            |             |
| csr_mhpmevent23_c            | std_ulogic_vector(11 downto 0)             |  x"337"                                            |             |
| csr_mhpmevent24_c            | std_ulogic_vector(11 downto 0)             |  x"338"                                            |             |
| csr_mhpmevent25_c            | std_ulogic_vector(11 downto 0)             |  x"339"                                            |             |
| csr_mhpmevent26_c            | std_ulogic_vector(11 downto 0)             |  x"33a"                                            |             |
| csr_mhpmevent27_c            | std_ulogic_vector(11 downto 0)             |  x"33b"                                            |             |
| csr_mhpmevent28_c            | std_ulogic_vector(11 downto 0)             |  x"33c"                                            |             |
| csr_mhpmevent29_c            | std_ulogic_vector(11 downto 0)             |  x"33d"                                            |             |
| csr_mhpmevent30_c            | std_ulogic_vector(11 downto 0)             |  x"33e"                                            |             |
| csr_mhpmevent31_c            | std_ulogic_vector(11 downto 0)             |  x"33f"                                            |             |
| csr_class_trap_c             | std_ulogic_vector(07 downto 0)             |  x"34"                                             |             |
| csr_mscratch_c               | std_ulogic_vector(11 downto 0)             |  x"340"                                            |             |
| csr_mepc_c                   | std_ulogic_vector(11 downto 0)             |  x"341"                                            |             |
| csr_mcause_c                 | std_ulogic_vector(11 downto 0)             |  x"342"                                            |             |
| csr_mtval_c                  | std_ulogic_vector(11 downto 0)             |  x"343"                                            |             |
| csr_mip_c                    | std_ulogic_vector(11 downto 0)             |  x"344"                                            |             |
| csr_class_pmpcfg_c           | std_ulogic_vector(07 downto 0)             |  x"3a"                                             |             |
| csr_pmpcfg0_c                | std_ulogic_vector(11 downto 0)             |  x"3a0"                                            |             |
| csr_pmpcfg1_c                | std_ulogic_vector(11 downto 0)             |  x"3a1"                                            |             |
| csr_pmpcfg2_c                | std_ulogic_vector(11 downto 0)             |  x"3a2"                                            |             |
| csr_pmpcfg3_c                | std_ulogic_vector(11 downto 0)             |  x"3a3"                                            |             |
| csr_pmpcfg4_c                | std_ulogic_vector(11 downto 0)             |  x"3a4"                                            |             |
| csr_pmpcfg5_c                | std_ulogic_vector(11 downto 0)             |  x"3a5"                                            |             |
| csr_pmpcfg6_c                | std_ulogic_vector(11 downto 0)             |  x"3a6"                                            |             |
| csr_pmpcfg7_c                | std_ulogic_vector(11 downto 0)             |  x"3a7"                                            |             |
| csr_pmpcfg8_c                | std_ulogic_vector(11 downto 0)             |  x"3a8"                                            |             |
| csr_pmpcfg9_c                | std_ulogic_vector(11 downto 0)             |  x"3a9"                                            |             |
| csr_pmpcfg10_c               | std_ulogic_vector(11 downto 0)             |  x"3aa"                                            |             |
| csr_pmpcfg11_c               | std_ulogic_vector(11 downto 0)             |  x"3ab"                                            |             |
| csr_pmpcfg12_c               | std_ulogic_vector(11 downto 0)             |  x"3ac"                                            |             |
| csr_pmpcfg13_c               | std_ulogic_vector(11 downto 0)             |  x"3ad"                                            |             |
| csr_pmpcfg14_c               | std_ulogic_vector(11 downto 0)             |  x"3ae"                                            |             |
| csr_pmpcfg15_c               | std_ulogic_vector(11 downto 0)             |  x"3af"                                            |             |
| csr_pmpaddr0_c               | std_ulogic_vector(11 downto 0)             |  x"3b0"                                            |             |
| csr_pmpaddr1_c               | std_ulogic_vector(11 downto 0)             |  x"3b1"                                            |             |
| csr_pmpaddr2_c               | std_ulogic_vector(11 downto 0)             |  x"3b2"                                            |             |
| csr_pmpaddr3_c               | std_ulogic_vector(11 downto 0)             |  x"3b3"                                            |             |
| csr_pmpaddr4_c               | std_ulogic_vector(11 downto 0)             |  x"3b4"                                            |             |
| csr_pmpaddr5_c               | std_ulogic_vector(11 downto 0)             |  x"3b5"                                            |             |
| csr_pmpaddr6_c               | std_ulogic_vector(11 downto 0)             |  x"3b6"                                            |             |
| csr_pmpaddr7_c               | std_ulogic_vector(11 downto 0)             |  x"3b7"                                            |             |
| csr_pmpaddr8_c               | std_ulogic_vector(11 downto 0)             |  x"3b8"                                            |             |
| csr_pmpaddr9_c               | std_ulogic_vector(11 downto 0)             |  x"3b9"                                            |             |
| csr_pmpaddr10_c              | std_ulogic_vector(11 downto 0)             |  x"3ba"                                            |             |
| csr_pmpaddr11_c              | std_ulogic_vector(11 downto 0)             |  x"3bb"                                            |             |
| csr_pmpaddr12_c              | std_ulogic_vector(11 downto 0)             |  x"3bc"                                            |             |
| csr_pmpaddr13_c              | std_ulogic_vector(11 downto 0)             |  x"3bd"                                            |             |
| csr_pmpaddr14_c              | std_ulogic_vector(11 downto 0)             |  x"3be"                                            |             |
| csr_pmpaddr15_c              | std_ulogic_vector(11 downto 0)             |  x"3bf"                                            |             |
| csr_pmpaddr16_c              | std_ulogic_vector(11 downto 0)             |  x"3c0"                                            |             |
| csr_pmpaddr17_c              | std_ulogic_vector(11 downto 0)             |  x"3c1"                                            |             |
| csr_pmpaddr18_c              | std_ulogic_vector(11 downto 0)             |  x"3c2"                                            |             |
| csr_pmpaddr19_c              | std_ulogic_vector(11 downto 0)             |  x"3c3"                                            |             |
| csr_pmpaddr20_c              | std_ulogic_vector(11 downto 0)             |  x"3c4"                                            |             |
| csr_pmpaddr21_c              | std_ulogic_vector(11 downto 0)             |  x"3c5"                                            |             |
| csr_pmpaddr22_c              | std_ulogic_vector(11 downto 0)             |  x"3c6"                                            |             |
| csr_pmpaddr23_c              | std_ulogic_vector(11 downto 0)             |  x"3c7"                                            |             |
| csr_pmpaddr24_c              | std_ulogic_vector(11 downto 0)             |  x"3c8"                                            |             |
| csr_pmpaddr25_c              | std_ulogic_vector(11 downto 0)             |  x"3c9"                                            |             |
| csr_pmpaddr26_c              | std_ulogic_vector(11 downto 0)             |  x"3ca"                                            |             |
| csr_pmpaddr27_c              | std_ulogic_vector(11 downto 0)             |  x"3cb"                                            |             |
| csr_pmpaddr28_c              | std_ulogic_vector(11 downto 0)             |  x"3cc"                                            |             |
| csr_pmpaddr29_c              | std_ulogic_vector(11 downto 0)             |  x"3cd"                                            |             |
| csr_pmpaddr30_c              | std_ulogic_vector(11 downto 0)             |  x"3ce"                                            |             |
| csr_pmpaddr31_c              | std_ulogic_vector(11 downto 0)             |  x"3cf"                                            |             |
| csr_pmpaddr32_c              | std_ulogic_vector(11 downto 0)             |  x"3d0"                                            |             |
| csr_pmpaddr33_c              | std_ulogic_vector(11 downto 0)             |  x"3d1"                                            |             |
| csr_pmpaddr34_c              | std_ulogic_vector(11 downto 0)             |  x"3d2"                                            |             |
| csr_pmpaddr35_c              | std_ulogic_vector(11 downto 0)             |  x"3d3"                                            |             |
| csr_pmpaddr36_c              | std_ulogic_vector(11 downto 0)             |  x"3d4"                                            |             |
| csr_pmpaddr37_c              | std_ulogic_vector(11 downto 0)             |  x"3d5"                                            |             |
| csr_pmpaddr38_c              | std_ulogic_vector(11 downto 0)             |  x"3d6"                                            |             |
| csr_pmpaddr39_c              | std_ulogic_vector(11 downto 0)             |  x"3d7"                                            |             |
| csr_pmpaddr40_c              | std_ulogic_vector(11 downto 0)             |  x"3d8"                                            |             |
| csr_pmpaddr41_c              | std_ulogic_vector(11 downto 0)             |  x"3d9"                                            |             |
| csr_pmpaddr42_c              | std_ulogic_vector(11 downto 0)             |  x"3da"                                            |             |
| csr_pmpaddr43_c              | std_ulogic_vector(11 downto 0)             |  x"3db"                                            |             |
| csr_pmpaddr44_c              | std_ulogic_vector(11 downto 0)             |  x"3dc"                                            |             |
| csr_pmpaddr45_c              | std_ulogic_vector(11 downto 0)             |  x"3dd"                                            |             |
| csr_pmpaddr46_c              | std_ulogic_vector(11 downto 0)             |  x"3de"                                            |             |
| csr_pmpaddr47_c              | std_ulogic_vector(11 downto 0)             |  x"3df"                                            |             |
| csr_pmpaddr48_c              | std_ulogic_vector(11 downto 0)             |  x"3e0"                                            |             |
| csr_pmpaddr49_c              | std_ulogic_vector(11 downto 0)             |  x"3e1"                                            |             |
| csr_pmpaddr50_c              | std_ulogic_vector(11 downto 0)             |  x"3e2"                                            |             |
| csr_pmpaddr51_c              | std_ulogic_vector(11 downto 0)             |  x"3e3"                                            |             |
| csr_pmpaddr52_c              | std_ulogic_vector(11 downto 0)             |  x"3e4"                                            |             |
| csr_pmpaddr53_c              | std_ulogic_vector(11 downto 0)             |  x"3e5"                                            |             |
| csr_pmpaddr54_c              | std_ulogic_vector(11 downto 0)             |  x"3e6"                                            |             |
| csr_pmpaddr55_c              | std_ulogic_vector(11 downto 0)             |  x"3e7"                                            |             |
| csr_pmpaddr56_c              | std_ulogic_vector(11 downto 0)             |  x"3e8"                                            |             |
| csr_pmpaddr57_c              | std_ulogic_vector(11 downto 0)             |  x"3e9"                                            |             |
| csr_pmpaddr58_c              | std_ulogic_vector(11 downto 0)             |  x"3ea"                                            |             |
| csr_pmpaddr59_c              | std_ulogic_vector(11 downto 0)             |  x"3eb"                                            |             |
| csr_pmpaddr60_c              | std_ulogic_vector(11 downto 0)             |  x"3ec"                                            |             |
| csr_pmpaddr61_c              | std_ulogic_vector(11 downto 0)             |  x"3ed"                                            |             |
| csr_pmpaddr62_c              | std_ulogic_vector(11 downto 0)             |  x"3ee"                                            |             |
| csr_pmpaddr63_c              | std_ulogic_vector(11 downto 0)             |  x"3ef"                                            |             |
| csr_class_debug_c            | std_ulogic_vector(09 downto 0)             |  x"7b" & "00"                                      |             |
| csr_dcsr_c                   | std_ulogic_vector(11 downto 0)             |  x"7b0"                                            |             |
| csr_dpc_c                    | std_ulogic_vector(11 downto 0)             |  x"7b1"                                            |             |
| csr_dscratch0_c              | std_ulogic_vector(11 downto 0)             |  x"7b2"                                            |             |
| csr_mcycle_c                 | std_ulogic_vector(11 downto 0)             |  x"b00"                                            |             |
| csr_minstret_c               | std_ulogic_vector(11 downto 0)             |  x"b02"                                            |             |
| csr_mhpmcounter3_c           | std_ulogic_vector(11 downto 0)             |  x"b03"                                            |             |
| csr_mhpmcounter4_c           | std_ulogic_vector(11 downto 0)             |  x"b04"                                            |             |
| csr_mhpmcounter5_c           | std_ulogic_vector(11 downto 0)             |  x"b05"                                            |             |
| csr_mhpmcounter6_c           | std_ulogic_vector(11 downto 0)             |  x"b06"                                            |             |
| csr_mhpmcounter7_c           | std_ulogic_vector(11 downto 0)             |  x"b07"                                            |             |
| csr_mhpmcounter8_c           | std_ulogic_vector(11 downto 0)             |  x"b08"                                            |             |
| csr_mhpmcounter9_c           | std_ulogic_vector(11 downto 0)             |  x"b09"                                            |             |
| csr_mhpmcounter10_c          | std_ulogic_vector(11 downto 0)             |  x"b0a"                                            |             |
| csr_mhpmcounter11_c          | std_ulogic_vector(11 downto 0)             |  x"b0b"                                            |             |
| csr_mhpmcounter12_c          | std_ulogic_vector(11 downto 0)             |  x"b0c"                                            |             |
| csr_mhpmcounter13_c          | std_ulogic_vector(11 downto 0)             |  x"b0d"                                            |             |
| csr_mhpmcounter14_c          | std_ulogic_vector(11 downto 0)             |  x"b0e"                                            |             |
| csr_mhpmcounter15_c          | std_ulogic_vector(11 downto 0)             |  x"b0f"                                            |             |
| csr_mhpmcounter16_c          | std_ulogic_vector(11 downto 0)             |  x"b10"                                            |             |
| csr_mhpmcounter17_c          | std_ulogic_vector(11 downto 0)             |  x"b11"                                            |             |
| csr_mhpmcounter18_c          | std_ulogic_vector(11 downto 0)             |  x"b12"                                            |             |
| csr_mhpmcounter19_c          | std_ulogic_vector(11 downto 0)             |  x"b13"                                            |             |
| csr_mhpmcounter20_c          | std_ulogic_vector(11 downto 0)             |  x"b14"                                            |             |
| csr_mhpmcounter21_c          | std_ulogic_vector(11 downto 0)             |  x"b15"                                            |             |
| csr_mhpmcounter22_c          | std_ulogic_vector(11 downto 0)             |  x"b16"                                            |             |
| csr_mhpmcounter23_c          | std_ulogic_vector(11 downto 0)             |  x"b17"                                            |             |
| csr_mhpmcounter24_c          | std_ulogic_vector(11 downto 0)             |  x"b18"                                            |             |
| csr_mhpmcounter25_c          | std_ulogic_vector(11 downto 0)             |  x"b19"                                            |             |
| csr_mhpmcounter26_c          | std_ulogic_vector(11 downto 0)             |  x"b1a"                                            |             |
| csr_mhpmcounter27_c          | std_ulogic_vector(11 downto 0)             |  x"b1b"                                            |             |
| csr_mhpmcounter28_c          | std_ulogic_vector(11 downto 0)             |  x"b1c"                                            |             |
| csr_mhpmcounter29_c          | std_ulogic_vector(11 downto 0)             |  x"b1d"                                            |             |
| csr_mhpmcounter30_c          | std_ulogic_vector(11 downto 0)             |  x"b1e"                                            |             |
| csr_mhpmcounter31_c          | std_ulogic_vector(11 downto 0)             |  x"b1f"                                            |             |
| csr_mcycleh_c                | std_ulogic_vector(11 downto 0)             |  x"b80"                                            |             |
| csr_minstreth_c              | std_ulogic_vector(11 downto 0)             |  x"b82"                                            |             |
| csr_mhpmcounter3h_c          | std_ulogic_vector(11 downto 0)             |  x"b83"                                            |             |
| csr_mhpmcounter4h_c          | std_ulogic_vector(11 downto 0)             |  x"b84"                                            |             |
| csr_mhpmcounter5h_c          | std_ulogic_vector(11 downto 0)             |  x"b85"                                            |             |
| csr_mhpmcounter6h_c          | std_ulogic_vector(11 downto 0)             |  x"b86"                                            |             |
| csr_mhpmcounter7h_c          | std_ulogic_vector(11 downto 0)             |  x"b87"                                            |             |
| csr_mhpmcounter8h_c          | std_ulogic_vector(11 downto 0)             |  x"b88"                                            |             |
| csr_mhpmcounter9h_c          | std_ulogic_vector(11 downto 0)             |  x"b89"                                            |             |
| csr_mhpmcounter10h_c         | std_ulogic_vector(11 downto 0)             |  x"b8a"                                            |             |
| csr_mhpmcounter11h_c         | std_ulogic_vector(11 downto 0)             |  x"b8b"                                            |             |
| csr_mhpmcounter12h_c         | std_ulogic_vector(11 downto 0)             |  x"b8c"                                            |             |
| csr_mhpmcounter13h_c         | std_ulogic_vector(11 downto 0)             |  x"b8d"                                            |             |
| csr_mhpmcounter14h_c         | std_ulogic_vector(11 downto 0)             |  x"b8e"                                            |             |
| csr_mhpmcounter15h_c         | std_ulogic_vector(11 downto 0)             |  x"b8f"                                            |             |
| csr_mhpmcounter16h_c         | std_ulogic_vector(11 downto 0)             |  x"b90"                                            |             |
| csr_mhpmcounter17h_c         | std_ulogic_vector(11 downto 0)             |  x"b91"                                            |             |
| csr_mhpmcounter18h_c         | std_ulogic_vector(11 downto 0)             |  x"b92"                                            |             |
| csr_mhpmcounter19h_c         | std_ulogic_vector(11 downto 0)             |  x"b93"                                            |             |
| csr_mhpmcounter20h_c         | std_ulogic_vector(11 downto 0)             |  x"b94"                                            |             |
| csr_mhpmcounter21h_c         | std_ulogic_vector(11 downto 0)             |  x"b95"                                            |             |
| csr_mhpmcounter22h_c         | std_ulogic_vector(11 downto 0)             |  x"b96"                                            |             |
| csr_mhpmcounter23h_c         | std_ulogic_vector(11 downto 0)             |  x"b97"                                            |             |
| csr_mhpmcounter24h_c         | std_ulogic_vector(11 downto 0)             |  x"b98"                                            |             |
| csr_mhpmcounter25h_c         | std_ulogic_vector(11 downto 0)             |  x"b99"                                            |             |
| csr_mhpmcounter26h_c         | std_ulogic_vector(11 downto 0)             |  x"b9a"                                            |             |
| csr_mhpmcounter27h_c         | std_ulogic_vector(11 downto 0)             |  x"b9b"                                            |             |
| csr_mhpmcounter28h_c         | std_ulogic_vector(11 downto 0)             |  x"b9c"                                            |             |
| csr_mhpmcounter29h_c         | std_ulogic_vector(11 downto 0)             |  x"b9d"                                            |             |
| csr_mhpmcounter30h_c         | std_ulogic_vector(11 downto 0)             |  x"b9e"                                            |             |
| csr_mhpmcounter31h_c         | std_ulogic_vector(11 downto 0)             |  x"b9f"                                            |             |
| csr_cycle_c                  | std_ulogic_vector(11 downto 0)             |  x"c00"                                            |             |
| csr_time_c                   | std_ulogic_vector(11 downto 0)             |  x"c01"                                            |             |
| csr_instret_c                | std_ulogic_vector(11 downto 0)             |  x"c02"                                            |             |
| csr_cycleh_c                 | std_ulogic_vector(11 downto 0)             |  x"c80"                                            |             |
| csr_timeh_c                  | std_ulogic_vector(11 downto 0)             |  x"c81"                                            |             |
| csr_instreth_c               | std_ulogic_vector(11 downto 0)             |  x"c82"                                            |             |
| csr_mvendorid_c              | std_ulogic_vector(11 downto 0)             |  x"f11"                                            |             |
| csr_marchid_c                | std_ulogic_vector(11 downto 0)             |  x"f12"                                            |             |
| csr_mimpid_c                 | std_ulogic_vector(11 downto 0)             |  x"f13"                                            |             |
| csr_mhartid_c                | std_ulogic_vector(11 downto 0)             |  x"f14"                                            |             |
| csr_mzext_c                  | std_ulogic_vector(11 downto 0)             |  x"fc0"                                            |             |
| cp_sel_shifter_c             | std_ulogic_vector(1 downto 0)              |  "00"                                              |             |
| cp_sel_muldiv_c              | std_ulogic_vector(1 downto 0)              |  "01"                                              |             |
| cp_sel_fpu_c                 | std_ulogic_vector(1 downto 0)              |  "11"                                              |             |
| alu_arith_cmd_addsub_c       | std_ulogic                                 |  '0'                                               |             |
| alu_arith_cmd_slt_c          | std_ulogic                                 |  '1'                                               |             |
| alu_logic_cmd_movb_c         | std_ulogic_vector(1 downto 0)              |  "00"                                              |             |
| alu_logic_cmd_xor_c          | std_ulogic_vector(1 downto 0)              |  "01"                                              |             |
| alu_logic_cmd_or_c           | std_ulogic_vector(1 downto 0)              |  "10"                                              |             |
| alu_logic_cmd_and_c          | std_ulogic_vector(1 downto 0)              |  "11"                                              |             |
| alu_func_cmd_arith_c         | std_ulogic_vector(1 downto 0)              |  "00"                                              |             |
| alu_func_cmd_logic_c         | std_ulogic_vector(1 downto 0)              |  "01"                                              |             |
| alu_func_cmd_csrr_c          | std_ulogic_vector(1 downto 0)              |  "10"                                              |             |
| alu_func_cmd_copro_c         | std_ulogic_vector(1 downto 0)              |  "11"                                              |             |
| trap_ima_c                   | std_ulogic_vector(6 downto 0)              |  "0" & "0" & "00000"                               |             |
| trap_iba_c                   | std_ulogic_vector(6 downto 0)              |  "0" & "0" & "00001"                               |             |
| trap_iil_c                   | std_ulogic_vector(6 downto 0)              |  "0" & "0" & "00010"                               |             |
| trap_brk_c                   | std_ulogic_vector(6 downto 0)              |  "0" & "0" & "00011"                               |             |
| trap_lma_c                   | std_ulogic_vector(6 downto 0)              |  "0" & "0" & "00100"                               |             |
| trap_lbe_c                   | std_ulogic_vector(6 downto 0)              |  "0" & "0" & "00101"                               |             |
| trap_sma_c                   | std_ulogic_vector(6 downto 0)              |  "0" & "0" & "00110"                               |             |
| trap_sbe_c                   | std_ulogic_vector(6 downto 0)              |  "0" & "0" & "00111"                               |             |
| trap_uenv_c                  | std_ulogic_vector(6 downto 0)              |  "0" & "0" & "01000"                               |             |
| trap_menv_c                  | std_ulogic_vector(6 downto 0)              |  "0" & "0" & "01011"                               |             |
| trap_nmi_c                   | std_ulogic_vector(6 downto 0)              |  "1" & "0" & "00000"                               |             |
| trap_msi_c                   | std_ulogic_vector(6 downto 0)              |  "1" & "0" & "00011"                               |             |
| trap_mti_c                   | std_ulogic_vector(6 downto 0)              |  "1" & "0" & "00111"                               |             |
| trap_mei_c                   | std_ulogic_vector(6 downto 0)              |  "1" & "0" & "01011"                               |             |
| trap_firq0_c                 | std_ulogic_vector(6 downto 0)              |  "1" & "0" & "10000"                               |             |
| trap_firq1_c                 | std_ulogic_vector(6 downto 0)              |  "1" & "0" & "10001"                               |             |
| trap_firq2_c                 | std_ulogic_vector(6 downto 0)              |  "1" & "0" & "10010"                               |             |
| trap_firq3_c                 | std_ulogic_vector(6 downto 0)              |  "1" & "0" & "10011"                               |             |
| trap_firq4_c                 | std_ulogic_vector(6 downto 0)              |  "1" & "0" & "10100"                               |             |
| trap_firq5_c                 | std_ulogic_vector(6 downto 0)              |  "1" & "0" & "10101"                               |             |
| trap_firq6_c                 | std_ulogic_vector(6 downto 0)              |  "1" & "0" & "10110"                               |             |
| trap_firq7_c                 | std_ulogic_vector(6 downto 0)              |  "1" & "0" & "10111"                               |             |
| trap_firq8_c                 | std_ulogic_vector(6 downto 0)              |  "1" & "0" & "11000"                               |             |
| trap_firq9_c                 | std_ulogic_vector(6 downto 0)              |  "1" & "0" & "11001"                               |             |
| trap_firq10_c                | std_ulogic_vector(6 downto 0)              |  "1" & "0" & "11010"                               |             |
| trap_firq11_c                | std_ulogic_vector(6 downto 0)              |  "1" & "0" & "11011"                               |             |
| trap_firq12_c                | std_ulogic_vector(6 downto 0)              |  "1" & "0" & "11100"                               |             |
| trap_firq13_c                | std_ulogic_vector(6 downto 0)              |  "1" & "0" & "11101"                               |             |
| trap_firq14_c                | std_ulogic_vector(6 downto 0)              |  "1" & "0" & "11110"                               |             |
| trap_firq15_c                | std_ulogic_vector(6 downto 0)              |  "1" & "0" & "11111"                               |             |
| trap_db_break_c              | std_ulogic_vector(6 downto 0)              |  "0" & "1" & "00010"                               |             |
| trap_db_halt_c               | std_ulogic_vector(6 downto 0)              |  "1" & "1" & "00011"                               |             |
| trap_db_step_c               | std_ulogic_vector(6 downto 0)              |  "1" & "1" & "00100"                               |             |
| exception_iaccess_c          | natural                                    |   0                                                |             |
| exception_iillegal_c         | natural                                    |   1                                                |             |
| exception_ialign_c           | natural                                    |   2                                                |             |
| exception_m_envcall_c        | natural                                    |   3                                                |             |
| exception_u_envcall_c        | natural                                    |   4                                                |             |
| exception_break_c            | natural                                    |   5                                                |             |
| exception_salign_c           | natural                                    |   6                                                |             |
| exception_lalign_c           | natural                                    |   7                                                |             |
| exception_saccess_c          | natural                                    |   8                                                |             |
| exception_laccess_c          | natural                                    |   9                                                |             |
| exception_db_break_c         | natural                                    |  10                                                |             |
| exception_width_c            | natural                                    |  11                                                |             |
| interrupt_nm_irq_c           | natural                                    |   0                                                |             |
| interrupt_msw_irq_c          | natural                                    |   1                                                |             |
| interrupt_mtime_irq_c        | natural                                    |   2                                                |             |
| interrupt_mext_irq_c         | natural                                    |   3                                                |             |
| interrupt_firq_0_c           | natural                                    |   4                                                |             |
| interrupt_firq_1_c           | natural                                    |   5                                                |             |
| interrupt_firq_2_c           | natural                                    |   6                                                |             |
| interrupt_firq_3_c           | natural                                    |   7                                                |             |
| interrupt_firq_4_c           | natural                                    |   8                                                |             |
| interrupt_firq_5_c           | natural                                    |   9                                                |             |
| interrupt_firq_6_c           | natural                                    |  10                                                |             |
| interrupt_firq_7_c           | natural                                    |  11                                                |             |
| interrupt_firq_8_c           | natural                                    |  12                                                |             |
| interrupt_firq_9_c           | natural                                    |  13                                                |             |
| interrupt_firq_10_c          | natural                                    |  14                                                |             |
| interrupt_firq_11_c          | natural                                    |  15                                                |             |
| interrupt_firq_12_c          | natural                                    |  16                                                |             |
| interrupt_firq_13_c          | natural                                    |  17                                                |             |
| interrupt_firq_14_c          | natural                                    |  18                                                |             |
| interrupt_firq_15_c          | natural                                    |  19                                                |             |
| interrupt_db_halt_c          | natural                                    |  20                                                |             |
| interrupt_db_step_c          | natural                                    |  21                                                |             |
| interrupt_width_c            | natural                                    |  22                                                |             |
| priv_mode_m_c                | std_ulogic_vector(1 downto 0)              |  "11"                                              |             |
| priv_mode_u_c                | std_ulogic_vector(1 downto 0)              |  "00"                                              |             |
| hpmcnt_event_cy_c            | natural                                    |  0                                                 |             |
| hpmcnt_event_never_c         | natural                                    |  1                                                 |             |
| hpmcnt_event_ir_c            | natural                                    |  2                                                 |             |
| hpmcnt_event_cir_c           | natural                                    |  3                                                 |             |
| hpmcnt_event_wait_if_c       | natural                                    |  4                                                 |             |
| hpmcnt_event_wait_ii_c       | natural                                    |  5                                                 |             |
| hpmcnt_event_wait_mc_c       | natural                                    |  6                                                 |             |
| hpmcnt_event_load_c          | natural                                    |  7                                                 |             |
| hpmcnt_event_store_c         | natural                                    |  8                                                 |             |
| hpmcnt_event_wait_ls_c       | natural                                    |  9                                                 |             |
| hpmcnt_event_jump_c          | natural                                    |  10                                                |             |
| hpmcnt_event_branch_c        | natural                                    |  11                                                |             |
| hpmcnt_event_tbranch_c       | natural                                    |  12                                                |             |
| hpmcnt_event_trap_c          | natural                                    |  13                                                |             |
| hpmcnt_event_illegal_c       | natural                                    |  14                                                |             |
| hpmcnt_event_size_c          | natural                                    |  15                                                |             |
| clk_div2_c                   | natural                                    |  0                                                 |             |
| clk_div4_c                   | natural                                    |  1                                                 |             |
| clk_div8_c                   | natural                                    |  2                                                 |             |
| clk_div64_c                  | natural                                    |  3                                                 |             |
| clk_div128_c                 | natural                                    |  4                                                 |             |
| clk_div1024_c                | natural                                    |  5                                                 |             |
| clk_div2048_c                | natural                                    |  6                                                 |             |
| clk_div4096_c                | natural                                    |  7                                                 |             |
## Types
| Name          | Type | Description |
| ------------- | ---- | ----------- |
| pmp_ctrl_if_t |      |             |
| pmp_addr_if_t |      |             |
| cp_data_if_t  |      |             |
| mem32_t       |      |             |
| mem8_t        |      |             |
## Functions
- index_size_f <font id="function_arguments">(input : natural)</font> <font id="function_return">return natural</font>
- cond_sel_natural_f <font id="function_arguments">(cond : boolean; val_t : natural; val_f : natural)</font> <font id="function_return">return natural</font>
- cond_sel_int_f <font id="function_arguments">(cond : boolean; val_t : integer; val_f : integer)</font> <font id="function_return">return integer</font>
- cond_sel_stdulogicvector_f <font id="function_arguments">(cond : boolean; val_t : std_ulogic_vector; val_f : std_ulogic_vector)</font> <font id="function_return">return std_ulogic_vector</font>
- cond_sel_stdulogic_f <font id="function_arguments">(cond : boolean; val_t : std_ulogic; val_f : std_ulogic)</font> <font id="function_return">return std_ulogic</font>
- cond_sel_string_f <font id="function_arguments">(cond : boolean; val_t : string; val_f : string)</font> <font id="function_return">return string</font>
- bool_to_ulogic_f <font id="function_arguments">(cond : boolean)</font> <font id="function_return">return std_ulogic</font>
- or_reduce_f <font id="function_arguments">(a : std_ulogic_vector)</font> <font id="function_return">return std_ulogic</font>
- and_reduce_f <font id="function_arguments">(a : std_ulogic_vector)</font> <font id="function_return">return std_ulogic</font>
- xor_reduce_f <font id="function_arguments">(a : std_ulogic_vector)</font> <font id="function_return">return std_ulogic</font>
- to_hexchar_f <font id="function_arguments">(input : std_ulogic_vector(3 downto 0))</font> <font id="function_return">return character</font>
- hexchar_to_stdulogicvector_f <font id="function_arguments">(input : character)</font> <font id="function_return">return std_ulogic_vector</font>
- bit_rev_f <font id="function_arguments">(input : std_ulogic_vector)</font> <font id="function_return">return std_ulogic_vector</font>
- is_power_of_two_f <font id="function_arguments">(input : natural)</font> <font id="function_return">return boolean</font>
- bswap32_f <font id="function_arguments">(input : std_ulogic_vector)</font> <font id="function_return">return std_ulogic_vector</font>
- char_tolower_f <font id="function_arguments">(ch : character)</font> <font id="function_return">return character</font>
- str_equal_f <font id="function_arguments">(str0 : string; str1 : string)</font> <font id="function_return">return boolean</font>
