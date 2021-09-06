# Entity: multiplierReal

- **File**: multiplierReal.vhd
## Diagram

![Diagram](multiplierReal.svg "Diagram")
## Description

-------------------------------------------------------------------------
 (c) Copyright: OscillatorIMP Digital
 Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
 Creation date : 2020/01/30
## Generics

| Generic name  | Type    | Value | Description |
| ------------- | ------- | ----- | ----------- |
| SIGNED_FORMAT | boolean | true  |             |
| DATA1_IN_SIZE | natural | 16    |             |
| DATA2_IN_SIZE | natural | 16    |             |
| DATA_OUT_SIZE | natural | 2*16  |             |
## Ports

| Port name   | Direction | Type                                       | Description     |
| ----------- | --------- | ------------------------------------------ | --------------- |
| data1_i     | in        | std_logic_vector(DATA1_IN_SIZE-1 downto 0) | data1 interface |
| data1_en_i  | in        | std_logic                                  |                 |
| data1_eof_i | in        | std_logic                                  |                 |
| data1_sof_i | in        | std_logic                                  |                 |
| data1_clk_i | in        | std_logic                                  |                 |
| data1_rst_i | in        | std_logic                                  |                 |
| data2_i     | in        | std_logic_vector(DATA2_IN_SIZE-1 downto 0) | data2 interface |
| data2_en_i  | in        | std_logic                                  |                 |
| data2_eof_i | in        | std_logic                                  |                 |
| data2_sof_i | in        | std_logic                                  |                 |
| data2_clk_i | in        | std_logic                                  |                 |
| data2_rst_i | in        | std_logic                                  |                 |
| data_o      | out       | std_logic_vector(DATA_OUT_SIZE-1 downto 0) | next            |
| data_en_o   | out       | std_logic                                  |                 |
| data_eof_o  | out       | std_logic                                  |                 |
| data_sof_o  | out       | std_logic                                  |                 |
| data_clk_o  | out       | std_logic                                  |                 |
| data_rst_o  | out       | std_logic                                  |                 |
## Signals

| Name            | Type                                       | Description     |
| --------------- | ------------------------------------------ | --------------- |
| data1_in_s      | std_logic_vector(DATA1_IN_SIZE-1 downto 0) |  input latches  |
| data2_in_s      | std_logic_vector(DATA2_IN_SIZE-1 downto 0) |                 |
| data1_in_en_s   | std_logic                                  |                 |
|  data2_in_en_s  | std_logic                                  |                 |
| data1_in_eof_s  | std_logic                                  |                 |
|  data2_in_eof_s | std_logic                                  |                 |
| data1_in_sof_s  | std_logic                                  |                 |
|  data2_in_sof_s | std_logic                                  |                 |
| data_s          | std_logic_vector(INT_DATA_SZ-1 downto 0)   |  mult           |
| data_en_s       | std_logic                                  |                 |
| data_eof_s      | std_logic                                  |                 |
| data_sof_s      | std_logic                                  |                 |
## Constants

| Name        | Type    | Value                          | Description |
| ----------- | ------- | ------------------------------ | ----------- |
| INT_DATA_SZ | natural |  DATA1_IN_SIZE + DATA2_IN_SIZE |             |
## Processes
- unnamed: ( data1_clk_i )
- unnamed: ( data2_clk_i )
## Instantiations

- redim_inst: work.multiplierReal_redim
