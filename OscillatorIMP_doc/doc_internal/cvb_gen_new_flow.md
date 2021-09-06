# Entity: cvb_gen_new_flow

- **File**: cvb_gen_new_flow.vhd
## Diagram

![Diagram](cvb_gen_new_flow.svg "Diagram")
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| ADDR         | natural | 1024  |             |
| DATA         | natural | 8     |             |
## Ports

| Port name  | Direction | Type                              | Description |
| ---------- | --------- | --------------------------------- | ----------- |
| clk_i      | in        | std_logic                         |             |
| rst_i      | in        | std_logic                         |             |
| cpt_max_i  | in        | std_logic_vector(ADDR-1 downto 0) | from cpu    |
| start_i    | in        | std_logic                         | start       |
| ram_i_i    | in        | std_logic_vector(DATA-1 downto 0) | ram         |
| ram_q_i    | in        | std_logic_vector(DATA-1 downto 0) |             |
| ram_addr_o | out       | std_logic_vector(ADDR-1 downto 0) |             |
| data_i_o   | out       | std_logic_vector(DATA-1 downto 0) | next        |
| data_q_o   | out       | std_logic_vector(DATA-1 downto 0) |             |
| data_eof_o | out       | std_logic                         |             |
| data_en_o  | out       | std_logic                         |             |
## Signals

| Name            | Type                              | Description   |
| --------------- | --------------------------------- | ------------- |
| ram_addr_s      | std_logic_vector(ADDR-1 downto 0) |               |
| ram_addr_next_s | std_logic_vector(ADDR-1 downto 0) |               |
| data_en_s       | std_logic                         |               |
|  data_en_next_s | std_logic                         |               |
| data_eof_s      | std_logic                         |               |
| busy_s          | std_logic                         |               |
| data_i_s        | std_logic_vector(DATA-1 downto 0) |  propagation  |
| data_q_s        | std_logic_vector(DATA-1 downto 0) |               |
| need_rst_s      | std_logic                         |               |
## Processes
- unnamed: ( clk_i )
</br>**Description**
 used because RAM out is delayed by one cycle 
- unnamed: ( clk_i )
- unnamed: ( clk_i )
- unnamed: ( clk_i )
