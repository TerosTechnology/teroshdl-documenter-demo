# Entity: pidv3_axi_comm

## Diagram

![Diagram](pidv3_axi_comm.svg "Diagram")
## Description

(c) Copyright: OscillatorIMP Digital
Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
Creation date : 2019/04/20
## Generics

| Generic name  | Type    | Value | Description    |
| ------------- | ------- | ----- | -------------- |
| P_SIZE        | integer | 14    |                |
| I_SIZE        | integer | 14    |                |
| D_SIZE        | integer | 14    |                |
| SETPOINT_SIZE | natural | 32    |                |
| BUS_SIZE      | natural | 32    | Data port size |
## Ports

| Port name   | Direction | Type                                       | Description    |
| ----------- | --------- | ------------------------------------------ | -------------- |
| reset       | in        | std_logic                                  | Syscon signals |
| clk         | in        | std_logic                                  |                |
| addr_i      | in        | std_logic_vector(2 downto 0)               | comm signals   |
| wr_en_i     | in        | std_logic                                  |                |
| writedata_i | in        | std_logic_vector( BUS_SIZE-1 downto 0)     |                |
| rd_en_i     | in        | std_logic                                  |                |
| readdata_o  | out       | std_logic_vector( BUS_SIZE-1 downto 0)     |                |
| kp_o        | out       | std_logic_vector(P_SIZE-1 downto 0)        | logic signals  |
| ki_o        | out       | std_logic_vector(I_SIZE-1 downto 0)        |                |
| kd_o        | out       | std_logic_vector(D_SIZE-1 downto 0)        |                |
| sign_o      | out       | std_logic                                  |                |
| setpoint_o  | out       | std_logic_vector(SETPOINT_SIZE-1 downto 0) |                |
| int_rst_o   | out       | std_logic                                  |                |
| is_input_o  | out       | std_logic_vector(5 downto 0)               |                |
## Signals

| Name            | Type                                       | Description |
| --------------- | ------------------------------------------ | ----------- |
| readdata_s      | std_logic_vector(BUS_SIZE-1 downto 0)      |             |
| readdata_next_s | std_logic_vector(BUS_SIZE-1 downto 0)      |             |
| setpoint_s      | std_logic_vector(SETPOINT_SIZE-1 downto 0) |             |
| kp_s            | std_logic_vector(P_SIZE-1 downto 0)        |             |
| ki_s            | std_logic_vector(I_SIZE-1 downto 0)        |             |
| kd_s            | std_logic_vector(D_SIZE-1 downto 0)        |             |
| sign_s          | std_logic                                  |             |
| int_rst_s       | std_logic                                  |             |
| is_input_s      | std_logic_vector(5 downto 0)               |             |
## Constants

| Name         | Type                         | Value  | Description |
| ------------ | ---------------------------- | ------ | ----------- |
| REG_KP       | std_logic_vector(2 downto 0) |  "000" |             |
| REG_KI       | std_logic_vector(2 downto 0) |  "001" |             |
| REG_KD       | std_logic_vector(2 downto 0) |  "010" |             |
| REG_SETPOINT | std_logic_vector(2 downto 0) |  "011" |             |
| REG_SIGN     | std_logic_vector(2 downto 0) |  "100" |             |
| REG_INT_RST  | std_logic_vector(2 downto 0) |  "101" |             |
| REG_INPUT    | std_logic_vector(2 downto 0) |  "110" |             |
## Processes
- write_bloc: ( clk )
**Description**
manage register

- read_async: ( addr_i, kp_s, ki_s, kd_s, setpoint_s, sign_s, is_input_s )
- read_bloc: ( clk )
