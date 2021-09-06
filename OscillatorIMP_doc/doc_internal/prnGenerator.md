# Entity: prnGenerator

- **File**: prnGenerator.vhd
## Diagram

![Diagram](prnGenerator.svg "Diagram")
## Description

-------------------------------------------------------------------------
 (c) Copyright: OscillatorIMP Digital
 Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
 Creation date : 2019/05/18
-------------------------------------------------------------------------
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| BIT_LEN      | natural | 7     |             |
| PRN_NUM      | natural | 1     |             |
| PERIOD_LEN   | natural | 1     |             |
## Ports

| Port name | Direction | Type      | Description |
| --------- | --------- | --------- | ----------- |
| clk       | in        | std_logic |             |
| reset     | in        | std_logic |             |
| tick_i    | in        | std_logic |             |
| prn_o     | out       | std_logic |             |
## Signals

| Name         | Type                                 | Description |
| ------------ | ------------------------------------ | ----------- |
| period_s     | unsigned(PERIOD_WIDTH-1 downto 0)    |             |
| tick_int_s   | std_logic                            |             |
| lfsr_s       | std_logic_vector(BIT_LEN-1 downto 0) |             |
|  lfsr_next_s | std_logic_vector(BIT_LEN-1 downto 0) |             |
| xorM_N       | std_logic                            |             |
## Constants

| Name         | Type    | Value                                  | Description |
| ------------ | ------- | -------------------------------------- | ----------- |
| PERIOD_WIDTH | natural |  natural(ceil(log2(real(PERIOD_LEN)))) |             |
## Processes
- unnamed: ( clk )
