# Entity: syncTrigStream_logic

- **File**: syncTrigStream_logic.vhd
## Diagram

![Diagram](syncTrigStream_logic.svg "Diagram")
## Description

(c) Copyright: OscillatorIMP Digital
Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
2013-2018
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| USE_EXT_TRIG | boolean | false |             |
| GEN_SIZE     | natural | 32    |             |
| DATA_SIZE    | natural | 16    |             |
| NB_SAMPLE    | natural | 1024  |             |
## Ports

| Port name    | Direction | Type                                   | Description    |
| ------------ | --------- | -------------------------------------- | -------------- |
| clk          | in        | std_logic                              | Syscon signals |
| reset        | in        | std_logic                              |                |
| ext_trig_i   | in        | std_logic                              | pulse          |
| pulse_o      | out       | std_logic                              |                |
| duty_cnt_i   | in        | std_logic_vector(GEN_SIZE-1 downto 0)  | axi            |
| period_cnt_i | in        | std_logic_vector(GEN_SIZE-1 downto 0)  |                |
| enable_i     | in        | std_logic                              |                |
| data_en_i    | in        | std_logic                              |                |
| data1_i_i    | in        | std_logic_vector(DATA_SIZE-1 downto 0) |                |
| data1_q_i    | in        | std_logic_vector(DATA_SIZE-1 downto 0) |                |
| data2_i_i    | in        | std_logic_vector(DATA_SIZE-1 downto 0) |                |
| data2_q_i    | in        | std_logic_vector(DATA_SIZE-1 downto 0) |                |
| data1_i_o    | out       | std_logic_vector(DATA_SIZE-1 downto 0) |                |
| data1_q_o    | out       | std_logic_vector(DATA_SIZE-1 downto 0) |                |
| data2_i_o    | out       | std_logic_vector(DATA_SIZE-1 downto 0) |                |
| data2_q_o    | out       | std_logic_vector(DATA_SIZE-1 downto 0) |                |
| data_en_o    | out       | std_logic                              |                |
| data_sof_o   | out       | std_logic                              |                |
| data_eof_o   | out       | std_logic                              |                |
## Signals

| Name            | Type                                   | Description |
| --------------- | -------------------------------------- | ----------- |
| pulse_counter_s | unsigned(GEN_SIZE-1 downto 0)          |             |
| pulse_s         | std_logic                              |             |
| pulse_d0_s      | std_logic                              |             |
| pulse_d1_s      | std_logic                              |             |
| restart_cnt     | boolean                                |             |
| start_tx_s      | std_logic                              |             |
| end_tx_s        | boolean                                |             |
| cpt_data_s      | unsigned(CPT_SIZE-1 downto 0)          |             |
| busy_s          | std_logic                              |             |
| data1_i_s       | std_logic_vector(DATA_SIZE-1 downto 0) |             |
|  data1_q_s      | std_logic_vector(DATA_SIZE-1 downto 0) |             |
| data2_i_s       | std_logic_vector(DATA_SIZE-1 downto 0) |             |
|  data2_q_s      | std_logic_vector(DATA_SIZE-1 downto 0) |             |
## Constants

| Name     | Type    | Value                                 | Description |
| -------- | ------- | ------------------------------------- | ----------- |
| CPT_SIZE | natural |  natural(ceil(log2(real(NB_SAMPLE)))) |             |
## Processes
- unnamed: ( clk )
- unnamed: ( clk )
- unnamed: ( clk )
