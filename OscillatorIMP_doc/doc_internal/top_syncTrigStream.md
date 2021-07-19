# Entity: top_genpulsetwowaycplx

- **File**: top_syncTrigStream.vhd
## Diagram

![Diagram](top_syncTrigStream.svg "Diagram")
## Ports

| Port name    | Direction | Type                          | Description |
| ------------ | --------- | ----------------------------- | ----------- |
| clk_i        | in        | std_logic                     |             |
| rst_i        | in        | std_logic                     |             |
| pulse_o      | out       | std_logic                     | pulse       |
| duty_cnt_i   | in        | std_logic_vector(31 downto 0) | config      |
| period_cnt_i | in        | std_logic_vector(31 downto 0) |             |
| data_en_i    | in        | std_logic                     | in          |
| data1_i_i    | in        | std_logic_vector(15 downto 0) |             |
| data1_q_i    | in        | std_logic_vector(15 downto 0) |             |
| data2_i_i    | in        | std_logic_vector(15 downto 0) |             |
| data2_q_i    | in        | std_logic_vector(15 downto 0) |             |
| data_en_o    | out       | std_logic                     |             |
| data1_i_o    | out       | std_logic_vector(15 downto 0) |             |
| data1_q_o    | out       | std_logic_vector(15 downto 0) |             |
| data2_i_o    | out       | std_logic_vector(15 downto 0) |             |
| data2_q_o    | out       | std_logic_vector(15 downto 0) |             |
| data_sof_o   | out       | std_logic                     |             |
| data_eof_o   | out       | std_logic                     |             |
## Instantiations

- lt_sz_inst: work.syncTrigStream_logic
