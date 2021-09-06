# Entity: xcorr_prn_slow_complex_mux

- **File**: xcorr_prn_slow_complex_mux.vhd
## Diagram

![Diagram](xcorr_prn_slow_complex_mux.svg "Diagram")
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| NB_BLK       | natural | 8     |             |
| IN_SIZE      | natural | 16    |             |
| OUT_SIZE     | natural | 32    |             |
## Ports

| Port name     | Direction | Type                                  | Description |
| ------------- | --------- | ------------------------------------- | ----------- |
| clk           | in        | std_logic                             |             |
| reset         | in        | std_logic                             |             |
| clear_accum_i | in        | std_logic                             |             |
| data_en_i     | in        | std_logic                             | input       |
| data_ready_i  | in        | std_logic_vector(NB_BLK-1 downto 0)   |             |
| end_cross_i   | in        | std_logic_vector(NB_BLK-1 downto 0)   |             |
| data_i_i      | in        | std_logic_vector(IN_SIZE-1 downto 0)  |             |
| data_q_i      | in        | std_logic_vector(IN_SIZE-1 downto 0)  |             |
| prn_i         | in        | std_logic_vector(NB_BLK-1 downto 0)   |             |
| data_en_o     | out       | std_logic                             | output      |
| data_i_o      | out       | std_logic_vector(OUT_SIZE-1 downto 0) |             |
| data_q_o      | out       | std_logic_vector(OUT_SIZE-1 downto 0) |             |
## Signals

| Name             | Type                                  | Description |
| ---------------- | ------------------------------------- | ----------- |
| accum_next_i_s   | std_logic_vector(OUT_SIZE-1 downto 0) |  accum      |
|  accum_next_q_s  | std_logic_vector(OUT_SIZE-1 downto 0) |  accum      |
| accum_i_s        | std_logic_vector(OUT_SIZE-1 downto 0) |             |
|  accum_q_s       | std_logic_vector(OUT_SIZE-1 downto 0) |             |
| accum_mux_i_s    | std_logic_vector(OUT_SIZE-1 downto 0) |             |
|  accum_mux_q_s   | std_logic_vector(OUT_SIZE-1 downto 0) |             |
| ext_rst_s        | std_logic_vector(NB_BLK-1 downto 0)   |             |
|  ext_rst_next_s  | std_logic_vector(NB_BLK-1 downto 0)   |             |
| clear_accum_s    | std_logic                             |             |
| data_end_i_s     | std_logic                             |  end        |
|  data_end_q_s    | std_logic                             |  end        |
| prn_s            | std_logic_vector(NB_BLK-1 downto 0)   |             |
| prn2_s           | std_logic                             |             |
|  prn2_next_s     | std_logic                             |             |
| wr_addr_s        | std_logic_vector(CPT_SZ-1 downto 0)   |  new        |
|  rd_addr_s       | std_logic_vector(CPT_SZ-1 downto 0)   |  new        |
| prn_addr_s       | std_logic_vector(CPT_SZ-1 downto 0)   |             |
| mux_prn_s        | std_logic                             |             |
| mux_data_ready_s | std_logic                             |             |
| mux_end_cross_s  | std_logic                             |             |
| data_i_s         | std_logic_vector(OUT_SIZE-1 downto 0) |             |
|  data_q_s        | std_logic_vector(OUT_SIZE-1 downto 0) |             |
| wr_en_i_s        | std_logic                             |             |
|  wr_en_q_s       | std_logic                             |             |
| data_en_s        | std_logic                             |  new new    |
| compute_en_s     | std_logic                             |             |
| global_end_s     | std_logic                             |             |
| ram_wr_data_i_s  | std_logic_vector(OUT_SIZE-1 downto 0) |             |
|  ram_wr_data_q_s | std_logic_vector(OUT_SIZE-1 downto 0) |             |
| data_in_i_s      | std_logic_vector(IN_SIZE-1 downto 0)  |             |
|  data_in_q_s     | std_logic_vector(IN_SIZE-1 downto 0)  |             |
| data_in_i_pos_s  | std_logic_vector(IN_SIZE-1 downto 0)  |             |
|  data_in_i_neg_s | std_logic_vector(IN_SIZE-1 downto 0)  |             |
| data_in_q_pos_s  | std_logic_vector(IN_SIZE-1 downto 0)  |             |
|  data_in_q_neg_s | std_logic_vector(IN_SIZE-1 downto 0)  |             |
| delay_en_s       | std_logic                             |             |
## Constants

| Name     | Type             | Value                              | Description |
| -------- | ---------------- | ---------------------------------- | ----------- |
| ALL_ZERO | std_logic_vector |  (NB_BLK -1 downto 0 => '0')       |             |
| CPT_SZ   | natural          |  natural(ceil(log2(real(NB_BLK)))) |             |
## Processes
- unnamed: ( clk )
- unnamed: ( ext_rst_s, wr_addr_s )
- unnamed: ( clk )
- unnamed: ( clk )
- unnamed: ( clk )
- unnamed: ( clk )
- unnamed: ( clk )
</br>**Description**
 compteur d'adresse pour la RAM  wr est en retard d'une valeur sur read pour precharger  la sortie alors que le wr est en direct  le wr est également utilise pour le mux sur les infos en entrees 
- unnamed: ( clk )
## Instantiations

- correl_i_inst: work.xcorr_prn_slow_complex_correl
- correl_q_inst: work.xcorr_prn_slow_complex_correl
- ram_i_inst: work.xcorr_prn_slow_complex_ram
- ram_q_inst: work.xcorr_prn_slow_complex_ram
