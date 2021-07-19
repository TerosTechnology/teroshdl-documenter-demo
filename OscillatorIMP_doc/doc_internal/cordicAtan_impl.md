# Entity: cordicAtan_impl

- **File**: cordicAtan_impl.vhd
## Diagram

![Diagram](cordicAtan_impl.svg "Diagram")
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| NB_ITER      | natural | 25    |             |
| SHIFT_V      | natural | 10    |             |
| ATAN_SIZE    | natural | 10    |             |
| ALPHA_SIZE   | natural | 8     |             |
| DATA_SIZE    | natural | 8     |             |
## Ports

| Port name   | Direction | Type                                    | Description    |
| ----------- | --------- | --------------------------------------- | -------------- |
| clk         | in        | std_logic                               | Syscon signals |
| sign_i      | in        | std_logic_vector(3 downto 0)            | sign		         |
| sign_o      | out       | std_logic_vector(3 downto 0)            |                |
| data_en_i   | in        | std_logic                               | input data     |
| data_i_i    | in        | std_logic_vector(DATA_SIZE-1 downto 0)  |                |
| data_q_i    | in        | std_logic_vector(DATA_SIZE-1 downto 0)  |                |
| data_atan_i | in        | std_logic_vector(ALPHA_SIZE-1 downto 0) |                |
| data_en_o   | out       | std_logic                               | output data    |
| data_i_o    | out       | std_logic_vector(DATA_SIZE-1 downto 0)  |                |
| data_q_o    | out       | std_logic_vector(DATA_SIZE-1 downto 0)  |                |
| data_atan_o | out       | std_logic_vector(ALPHA_SIZE-1 downto 0) |                |
## Signals

| Name             | Type                          | Description |
| ---------------- | ----------------------------- | ----------- |
| s_alpha_next_s   | signed(ALPHA_SIZE-1 downto 0) |             |
| sign_s           | std_logic_vector(3 downto 0)  |             |
| sign_next_s      | std_logic                     |             |
| i_div_s          | signed(T_SZ_SHIFT-1 downto 0) |             |
| q_div_s          | signed(T_SZ_SHIFT-1 downto 0) |             |
| s_i_div_s        | signed(T_SZ_SHIFT-1 downto 0) |             |
| s_q_div_s        | signed(T_SZ_SHIFT-1 downto 0) |             |
| s_alpha_s        | signed(ALPHA_SIZE-1 downto 0) |             |
| data_i_next_s    | signed(DATA_SIZE-1 downto 0)  |             |
| data_q_next_s    | signed(DATA_SIZE-1 downto 0)  |             |
| data_atan_next_s | signed(ALPHA_SIZE-1 downto 0) |             |
| data_i_s         | signed(DATA_SIZE-1 downto 0)  |             |
| data_q_s         | signed(DATA_SIZE-1 downto 0)  |             |
| data_atan_s      | signed(ALPHA_SIZE-1 downto 0) |             |
## Constants

| Name         | Type                          | Value                                                                      | Description |
| ------------ | ----------------------------- | -------------------------------------------------------------------------- | ----------- |
| SCALE_VAL    | natural                       |  NB_ITER-1                                                                 |             |
| SCALE_FACTOR | real                          |  2**real(SCALE_VAL)                                                        |             |
| RATAN        | real                          |  ARCTAN(real(2**(-real(SHIFT_V))))  * SCALE_FACTOR                         |             |
| val_alpha_s  | signed(ALPHA_SIZE-1 downto 0) |  to_signed(natural(RATAN),<br><span style="padding-left:20px"> ALPHA_SIZE) |             |
| T_SZ_SHIFT   | natural                       |  DATA_SIZE-SHIFT_V                                                         |             |
## Processes
- unnamed: ( clk )
