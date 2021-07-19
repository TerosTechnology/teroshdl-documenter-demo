# Entity: prn20b_logic

- **File**: prn20b_logic.vhd
## Diagram

![Diagram](prn20b_logic.svg "Diagram")
## Description

(c) Copyright: OscillatorIMP Digital
Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
Creation date : 2018/06/11
## Ports

| Port name | Direction | Type                          | Description |
| --------- | --------- | ----------------------------- | ----------- |
| clk       | in        | std_logic                     |             |
| reset     | in        | std_logic                     |             |
| tick_i    | in        | std_logic                     |             |
| prn_o     | out       | std_logic_vector(19 downto 0) | start       |
| bit_o     | out       | std_logic                     |             |
## Signals

| Name         | Type                          | Description |
| ------------ | ----------------------------- | ----------- |
| lfsr_s       | std_logic_vector(19 downto 0) |             |
|  lfsr_next_s | std_logic_vector(19 downto 0) |             |
| xor20_17     | std_logic                     |             |
| xorPlusOne   | std_logic                     |             |
## Processes
- unnamed: ( clk )
