# Entity: top_shiftercomplex

- **File**: top_mixerComplex_sin.vhd
## Diagram

![Diagram](top_mixerComplex_sin.svg "Diagram")
## Ports

| Port name    | Direction | Type                          | Description |
| ------------ | --------- | ----------------------------- | ----------- |
| clk_i        | in        | std_logic                     |             |
| rst_i        | in        | std_logic                     |             |
| nco_en_i     | in        | std_logic                     | in          |
| nco_i_i      | in        | std_logic_vector(15 downto 0) |             |
| nco_q_i      | in        | std_logic_vector(15 downto 0) |             |
| data_en_i    | in        | std_logic                     |             |
| data_i_i     | in        | std_logic_vector(15 downto 0) |             |
| data_q_i     | in        | std_logic_vector(15 downto 0) |             |
| data_lt_i_o  | out       | std_logic_vector(15 downto 0) | out         |
| data_lt_q_o  | out       | std_logic_vector(15 downto 0) |             |
| data_lt_en_o | out       | std_logic                     |             |
| data_eq_i_o  | out       | std_logic_vector(31 downto 0) |             |
| data_eq_q_o  | out       | std_logic_vector(31 downto 0) |             |
| data_eq_en_o | out       | std_logic                     |             |
| data_gt_i_o  | out       | std_logic_vector(32 downto 0) |             |
| data_gt_q_o  | out       | std_logic_vector(32 downto 0) |             |
| data_gt_en_o | out       | std_logic                     |             |
## Instantiations

- lt_sz_inst: work.mixerComplex_sin
- eq_sz_inst: work.mixerComplex_sin
</br>**Description**
 16x16 -1 => 31 => 16

- gt_sz_inst: work.mixerComplex_sin
</br>**Description**
 16x16 -1 => 31 => 16

