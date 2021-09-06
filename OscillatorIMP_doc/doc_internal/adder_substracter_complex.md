# Entity: adder_substracter_complex

- **File**: adder_substracter_complex.vhd
## Diagram

![Diagram](adder_substracter_complex.svg "Diagram")
## Generics

| Generic name | Type    | Value    | Description |
| ------------ | ------- | -------- | ----------- |
| format       | string  | "signed" |             |
| opp          | string  | "add"    |             |
| DATA_SIZE    | natural | 16       |             |
## Ports

| Port name   | Direction | Type                                   | Description            |
| ----------- | --------- | -------------------------------------- | ---------------------- |
| data1_i_i   | in        | std_logic_vector(DATA_SIZE-1 downto 0) | input data             |
| data1_q_i   | in        | std_logic_vector(DATA_SIZE-1 downto 0) |                        |
| data1_en_i  | in        | std_logic                              |                        |
| data1_sof_i | in        | std_logic                              |                        |
| data1_eof_i | in        | std_logic                              |                        |
| data1_clk_i | in        | std_logic                              |                        |
| data1_rst_i | in        | std_logic                              |                        |
| data2_i_i   | in        | std_logic_vector(DATA_SIZE-1 downto 0) |                        |
| data2_q_i   | in        | std_logic_vector(DATA_SIZE-1 downto 0) |                        |
| data2_en_i  | in        | std_logic                              |                        |
| data2_sof_i | in        | std_logic                              |                        |
| data2_eof_i | in        | std_logic                              |                        |
| data2_clk_i | in        | std_logic                              |                        |
| data2_rst_i | in        | std_logic                              |                        |
| data_i_o    | out       | std_logic_vector(DATA_SIZE downto 0)   | for the next component |
| data_q_o    | out       | std_logic_vector(DATA_SIZE downto 0)   |                        |
| data_en_o   | out       | std_logic                              |                        |
| data_sof_o  | out       | std_logic                              |                        |
| data_eof_o  | out       | std_logic                              |                        |
| data_clk_o  | out       | std_logic                              |                        |
| data_rst_o  | out       | std_logic                              |                        |
## Signals

| Name          | Type                                   | Description               |
| ------------- | -------------------------------------- | ------------------------- |
| data_in_i_s   | std_logic_vector(DATA_SIZE downto 0)   |                           |
|  data_in_q_s  | std_logic_vector(DATA_SIZE downto 0)   |                           |
| data_i_s      | std_logic_vector(DATA_SIZE downto 0)   |                           |
|  data_q_s     | std_logic_vector(DATA_SIZE downto 0)   |                           |
| data_en_s     | std_logic                              |                           |
|  data_eof_s   | std_logic                              |                           |
|  data_sof_s   | std_logic                              |                           |
| data1_i_s     | std_logic_vector(DATA_SIZE-1 downto 0) |                           |
|  data2_i_s    | std_logic_vector(DATA_SIZE-1 downto 0) |                           |
| data1_q_s     | std_logic_vector(DATA_SIZE-1 downto 0) |                           |
|  data2_q_s    | std_logic_vector(DATA_SIZE-1 downto 0) |                           |
| data11_en_s   | std_logic                              |                           |
|  data21_en_s  | std_logic                              |                           |
| data11_sof_s  | std_logic                              |                           |
|  data21_sof_s | std_logic                              |                           |
| data11_eof_s  | std_logic                              |                           |
|  data21_eof_s | std_logic                              |                           |
| data11_i_s    | std_logic_vector(DATA_SIZE-1 downto 0) |                           |
|  data21_i_s   | std_logic_vector(DATA_SIZE-1 downto 0) |                           |
| data11_q_s    | std_logic_vector(DATA_SIZE-1 downto 0) |                           |
|  data21_q_s   | std_logic_vector(DATA_SIZE-1 downto 0) |                           |
| d1_en_s       | std_logic                              |                           |
|  d2_en_s      | std_logic                              |                           |
| d1_sof_s      | std_logic                              |                           |
|  d2_sof_s     | std_logic                              |                           |
| d1_eof_s      | std_logic                              |                           |
|  d2_eof_s     | std_logic                              |                           |
| d1_i_s        | std_logic_vector(DATA_SIZE downto 0)   |  resize before operation  |
|  d1_q_s       | std_logic_vector(DATA_SIZE downto 0)   |  resize before operation  |
| d2_i_s        | std_logic_vector(DATA_SIZE downto 0)   |                           |
|  d2_q_s       | std_logic_vector(DATA_SIZE downto 0)   |                           |
## Processes
- unnamed: ( data1_clk_i )
- unnamed: ( data2_clk_i )
- unnamed: ( data1_clk_i )
**Description**
 resynchro 
- unnamed: ( data1_clk_i )
