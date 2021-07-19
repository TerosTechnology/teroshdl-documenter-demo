# Entity: gen_radar_prog_logic

- **File**: gen_radar_prog_logic.vhd
## Diagram

![Diagram](gen_radar_prog_logic.svg "Diagram")
## Description

(c) Copyright: OscillatorIMP Digital
Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
2013-2018
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| DATA_SIZE    | natural | 16    |             |
| BURST_SIZE   | natural | 1024  |             |
## Ports

| Port name      | Direction | Type                                   | Description    |
| -------------- | --------- | -------------------------------------- | -------------- |
| clk            | in        | std_logic                              | Syscon signals |
| reset          | in        | std_logic                              |                |
| switch_o       | out       | std_logic                              |                |
| switchn_o      | out       | std_logic                              |                |
| rxoff_i        | in        | std_logic_vector(15 downto 0)          | axi            |
| txon_i         | in        | std_logic_vector(15 downto 0)          |                |
| point_period_i | in        | std_logic_vector(15 downto 0)          |                |
| data_i_i       | in        | std_logic_vector(DATA_SIZE-1 downto 0) |                |
| data_q_i       | in        | std_logic_vector(DATA_SIZE-1 downto 0) |                |
| data_en_i      | in        | std_logic                              |                |
| data_i_o       | out       | std_logic_vector(DATA_SIZE-1 downto 0) |                |
| data_q_o       | out       | std_logic_vector(DATA_SIZE-1 downto 0) |                |
| data_en_o      | out       | std_logic                              |                |
| data_eof_o     | out       | std_logic                              |                |
## Signals

| Name             | Type                                   | Description |
| ---------------- | -------------------------------------- | ----------- |
| switch_time      | integer range 0 to 2**16-1             |             |
| switch_rxoff     | integer range 0 to 2**16-1             |             |
| switch_rxtx      | integer range 0 to 2**16-1             |             |
| ct               | natural range 0 to 2**16-1             |             |
| switch_s         | std_logic                              |             |
| switch_tx        | std_logic                              |             |
| point_per_nat_s  | natural range 0 to 2**16-1             |             |
| data_i_s         | std_logic_vector(DATA_SIZE-1 downto 0) |             |
|  data_q_s        | std_logic_vector(DATA_SIZE-1 downto 0) |             |
| data_en_s        | std_logic                              |             |
| cpt_s            | natural range 0 to 2**16-1             |             |
|  cpt_next_s      | natural range 0 to 2**16-1             |             |
| restart_switch_s | std_logic                              |             |
## Processes
- unnamed: ( clk, reset )
- unnamed: ( clk, reset )
- unnamed: ( clk, reset )
