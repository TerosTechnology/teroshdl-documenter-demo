# Entity: wb_prn20b

- **File**: wb_prn20b.vhd
## Diagram

![Diagram](wb_prn20b.svg "Diagram")
## Description

(c) Copyright: OscillatorIMP Digital
Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
Creation date : 2018/06/11
## Generics

| Generic name | Type    | Value | Description                 |
| ------------ | ------- | ----- | --------------------------- |
| PRESC_SIZE   | natural | 16    |                             |
| DFLT_PRESC   | natural | 15    |                             |
| ADDR_SIZE    | natural | 4     |                             |
| wb_size      | natural | 16    | Data port size for wishbone |
## Ports

| Port name     | Direction | Type                                    | Description      |
| ------------- | --------- | --------------------------------------- | ---------------- |
| reset         | in        | std_logic                               | Syscon signals   |
| clk           | in        | std_logic                               |                  |
| wbs_add       | in        | std_logic_vector(ADDR_SIZE-1 downto 0)  | Wishbone signals |
| wbs_writedata | in        | std_logic_vector(wb_size-1 downto 0)    |                  |
| wbs_readdata  | out       | std_logic_vector(wb_size-1 downto 0)    |                  |
| wbs_read      | in        | std_logic                               |                  |
| wbs_read_ack  | out       | std_logic                               |                  |
| wbs_write     | in        | std_logic                               |                  |
| prescaler_o   | out       | std_logic_vector(PRESC_SIZE-1 downto 0) |                  |
## Signals

| Name            | Type                                    | Description |
| --------------- | --------------------------------------- | ----------- |
| readdata_s      | std_logic_vector(wb_size-1 downto 0)    |             |
| readdata_next_s | std_logic_vector(wb_size-1 downto 0)    |             |
| prescaler_s     | std_logic_vector(PRESC_SIZE-1 downto 0) |             |
## Constants

| Name          | Type                                   | Value | Description |
| ------------- | -------------------------------------- | ----- | ----------- |
| REG_PRESCALER | std_logic_vector(ADDR_SIZE-1 downto 0) |  "0"  |             |
## Processes
- write_bloc: ( clk )
**Description**
manage register

- unnamed: ( wbs_add, prescaler_s )
- read_bloc: ( clk )
