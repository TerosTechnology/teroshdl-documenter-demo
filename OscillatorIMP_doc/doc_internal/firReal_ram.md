# Entity: firReal_ram

- **File**: firReal_ram.vhd
## Diagram

![Diagram](firReal_ram.svg "Diagram")
## Description

-------------------------------------------------------------------------
 (c) Copyright: OscillatorIMP Digital
 Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
 Creation date : 2018/05/26
-------------------------------------------------------------------------
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| DATA         | integer | 72    |             |
| ADDR         | integer | 10    |             |
## Ports

| Port name | Direction | Type                              | Description             |
| --------- | --------- | --------------------------------- | ----------------------- |
| clk_a     | in        | std_logic                         |                         |
| clk_b     | in        | std_logic                         |                         |
| we_a      | in        | std_logic                         | state machine interface |
| addr_a    | in        | std_logic_vector(ADDR-1 downto 0) |                         |
| din_a     | in        | std_logic_vector(DATA-1 downto 0) |                         |
| addr_b    | in        | std_logic_vector(ADDR-1 downto 0) |                         |
| dout_b    | out       | std_logic_vector(DATA-1 downto 0) |                         |
## Signals

| Name | Type     | Description |
| ---- | -------- | ----------- |
| mem  | mem_type |             |
## Types

| Name     | Type | Description |
| -------- | ---- | ----------- |
| mem_type |      |             |
## Processes
- unnamed: ( clk_a )
- unnamed: ( clk_b )
**Description**
 Port B 
