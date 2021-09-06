# Entity: mixer_sin

- **File**: mixer_sin.vhd
## Diagram

![Diagram](mixer_sin.svg "Diagram")
## Description

-------------------------------------------------------------------------
 (c) Copyright: OscillatorIMP Digital
 Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
 Creation date : 2016/09/14
-------------------------------------------------------------------------
## Generics

| Generic name  | Type    | Value     | Description |
| ------------- | ------- | --------- | ----------- |
| NCO_SIZE      | natural | 16        |             |
| ENABLE_SEL    | string  | "data_in" |             |
| DATA_IN_SIZE  | natural | 16        |             |
| DATA_OUT_SIZE | natural | 16        |             |
## Ports

| Port name  | Direction | Type                                       | Description   |
| ---------- | --------- | ------------------------------------------ | ------------- |
| data_en_i  | in        | std_logic                                  | ADC interface |
| data_clk_i | in        | std_logic                                  |               |
| data_rst_i | in        | std_logic                                  |               |
| data_i     | in        | std_logic_vector(DATA_IN_SIZE-1 downto 0)  |               |
| nco_i_i    | in        | std_logic_vector(NCO_SIZE-1 downto 0)      | NCO interface |
| nco_q_i    | in        | std_logic_vector(NCO_SIZE-1 downto 0)      |               |
| nco_en_i   | in        | std_logic                                  |               |
| nco_rst_i  | in        | std_logic                                  |               |
| nco_clk_i  | in        | std_logic                                  |               |
| data_en_o  | out       | std_logic                                  | next          |
| data_clk_o | out       | std_logic                                  |               |
| data_rst_o | out       | std_logic                                  |               |
| data_i_o   | out       | std_logic_vector(DATA_OUT_SIZE-1 downto 0) |               |
| data_q_o   | out       | std_logic_vector(DATA_OUT_SIZE-1 downto 0) |               |
## Signals

| Name          | Type                                        | Description      |
| ------------- | ------------------------------------------- | ---------------- |
| nco_i_s       | signed(NCO_SIZE-1 downto 0)                 |                  |
| nco_q_s       | signed(NCO_SIZE-1 downto 0)                 |                  |
| nco_en_s      | std_logic                                   |                  |
| data_en_s     | std_logic                                   |                  |
| data_s        | signed(DATA_IN_SIZE-1 downto 0)             |                  |
| clk_s         | std_logic                                   |                  |
|  rst_s        | std_logic                                   |                  |
| res_i_s       | signed(MULT_SIZE-1 downto 0)                |                  |
|  res_q_s      | signed(MULT_SIZE-1 downto 0)                |                  |
| data_sel_en_s | std_logic                                   |  output latches  |
| data_i_s      | std_logic_vector(POST_MULT_SIZE-1 downto 0) |                  |
|  data_q_s     | std_logic_vector(POST_MULT_SIZE-1 downto 0) |                  |
## Constants

| Name           | Type    | Value                    | Description      |
| -------------- | ------- | ------------------------ | ---------------- |
| MULT_SIZE      | natural |  NCO_SIZE + DATA_IN_SIZE |  multiplication  |
| POST_MULT_SIZE | natural |  MULT_SIZE-1             |                  |
## Processes
- unnamed: ( nco_clk_i )
- unnamed: ( data_clk_i )
## Instantiations

- resize_inst: work.mixer_redim
