# Entity: pidv3_axi_sync_vector

## Diagram

![Diagram](pidv3_axi_sync_vector.svg "Diagram")
## Description

(c) Copyright: OscillatorIMP Digital
Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
Creation date : 2016/05/25
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| stages       | natural | 3     |             |
| DATA         | natural | 16    |             |
## Ports

| Port name | Direction | Type                              | Description |
| --------- | --------- | --------------------------------- | ----------- |
| ref_clk_i | in        | std_logic                         |             |
| clk_i     | in        | std_logic                         |             |
| bit_i     | in        | std_logic_vector(DATA-1 downto 0) |             |
| bit_o     | out       | std_logic_vector(DATA-1 downto 0) |             |
## Signals

| Name               | Type                              | Description |
| ------------------ | --------------------------------- | ----------- |
| sync_vect_stage0_s | std_logic_vector(DATA-1 downto 0) |             |
| flipflops_vect     | data_tab(stages -1 downto 0)      |             |
## Types

| Name     | Type                                                           | Description |
| -------- | -------------------------------------------------------------- | ----------- |
| data_tab | array (natural range <>) of std_logic_vector(DATA-1 downto 0)  |             |
## Processes
- ref_proc: ( ref_clk_i )
- sync_proc: ( clk_i )
