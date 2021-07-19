# Entity: shifterComplex

- **File**: shifterComplex.vhd
## Diagram

![Diagram](shifterComplex.svg "Diagram")
## Description

(c) Copyright: OscillatorIMP Digital
Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
Creation date : 2014/08/01
## Generics

| Generic name  | Type    | Value | Description |
| ------------- | ------- | ----- | ----------- |
| DATA_IN_SIZE  | natural | 32    |             |
| DATA_OUT_SIZE | natural | 16    |             |
## Ports

| Port name  | Direction | Type                                       | Description            |
| ---------- | --------- | ------------------------------------------ | ---------------------- |
| data_i_i   | in        | std_logic_vector(DATA_IN_SIZE-1 downto 0)  | input data             |
| data_q_i   | in        | std_logic_vector(DATA_IN_SIZE-1 downto 0)  |                        |
| data_en_i  | in        | std_logic                                  |                        |
| data_eof_i | in        | std_logic                                  |                        |
| data_clk_i | in        | std_logic                                  |                        |
| data_rst_i | in        | std_logic                                  |                        |
| data_q_o   | out       | std_logic_vector(DATA_OUT_SIZE-1 downto 0) | for the next component |
| data_i_o   | out       | std_logic_vector(DATA_OUT_SIZE-1 downto 0) |                        |
| data_en_o  | out       | std_logic                                  |                        |
| data_eof_o | out       | std_logic                                  |                        |
| data_rst_o | out       | std_logic                                  |                        |
| data_clk_o | out       | std_logic                                  |                        |
## Signals

| Name           | Type                                       | Description |
| -------------- | ------------------------------------------ | ----------- |
| data_i_s       | std_logic_vector(DATA_OUT_SIZE-1 downto 0) |             |
|  data_q_s      | std_logic_vector(DATA_OUT_SIZE-1 downto 0) |             |
| data_i_next_s  | std_logic_vector(DATA_OUT_SIZE-1 downto 0) |             |
|  data_q_next_s | std_logic_vector(DATA_OUT_SIZE-1 downto 0) |             |
## Processes
- unnamed: ( data_clk_i )
