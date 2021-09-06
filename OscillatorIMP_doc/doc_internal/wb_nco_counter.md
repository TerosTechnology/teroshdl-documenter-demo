# Entity: wb_nco_counter

- **File**: wb_nco_counter.vhd
## Diagram

![Diagram](wb_nco_counter.svg "Diagram")
## Description

-------------------------------------------------------------------------
 (c) Copyright: OscillatorIMP Digital
 Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
 Creation date : 2015/04/08
-------------------------------------------------------------------------
## Generics

| Generic name          | Type    | Value | Description                  |
| --------------------- | ------- | ----- | ---------------------------- |
| COUNTER_SIZE          | natural | 28    |                              |
| DEFAULT_RST_ACCUM_VAL | natural | 25    |                              |
| LUT_SIZE              | natural | 10    |                              |
| id                    | natural | 1     |                              |
| wb_size               | natural | 16    |  Data port size for wishbone |
## Ports

| Port name     | Direction | Type                                      | Description                                                              |
| ------------- | --------- | ----------------------------------------- | ------------------------------------------------------------------------ |
| reset         | in        | std_logic                                 | Syscon signals                                                           |
| clk           | in        | std_logic                                 |                                                                          |
| wbs_add       | in        | std_logic_vector(2 downto 0)              | Wishbone signalstep_scale_i : in std_logic_vector(LUT_SIZE-1 downto 0);  |
| wbs_write     | in        | std_logic                                 |                                                                          |
| wbs_writedata | in        | std_logic_vector( wb_size-1 downto 0)     |                                                                          |
| wbs_read      | in        | std_logic                                 |                                                                          |
| wbs_readdata  | out       | std_logic_vector( wb_size-1 downto 0)     |                                                                          |
| max_accum_o   | out       | std_logic_vector(COUNTER_SIZE-1 downto 0) |                                                                          |
| enable_o      | out       | std_logic                                 |                                                                          |
| pinc_sw_o     | out       | std_logic                                 |                                                                          |
| poff_sw_o     | out       | std_logic                                 |                                                                          |
| cpt_off_o     | out       | std_logic_vector(LUT_SIZE-1 downto 0)     |                                                                          |
| cpt_step_o    | out       | std_logic_vector(COUNTER_SIZE-1 downto 0) |                                                                          |
## Signals

| Name            | Type                                 | Description |
| --------------- | ------------------------------------ | ----------- |
| max_accum_s     | std_logic_vector(63 downto 0)        |             |
| max_accum_low_s | std_logic_vector(31 downto 0)        |             |
| cpt_step_s      | std_logic_vector(63 downto 0)        |             |
| cpt_step_low_s  | std_logic_vector(31 downto 0)        |             |
| cpt_off_s       | std_logic_vector(31 downto 0)        |             |
| poff_sw_s       | std_logic                            |             |
| pinc_sw_s       | std_logic                            |             |
| readdata_s      | std_logic_vector(wb_size-1 downto 0) |             |
| enable_s        | std_logic                            |             |
## Constants

| Name            | Type             | Value  | Description |
| --------------- | ---------------- | ------ | ----------- |
| REG_ID          | std_logic_vector |  "000" |             |
| REG_POFF        | std_logic_vector | "001"  |             |
| REG_CTRL        | std_logic_vector | "010"  |             |
| REG_PINC_L      | std_logic_vector | "011"  |             |
| REG_PINC_H      | std_logic_vector | "100"  |             |
| REG_MAX_ACCUM_L | std_logic_vector | "101"  |             |
| REG_MAX_ACCUM_H | std_logic_vector | "110"  |             |
| REG_CTRL2       | std_logic_vector | "111"  |             |
## Processes
- write_bloc: ( clk )
</br>**Description**
 manage register 
- read_bloc: ( clk )
