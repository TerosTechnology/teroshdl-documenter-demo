# Entity: dataComplex_to_ram_top

## Diagram

![Diagram](dataComplex_top.svg "Diagram")
## Description

(c) Copyright: OscillatorIMP Digital
Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
Creation date : 2018/11/30
## Generics

| Generic name | Type    | Value    | Description |
| ------------ | ------- | -------- | ----------- |
| DATA_FORMAT  | string  | "signed" |             |
| USE_EOF      | boolean | true     |             |
| NB_WAY       | natural | 4        |             |
| NB_SAMPLE    | natural | 1024     |             |
| INPUT_SIZE   | natural | 32       |             |
| DATA_SIZE    | natural | 32       |             |
| AXI_SIZE     | natural | 32       |             |
| ADDR_SIZE    | natural | 12       |             |
| RD_ADDR_SIZE | natural | 12       |             |
| CHAN_MUX_SZ  | natural | 12       |             |
| PKT_MUX_SZ   | natural | 12       |             |
## Ports

| Port name           | Direction | Type                                             | Description    |
| ------------------- | --------- | ------------------------------------------------ | -------------- |
| cpu_clk_i           | in        | std_logic                                        |                |
| rst_i               | in        | std_logic                                        |                |
| data_clk_i          | in        | std_logic_vector(NB_WAY-1 downto 0)              | Syscon signals |
| data_rst_i          | in        | std_logic_vector(NB_WAY-1 downto 0)              |                |
| start_acquisition_i |           | std_logic                                        |                |
| busy_o              | out       | std_logic                                        |                |
| res_o               | out       | std_logic_vector(AXI_SIZE-1 downto 0)            | results        |
| ram_incr_i          | in        | std_logic                                        |                |
| ram_reinit_i        | in        | std_logic                                        |                |
| data_i_i            | in        | std_logic_vector((NB_WAY*INPUT_SIZE)-1 downto 0) | input          |
| data_q_i            | in        | std_logic_vector((NB_WAY*INPUT_SIZE)-1 downto 0) |                |
| data_en_i           | in        | std_logic_vector(NB_WAY-1 downto 0)              |                |
| data_eof_i          | in        | std_logic_vector(NB_WAY-1 downto 0)              |                |
## Signals

| Name               | Type                                     | Description |
| ------------------ | ---------------------------------------- | ----------- |
| busy_s             | std_logic_vector(NB_WAY-1 downto 0)      |             |
| busy_out_s         | std_logic                                |             |
| start_s            | std_logic                                |             |
| res_s              | res_tab(NB_WAY-1 downto 0)               |             |
| incr_chan_s        | std_logic                                |             |
| incr_addr_s        | std_logic                                |             |
| ram_addr_s         | std_logic_vector(ADDR_SIZE-1 downto 0)   |             |
| ram_addr_next_s    | std_logic_vector(ADDR_SIZE-1 downto 0)   |             |
| select_chan_s      | std_logic_vector(CHAN_MUX_SZ-1 downto 0) |             |
| select_chan_next_s | std_logic_vector(CHAN_MUX_SZ-1 downto 0) |             |
| select_s           | std_logic_vector(PKT_MUX_SZ-1 downto 0)  |             |
| select_next_s      | std_logic_vector(PKT_MUX_SZ-1 downto 0)  |             |
## Constants

| Name            | Type    | Value          | Description          |
| --------------- | ------- | -------------- | -------------------- |
| NB_PKT_PER_SAMP | natural |  2**PKT_MUX_SZ | address manipulation |
## Types

| Name    | Type                                                               | Description |
| ------- | ------------------------------------------------------------------ | ----------- |
| res_tab | array (natural range <>) of std_logic_vector(AXI_SIZE-1 downto 0)  |             |
## Processes
- unnamed: ( ram_addr_s, incr_addr_s )
**Description**
select ram addr part

- unnamed: ( cpu_clk_i )
- unnamed: ( cpu_clk_i )
