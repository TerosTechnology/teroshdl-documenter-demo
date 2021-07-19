# Entity: meanReal

- **File**: meanReal.vhd
## Diagram

![Diagram](meanReal.svg "Diagram")
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
| data_i     | in        | std_logic_vector(DATA_IN_SIZE-1 downto 0)  | input data             |
| data_en_i  | in        | std_logic                                  |                        |
| data_clk_i | in        | std_logic                                  |                        |
| data_rst_i | in        | std_logic                                  |                        |
| data_o     | out       | std_logic_vector(DATA_OUT_SIZE-1 downto 0) | for the next component |
| data_clk_o | out       | std_logic                                  |                        |
| data_rst_o | out       | std_logic                                  |                        |
| data_en_o  | out       | std_logic                                  |                        |
## Signals

| Name          | Type                                       | Description |
| ------------- | ------------------------------------------ | ----------- |
| data_resize_s | std_logic_vector(TMP_DATA_SIZE-1 downto 0) |             |
| accum_s       | std_logic_vector(TMP_DATA_SIZE-1 downto 0) |             |
| accum_next_s  | std_logic_vector(TMP_DATA_SIZE-1 downto 0) |             |
| final_s       | std_logic_vector(DATA_OUT_SIZE-1 downto 0) |             |
| cpt           | natural range 0 to NB_ACCUM-1              |             |
## Constants

| Name          | Type    | Value                | Description |
| ------------- | ------- | -------------------- | ----------- |
| TMP_DATA_SIZE | natural |  DATA_OUT_SIZE+SHIFT |             |
## Processes
- unnamed: ( data_clk_i )
- unnamed: ( data_clk_i )
