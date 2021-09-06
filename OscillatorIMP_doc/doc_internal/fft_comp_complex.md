# Entity: fft_comp_complex

- **File**: fft_comp_complex.vhd
## Diagram

![Diagram](fft_comp_complex.svg "Diagram")
## Generics

| Generic name   | Type    | Value | Description |
| -------------- | ------- | ----- | ----------- |
| USE_FIRST_BUFF | boolean | true  |             |
| USE_SEC_BUFF   | boolean | true  |             |
| DEBUG          | boolean | false |             |
| SHIFT_VAL      | natural | 16    |             |
| COEFF_SIZE     | natural | 16    |             |
| ADDR_SIZE      | natural | 10    |             |
| DATA_SIZE      | natural | 16    |             |
## Ports

| Port name     | Direction | Type                                    | Description            |
| ------------- | --------- | --------------------------------------- | ---------------------- |
| clk_i         | in        | std_logic                               | Syscon signals         |
| rst_i         | in        | std_logic                               |                        |
| t_stage_i     | in        | std_logic_vector(ADDR_SIZE-1 downto 0)  | test                   |
| t_nb_index_i  | in        | std_logic_vector(ADDR_SIZE-1 downto 0)  |                        |
| t_sb_index_i  | in        | std_logic_vector(ADDR_SIZE-1 downto 0)  |                        |
| data_en_i     | in        | std_logic                               | input data             |
| data_a_re_i   | in        | std_logic_vector(DATA_SIZE-1 downto 0)  |                        |
| data_a_im_i   | in        | std_logic_vector(DATA_SIZE-1 downto 0)  |                        |
| a_addr_i      | in        | std_logic_vector(ADDR_SIZE-1 downto 0)  |                        |
| data_b_re_i   | in        | std_logic_vector(DATA_SIZE-1 downto 0)  |                        |
| data_b_im_i   | in        | std_logic_vector(DATA_SIZE-1 downto 0)  |                        |
| b_addr_i      | in        | std_logic_vector(ADDR_SIZE-1 downto 0)  |                        |
| coeff_re_i    | in        | std_logic_vector(COEFF_SIZE-1 downto 0) |                        |
| coeff_im_i    | in        | std_logic_vector(COEFF_SIZE-1 downto 0) |                        |
| data_addr_a_o | out       | std_logic_vector(ADDR_SIZE-1 downto 0)  | for the next component |
| data_addr_b_o | out       | std_logic_vector(ADDR_SIZE-1 downto 0)  |                        |
| data_a_re_o   | out       | std_logic_vector(DATA_SIZE-1 downto 0)  |                        |
| data_a_im_o   | out       | std_logic_vector(DATA_SIZE-1 downto 0)  |                        |
| data_b_re_o   | out       | std_logic_vector(DATA_SIZE-1 downto 0)  |                        |
| data_b_im_o   | out       | std_logic_vector(DATA_SIZE-1 downto 0)  |                        |
| comp_done_o   | out       | std_logic                               |                        |
## Signals

| Name               | Type                                             | Description     |
| ------------------ | ------------------------------------------------ | --------------- |
| res_mult_re_cos    | std_logic_vector(MULT_SIZE-1 downto 0)           |  internal       |
| res_mult_re_sin    | std_logic_vector(MULT_SIZE-1 downto 0)           |                 |
| res_mult_im_cos    | std_logic_vector(MULT_SIZE-1 downto 0)           |                 |
| res_mult_im_sin    | std_logic_vector(MULT_SIZE-1 downto 0)           |                 |
| tmp_real_s         | std_logic_vector(DATA_SIZE-1 downto 0)           |                 |
|  tmp_im_s          | std_logic_vector(DATA_SIZE-1 downto 0)           |                 |
| tmp_re_s           | std_logic_vector(DATA_SIZE-1 downto 0)           |                 |
|  tmp_imag_s        | std_logic_vector(DATA_SIZE-1 downto 0)           |                 |
| res_mult_re_cos_s  | std_logic_vector((UPPER_SIZE)-1 downto 0)        |                 |
| res_mult_re_sin_s  | std_logic_vector((UPPER_SIZE)-1 downto 0)        |                 |
| res_mult_im_cos_s  | std_logic_vector((UPPER_SIZE)-1 downto 0)        |                 |
| res_mult_im_sin_s  | std_logic_vector((UPPER_SIZE)-1 downto 0)        |                 |
| res2_mult_re_cos_s | std_logic_vector((UPPER_SIZE)-1 downto 0)        |                 |
| res2_mult_re_sin_s | std_logic_vector((UPPER_SIZE)-1 downto 0)        |                 |
| res2_mult_im_cos_s | std_logic_vector((UPPER_SIZE)-1 downto 0)        |                 |
| res2_mult_im_sin_s | std_logic_vector((UPPER_SIZE)-1 downto 0)        |                 |
| tmp_a_re_s         | std_logic_vector(DATA_SIZE-1 downto 0)           |                 |
|  tmp_a_im_s        | std_logic_vector(DATA_SIZE-1 downto 0)           |                 |
| tmp_b_re_s         | std_logic_vector(DATA_SIZE-1 downto 0)           |                 |
|  tmp_b_im_s        | std_logic_vector(DATA_SIZE-1 downto 0)           |                 |
| data_re_a_s        | std_logic_vector(DATA_SIZE-1 downto 0)           |  output result  |
| data_im_a_s        | std_logic_vector(DATA_SIZE-1 downto 0)           |                 |
| data_re_b_s        | std_logic_vector(DATA_SIZE-1 downto 0)           |                 |
| data_im_b_s        | std_logic_vector(DATA_SIZE-1 downto 0)           |                 |
| data_addr_a_s      | std_logic_vector(ADDR_SIZE-1 downto 0)           |                 |
| data_addr_b_s      | std_logic_vector(ADDR_SIZE-1 downto 0)           |                 |
| coeff_re_in_s      | std_logic_vector(COEFF_SIZE-1 downto 0)          |  new            |
| coeff_im_in_s      | std_logic_vector(COEFF_SIZE-1 downto 0)          |                 |
| data_a_re_in_s     | std_logic_vector(DATA_SIZE-1 downto 0)           |                 |
| data_a_im_in_s     | std_logic_vector(DATA_SIZE-1 downto 0)           |                 |
| data_b_re_in_s     | std_logic_vector(DATA_SIZE-1 downto 0)           |                 |
| data_b_im_in_s     | std_logic_vector(DATA_SIZE-1 downto 0)           |                 |
| data_en_s          | std_logic                                        |                 |
|  data2_en_s        | std_logic                                        |                 |
| truc               | std_logic_vector(MULT_SIZE-SHIFT_VAL-1 downto 0) |                 |
## Constants

| Name       | Type    | Value                      | Description |
| ---------- | ------- | -------------------------- | ----------- |
| MULT_SIZE  | natural |  DATA_SIZE+COEFF_SIZE      |             |
| TRICK      | natural |  2                         |             |
| UPPER_SIZE | natural |  MULT_SIZE-SHIFT_VAL-TRICK |             |
## Processes
- unnamed: ( clk_i )
