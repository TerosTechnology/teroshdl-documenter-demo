# Entity: xcorr_prn_slow_complex

## Diagram

![Diagram](xcorr_prn_slow_complex.svg "Diagram")
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| NB_BLK       | natural | 25    |             |
| LENGTH       | natural | 1023  |             |
| IN_SIZE      | natural | 16    |             |
| OUT_SIZE     | natural | 32    |             |
## Ports

| Port name  | Direction | Type                                  | Description |
| ---------- | --------- | ------------------------------------- | ----------- |
| ext_rst_i  | in        | std_logic                             |             |
| data_clk_i | in        | std_logic                             | data in     |
| data_rst_i | in        | std_logic                             |             |
| data_en_i  | in        | std_logic                             |             |
| data_i_i   | in        | std_logic_vector(IN_SIZE-1 downto 0)  |             |
| data_q_i   | in        | std_logic_vector(IN_SIZE-1 downto 0)  |             |
| prn_i      | in        | std_logic                             | prn in      |
| prn_sync_o | out       | std_logic                             |             |
| data_en_o  | out       | std_logic                             | data out    |
| data_i_o   | out       | std_logic_vector(OUT_SIZE-1 downto 0) |             |
| data_q_o   | out       | std_logic_vector(OUT_SIZE-1 downto 0) |             |
| data_clk_o | out       | std_logic                             |             |
| data_rst_o | out       | std_logic                             |             |
## Signals

| Name              | Type                                  | Description |
| ----------------- | ------------------------------------- | ----------- |
| delay_s           | std_logic_vector(LENGTH-1 downto 0)   | control     |
|  delay_next_s     | std_logic_vector(LENGTH-1 downto 0)   | control     |
| delay2_s          | std_logic_vector(LENGTH-1 downto 0)   |             |
| prn_s             | std_logic_vector(LENGTH-1 downto 0)   |             |
|  prn_next_s       | std_logic_vector(LENGTH-1 downto 0)   |             |
| prn2_s            | std_logic_vector(LENGTH-1 downto 0)   |             |
| cpt_s             | unsigned(CPT_SIZE-1 downto 0)         |             |
|  cpt_next_s       | unsigned(CPT_SIZE-1 downto 0)         |             |
| delay_end_s       | std_logic_vector(LENGTH-1 downto 0)   |             |
|  delay_end_next_s | std_logic_vector(LENGTH-1 downto 0)   |             |
| delay2_end_s      | std_logic_vector(LENGTH-1 downto 0)   |             |
| end_cross_s       | std_logic                             |             |
| data_en_s         | std_logic_vector(NB_BLK downto 0)     | xcorr       |
| data_i_s          | data_tab(NB_BLK downto 0)             |             |
|  data_q_s         | data_tab(NB_BLK downto 0)             |             |
| cpt_store_s       | unsigned(CPT_SIZE-1 downto 0)         | last        |
|  cpt_store_next_s | unsigned(CPT_SIZE-1 downto 0)         | last        |
| data_en_next      | std_logic                             |             |
| data_out_i_next_s | std_logic_vector(OUT_SIZE-1 downto 0) |             |
|  data_out_i_s     | std_logic_vector(OUT_SIZE-1 downto 0) |             |
| data_out_q_next_s | std_logic_vector(OUT_SIZE-1 downto 0) |             |
|  data_out_q_s     | std_logic_vector(OUT_SIZE-1 downto 0) |             |
| prn_in_s          | std_logic                             |             |
| data_in_i_s       | std_logic_vector(IN_SIZE-1 downto 0)  |             |
|  data_in_q_s      | std_logic_vector(IN_SIZE-1 downto 0)  |             |
| data_in_en_s      | std_logic                             |             |
## Constants

| Name     | Type                              | Value                              | Description |
| -------- | --------------------------------- | ---------------------------------- | ----------- |
| V1       | natural                           |  LENGTH/NB_BLK                     |             |
| V2       | natural                           |  LENGTH - (V1 * NB_BLK)            |             |
| ALL_ZERO | std_logic_vector(NB_BLK downto 0) |  (others => '0')                   |             |
| CPT_SIZE | natural                           |  natural(ceil(log2(real(LENGTH)))) | cpt         |
## Types

| Name     | Type                                                               | Description |
| -------- | ------------------------------------------------------------------ | ----------- |
| data_tab | array (natural range <>) of std_logic_vector(OUT_SIZE-1 downto 0)  |             |
## Processes
- unnamed: ( data_clk_i )
- unnamed: ( data_clk_i )
- unnamed: ( data_clk_i )
- unnamed: ( data_clk_i )
- unnamed: ( data_out_i_s, data_i_s, data_en_s )
- unnamed: ( data_out_q_s, data_q_s, data_en_s )
- unnamed: ( data_clk_i )
- unnamed: ( data_clk_i )
## Instantiations

- xcorr_last_inst: work.xcorr_prn_slow_complex_mux
