# Entity: ram_storage16

- **File**: ram_storage16.vhd
## Diagram

![Diagram](ram_storage16.svg "Diagram")
## Description

Library UNISIM;
use UNISIM.vcomponents.all;
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
| dout_a    | out       | std_logic_vector(DATA-1 downto 0) |                         |
| we_b      | in        | std_logic                         |                         |
| addr_b    | in        | std_logic_vector(ADDR-1 downto 0) |                         |
| din_b     | in        | std_logic_vector(DATA-1 downto 0) |                         |
| dout_b    | out       | std_logic_vector(DATA-1 downto 0) |                         |
## Types

| Name     | Type | Description |
| -------- | ---- | ----------- |
| mem_type |      |             |
## Processes
- unnamed: ( clk_a )
- unnamed: ( clk_b )
</br>**Description**
 Port B 
