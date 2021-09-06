# Entity: cordicAtan

- **File**: cordicAtan.vhd
## Diagram

![Diagram](cordicAtan.svg "Diagram")
## Generics

| Generic name  | Type    | Value    | Description            |
| ------------- | ------- | -------- | ---------------------- |
| NB_ITER       | natural | 25       |                        |
| DATA_IN_SIZE  | natural | 32       |                        |
| DATA_OUT_SIZE | natural | 28       |                        |
| PI_VALUE      | natural | 52707179 |  M_PI * 2**(NB_ITER-1) |
## Ports

| Port name  | Direction | Type                                       | Description |
| ---------- | --------- | ------------------------------------------ | ----------- |
| data_en_i  | in        | std_logic                                  | input data  |
| data_i_i   | in        | std_logic_vector(DATA_IN_SIZE-1 downto 0)  |             |
| data_q_i   | in        | std_logic_vector(DATA_IN_SIZE-1 downto 0)  |             |
| data_clk_i | in        | std_logic                                  |             |
| data_rst_i | in        | std_logic                                  |             |
| atan_o     | out       | std_logic_vector(DATA_OUT_SIZE-1 downto 0) | output      |
| atan_en_o  | out       | std_logic                                  |             |
| atan_clk_o | out       | std_logic                                  |             |
| atan_rst_o | out       | std_logic                                  |             |
## Signals

| Name          | Type                                          | Description |
| ------------- | --------------------------------------------- | ----------- |
| data_i_in_s   | std_logic_vector(RESIZE_DATA_SIZE-1 downto 0) |             |
| data_q_in_s   | std_logic_vector(RESIZE_DATA_SIZE-1 downto 0) |             |
| data_en_in_s  | std_logic                                     |             |
| data_i_s      | data_tab(NB_ITER downto 0)                    |             |
| data_q_s      | data_tab(NB_ITER downto 0)                    |             |
| data_en_s     | std_logic_vector(NB_ITER downto 0)            |             |
| atan_s        | atan_tab(NB_ITER downto 0)                    |             |
| sign_s        | sign_tab(NB_ITER downto 0)                    |             |
| sign_tmp_s    | std_logic_vector(3 downto 0)                  |             |
| atan_corr_s   | std_logic_vector(ALPHA_SIZE-1 downto 0)       |             |
| atan_fin_s    | std_logic_vector(ALPHA_SIZE-1 downto 0)       |             |
| data_en_fin_s | std_logic                                     |             |
## Constants

| Name             | Type                                     | Value                                                                                  | Description |
| ---------------- | ---------------------------------------- | -------------------------------------------------------------------------------------- | ----------- |
| ATAN_SIZE        | natural                                  |  NB_ITER-1                                                                             |             |
| SHIFT_FACTOR     | natural                                  |  NB_ITER-1                                                                             |             |
| RESIZE_DATA_SIZE | natural                                  |  2+DATA_IN_SIZE+SHIFT_FACTOR                                                           |             |
| ALPHA_SIZE       | natural                                  |  ATAN_SIZE+4                                                                           |             |
| pi_resize_s      | std_logic_vector(ALPHA_SIZE -1 downto 0) |  std_logic_vector(to_signed(PI_VALUE,<br><span style="padding-left:20px"> ALPHA_SIZE)) |             |
## Types

| Name     | Type                                                                       | Description |
| -------- | -------------------------------------------------------------------------- | ----------- |
| atan_tab | array (natural range <>) of std_logic_vector(ALPHA_SIZE-1 downto 0)        |             |
| data_tab | array (natural range <>) of std_logic_vector(RESIZE_DATA_SIZE-1 downto 0)  |             |
| sign_tab | array (natural range <>) of std_logic_vector(3 downto 0)                   |             |
## Processes
- unnamed: ( data_clk_i )
- unnamed: ( sign_tmp_s, atan_s )
</br>**Description**
 correction 
- unnamed: ( data_clk_i )
