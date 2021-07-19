# Entity: fft_top_logic

- **File**: fft_top_logic.vhd
## Diagram

![Diagram](fft_top_logic.svg "Diagram")
## Generics

| Generic name   | Type    | Value | Description |
| -------------- | ------- | ----- | ----------- |
| USE_EOF        | boolean | true  |             |
| USE_FIRST_BUFF | boolean | true  |             |
| USE_SEC_BUFF   | boolean | true  |             |
| DEBUG          | boolean | false |             |
| LOG_2_N_FFT    | natural | 8     |             |
| N_FFT          | natural | 2048  |             |
| COEFF_SIZE     | natural | 16    |             |
| SHIFT_VAL      | natural | 16    |             |
| ADDR_SIZE      | natural | 10    |             |
| DATA_SIZE      | natural | 32    |             |
| DATA_IN_SIZE   | natural | 16    |             |
## Ports

| Port name       | Direction | Type                                      | Description    |
| --------------- | --------- | ----------------------------------------- | -------------- |
| clk_i           | in        | std_logic                                 | Syscon signals |
| cpu_clk_i       | in        | std_logic                                 |                |
| cpu_rst_i       | in        | std_logic                                 |                |
| data_rst_i      | in        | std_logic                                 |                |
| data_i          | in        | std_logic_vector(DATA_IN_SIZE-1 downto 0) | input data     |
| data_en_i       | in        | std_logic                                 |                |
| data_eof_i      | in        | std_logic                                 |                |
| read_coeff_re_o | out       | std_logic_vector(COEFF_SIZE-1 downto 0)   |                |
| read_coeff_im_o | out       | std_logic_vector(COEFF_SIZE-1 downto 0)   |                |
| coeff_re_i      | in        | std_logic_vector(COEFF_SIZE-1 downto 0)   |                |
| coeff_im_i      | in        | std_logic_vector(COEFF_SIZE-1 downto 0)   |                |
| coeff_re_addr_i |           | std_logic_vector(ADDR_SIZE-1 downto 0)    |                |
| coeff_im_addr_i |           | std_logic_vector(ADDR_SIZE-1 downto 0)    |                |
| coeff_re_en_i   |           | std_logic                                 |                |
| coeff_im_en_i   |           | std_logic                                 |                |
| res_re_o        | out       | std_logic_vector(DATA_SIZE-1 downto 0)    | results        |
| res_im_o        | out       | std_logic_vector(DATA_SIZE-1 downto 0)    |                |
| res_en_o        | out       | std_logic                                 |                |
| res_eof_o       | out       | std_logic                                 |                |
## Signals

| Name                | Type                                   | Description     |
| ------------------- | -------------------------------------- | --------------- |
| NB_ELEM             | natural                                |                 |
| state_s             | state_type                             |                 |
|  state_next_s       | state_type                             |                 |
| data_addr_s         | std_logic_vector(ADDR_SIZE-1 downto 0) |                 |
| data_addr2_s        | std_logic_vector(ADDR_SIZE-1 downto 0) |                 |
| data_addr_next_s    | std_logic_vector(ADDR_SIZE-1 downto 0) |                 |
| start_fft_s         | std_logic                              |                 |
|  done_fft_s         | std_logic                              |                 |
| data_in_en_s        | std_logic                              |                 |
| data_in_eof_s       | std_logic                              |                 |
| result_addr_s       | std_logic_vector(ADDR_SIZE-1 downto 0) | results         |
| tmp_im_s            | std_logic_vector(DATA_SIZE-1 downto 0) |                 |
| tmp_re_s            | std_logic_vector(DATA_SIZE-1 downto 0) |                 |
| done_transmit_s     | std_logic                              |                 |
| data_in_s           | std_logic_vector(DATA_SIZE-1 downto 0) | size conversion |
| transmit_en_s       | std_logic                              |                 |
|  transmit_en_next_s | std_logic                              |                 |
| start_fft_next_s    | std_logic                              |                 |
## Constants

| Name       | Type                                   | Value                            | Description |
| ---------- | -------------------------------------- | -------------------------------- | ----------- |
| ALL_IN_ONE | std_logic_vector(ADDR_SIZE-1 downto 0) |  		(ADDR_SIZE-1 downto 0 => '1') |             |
## Types

| Name       | Type                                                                                                                                                            | Description |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| state_type | (IDLE,<br><span style="padding-left:20px"> WAIT_END_COMP,<br><span style="padding-left:20px"> WAIT_END_TRANSMIT,<br><span style="padding-left:20px"> WAIT_EOF)  |             |
## Processes
- unnamed: ( clk_i )
- unnamed: ( state_s, start_fft_s, done_fft_s,
		data_in_en_s, data_in_eof_s,
		transmit_en_s, done_transmit_s, data_addr2_s )
- unnamed: ( data_addr2_s )
## Instantiations

- transmitter: work.fft_transfert
- fft_loop_stage_inst: work.fft_loop_stage
