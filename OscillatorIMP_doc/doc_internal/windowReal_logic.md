# Entity: windowReal_logic

- **File**: windowReal_logic.vhd
## Diagram

![Diagram](windowReal_logic.svg "Diagram")
## Generics

| Generic name    | Type    | Value | Description |
| --------------- | ------- | ----- | ----------- |
| DATA_SIZE       | natural | 32    |             |
| COEFF_ADDR_SIZE | natural | 8     |             |
| SHIFT           | natural | 16    |             |
| COEFF_SIZE      | natural | 16    |             |
## Ports

| Port name    | Direction | Type                                         | Description |
| ------------ | --------- | -------------------------------------------- | ----------- |
| clk_i        | in        | std_logic                                    |             |
| cpu_clk_i    | in        | std_logic                                    |             |
| reset        | in        | std_logic                                    |             |
| data_en_i    | in        | std_logic                                    | input       |
| data_i       | in        | std_logic_vector(DATA_SIZE-1 downto 0)       |             |
| data_en_o    | out       | std_logic                                    | output      |
| data_eof_o   | out       | std_logic                                    |             |
| data_o       | out       | std_logic_vector(DATA_SIZE-1 downto 0)       |             |
| coeff_en_i   | in        | std_logic                                    | coeff       |
| coeff_addr_i | in        | std_logic_vector(COEFF_ADDR_SIZE-1 downto 0) |             |
| coeff_i      | in        | std_logic_vector(COEFF_SIZE-1 downto 0)      |             |
## Signals

| Name              | Type                                         | Description    |
| ----------------- | -------------------------------------------- | -------------- |
| data_in_s         | std_logic_vector(DATA_SIZE-1 downto 0)       | input latch -- |
| data_in_en_s      | std_logic                                    |                |
| coeff_s           | std_logic_vector(COEFF_SIZE-1 downto 0)      | coeff          |
|  coeff_next_s     | std_logic_vector(COEFF_SIZE-1 downto 0)      | coeff          |
| coeff_addr_s      | std_logic_vector(COEFF_ADDR_SIZE-1 downto 0) |                |
| rst_s             | std_logic                                    | reset          |
| data_s            | std_logic_vector(DATA_SIZE-1 downto 0)       | input latch    |
| data_en_s         | std_logic                                    |                |
| mult_res_s        | std_logic_vector(MULT_SIZE-1 downto 0)       | mult           |
| mult_res_resize_s | std_logic_vector(MULT_RESIZE-1 downto 0)     |                |
| mult_res_scale_s  | std_logic_vector(DATA_SIZE-1 downto 0)       |                |
| data_out_s        | std_logic_vector(DATA_SIZE-1 downto 0)       | output         |
## Constants

| Name        | Type    | Value                 | Description |
| ----------- | ------- | --------------------- | ----------- |
| MULT_SIZE   | natural |  COEFF_SIZE+DATA_SIZE |             |
| MULT_RESIZE | natural |  MULT_SIZE-1          |             |
## Processes
- unnamed: ( clk_i )
- unnamed: ( clk_i )
- unnamed: ( clk_i )
**Description**
update RAM for each new data_en_i

- unnamed: ( clk_i )
- unnamed: ( clk_i )
## Instantiations

- ram1: work.windowReal_ram
