# Entity: shifterReal_dyn_comm

- **File**: shifterReal_dyn_comm.vhd
## Diagram

![Diagram](shifterReal_dyn_comm.svg "Diagram")
## Description

(c) Copyright: OscillatorIMP Digital
Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
Creation date : 2016/05/25
## Generics

| Generic name  | Type    | Value | Description |
| ------------- | ------- | ----- | ----------- |
| id            | natural | 1     |             |
| wb_size       | natural | 16    |             |
| SHFT_ADDR_SZ  | natural | 4     |             |
| DEFAULT_SHIFT | natural | 16    |             |
## Ports

| Port name   | Direction | Type                                      | Description    |
| ----------- | --------- | ----------------------------------------- | -------------- |
| reset       | in        | std_logic                                 | Syscon signals |
| clk         | in        | std_logic                                 |                |
| addr_i      | in        | std_logic_vector(1 downto 0)              | comm signals   |
| wr_en_i     | in        | std_logic                                 |                |
| writedata_i | in        | std_logic_vector( wb_size-1 downto 0)     |                |
| rd_en_i     | in        | std_logic                                 |                |
| readdata_o  | out       | std_logic_vector( wb_size-1 downto 0)     |                |
| shift_val_o | out       | std_logic_vector(SHFT_ADDR_SZ-1 downto 0) |                |
## Signals

| Name            | Type                                      | Description |
| --------------- | ----------------------------------------- | ----------- |
| shift_val_s     | std_logic_vector(SHFT_ADDR_SZ-1 downto 0) |             |
| readdata_s      | std_logic_vector(wb_size-1 downto 0)      |             |
| readdata_next_s | std_logic_vector(wb_size-1 downto 0)      |             |
## Constants

| Name          | Type             | Value | Description |
| ------------- | ---------------- | ----- | ----------- |
| REG_ID        | std_logic_vector |  "00" |             |
| REG_SHIFT_VAL | std_logic_vector |  "01" |             |
## Processes
- write_bloc: ( clk )
**Description**
manage register

- read_async_bloc: ( shift_val_s, addr_i )
- read_bloc: ( clk )
