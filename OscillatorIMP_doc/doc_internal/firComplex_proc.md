# Entity: firComplex_proc

## Diagram

![Diagram](firComplex_proc.svg "Diagram")
## Generics

| Generic name  | Type    | Value    | Description |
| ------------- | ------- | -------- | ----------- |
| coeff_format  | string  | "signed" |             |
| NB_COEFF      | natural | 128      |             |
| DATA_SIZE     | natural | 16       |             |
| DATA_OUT_SIZE | natural | 32       |             |
| COEFF_SIZE    | natural | 16       |             |
## Ports

| Port name | Direction | Type                                       | Description    |
| --------- | --------- | ------------------------------------------ | -------------- |
| reset     | in        | std_logic                                  | Syscon signals |
| clk       | in        | std_logic                                  |                |
| ready_i   | in        | std_logic                                  | input data     |
| end_i     | in        | std_logic                                  |                |
| data_i_i  | in        | std_logic_vector(DATA_SIZE-1 downto 0)     |                |
| data_q_i  | in        | std_logic_vector(DATA_SIZE-1 downto 0)     |                |
| coeff_i   | in        | std_logic_vector(COEFF_SIZE-1 downto 0)    |                |
| data_en_i | in        | std_logic                                  |                |
| data_i_o  | out       | std_logic_vector(DATA_OUT_SIZE-1 downto 0) |                |
| data_q_o  | out       | std_logic_vector(DATA_OUT_SIZE-1 downto 0) |                |
| data_en_o | out       | std_logic                                  |                |
## Signals

| Name               | Type                                       | Description |
| ------------------ | ------------------------------------------ | ----------- |
| ready_s            | std_logic                                  |             |
| must_rst_s         | std_logic                                  |             |
| data_i_s           | std_logic_vector(DATA_SIZE-1 downto 0)     | i part      |
| mult_i_res         | std_logic_vector(MULT_SZ-1 downto 0)       |             |
| mux_accum_i_s      | std_logic_vector(INT_SZ-1 downto 0)        |             |
| res_i_s            | std_logic_vector(INT_SZ-1 downto 0)        |             |
|  res_i_next_s      | std_logic_vector(INT_SZ-1 downto 0)        |             |
| final_res_i_s      | std_logic_vector(DATA_OUT_SIZE-1 downto 0) |             |
| final_res_i_next_s | std_logic_vector(DATA_OUT_SIZE-1 downto 0) |             |
| data_q_s           | std_logic_vector(DATA_SIZE-1 downto 0)     | q part      |
| mult_q_res         | std_logic_vector(MULT_SZ-1 downto 0)       |             |
| mux_accum_q_s      | std_logic_vector(INT_SZ-1 downto 0)        |             |
| res_q_s            | std_logic_vector(INT_SZ-1 downto 0)        |             |
|  res_q_next_s      | std_logic_vector(INT_SZ-1 downto 0)        |             |
| final_res_q_s      | std_logic_vector(DATA_OUT_SIZE-1 downto 0) |             |
| final_res_q_next_s | std_logic_vector(DATA_OUT_SIZE-1 downto 0) |             |
| data_en_s          | std_logic                                  |             |
| end_s              | std_logic                                  |             |
| data_out_en_s      | std_logic                                  |             |
## Constants

| Name     | Type                                | Value                                          | Description |
| -------- | ----------------------------------- | ---------------------------------------------- | ----------- |
| MULT_SZ  | natural                             |  DATA_SIZE+COEFF_SIZE                          |             |
| INT_SZ   | natural                             |  MULT_SZ + natural(ceil(log2(real(NB_COEFF)))) |             |
| ALL_ZERO | std_logic_vector(INT_SZ-1 downto 0) |  (INT_SZ-1 downto 0 => '0')                    |             |
## Processes
- unnamed: ( clk )
- unnamed: ( clk )
- unnamed: ( clk )
- unnamed: ( clk )
- unnamed: ( clk )
