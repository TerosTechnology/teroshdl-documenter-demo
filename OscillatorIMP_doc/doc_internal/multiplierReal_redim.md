# Entity: multiplierReal_redim

- **File**: multiplierReal_redim.vhd
## Diagram

![Diagram](multiplierReal_redim.svg "Diagram")
## Description

(c) Copyright: OscillatorIMP Digital
Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
Creation date : 2016/09/14
## Generics

| Generic name  | Type    | Value | Description |
| ------------- | ------- | ----- | ----------- |
| SIGNED_FORMAT | boolean | false |             |
| IN_SZ         | natural | 16    |             |
| OUT_SZ        | natural | 16    |             |
## Ports

| Port name  | Direction | Type                                | Description   |
| ---------- | --------- | ----------------------------------- | ------------- |
| clk_i      | in        | std_logic                           | candr         |
| rst_i      | in        | std_logic                           |               |
| data_i     | in        | std_logic_vector(IN_SZ-1 downto 0)  | in interface  |
| data_en_i  | in        | std_logic                           |               |
| data_eof_i | in        | std_logic                           |               |
| data_sof_i | in        | std_logic                           |               |
| data_en_o  | out       | std_logic                           | out interface |
| data_eof_o | out       | std_logic                           |               |
| data_sof_o | out       | std_logic                           |               |
| data_o     | out       | std_logic_vector(OUT_SZ-1 downto 0) |               |
## Signals

| Name            | Type                                | Description |
| --------------- | ----------------------------------- | ----------- |
| data_en_in_s    | std_logic                           |             |
|  data_eof_in_s  | std_logic                           |             |
|  data_sof_in_s  | std_logic                           |             |
| data_in_s       | std_logic_vector(OUT_SZ-1 downto 0) |             |
| d1_s            | std_logic_vector(OUT_SZ-1 downto 0) |             |
| data_en_out_s   | std_logic                           |             |
|  data_eof_out_s | std_logic                           |             |
|  data_sof_out_s | std_logic                           |             |
| data_out_s      | std_logic_vector(OUT_SZ-1 downto 0) |             |
| is_neg_s        | signed(1 downto 0)                  |             |
| is_neg_d0_s     | signed(1 downto 0)                  |             |
| is_null_s       | boolean                             |             |
| is_null_d0_s    | boolean                             |             |
| shft_dat_s      | std_logic_vector(IN_SZ-1 downto 0)  |             |
| shft_dat_q_s    | std_logic_vector(IN_SZ-1 downto 0)  |             |
## Constants

| Name     | Type                                 | Value                                                              | Description |
| -------- | ------------------------------------ | ------------------------------------------------------------------ | ----------- |
| SHFT_SZ  | natural                              |  sub_min_to_max(IN_SZ,<br><span style="padding-left:20px"> OUT_SZ) |             |
| ALL_ZERO | std_logic_vector(SHFT_SZ-1 downto 0) |  (SHFT_SZ-1 downto 0 => '0')                                       |             |
| ALL_ONE  | std_logic_vector(SHFT_SZ-1 downto 0) |  (SHFT_SZ-1 downto 0 => '1')                                       |             |
## Functions
- sub_min_to_max <font id="function_arguments">(size1,<br><span style="padding-left:20px"> size2: natural) </font> <font id="function_return">return natural </font>
## Processes
- unnamed: ( clk_i )
