# Entity: shifterReal

- **File**: shifterReal.vhd
## Diagram

![Diagram](shifterReal.svg "Diagram")
## Description

(c) Copyright: OscillatorIMP Digital
Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
2013-2018
## Generics

| Generic name  | Type    | Value | Description |
| ------------- | ------- | ----- | ----------- |
| DATA_IN_SIZE  | natural | 32    |             |
| DATA_OUT_SIZE | natural | 16    |             |
## Ports

| Port name  | Direction | Type                                       | Description            |
| ---------- | --------- | ------------------------------------------ | ---------------------- |
| data_i     | in        | std_logic_vector(DATA_IN_SIZE-1 downto 0)  | input data             |
| data_en_i  | in        | std_logic                                  |                        |
| data_eof_i | in        | std_logic                                  |                        |
| data_clk_i | in        | std_logic                                  |                        |
| data_rst_i | in        | std_logic                                  |                        |
| data_o     | out       | std_logic_vector(DATA_OUT_SIZE-1 downto 0) | for the next component |
| data_en_o  | out       | std_logic                                  |                        |
| data_eof_o | out       | std_logic                                  |                        |
| data_rst_o | out       | std_logic                                  |                        |
| data_clk_o | out       | std_logic                                  |                        |
## Signals

| Name         | Type                                       | Description |
| ------------ | ------------------------------------------ | ----------- |
| data_s       | std_logic_vector(DATA_OUT_SIZE-1 downto 0) |             |
|  data_next_s | std_logic_vector(DATA_OUT_SIZE-1 downto 0) |             |
## Processes
- unnamed: ( data_clk_i )
