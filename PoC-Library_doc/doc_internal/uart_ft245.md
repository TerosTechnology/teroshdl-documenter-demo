# Entity: uart_ft245
## Diagram
![Diagram](uart_ft245.svg "Diagram")
## Generics
| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| CLK_FREQ     | positive |       |             |
## Ports
| Port name    | Direction | Type                         | Description |
| ------------ | --------- | ---------------------------- | ----------- |
| clk          | in        | std_logic                    |             |
| rst          | in        | std_logic                    |             |
| snd_ready    | out       | std_logic                    |             |
| snd_strobe   | in        | std_logic                    |             |
| snd_data     | in        | std_logic_vector(7 downto 0) |             |
| rec_strobe   | out       | std_logic                    |             |
| rec_data     | out       | std_logic_vector(7 downto 0) |             |
| ft245_data   | inout     | std_logic_vector(7 downto 0) |             |
| ft245_rdn    | out       | std_logic                    |             |
| ft245_wrn    | out       | std_logic                    |             |
| ft245_rxfn   | in        | std_logic                    |             |
| ft245_txen   | in        | std_logic                    |             |
| ft245_pwrenn | in        | std_logic                    |             |
## Signals
| Name          | Type                             | Description |
| ------------- | -------------------------------- | ----------- |
| reg_delay     | unsigned(DELAY_WIDTH-1 downto 0) |             |
| fsm_state     | tState                           |             |
| fsm_nextstate | tState                           |             |
| reg_data_snd  | std_logic_vector(7 downto 0)     |             |
| reg_data_rec  | std_logic_vector(7 downto 0)     |             |
| reg_ld_rec    | std_logic                        |             |
| reg_dto_b     | std_logic                        |             |
| reg_wr_b      | std_logic                        |             |
| reg_rd_b      | std_logic                        |             |
| ff_susp       | std_logic                        |             |
| ff_rxf        | std_logic                        |             |
| ff_txe        | std_logic                        |             |
| ctrl_ld_rec   | std_logic                        |             |
| ctrl_delay    | std_logic                        |             |
| ctrl_rd       | std_logic                        |             |
| ctrl_wr       | std_logic                        |             |
| ctrl_dto      | std_logic                        |             |
| data_in       | std_logic_vector(7 downto 0)     |             |
## Constants
| Name         | Type                             | Value                                         | Description |
| ------------ | -------------------------------- | --------------------------------------------- | ----------- |
| CLK_FREQ_MHZ | integer                          |  CLK_FREQ / 1000000                           |             |
| DELAY_CYCLES | integer                          |  CLK_FREQ_MHZ / 20                            |             |
| DELAY_WIDTH  | integer                          |  log2ceilnz(DELAY_CYCLES + 1)                 |             |
| DELAY_LOAD   | unsigned(DELAY_WIDTH-1 downto 0) |        to_unsigned(DELAY_CYCLES, DELAY_WIDTH) |             |
## Types
| Name   | Type                                             | Description |
| ------ | ------------------------------------------------ | ----------- |
| tState | ( IDLE, RD1, RD2, RD3, RD4, WR1, WR2, WR3, WR4 ) |             |
## Processes
- unnamed: _( clk )_

- unnamed: _( fsm_state, snd_strobe, reg_delay, ff_susp, ff_rxf, ff_txe )_

- unnamed: _( clk )_

