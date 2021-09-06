# Entity: dupplComplex_1_to_2

- **File**: dupplComplex_1_to_2.vhd
## Diagram

![Diagram](dupplComplex_1_to_2.svg "Diagram")
## Description

-------------------------------------------------------------------------
 (c) Copyright: OscillatorIMP Digital
 Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
 Creation date : 2014/10/14
-------------------------------------------------------------------------
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| DATA_SIZE    | natural | 8     |             |
## Ports

| Port name   | Direction | Type                                   | Description |
| ----------- | --------- | -------------------------------------- | ----------- |
| data_en_i   | in        | std_logic                              | DATA in     |
| data_clk_i  | in        | std_logic                              |             |
| data_rst_i  | in        | std_logic                              |             |
| data_eof_i  | in        | std_logic                              |             |
| data_i_i    | in        | std_logic_vector(DATA_SIZE-1 downto 0) |             |
| data_q_i    | in        | std_logic_vector(DATA_SIZE-1 downto 0) |             |
| data1_en_o  | out       | std_logic                              | next        |
| data1_clk_o | out       | std_logic                              |             |
| data1_rst_o | out       | std_logic                              |             |
| data1_eof_o | out       | std_logic                              |             |
| data1_i_o   | out       | std_logic_vector(DATA_SIZE-1 downto 0) |             |
| data1_q_o   | out       | std_logic_vector(DATA_SIZE-1 downto 0) |             |
| data2_en_o  | out       | std_logic                              |             |
| data2_clk_o | out       | std_logic                              |             |
| data2_rst_o | out       | std_logic                              |             |
| data2_eof_o | out       | std_logic                              |             |
| data2_i_o   | out       | std_logic_vector(DATA_SIZE-1 downto 0) |             |
| data2_q_o   | out       | std_logic_vector(DATA_SIZE-1 downto 0) |             |
