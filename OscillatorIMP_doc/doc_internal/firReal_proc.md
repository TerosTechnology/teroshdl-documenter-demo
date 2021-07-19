# Entity: firReal_proc

- **File**: firReal_proc.vhd
## Diagram

![Diagram](firReal_proc.svg "Diagram")
## Description

(c) Copyright: OscillatorIMP Digital
Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
Creation date : 2018/05/26
## Generics

| Generic name  | Type    | Value    | Description |
| ------------- | ------- | -------- | ----------- |
| coeff_format  | string  | "signed" |             |
| NB_COEFF      | natural | 128      |             |
| DATA_SIZE     | natural | 16       |             |
| DATA_OUT_SIZE | natural | 32       |             |
| COEFF_SIZE    | natural | 16       |             |
## Ports

| Port name | Direction | Type                                       | Description    |
| --------- | --------- | ------------------------------------------ | -------------- |
| reset     | in        | std_logic                                  | Syscon signals |
| clk       | in        | std_logic                                  |                |
| ready_i   | in        | std_logic                                  | input data     |
| end_i     | in        | std_logic                                  |                |
| data_i    | in        | std_logic_vector(DATA_SIZE-1 downto 0)     |                |
| coeff_i   | in        | std_logic_vector(COEFF_SIZE-1 downto 0)    |                |
| data_en_i | in        | std_logic                                  |                |
| data_o    | out       | std_logic_vector(DATA_OUT_SIZE-1 downto 0) |                |
| data_en_o | out       | std_logic                                  |                |
## Signals

| Name             | Type                                       | Description |
| ---------------- | ------------------------------------------ | ----------- |
| ready_s          | std_logic                                  |             |
| must_rst_s       | std_logic                                  |             |
| mux_accum_s      | std_logic_vector(INT_SZ-1 downto 0)        |             |
| mult_res         | std_logic_vector(MULT_SZ-1 downto 0)       |             |
| res_s            | std_logic_vector(INT_SZ-1 downto 0)        |             |
|  res_next_s      | std_logic_vector(INT_SZ-1 downto 0)        |             |
| final_res_s      | std_logic_vector(DATA_OUT_SIZE-1 downto 0) |             |
| final_res_next_s | std_logic_vector(DATA_OUT_SIZE-1 downto 0) |             |
| data_en_s        | std_logic                                  |             |
| end_s            | std_logic                                  |             |
| data_s           | std_logic_vector(DATA_SIZE-1 downto 0)     |             |
| data_out_en_s    | std_logic                                  |             |
## Constants

| Name     | Type                                | Value                                          | Description |
| -------- | ----------------------------------- | ---------------------------------------------- | ----------- |
| MULT_SZ  | natural                             |  DATA_SIZE+COEFF_SIZE                          |             |
| INT_SZ   | natural                             |  MULT_SZ + natural(ceil(log2(real(NB_COEFF)))) |             |
| ALL_ZERO | std_logic_vector(INT_SZ-1 downto 0) |  (INT_SZ-1 downto 0 => '0')                    |             |
## Processes
- unnamed: ( clk )
- unnamed: ( clk )
- unnamed: ( clk )
- unnamed: ( clk )
- unnamed: ( clk )
