# Entity: wb_dataComplex_to_ram

- **File**: wb_dataComplex.vhd
## Diagram

![Diagram](wb_dataComplex.svg "Diagram")
## Description

(c) Copyright: OscillatorIMP Digital
Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
Creation date : 2018/11/30
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| wb_size      | natural | 16    |             |
## Ports

| Port name     | Direction | Type                                 | Description    |
| ------------- | --------- | ------------------------------------ | -------------- |
| reset         | in        | std_logic                            | Syscon signals |
| clk           | in        | std_logic                            |                |
| wbs_add       | in        | std_logic_vector(1 downto 0)         | signals        |
| wbs_writedata | in        | std_logic_vector(wb_size-1 downto 0) |                |
| wbs_readdata  | out       | std_logic_vector(wb_size-1 downto 0) |                |
| wbs_read      | in        | std_logic                            |                |
| wbs_read_ack  | out       | std_logic                            |                |
| wbs_write     | in        | std_logic                            |                |
| ram_data_i    | in        | std_logic_vector(wb_size-1 downto 0) | results        |
| ram_incr_o    | out       | std_logic                            |                |
| ram_reinit_o  | out       | std_logic                            |                |
| busy_i        | in        | std_logic                            |                |
| start_o       | out       | std_logic                            |                |
## Signals

| Name       | Type                                 | Description |
| ---------- | ------------------------------------ | ----------- |
| readdata_s | std_logic_vector(wb_size-1 downto 0) |             |
## Constants

| Name      | Type                         | Value | Description |
| --------- | ---------------------------- | ----- | ----------- |
| REG_START | std_logic_vector(1 downto 0) |  "00" |             |
| REG_STAT  | std_logic_vector(1 downto 0) |  "01" |             |
| REG_DATA  | std_logic_vector(1 downto 0) |  "10" |             |
## Processes
- write_bloc: ( clk )
- read_bloc: ( clk )
