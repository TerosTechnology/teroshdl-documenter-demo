# Entity: MUXrealNto1_wb

- **File**: MUXrealNto1_wb.vhd
## Diagram

![Diagram](MUXrealNto1_wb.svg "Diagram")
## Description

-------------------------------------------------------------------------
 (c) Copyright: OscillatorIMP Digital
 Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
 modified : 2021/06/11
 Creation date : 2015/04/08
-------------------------------------------------------------------------
## Generics

| Generic name | Type    | Value | Description                   |
| ------------ | ------- | ----- | ----------------------------- |
| id           | natural | 1     |                               |
| wb_size      | natural | 16    |  Data port size for wishbone |
| SEL_SIZE     | integer | 2     |                               |
## Ports

| Port name     | Direction | Type                                    | Description      |
| ------------- | --------- | --------------------------------------- | ---------------- |
| reset         | in        | std_logic                               | Syscon signals   |
| clk           | in        | std_logic                               |                  |
| wbs_add       | in        | std_logic_vector(1 downto 0)            | Wishbone signals |
| wbs_write     | in        | std_logic                               |                  |
| wbs_writedata | in        | std_logic_vector( wb_size-1 downto 0)   |                  |
| wbs_read      | in        | std_logic                               |                  |
| wbs_readdata  | out       | std_logic_vector( wb_size-1 downto 0)   |                  |
| outputSelect  | out       | std_logic_vector(SEL_SIZE - 1 downto 0) |  modified IR     |
## Signals

| Name           | Type                                   | Description   |
| -------------- | -------------------------------------- | ------------- |
| outputSelect_s | std_logic_vector(SEL_SIZE -1 downto 0) |  modified IR |
| readdata_s     | std_logic_vector(wb_size-1 downto 0)   |               |
## Constants

| Name      | Type                         | Value | Description |
| --------- | ---------------------------- | ----- | ----------- |
| REG_ID    | std_logic_vector(1 downto 0) |  "00" |             |
| REG_INPUT | std_logic_vector(1 downto 0) | "01"  |             |
## Processes
- write_bloc: ( clk )
**Description**
 modified IR  manage register 
- read_bloc: ( clk )
