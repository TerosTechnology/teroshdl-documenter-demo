# Entity: syncTrigStream_comm

- **File**: syncTrigStream_comm.vhd
## Diagram

![Diagram](syncTrigStream_comm.svg "Diagram")
## Description

(c) Copyright: OscillatorIMP Digital
Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
2013-2018
## Generics

| Generic name | Type    | Value     | Description    |
| ------------ | ------- | --------- | -------------- |
| DFLT_PERIOD  | natural | 300000000 | 3s@100MHz      |
| DFLT_DUTY    | natural | 100       | 1us@100MHz     |
| GEN_SIZE     | natural | 32        |                |
| bus_size     | natural | 32        | Data port size |
## Ports

| Port name    | Direction | Type                                  | Description    |
| ------------ | --------- | ------------------------------------- | -------------- |
| reset        | in        | std_logic                             | Syscon signals |
| clk          | in        | std_logic                             |                |
| addr_i       | in        | std_logic_vector(1 downto 0)          | CPU signals    |
| wr_en_i      | in        | std_logic                             |                |
| writedata_i  | in        | std_logic_vector(bus_size-1 downto 0) |                |
| rd_en_i      | in        | std_logic                             |                |
| readdata_o   | out       | std_logic_vector(bus_size-1 downto 0) |                |
| enable_o     | out       | std_logic                             |                |
| period_cnt_o | out       | std_logic_vector(GEN_SIZE-1 downto 0) |                |
| duty_cnt_o   | out       | std_logic_vector(GEN_SIZE-1 downto 0) |                |
## Signals

| Name         | Type                                  | Description |
| ------------ | ------------------------------------- | ----------- |
| readdata_s   | std_logic_vector(bus_size-1 downto 0) |             |
| enable_s     | std_logic                             |             |
| period_cnt_s | std_logic_vector(GEN_SIZE-1 downto 0) |             |
| duty_cnt_s   | std_logic_vector(GEN_SIZE-1 downto 0) |             |
## Constants

| Name       | Type                         | Value | Description |
| ---------- | ---------------------------- | ----- | ----------- |
| REG_PERIOD | std_logic_vector(1 downto 0) | "00"  |             |
| REG_DUTY   | std_logic_vector(1 downto 0) | "01"  |             |
| REG_ENABLE | std_logic_vector(1 downto 0) | "10"  |             |
## Processes
- write_bloc: ( clk )
**Description**
manage register

- read_bloc: ( clk, reset )
