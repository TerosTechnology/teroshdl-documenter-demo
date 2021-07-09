# Entity: expanderComplex

## Diagram

![Diagram](expanderComplex.svg "Diagram")
## Description

(c) Copyright: OscillatorIMP Digital
Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
Creation date : 2017/05/27
## Generics

| Generic name  | Type    | Value    | Description |
| ------------- | ------- | -------- | ----------- |
| format        | string  | "signed" |             |
| DATA_IN_SIZE  | natural | 16       |             |
| DATA_OUT_SIZE | natural | 16       |             |
## Ports

| Port name  | Direction | Type                                       | Description            |
| ---------- | --------- | ------------------------------------------ | ---------------------- |
| data_i_i   | in        | std_logic_vector(DATA_IN_SIZE-1 downto 0)  | input data             |
| data_q_i   | in        | std_logic_vector(DATA_IN_SIZE-1 downto 0)  |                        |
| data_en_i  | in        | std_logic                                  |                        |
| data_sof_i | in        | std_logic                                  |                        |
| data_eof_i | in        | std_logic                                  |                        |
| data_rst_i | in        | std_logic                                  |                        |
| data_clk_i | in        | std_logic                                  |                        |
| data_i_o   | out       | std_logic_vector(DATA_OUT_SIZE-1 downto 0) | for the next component |
| data_q_o   | out       | std_logic_vector(DATA_OUT_SIZE-1 downto 0) |                        |
| data_en_o  | out       | std_logic                                  |                        |
| data_sof_o | out       | std_logic                                  |                        |
| data_eof_o | out       | std_logic                                  |                        |
| data_rst_o | out       | std_logic                                  |                        |
| data_clk_o | out       | std_logic                                  |                        |
