# Entity: shifterComplex_dyn_logic

## Diagram

![Diagram](shifterComplex_dyn_logic.svg "Diagram")
## Description

(c) Copyright: OscillatorIMP Digital
Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
Creation date : 2016/05/25
## Generics

| Generic name  | Type    | Value | Description |
| ------------- | ------- | ----- | ----------- |
| SIGNED_FORMAT | boolean | true  |             |
| MAX_SHIFT     | natural | 10    |             |
| ADDR_SZ       | natural | 4     |             |
| DATA_IN_SIZE  | natural | 32    |             |
| DATA_OUT_SIZE | natural | 16    |             |
## Ports

| Port name   | Direction | Type                                       | Description            |
| ----------- | --------- | ------------------------------------------ | ---------------------- |
| rst_i       | in        | std_logic                                  |                        |
| clk_i       | in        | std_logic                                  |                        |
| shift_val_i | in        | std_logic_vector(ADDR_SZ-1 downto 0)       |                        |
| data_i_i    | in        | std_logic_vector(DATA_IN_SIZE-1 downto 0)  | input data             |
| data_q_i    | in        | std_logic_vector(DATA_IN_SIZE-1 downto 0)  |                        |
| data_en_i   | in        | std_logic                                  |                        |
| data_eof_i  | in        | std_logic                                  |                        |
| data_sof_i  | in        | std_logic                                  |                        |
| data_q_o    | out       | std_logic_vector(DATA_OUT_SIZE-1 downto 0) | for the next component |
| data_i_o    | out       | std_logic_vector(DATA_OUT_SIZE-1 downto 0) |                        |
| data_en_o   | out       | std_logic                                  |                        |
| data_eof_o  | out       | std_logic                                  |                        |
| data_sof_o  | out       | std_logic                                  |                        |
## Signals

| Name                   | Type                                       | Description |
| ---------------------- | ------------------------------------------ | ----------- |
| data_i_s               | std_logic_vector(DATA_OUT_SIZE-1 downto 0) |             |
|  data_q_s              | std_logic_vector(DATA_OUT_SIZE-1 downto 0) |             |
| data_in_i_s            | std_logic_vector(DATA_OUT_SIZE-1 downto 0) |             |
|  data_in_q_s           | std_logic_vector(DATA_OUT_SIZE-1 downto 0) |             |
| data_en_s              | std_logic                                  |             |
| data_eof_s             | std_logic                                  |             |
| data_sof_s             | std_logic                                  |             |
| array_val_i            | mux_array                                  |             |
| array_val_q            | mux_array                                  |             |
| rest_q_is_zero_s       | boolean                                    |             |
| rest_q_is_zero_next_s  | boolean                                    |             |
| rest_i_is_zero_s       | boolean                                    |             |
| rest_i_is_zero_next_s  | boolean                                    |             |
| array_rest_q_is_zero_s | rest_array                                 |             |
| array_rest_i_is_zero_s | rest_array                                 |             |
| neg_val_i_s            | boolean                                    |             |
|  neg_val_i_next_s      | boolean                                    |             |
| neg_val_q_s            | boolean                                    |             |
|  neg_val_q_next_s      | boolean                                    |             |
## Types

| Name       | Type | Description |
| ---------- | ---- | ----------- |
| mux_array  |      |             |
| rest_array |      |             |
## Processes
- unnamed: ( clk_i )
**Description**
store data before shift

