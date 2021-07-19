# Entity: meanComplex

- **File**: meanComplex.vhd
## Diagram

![Diagram](meanComplex.svg "Diagram")
## Generics

| Generic name  | Type    | Value | Description |
| ------------- | ------- | ----- | ----------- |
| SIGNED_FORMAT | boolean | true  |             |
| NB_ACCUM      | natural | 8     |             |
| SHIFT         | natural | 3     |             |
| DATA_OUT_SIZE | natural | 18    |             |
| DATA_IN_SIZE  | natural | 16    |             |
## Ports

| Port name  | Direction | Type                                       | Description            |
| ---------- | --------- | ------------------------------------------ | ---------------------- |
| data_i_i   | in        | std_logic_vector(DATA_IN_SIZE-1 downto 0)  | input data             |
| data_q_i   | in        | std_logic_vector(DATA_IN_SIZE-1 downto 0)  |                        |
| data_en_i  | in        | std_logic                                  |                        |
| data_clk_i | in        | std_logic                                  |                        |
| data_rst_i | in        | std_logic                                  |                        |
| data_i_o   | out       | std_logic_vector(DATA_OUT_SIZE-1 downto 0) | for the next component |
| data_q_o   | out       | std_logic_vector(DATA_OUT_SIZE-1 downto 0) |                        |
| data_clk_o | out       | std_logic                                  |                        |
| data_rst_o | out       | std_logic                                  |                        |
| data_en_o  | out       | std_logic                                  |                        |
## Signals

| Name            | Type                                       | Description |
| --------------- | ------------------------------------------ | ----------- |
| data_i_resize_s | std_logic_vector(TMP_DATA_SIZE-1 downto 0) |             |
| data_q_resize_s | std_logic_vector(TMP_DATA_SIZE-1 downto 0) |             |
| accum_i_s       | std_logic_vector(TMP_DATA_SIZE-1 downto 0) |             |
| accum_q_s       | std_logic_vector(TMP_DATA_SIZE-1 downto 0) |             |
| accum_next_i_s  | std_logic_vector(TMP_DATA_SIZE-1 downto 0) |             |
| accum_next_q_s  | std_logic_vector(TMP_DATA_SIZE-1 downto 0) |             |
| final_i_s       | std_logic_vector(DATA_OUT_SIZE-1 downto 0) |             |
| final_q_s       | std_logic_vector(DATA_OUT_SIZE-1 downto 0) |             |
| cpt             | natural range 0 to NB_ACCUM-1              |             |
## Constants

| Name          | Type    | Value                | Description |
| ------------- | ------- | -------------------- | ----------- |
| TMP_DATA_SIZE | natural |  DATA_OUT_SIZE+SHIFT |             |
## Processes
- unnamed: ( data_clk_i )
- unnamed: ( data_clk_i )
