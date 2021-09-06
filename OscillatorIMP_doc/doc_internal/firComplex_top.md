# Entity: firComplex_top

- **File**: firComplex_top.vhd
## Diagram

![Diagram](firComplex_top.svg "Diagram")
## Generics

| Generic name    | Type    | Value    | Description |
| --------------- | ------- | -------- | ----------- |
| coeff_format    | string  | "signed" |             |
| NB_COEFF        | natural | 128      |             |
| DECIMATE_FACTOR | natural | 32       |             |
| COEFF_SIZE      | natural | 16       |             |
| COEFF_ADDR_SZ   | natural | 10       |             |
| DATA_SIZE       | natural | 16       |             |
| DATA_OUT_SIZE   | natural | 32       |             |
## Ports

| Port name       | Direction | Type                                       | Description            |
| --------------- | --------- | ------------------------------------------ | ---------------------- |
| reset           | in        | std_logic                                  | Syscon signals         |
| clk             | in        | std_logic                                  |                        |
| clk_axi         | in        | std_logic                                  |                        |
| wr_coeff_en_i   | in        | std_logic                                  | coeff configuration    |
| wr_coeff_addr_i | in        | std_logic_vector(COEFF_ADDR_SZ-1 downto 0) |                        |
| wr_coeff_val_i  | in        | std_logic_vector(COEFF_SIZE-1 downto 0)    |                        |
| rd_coeff_val_o  | out       | std_logic_vector(COEFF_SIZE-1 downto 0)    |                        |
| data_en_i       | in        | std_logic                                  | input data             |
| data_i_i        | in        | std_logic_vector(DATA_SIZE-1 downto 0)     |                        |
| data_q_i        | in        | std_logic_vector(DATA_SIZE-1 downto 0)     |                        |
| data_i_o        | out       | std_logic_vector(DATA_OUT_SIZE-1 downto 0) | for the next component |
| data_q_o        | out       | std_logic_vector(DATA_OUT_SIZE-1 downto 0) |                        |
| data_en_o       | out       | std_logic                                  |                        |
## Signals

| Name               | Type                                       | Description |
| ------------------ | ------------------------------------------ | ----------- |
| ready_s            | std_logic_vector(READY_SZ-1 downto 0)      |             |
|  ready_next_s      | std_logic_vector(READY_SZ-1 downto 0)      |             |
| end_macc_s         | std_logic                                  |             |
| end_s              | std_logic_vector(READY_SZ-1 downto 0)      |             |
|  end_next_s        | std_logic_vector(READY_SZ-1 downto 0)      |             |
| cpt_s              | natural range 0 to READY_SZ-1              |             |
| cpt_next_s         | natural range 0 to READY_SZ-1              |             |
|  mux_cpt_s         | natural range 0 to READY_SZ-1              |             |
| rst_cpt_s          | std_logic                                  |             |
| rd_coeff_addr_s    | std_logic_vector(COEFF_ADDR_SZ-1 downto 0) |             |
| coeff_s            | std_logic_vector(COEFF_SIZE-1 downto 0)    |             |
| coeff_tab_s        | coeff_tab(READY_SZ-1 downto 0)             |             |
|  coeff_tab_next_s  | coeff_tab(READY_SZ-1 downto 0)             |             |
| coeff2_tab_s       | coeff_tab(READY_SZ-1 downto 0)             |             |
| data_in_en_s       | std_logic                                  |             |
| data_i_in_s        | std_logic_vector(DATA_SIZE-1 downto 0)     |             |
|  data_q_in_s       | std_logic_vector(DATA_SIZE-1 downto 0)     |             |
| end_delay_macc_s   | std_logic                                  |             |
| cpt_store_s        | natural range 0 to NB_THREAD-1             |  last       |
|  cpt_store_next_s  | natural range 0 to NB_THREAD-1             |  last       |
| clr_cpt_store_s    | std_logic                                  |             |
| data_i_out_s       | std_logic_vector(DATA_OUT_SIZE-1 downto 0) |             |
|  data_i_out_next_s | std_logic_vector(DATA_OUT_SIZE-1 downto 0) |             |
| data_q_out_s       | std_logic_vector(DATA_OUT_SIZE-1 downto 0) |             |
|  data_q_out_next_s | std_logic_vector(DATA_OUT_SIZE-1 downto 0) |             |
| data_i_s           | data_tab(NB_THREAD-1 downto 0)             |             |
|  data_q_s          | data_tab(NB_THREAD-1 downto 0)             |             |
| data_en_s          | std_logic_vector(NB_THREAD-1 downto 0)     |             |
| data_en_next       | std_logic                                  |             |
## Constants

| Name      | Type    | Value                                                         | Description |
| --------- | ------- | ------------------------------------------------------------- | ----------- |
| NB_THREAD | natural |  			natural(ceil(real(real(NB_COEFF)/real(DECIMATE_FACTOR)))) |             |
| READY_SZ  | natural |  NB_THREAD * DECIMATE_FACTOR                                  |             |
## Types

| Name      | Type                                                                    | Description |
| --------- | ----------------------------------------------------------------------- | ----------- |
| data_tab  | array (natural range <>) of std_logic_vector(DATA_OUT_SIZE-1 downto 0)  |             |
| coeff_tab | array (natural range <>) of std_logic_vector(COEFF_SIZE-1 downto 0)     |             |
## Processes
- unnamed: ( clk )
- unnamed: ( clk )
- unnamed: ( clk )
- unnamed: ( clk )
## Instantiations

- ram_coeff: work.firComplex_ram
