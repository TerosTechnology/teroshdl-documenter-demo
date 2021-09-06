# Entity: pidv3_axi_logic

- **File**: pidv3_axi_logic.vhd
## Diagram

![Diagram](pidv3_axi_logic.svg "Diagram")
## Generics

| Generic name  | Type    | Value | Description |
| ------------- | ------- | ----- | ----------- |
| P_SIZE        | integer | 16    |             |
| PSR           | integer | 12    | PSR_SIZE    |
| I_SIZE        | integer | 16    |             |
| ISR           | integer | 18    |             |
| D_SIZE        | integer | 16    |             |
| DSR           | integer | 10    |             |
| DATA_IN_SIZE  | natural | 14    |             |
| DATA_OUT_SIZE | natural | 14    |             |
## Ports

| Port name  | Direction | Type                                       | Description                |
| ---------- | --------- | ------------------------------------------ | -------------------------- |
| clk_i      | in        | std_logic                                  | yscon signals              |
| reset      | in        | std_logic                                  |                            |
| data_i     | in        | std_logic_vector(DATA_IN_SIZE-1 downto 0)  | ata                        |
| data_en_i  | in        | std_logic                                  |                            |
| data_o     | out       | std_logic_vector(DATA_OUT_SIZE-1 downto 0) |                            |
| data_en_o  | out       | std_logic                                  |                            |
| setpoint_i | in        | std_logic_vector(DATA_IN_SIZE-1 downto 0)  | ettingsmplementer le sens  |
| kp_i       | in        | std_logic_vector(P_SIZE-1 downto 0)        |                            |
| ki_i       | in        | std_logic_vector(I_SIZE-1 downto 0)        |                            |
| kd_i       | in        | std_logic_vector(D_SIZE-1 downto 0)        |                            |
| sign_i     | in        | std_logic                                  |                            |
| int_rst_i  | in        | std_logic                                  |                            |
## Signals

| Name          | Type                                  | Description                            |
| ------------- | ------------------------------------- | -------------------------------------- |
| data_in_s     | signed(ERR_SZ-1 downto 0)             |                                        |
| setpoint_s    | signed(ERR_SZ-1 downto 0)             |                                        |
| error_s       | signed(ERR_SZ-1 downto 0)             |                                        |
| data_en_s     | std_logic                             |                                        |
| data2_en_s    | std_logic                             |                                        |
| data_en_out_s | std_logic                             |                                        |
| P_temp_s      | signed(P_MULT_SZ-1 downto 0)          |                                        |
| P_s           | signed(P_RES_SZ-1 downto 0)           |                                        |
| Pd_s          | signed(P_RES_SZ-1 downto 0)           |                                        |
| I_sum_s       | signed(I_MULT_SZ downto 0)            | somme avec overflow detect             |
| I_temp_s      | signed(I_MULT_SZ-1 downto 0)          | somme utile                            |
| I_s           | signed(I_RES_SZ-1 downto 0)           |                                        |
| p_pid_s       | signed(PID_SZ-1 downto 0)             |                                        |
| i_pid_s       | signed(PID_SZ-1 downto 0)             |                                        |
| pid_sum_s     | std_logic_vector(PID_SZ downto 0)     | v_k                                    |
| pid_out_s     | std_logic_vector(PID_SZ-1 downto 0)   | u_k                                    |
| msb_s         | std_logic_vector(MSB_SIZE-1 downto 0) |  dropped part of the I input signal    |
| is_zero       | boolean                               |  check is high slice is fully 0 and 1  |
|  is_one       | boolean                               |  check is high slice is fully 0 and 1  |
## Constants

| Name      | Type    | Value                                                                         | Description                                                 |
| --------- | ------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------- |
| ERR_SZ    | natural |  DATA_IN_SIZE+1                                                               |                                                             |
| P_MULT_SZ | natural |  ERR_SZ + P_SIZE                                                              |  p --                                                       |
| P_RES_SZ  | natural |  P_MULT_SZ-PSR                                                                |                                                             |
| I_MULT_SZ | natural |  ERR_SZ + I_SIZE                                                              |  i -- signal I_desat_s  : std_logic_vector(33-1 downto 0);  |
| I_RES_SZ  | natural |  I_MULT_SZ-ISR                                                                |                                                             |
| PID_SZ    | natural |  sel(P_RES_SZ,<br><span style="padding-left:20px"> I_RES_SZ)                  |                                                             |
| MSB_SIZE  | natural |  comp_unused_slice(PID_SZ,<br><span style="padding-left:20px"> DATA_OUT_SIZE) |  size of the dropped part of input signal                   |
## Functions
- sel <font id="function_arguments">(P,<br><span style="padding-left:20px"> I: natural) </font> <font id="function_return">return natural </font>
**Description**
signal I_s	  : std_logic_vector(33-1 downto 0);

- comp_unused_slice <font id="function_arguments">(in_size,<br><span style="padding-left:20px"> out_size: natural) </font> <font id="function_return">return natural </font>
**Description**
 return static size or difference between input and output size
 if in_size > out_size

## Processes
- unnamed: ( clk_i )
**Description**
error signal 
- unnamed: ( clk_i )
- unnamed: ( clk_i )
- unnamed: ( clk_i )
**Description**
derivative --none for the moment sum + sat + integr desat 
