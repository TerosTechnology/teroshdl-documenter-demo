# Entity: convertRealToComplex

- **File**: convertRealToComplex.vhd
## Diagram

![Diagram](convertRealToComplex.svg "Diagram")
## Description

-------------------------------------------------------------------------
 (c) Copyright: OscillatorIMP Digital
 Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
 2015-2018
-------------------------------------------------------------------------
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| DATA_SIZE    | natural | 8     |             |
## Ports

| Port name   | Direction | Type                                   | Description            |
| ----------- | --------- | -------------------------------------- | ---------------------- |
| dataI_i     | in        | std_logic_vector(DATA_SIZE-1 downto 0) | input data             |
| dataI_en_i  | in        | std_logic                              |                        |
| dataI_eof_i | in        | std_logic                              |                        |
| dataI_rst_i | in        | std_logic                              |                        |
| dataI_clk_i | in        | std_logic                              |                        |
| dataQ_i     | in        | std_logic_vector(DATA_SIZE-1 downto 0) |                        |
| dataQ_en_i  | in        | std_logic                              |                        |
| dataQ_rst_i | in        | std_logic                              |                        |
| dataQ_eof_i | in        | std_logic                              |                        |
| dataQ_clk_i | in        | std_logic                              |                        |
| data_i_o    | out       | std_logic_vector(DATA_SIZE-1 downto 0) | for the next component |
| data_q_o    | out       | std_logic_vector(DATA_SIZE-1 downto 0) |                        |
| data_eof_o  | out       | std_logic                              |                        |
| data_rst_o  | out       | std_logic                              |                        |
| data_en_o   | out       | std_logic                              |                        |
| data_clk_o  | out       | std_logic                              |                        |
