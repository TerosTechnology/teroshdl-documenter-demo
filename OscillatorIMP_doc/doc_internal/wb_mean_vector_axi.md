# Entity: wb_mean_vector_axi

- **File**: wb_mean_vector_axi.vhd
## Diagram

![Diagram](wb_mean_vector_axi.svg "Diagram")
## Description

-------------------------------------------------------------------------
 (c) Copyright: OscillatorIMP Digital
 Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
 2013-2019
-------------------------------------------------------------------------
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| id           | natural | 1     |             |
| wb_size      | natural | 16    |             |
| MAX_NB_ACCUM | natural | 1024  |             |
| ACCUM_SIZE   | natural | 10    |             |
| SHIFT_SIZE   | natural | 4     |             |
## Ports

| Port name     | Direction | Type                                    | Description      |
| ------------- | --------- | --------------------------------------- | ---------------- |
| reset         | in        | std_logic                               | Syscon signals   |
| clk           | in        | std_logic                               |                  |
| wbs_add       | in        | std_logic_vector(1 downto 0)            | Wishbone signals |
| wbs_write     | in        | std_logic                               |                  |
| wbs_writedata | in        | std_logic_vector( wb_size-1 downto 0)   |                  |
| wbs_read      | in        | std_logic                               |                  |
| wbs_readdata  | out       | std_logic_vector( wb_size-1 downto 0)   |                  |
| shift_val_o   | out       | std_logic_vector(SHIFT_SIZE-1 downto 0) |                  |
| nb_iter_o     | out       | std_logic_vector(ACCUM_SIZE-1 downto 0) |                  |
## Signals

| Name        | Type                                    | Description |
| ----------- | --------------------------------------- | ----------- |
| shift_val_s | std_logic_vector(SHIFT_SIZE-1 downto 0) |             |
| nb_iter_s   | std_logic_vector(ACCUM_SIZE-1 downto 0) |             |
| readdata_s  | std_logic_vector(wb_size-1 downto 0)    |             |
## Constants

| Name          | Type             | Value | Description |
| ------------- | ---------------- | ----- | ----------- |
| REG_ID        | std_logic_vector |  "00" |             |
| REG_SHIFT_VAL | std_logic_vector | "01"  |             |
| REG_NB_ITER   | std_logic_vector | "10"  |             |
## Processes
- write_bloc: ( clk, reset )
**Description**
 manage register 
- read_bloc: ( clk, reset )
