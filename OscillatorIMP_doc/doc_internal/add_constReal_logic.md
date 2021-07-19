# Entity: add_constReal_logic

- **File**: add_constReal_logic.vhd
## Diagram

![Diagram](add_constReal_logic.svg "Diagram")
## Generics

| Generic name  | Type    | Value    | Description |
| ------------- | ------- | -------- | ----------- |
| format        | string  | "signed" |             |
| DATA_OUT_SIZE | natural | 18       |             |
| DATA_IN_SIZE  | natural | 16       |             |
## Ports

| Port name | Direction | Type                                       | Description            |
| --------- | --------- | ------------------------------------------ | ---------------------- |
| rst_i     | in        | std_logic                                  | Syscon signals         |
| clk_i     | in        | std_logic                                  |                        |
| add_val   | in        | std_logic_vector(DATA_IN_SIZE-1 downto 0)  | config                 |
| data_i    | in        | std_logic_vector(DATA_IN_SIZE-1 downto 0)  | input data             |
| data_en_i | in        | std_logic                                  |                        |
| data_o    | out       | std_logic_vector(DATA_OUT_SIZE-1 downto 0) | for the next component |
| data_en_o | out       | std_logic                                  |                        |
## Signals

| Name      | Type                                       | Description |
| --------- | ------------------------------------------ | ----------- |
| data_in_s | std_logic_vector(DATA_OUT_SIZE-1 downto 0) |             |
|  data_s   | std_logic_vector(DATA_OUT_SIZE-1 downto 0) |             |
## Processes
- unnamed: ( clk_i )
