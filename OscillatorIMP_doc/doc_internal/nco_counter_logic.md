# Entity: nco_counter_logic

## Diagram

![Diagram](nco_counter_logic.svg "Diagram")
## Description

(c) Copyright: OscillatorIMP Digital
Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
Creation date : 2015/04/08
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| TEST         | boolean | false |             |
| RESET_ACCUM  | boolean | false |             |
| LUT_SIZE     | natural | 10    |             |
| COUNTER_SIZE | natural | 32    |             |
| DATA_SIZE    | natural | 16    |             |
## Ports

| Port name   | Direction | Type                                      | Description              |
| ----------- | --------- | ----------------------------------------- | ------------------------ |
| cpu_clk_i   | in        | std_logic                                 |                          |
| clk_i       | in        | std_logic                                 |                          |
| rst_i       | in        | std_logic                                 |                          |
| enable_i    | in        | std_logic                                 | configuration (wishbone) |
| sync_i      | in        | std_logic                                 |                          |
| max_accum_i | in        | std_logic_vector(COUNTER_SIZE-1 downto 0) |                          |
| cpt_off_i   | in        | std_logic_vector(LUT_SIZE-1 downto 0)     |                          |
| cpt_inc_i   | in        | std_logic_vector(COUNTER_SIZE-1 downto 0) |                          |
| trigger_o   | out       | std_logic                                 |                          |
| cos_o       | out       | std_logic_vector(DATA_SIZE -1 downto 0)   | next                     |
| sin_o       | out       | std_logic_vector(DATA_SIZE -1 downto 0)   |                          |
| sin_fake_o  | out       | std_logic                                 |                          |
| wave_en_o   | out       | std_logic                                 |                          |
| cos_fake_o  | out       | std_logic                                 |                          |
## Signals

| Name                | Type                                      | Description |
| ------------------- | ----------------------------------------- | ----------- |
| counter_next_s      | std_logic_vector(COUNTER_SIZE-1 downto 0) |             |
|  counter_s          | std_logic_vector(COUNTER_SIZE-1 downto 0) |             |
| counter_sin_s       | std_logic_vector(COUNTER_SIZE-1 downto 0) |             |
| counter_scale_s     | std_logic_vector(LUT_SIZE-1 downto 0)     |             |
| counter_sin_scale_s | std_logic_vector(LUT_SIZE-1 downto 0)     |             |
| counter_sin_off_s   | std_logic_vector(LUT_SIZE-1 downto 0)     |             |
| counter_cos_off_s   | std_logic_vector(LUT_SIZE-1 downto 0)     |             |
| sin_next            | std_logic                                 |             |
|  cos_next           | std_logic                                 |             |
| cos_s               | std_logic_vector(15 downto 0)             |             |
|  sin_s              | std_logic_vector(15 downto 0)             |             |
| cos_scale_del_s     | std_logic_vector(LUT_SIZE-1 downto 0)     |             |
| cos_del_s           | std_logic_vector(COUNTER_SIZE-1 downto 0) |             |
| int_rst_s           | std_logic                                 |             |
| rst_accum_s         | std_logic                                 | reset accum |
| cpt_s               | std_logic_vector(COUNTER_SIZE-1 downto 0) |             |
| trig_cpt_s          | natural range 0 to MAX_TRIG               |             |
| counter_old_s       | std_logic                                 |             |
|  reinit_counter_s   | std_logic                                 |             |
## Constants

| Name                | Type                              | Value                                   | Description |
| ------------------- | --------------------------------- | --------------------------------------- | ----------- |
| MAX_TRIG            | natural                           |  3                                      | trigger     |
| sin_static_offset_s | unsigned(COUNTER_SIZE-2 downto 0) |  '1' & (COUNTER_SIZE-3 downto 0 => '0') |             |
## Processes
- sin_cos_proc: ( clk_i )
- cpt_sin_proc: ( clk_i )
- unnamed: ( clk_i )
