# Entity: wb_gen_radar_prog

## Diagram

![Diagram](wb_gen_radar_prog.svg "Diagram")
## Description

(c) Copyright: OscillatorIMP Digital
Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
2013-2018
## Generics

| Generic name | Type    | Value | Description                 |
| ------------ | ------- | ----- | --------------------------- |
| id           | natural | 1     |                             |
| NB_POINT     | natural | 16    |                             |
| RXOFF        | natural | 2     | exprime' en cycle           |
| TXON         | natural | 8     | idem                        |
| wb_size      | natural | 16    | Data port size for wishbone |
## Ports

| Port name      | Direction | Type                                  | Description      |
| -------------- | --------- | ------------------------------------- | ---------------- |
| reset          | in        | std_logic                             | Syscon signals   |
| clk            | in        | std_logic                             |                  |
| wbs_add        | in        | std_logic_vector(1 downto 0)          | Wishbone signals |
| wbs_write      | in        | std_logic                             |                  |
| wbs_writedata  | in        | std_logic_vector( wb_size-1 downto 0) |                  |
| wbs_read       | in        | std_logic                             |                  |
| wbs_readdata   | out       | std_logic_vector( wb_size-1 downto 0) |                  |
| rx_off_o       | out       | std_logic_vector(15 downto 0)         |                  |
| tx_on_o        | out       | std_logic_vector(15 downto 0)         |                  |
| point_period_o | out       | std_logic_vector(15 downto 0)         |                  |
## Signals

| Name        | Type                                 | Description |
| ----------- | ------------------------------------ | ----------- |
| point_pos_s | std_logic_vector(15 downto 0)        |             |
| readdata_s  | std_logic_vector(wb_size-1 downto 0) |             |
| rx_off_s    | std_logic_vector(15 downto 0)        |             |
|  tx_on_s    | std_logic_vector(15 downto 0)        |             |
## Constants

| Name             | Type                         | Value | Description |
| ---------------- | ---------------------------- | ----- | ----------- |
| REG_ID           | std_logic_vector(1 downto 0) |  "00" |             |
| REG_POINT_PERIOD | std_logic_vector(1 downto 0) | "01"  |             |
| REG_RXOFF        | std_logic_vector(1 downto 0) | "10"  |             |
| REG_TXON         | std_logic_vector(1 downto 0) | "11"  |             |
## Processes
- write_bloc: ( clk, reset )
**Description**
manage register

- read_bloc: ( clk, reset )
