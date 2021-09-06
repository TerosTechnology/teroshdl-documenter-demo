# Entity: redpitaya_converters_12_sync_bit

- **File**: redpitaya_converters_12_sync_bit.vhd
## Diagram

![Diagram](redpitaya_converters_12_sync_bit.svg "Diagram")
## Description

-------------------------------------------------------------------------
 (c) Copyright: OscillatorIMP Digital
 Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
 Creation date : 2015/04/08
-------------------------------------------------------------------------
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| stages       | natural | 3     |             |
## Ports

| Port name | Direction | Type      | Description |
| --------- | --------- | --------- | ----------- |
| ref_clk_i | in        | std_logic |             |
| clk_i     | in        | std_logic |             |
| bit_i     | in        | std_logic |             |
| bit_o     | out       | std_logic |             |
## Signals

| Name          | Type                                 | Description |
| ------------- | ------------------------------------ | ----------- |
| sync_stage0_s | std_logic                            |             |
| flipflops     | std_logic_vector(stages -1 downto 0) |             |
## Processes
- ref_proc: ( ref_clk_i )
- sync_proc: ( clk_i )
