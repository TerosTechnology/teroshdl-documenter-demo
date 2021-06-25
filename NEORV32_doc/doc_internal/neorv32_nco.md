# Entity: neorv32_nco
## Diagram
![Diagram](neorv32_nco.svg "Diagram")
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
| nco_o       | out       | std_ulogic_vector(02 downto 0) |             |
## Signals
| Name        | Type                                      | Description |
| ----------- | ----------------------------------------- | ----------- |
| acc_en      | std_ulogic                                |             |
| addr        | std_ulogic_vector(31 downto 0)            |             |
| wren        | std_ulogic                                |             |
| rden        | std_ulogic                                |             |
| tuning_word | tuning_word_t                             |             |
| ctrl        | std_ulogic_vector(ctrl_size_c-1 downto 0) |             |
| nco         | nco_core_t                                |             |
## Constants
| Name                | Type    | Value                              | Description |
| ------------------- | ------- | ---------------------------------- | ----------- |
| phase_accu_width_c  | natural |  20                                |             |
| num_channels_c      | natural |   3                                |             |
| hi_abb_c            | natural |  index_size_f(io_size_c)-1         |             |
| lo_abb_c            | natural |  index_size_f(nco_size_c)          |             |
| ctrl_en_c           | natural |   0                                |             |
| ctrl_ch0_mode_c     | natural |   1                                |             |
| ctrl_ch0_idle_pol_c | natural |   2                                |             |
| ctrl_ch0_oe_c       | natural |   3                                |             |
| ctrl_ch0_output_c   | natural |   4                                |             |
| ctrl_ch0_prsc0_c    | natural |   5                                |             |
| ctrl_ch0_prsc1_c    | natural |   6                                |             |
| ctrl_ch0_prsc2_c    | natural |   7                                |             |
| ctrl_ch0_pulse0_c   | natural |   8                                |             |
| ctrl_ch0_pulse1_c   | natural |   9                                |             |
| ctrl_ch0_pulse2_c   | natural |  10                                |             |
| ctrl_ch1_mode_c     | natural |  21                                |             |
| ctrl_ch1_idle_pol_c | natural |  22                                |             |
| ctrl_ch1_oe_c       | natural |  23                                |             |
| ctrl_ch1_output_c   | natural |  24                                |             |
| ctrl_ch1_prsc0_c    | natural |  25                                |             |
| ctrl_ch1_prsc1_c    | natural |  26                                |             |
| ctrl_ch1_prsc2_c    | natural |  27                                |             |
| ctrl_ch1_pulse0_c   | natural |  28                                |             |
| ctrl_ch1_pulse1_c   | natural |  29                                |             |
| ctrl_ch1_pulse2_c   | natural |  20                                |             |
| ctrl_ch2_mode_c     | natural |  21                                |             |
| ctrl_ch2_idle_pol_c | natural |  22                                |             |
| ctrl_ch2_oe_c       | natural |  23                                |             |
| ctrl_ch2_output_c   | natural |  24                                |             |
| ctrl_ch2_prsc0_c    | natural |  25                                |             |
| ctrl_ch2_prsc1_c    | natural |  26                                |             |
| ctrl_ch2_prsc2_c    | natural |  27                                |             |
| ctrl_ch2_pulse0_c   | natural |  28                                |             |
| ctrl_ch2_pulse1_c   | natural |  29                                |             |
| ctrl_ch2_pulse2_c   | natural |  30                                |             |
| ctrl_ch_offset_c    | natural |  10                                |             |
| ctrl_size_c         | natural |  num_channels_c*ctrl_ch_offset_c+1 |             |
## Types
| Name          | Type | Description |
| ------------- | ---- | ----------- |
| tuning_word_t |      |             |
| nco_sel_t     |      |             |
| pulse_cnt_t   |      |             |
| accu_t        |      |             |
| nco_core_t    |      |             |
## Processes
- rw_access: _( clk_i )_

- nco_core: _( clk_i )_

- pulse_generator: _( clk_i )_

- output_generator: _( clk_i )_

