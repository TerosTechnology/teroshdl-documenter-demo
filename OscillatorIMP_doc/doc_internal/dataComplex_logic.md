# Entity: dataComplex_to_ram_subtop

## Diagram

![Diagram](dataComplex_logic.svg "Diagram")
## Description

(c) Copyright: OscillatorIMP Digital
Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
Creation date : 2018/11/30
## Generics

| Generic name | Type    | Value    | Description |
| ------------ | ------- | -------- | ----------- |
| USE_EOF      | boolean | true     |             |
| DATA_FORMAT  | string  | "signed" |             |
| NB_SAMPLE    | natural | 1024     |             |
| INPUT_SIZE   | natural | 32       |             |
| DATA_SIZE    | natural | 16       |             |
| AXI_SIZE     | natural | 32       |             |
| SELECT_SZ    | natural | 1        |             |
| ADDR_SIZE    | natural | 12       |             |
## Ports

| Port name     | Direction | Type                                    | Description    |
| ------------- | --------- | --------------------------------------- | -------------- |
| cpu_clk_i     | in        | std_logic                               |                |
| cpu_rst_i     | in        | std_logic                               |                |
| data_clk_i    | in        | std_logic                               | Syscon signals |
| data_rst_i    | in        | std_logic                               |                |
| start_acq_i   |           | std_logic                               |                |
| busy_o        | out       | std_logic                               |                |
| data_o        | out       | std_logic_vector((AXI_SIZE)-1 downto 0) | results        |
| result_addr_i | in        | std_logic_vector(ADDR_SIZE-1 downto 0)  |                |
| select_word_i | in        | std_logic_vector(SELECT_SZ-1 downto 0)  |                |
| data_i_i      | in        | std_logic_vector(INPUT_SIZE-1 downto 0) | in             |
| data_q_i      | in        | std_logic_vector(INPUT_SIZE-1 downto 0) |                |
| data_en_i     | in        | std_logic                               |                |
| data_eof_i    | in        | std_logic                               |                |
## Signals

| Name         | Type                                   | Description                      |
| ------------ | -------------------------------------- | -------------------------------- |
| start_acq2_s | std_logic                              |                                  |
| start_acq4_s | std_logic                              |                                  |
|  start_acq_s | std_logic                              |                                  |
| busy_s       | std_logic                              |                                  |
|  busy_sync_s | std_logic                              |                                  |
| data_s       | std_logic_vector(RAM_SIZE-1 downto 0)  | ram writedata resized and merged |
| data_en_s    | std_logic                              |                                  |
|  must_stop_s | std_logic                              |                                  |
| sample_cpt_s | std_logic_vector(ADDR_SIZE-1 downto 0) |                                  |
| ram_data_s   | std_logic_vector(RAM_SIZE-1 downto 0)  | ram read                         |
| array_val    | mux_array                              |                                  |
## Constants

| Name     | Type    | Value         | Description |
| -------- | ------- | ------------- | ----------- |
| RAM_SIZE | natural |  2*DATA_SIZE  |             |
| NB_PKT   | natural |  2**SELECT_SZ |             |
## Types

| Name      | Type | Description |
| --------- | ---- | ----------- |
| mux_array |      |             |
## Processes
- unnamed: ( cpu_clk_i )
- unnamed: ( data_clk_i )
- unnamed: ( data_clk_i )
## Instantiations

- data_resizer: work.dataComplex_resizer
- busy_sync: work.dataComplex_sync
- sync_start: work.dataComplex_sync
- ram_msb: work.dataComplex_to_ram_storage
**Description**
RAM --

