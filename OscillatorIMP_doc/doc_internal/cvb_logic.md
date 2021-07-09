# Entity: cvb_logic

## Diagram

![Diagram](cvb_logic.svg "Diagram")
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| ACCUM_SIZE   | natural | 32    |             |
| DATA_SIZE    | natural | 32    |             |
| ADDR_SIZE    | natural | 8     |             |
## Ports

| Port name           | Direction | Type                                    | Description     |
| ------------------- | --------- | --------------------------------------- | --------------- |
| clk_i               | in        | std_logic                               |                 |
| reset               | in        | std_logic                               |                 |
| data_en_i           | in        | std_logic                               | input           |
| data_eof_i          | in        | std_logic                               |                 |
| data_i_i            | in        | std_logic_vector(DATA_SIZE-1 downto 0)  |                 |
| data_q_i            | in        | std_logic_vector(DATA_SIZE-1 downto 0)  |                 |
| data_en_o           | out       | std_logic                               | output          |
| data_eof_o          | out       | std_logic                               |                 |
| data_i_o            | out       | std_logic_vector(DATA_SIZE-1 downto 0)  |                 |
| data_q_o            | out       | std_logic_vector(DATA_SIZE-1 downto 0)  |                 |
| start_mean_offset_i | in        | std_logic_vector(ADDR_SIZE-1 downto 0)  | config from CPU |
| max_allowed_val_i   | in        | std_logic_vector(ACCUM_SIZE-1 downto 0) |                 |
| cpt_max_i           | in        | std_logic_vector(ADDR_SIZE-1 downto 0)  |                 |
## Signals

| Name           | Type                                       | Description |
| -------------- | ------------------------------------------ | ----------- |
| data_en_s      | std_logic                                  |             |
| data_eof_s     | std_logic                                  |             |
| w_addr_s       | std_logic_vector(ADDR_SIZE-1 downto 0)     |             |
| frame_valid_s  | std_logic                                  | check       |
| w_data_s       | std_logic_vector((DATA_SIZE*2)-1 downto 0) | dual ram    |
| r_data_s       | std_logic_vector((DATA_SIZE*2)-1 downto 0) |             |
| data_eof_out_s | std_logic                                  | gen flow    |
| r_data_i_s     | std_logic_vector(DATA_SIZE-1 downto 0)     |             |
|  r_data_q_s    | std_logic_vector(DATA_SIZE-1 downto 0)     |             |
| r_addr_s       | std_logic_vector(ADDR_SIZE-1 downto 0)     |             |
## Instantiations

- cpt_en: work.cvb_cpt_en
- check_mean: work.cvb_check_mean
**Description**
check if input frame respect condition

- dual_ram: work.cvb_dual_ram
- gen_new_flow: work.cvb_gen_new_flow
**Description**
regen a data flow

