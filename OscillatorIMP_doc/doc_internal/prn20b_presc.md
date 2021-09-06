# Entity: prn20b_presc

- **File**: prn20b_presc.vhd
## Diagram

![Diagram](prn20b_presc.svg "Diagram")
## Description

-------------------------------------------------------------------------
 (c) Copyright: OscillatorIMP Digital
 Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
 Creation date : 2018/06/11
-------------------------------------------------------------------------
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| CPT_SIZE     | integer | 32    |             |
## Ports

| Port name   | Direction | Type                                  | Description            |
| ----------- | --------- | ------------------------------------- | ---------------------- |
| clk_i       | in        | std_logic                             |  Main clock            |
| rst_i       | in        | std_logic                             |  Main reset            |
| prescaler_i | in        | std_logic_vector(CPT_SIZE-1 downto 0) |                        |
| clk_gen_o   | out       | std_logic                             |  slow generated clock  |
| tick_o      | out       | std_logic                             |  one tick per slow clk |
## Signals

| Name         | Type                                  | Description |
| ------------ | ------------------------------------- | ----------- |
| counter      | std_logic_vector(CPT_SIZE-1 downto 0) |             |
| counter_next | std_logic_vector(CPT_SIZE-1 downto 0) |             |
| presc_m1_s   | std_logic_vector(CPT_SIZE-1 downto 0) |             |
| load_en_s    | std_logic                             |             |
## Processes
- tx_clk_gen: ( clk_i )
- unnamed: ( clk_i )
