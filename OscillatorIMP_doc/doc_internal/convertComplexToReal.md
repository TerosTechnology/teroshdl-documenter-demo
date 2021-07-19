# Entity: convertComplexToReal

- **File**: convertComplexToReal.vhd
## Diagram

![Diagram](convertComplexToReal.svg "Diagram")
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| DATA_SIZE    | natural | 8     |             |
## Ports

| Port name   | Direction | Type                                   | Description |
| ----------- | --------- | -------------------------------------- | ----------- |
| data1_o     | out       | std_logic_vector(DATA_SIZE-1 downto 0) | output data |
| data1_en_o  | out       | std_logic                              |             |
| data1_eof_o | out       | std_logic                              |             |
| data1_clk_o | out       | std_logic                              |             |
| data1_rst_o | out       | std_logic                              |             |
| data2_o     | out       | std_logic_vector(DATA_SIZE-1 downto 0) |             |
| data2_en_o  | out       | std_logic                              |             |
| data2_eof_o | out       | std_logic                              |             |
| data2_clk_o | out       | std_logic                              |             |
| data2_rst_o | out       | std_logic                              |             |
| data_i_i    | in        | std_logic_vector(DATA_SIZE-1 downto 0) | input data  |
| data_q_i    | in        | std_logic_vector(DATA_SIZE-1 downto 0) |             |
| data_eof_i  | in        | std_logic                              |             |
| data_en_i   | in        | std_logic                              |             |
| data_rst_i  | in        | std_logic                              |             |
| data_clk_i  | in        | std_logic                              |             |
