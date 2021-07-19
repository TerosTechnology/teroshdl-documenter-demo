# Entity: fft_loop_stage

- **File**: fft_loop_stage.vhd
## Diagram

![Diagram](fft_loop_stage.svg "Diagram")
## Generics

| Generic name   | Type    | Value | Description |
| -------------- | ------- | ----- | ----------- |
| USE_FIRST_BUFF | boolean | true  |             |
| USE_SEC_BUFF   | boolean | true  |             |
| DEBUG          | boolean | false |             |
| LOG_2_N_FFT    | natural | 8     |             |
| SHIFT_VAL      | natural | 16    |             |
| COEFF_SIZE     | natural | 16    |             |
| N_FFT          | natural | 2048  |             |
| ADDR_SIZE      | natural | 10    |             |
| DATA_SIZE      | natural | 16    |             |
## Ports

| Port name       | Direction | Type                                    | Description    |
| --------------- | --------- | --------------------------------------- | -------------- |
| clk_i           | in        | std_logic                               | Syscon signals |
| cpu_clk_i       | in        | std_logic                               |                |
| rst_i           | in        | std_logic                               |                |
| start_fft_i     | in        | std_logic                               | control        |
| done_fft_o      | out       | std_logic                               |                |
| data_re_i       | in        | std_logic_vector(DATA_SIZE-1 downto 0)  | input data     |
| data_im_i       | in        | std_logic_vector(DATA_SIZE-1 downto 0)  |                |
| data_addr_i     | in        | std_logic_vector(ADDR_SIZE-1 downto 0)  |                |
| data_en_i       | in        | std_logic                               |                |
| read_coeff_re_o | out       | std_logic_vector(COEFF_SIZE-1 downto 0) |                |
| read_coeff_im_o | out       | std_logic_vector(COEFF_SIZE-1 downto 0) |                |
| coeff_re_i      | in        | std_logic_vector(COEFF_SIZE-1 downto 0) |                |
| coeff_re_addr_i |           | std_logic_vector(ADDR_SIZE-1 downto 0)  |                |
| coeff_re_en_i   |           | std_logic                               |                |
| coeff_im_i      | in        | std_logic_vector(COEFF_SIZE-1 downto 0) |                |
| coeff_im_addr_i |           | std_logic_vector(ADDR_SIZE-1 downto 0)  |                |
| coeff_im_en_i   |           | std_logic                               |                |
| res_re_o        | out       | std_logic_vector(DATA_SIZE-1 downto 0)  |                |
| res_im_o        | out       | std_logic_vector(DATA_SIZE-1 downto 0)  |                |
| res_addr_i      | in        | std_logic_vector(ADDR_SIZE-1 downto 0)  |                |
## Signals

| Name               | Type                                   | Description |
| ------------------ | -------------------------------------- | ----------- |
| state_s            | state_type                             |             |
|  state_next_s      | state_type                             |             |
| stage_s            | natural range 0 to LOG_2_N_FFT         |             |
|  stage_next_s      | natural range 0 to LOG_2_N_FFT         |             |
| n_of_b_s           | std_logic_vector(ADDR_SIZE-1 downto 0) |             |
|  n_of_b_next_s     | std_logic_vector(ADDR_SIZE-1 downto 0) |             |
| s_of_b_s           | std_logic_vector(ADDR_SIZE-1 downto 0) |             |
|  s_of_b_next_s     | std_logic_vector(ADDR_SIZE-1 downto 0) |             |
| start_radix_s      | std_logic                              |             |
|  radix_done_s      | std_logic                              |             |
| start_radix_next_s | std_logic                              |             |
| stage_slv_s        | std_logic_vector(ADDR_SIZE-1 downto 0) |             |
| done_fft_next_s    | std_logic                              |             |
## Constants

| Name        | Type                                   | Value                                 | Description |
| ----------- | -------------------------------------- | ------------------------------------- | ----------- |
| N_FFT_DIV_2 | std_logic_vector(ADDR_SIZE-1 downto 0) |   		'1'&(ADDR_SIZE-2 downto 0 => '0') |             |
## Types

| Name       | Type                                                       | Description |
| ---------- | ---------------------------------------------------------- | ----------- |
| state_type | (IDLE,<br><span style="padding-left:20px"> WAIT_END_COMP)  |             |
## Processes
- unnamed: ( clk_i )
- unnamed: ( state_s, n_of_b_s, s_of_b_s, stage_s,
			start_fft_i, radix_done_s )
- unnamed: ( radix_done_s, stage_s )
## Instantiations

- fft_radix_inst: work.fft_loop_radix
