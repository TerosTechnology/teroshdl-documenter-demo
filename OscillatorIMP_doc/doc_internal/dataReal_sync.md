# Entity: dataReal_sync

## Diagram

![Diagram](dataReal_sync.svg "Diagram")
## Description

(c) Copyright: OscillatorIMP Digital
Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
Creation date : 2018/12/16
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

| Name           | Type      | Description |
| -------------- | --------- | ----------- |
| sync_stage0_s  | std_logic |             |
|  sync_stage1_s | std_logic |             |
| sync_stage2_s  | std_logic |             |
|  sync_stage3_s | std_logic |             |
## Processes
- ref_proc: ( ref_clk_i )
- sync_proc: ( clk_i )
