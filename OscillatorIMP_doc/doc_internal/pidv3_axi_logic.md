# Entity: pidv3_axi_logic

- **File**: pidv3_axi_logic.vhd
## Diagram

![Diagram](pidv3_axi_logic.svg "Diagram")
## Generics

| Generic name  | Type    | Value | Description |
| ------------- | ------- | ----- | ----------- |
| P_SIZE        | integer | 16    |             |
| PSR           | integer | 12    |             |
| I_SIZE        | integer | 16    |             |
| ISR           | integer | 18    |             |
| D_SIZE        | integer | 16    |             |
| DSR           | integer | 10    |             |
| DATA_IN_SIZE  | natural | 14    |             |
| DATA_OUT_SIZE | natural | 14    |             |
## Ports

| Port name  | Direction | Type                                       | Description |
| ---------- | --------- | ------------------------------------------ | ----------- |
| clk_i      | in        | std_logic                                  |             |
| reset      | in        | std_logic                                  |             |
| data_i     | in        | std_logic_vector(DATA_IN_SIZE-1 downto 0)  |             |
| data_en_i  | in        | std_logic                                  |             |
| data_o     | out       | std_logic_vector(DATA_OUT_SIZE-1 downto 0) |             |
| data_en_o  | out       | std_logic                                  |             |
| setpoint_i | in        | std_logic_vector(DATA_IN_SIZE-1 downto 0)  |             |
| kp_i       | in        | std_logic_vector(P_SIZE-1 downto 0)        |             |
| ki_i       | in        | std_logic_vector(I_SIZE-1 downto 0)        |             |
| kd_i       | in        | std_logic_vector(D_SIZE-1 downto 0)        |             |
| sign_i     | in        | std_logic                                  |             |
| int_rst_i  | in        | std_logic                                  |             |
## Signals

| Name          | Type                                   | Description |
| ------------- | -------------------------------------- | ----------- |
| data_in_s     | std_logic_vector(ERR_SZ-1 downto 0)    |             |
| setpoint_s    | std_logic_vector(ERR_SZ-1 downto 0)    |             |
| error_s       | std_logic_vector(ERR_SZ-1 downto 0)    |             |
| data_en_s     | std_logic                              |             |
| data2_en_s    | std_logic                              |             |
| data_en_out_s | std_logic                              |             |
| P_temp_s      | std_logic_vector(P_MULT_SZ-1 downto 0) |             |
| P_s           | std_logic_vector(P_RES_SZ-1 downto 0)  |             |
| Pd_s          | std_logic_vector(P_RES_SZ-1 downto 0)  |             |
| I_sum_s       | std_logic_vector(I_MULT_SZ downto 0)   |             |
| I_temp_s      | std_logic_vector(I_MULT_SZ-1 downto 0) |             |
| I_s           | std_logic_vector(I_RES_SZ-1 downto 0)  |             |
| p_pid_s       | std_logic_vector(PID_SZ-1 downto 0)    |             |
| i_pid_s       | std_logic_vector(PID_SZ-1 downto 0)    |             |
| pid_sum_s     | std_logic_vector(PID_SZ downto 0)      |             |
| pid_out_s     | std_logic_vector(PID_SZ-1 downto 0)    |             |
## Constants

| Name      | Type    | Value                                                        | Description |
| --------- | ------- | ------------------------------------------------------------ | ----------- |
| ERR_SZ    | natural |  DATA_IN_SIZE+1                                              |             |
| P_MULT_SZ | natural |  ERR_SZ + P_SIZE                                             | p --        |
| P_RES_SZ  | natural |  P_MULT_SZ-PSR                                               |             |
| I_MULT_SZ | natural |  ERR_SZ + I_SIZE                                             |             |
| I_RES_SZ  | natural |  I_MULT_SZ-ISR                                               |             |
| PID_SZ    | natural |  sel(P_RES_SZ,<br><span style="padding-left:20px"> I_RES_SZ) |             |
## Functions
- sel <font id="function_arguments">(P,<br><span style="padding-left:20px"> I: natural) </font> <font id="function_return">return natural </font>
## Processes
- unnamed: ( clk_i )
- unnamed: ( clk_i )
- unnamed: ( clk_i )
- unnamed: ( clk_i )
