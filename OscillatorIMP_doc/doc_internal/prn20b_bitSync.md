# Entity: prn20b_bitSync

- **File**: prn20b_bitSync.vhd
## Diagram

![Diagram](prn20b_bitSync.svg "Diagram")
## Description

-------------------------------------------------------------------------
 (c) Copyright: OscillatorIMP Digital
 Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
 Creation date : 2018/06/11
-------------------------------------------------------------------------
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| stages       | natural | 3     |             |
## Ports

| Port name | Direction | Type      | Description |
| --------- | --------- | --------- | ----------- |
| clk_i     | in        | std_logic |             |
| bit_i     | in        | std_logic |             |
| bit_o     | out       | std_logic |             |
## Signals

| Name      | Type                                 | Description |
| --------- | ------------------------------------ | ----------- |
| flipflops | std_logic_vector(stages -1 downto 0) |             |
## Processes
- sync_proc: ( clk_i )
