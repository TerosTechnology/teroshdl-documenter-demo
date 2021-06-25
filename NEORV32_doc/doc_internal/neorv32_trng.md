# Entity: neorv32_trng
## Diagram
![Diagram](neorv32_trng.svg "Diagram")
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
## Signals
| Name             | Type                                      | Description |
| ---------------- | ----------------------------------------- | ----------- |
| acc_en           | std_ulogic                                |             |
| wren             | std_ulogic                                |             |
| rden             | std_ulogic                                |             |
| osc_array_en_in  | std_ulogic_vector(num_roscs_c-1 downto 0) |             |
| osc_array_en_out | std_ulogic_vector(num_roscs_c-1 downto 0) |             |
| osc_array_data   | std_ulogic_vector(num_roscs_c-1 downto 0) |             |
| debiasing        | debiasing_t                               |             |
| processing       | processing_t                              |             |
## Constants
| Name            | Type                          | Value                      | Description |
| --------------- | ----------------------------- | -------------------------- | ----------- |
| num_roscs_c     | natural                       |  4                         |             |
| num_inv_start_c | natural                       |  5                         |             |
| num_inv_inc_c   | natural                       |  2                         |             |
| lfsr_en_c       | boolean                       |  true                      |             |
| lfsr_taps_c     | std_ulogic_vector(7 downto 0) |  "10111000"                |             |
| ctrl_data_lsb_c | natural                       |   0                        |             |
| ctrl_data_msb_c | natural                       |   7                        |             |
| ctrl_en_c       | natural                       |  30                        |             |
| ctrl_valid_c    | natural                       |  31                        |             |
| hi_abb_c        | natural                       |  index_size_f(io_size_c)-1 |             |
| lo_abb_c        | natural                       |  index_size_f(trng_size_c) |             |
## Types
| Name         | Type | Description |
| ------------ | ---- | ----------- |
| debiasing_t  |      |             |
| processing_t |      |             |
## Processes
- rw_access: _( clk_i )_

- array_intercon: _( processing.enable, osc_array_en_out )_

- neumann_debiasing_sync: _( clk_i )_

- neumann_debiasing_comb: _( debiasing )_

- processing_core: _( clk_i )_

