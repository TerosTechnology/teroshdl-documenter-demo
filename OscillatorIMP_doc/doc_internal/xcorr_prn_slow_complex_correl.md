# Entity: xcorr_prn_slow_complex_correl

- **File**: xcorr_prn_slow_complex_correl.vhd
## Diagram

![Diagram](xcorr_prn_slow_complex_correl.svg "Diagram")
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| IN_SIZE      | natural | 16    |             |
| OUT_SIZE     | natural | 32    |             |
## Ports

| Port name   | Direction | Type                                  | Description |
| ----------- | --------- | ------------------------------------- | ----------- |
| end_cross_i | in        | std_logic                             | input       |
| data_en_i   | in        | std_logic                             |             |
| accum_i     | in        | std_logic_vector(OUT_SIZE-1 downto 0) |             |
| data_pos_i  | in        | std_logic_vector(IN_SIZE-1 downto 0)  |             |
| data_neg_i  | in        | std_logic_vector(IN_SIZE-1 downto 0)  |             |
| prn_i       | in        | std_logic                             |             |
| data_en_o   | out       | std_logic                             | output      |
| data_end_o  | out       | std_logic                             |             |
| data_o      | out       | std_logic_vector(OUT_SIZE-1 downto 0) |             |
## Signals

| Name       | Type                       | Description |
| ---------- | -------------------------- | ----------- |
| val_sub_s  | signed(IN_SIZE-1 downto 0) |             |
|  val_add_s | signed(IN_SIZE-1 downto 0) |             |
|  val_s     | signed(IN_SIZE-1 downto 0) |             |
