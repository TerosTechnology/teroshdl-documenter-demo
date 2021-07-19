# Entity: fft_coeff_handler

- **File**: fft_coeff_handler.vhd
## Diagram

![Diagram](fft_coeff_handler.svg "Diagram")
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| ADDR_SIZE    | natural | 10    |             |
| DATA_SIZE    | natural | 16    |             |
## Ports

| Port name       | Direction | Type                                   | Description    |
| --------------- | --------- | -------------------------------------- | -------------- |
| clk_i           | in        | std_logic                              | Syscon signals |
| cpu_clk_i       | in        | std_logic                              |                |
| rst_i           | in        | std_logic                              |                |
| read_coeff_re_o | out       | std_logic_vector(DATA_SIZE-1 downto 0) | input data     |
| read_coeff_im_o | out       | std_logic_vector(DATA_SIZE-1 downto 0) |                |
| coeff_re_i      | in        | std_logic_vector(DATA_SIZE-1 downto 0) |                |
| coeff_re_addr_i |           | std_logic_vector(ADDR_SIZE-1 downto 0) |                |
| coeff_re_we_i   |           | std_logic                              |                |
| coeff_im_i      | in        | std_logic_vector(DATA_SIZE-1 downto 0) |                |
| coeff_im_addr_i |           | std_logic_vector(ADDR_SIZE-1 downto 0) |                |
| coeff_im_we_i   |           | std_logic                              |                |
| n_of_b_i        | in        | std_logic_vector(ADDR_SIZE-1 downto 0) | control        |
| clear_accum_i   | in        | std_logic                              |                |
| enable_incr_i   | in        | std_logic                              |                |
| coeff_re_o      | out       | std_logic_vector(DATA_SIZE-1 downto 0) | output data    |
| coeff_im_o      | out       | std_logic_vector(DATA_SIZE-1 downto 0) |                |
## Signals

| Name        | Type                                    | Description |
| ----------- | --------------------------------------- | ----------- |
| coeff_re_s  | std_logic_vector(DATA_SIZE-1 downto 0)  |             |
|  coeff_im_s | std_logic_vector(DATA_SIZE-1 downto 0)  |             |
| tmp_re_s    | std_logic_vector(DATA_SIZE-1 downto 0)  |             |
|  tmp_im_s   | std_logic_vector(DATA_SIZE-1 downto 0)  |             |
| addr_s      | std_logic_vector(ADDR_SIZE -1 downto 0) |             |
| tmp_incr_s  | std_logic                               |             |
| addr_next_s | std_logic_vector(ADDR_SIZE-1 downto 0)  |             |
## Processes
- unnamed: ( clk_i )
- unnamed: ( clk_i )
- unnamed: ( addr_s, clear_accum_i, enable_incr_i, n_of_b_i )
## Instantiations

- coeff_re_inst: work.fft_ram_coeff
- coeff_im_inst: work.fft_ram_coeff
