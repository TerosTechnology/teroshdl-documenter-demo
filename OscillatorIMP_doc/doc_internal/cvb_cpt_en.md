# Entity: cvb_cpt_en

- **File**: cvb_cpt_en.vhd
## Diagram

![Diagram](cvb_cpt_en.svg "Diagram")
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| DATA         | integer | 72    |             |
| ADDR         | integer | 10    |             |
## Ports

| Port name   | Direction | Type                              | Description |
| ----------- | --------- | --------------------------------- | ----------- |
| clk_i       | in        | std_logic                         |             |
| rst_i       | in        | std_logic                         |             |
| data_en_i   | in        | std_logic                         |             |
| data_eof_i  | in        | std_logic                         |             |
| data_en_o   | out       | std_logic                         |             |
| data_eof_o  | out       | std_logic                         |             |
| data_addr_o | out       | std_logic_vector(ADDR-1 downto 0) |             |
## Signals

| Name         | Type                              | Description   |
| ------------ | --------------------------------- | ------------- |
| ready_s      | std_logic                         |               |
| data_en_s    | std_logic                         |               |
| data_eof_s   | std_logic                         |               |
| addr_s       | std_logic_vector(ADDR-1 downto 0) |  counter RAM  |
|  addr_next_s | std_logic_vector(ADDR-1 downto 0) |  counter RAM  |
## Processes
- unnamed: ( clk_i )
- unnamed: ( clk_i )
