# Entity: top_multiplierreal

- **File**: top_multiplierReal.vhd
## Diagram

![Diagram](top_multiplierReal.svg "Diagram")
## Ports

| Port name    | Direction | Type                          | Description |
| ------------ | --------- | ----------------------------- | ----------- |
| clk_i        | in        | std_logic                     |             |
| rst_i        | in        | std_logic                     |             |
| data1_en_i   | in        | std_logic                     | in          |
| data1_eof_i  | in        | std_logic                     |             |
| data1_sof_i  | in        | std_logic                     |             |
| data1_i      | in        | std_logic_vector(15 downto 0) |             |
| data2_en_i   | in        | std_logic                     |             |
| data2_eof_i  | in        | std_logic                     |             |
| data2_sof_i  | in        | std_logic                     |             |
| data2_i      | in        | std_logic_vector(15 downto 0) |             |
| data2_q_i    | in        | std_logic_vector(15 downto 0) |             |
| data_lt_o    | out       | std_logic_vector(15 downto 0) | out         |
| data_lt_en_o | out       | std_logic                     |             |
| data_eq_o    | out       | std_logic_vector(31 downto 0) |             |
| data_eq_en_o | out       | std_logic                     |             |
| data_gt_o    | out       | std_logic_vector(32 downto 0) |             |
| data_gt_en_o | out       | std_logic                     |             |
## Instantiations

- lt_sz_inst: work.multiplierReal
- eq_sz_inst: work.multiplierReal
**Description**
 16x16 -1 => 31 => 16

- gt_sz_inst: work.multiplierReal
**Description**
 16x16 -1 => 31 => 16

