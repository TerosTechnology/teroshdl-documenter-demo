# Entity: shifterReal_dyn_logic

## Diagram

![Diagram](shifterReal_dyn_logic.svg "Diagram")
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
| data_i      | in        | std_logic_vector(DATA_IN_SIZE-1 downto 0)  | input data             |
| data_en_i   | in        | std_logic                                  |                        |
| data_eof_i  | in        | std_logic                                  |                        |
| data_sof_i  | in        | std_logic                                  |                        |
| data_o      | out       | std_logic_vector(DATA_OUT_SIZE-1 downto 0) | for the next component |
| data_en_o   | out       | std_logic                                  |                        |
| data_eof_o  | out       | std_logic                                  |                        |
| data_sof_o  | out       | std_logic                                  |                        |
## Signals

| Name                 | Type                                       | Description |
| -------------------- | ------------------------------------------ | ----------- |
| data_s               | std_logic_vector(DATA_OUT_SIZE-1 downto 0) |             |
| data_in_s            | std_logic_vector(DATA_OUT_SIZE-1 downto 0) |             |
| data_en_s            | std_logic                                  |             |
| data_eof_s           | std_logic                                  |             |
| data_sof_s           | std_logic                                  |             |
| array_val            | mux_array                                  |             |
| rest_is_zero_s       | boolean                                    |             |
| rest_is_zero_next_s  | boolean                                    |             |
| array_rest_is_zero_s | rest_array                                 |             |
| neg_val_s            | boolean                                    |             |
|  neg_val_next_s      | boolean                                    |             |
## Types

| Name       | Type | Description |
| ---------- | ---- | ----------- |
| mux_array  |      |             |
| rest_array |      |             |
## Processes
- unnamed: ( clk_i )
**Description**
store data before shift

