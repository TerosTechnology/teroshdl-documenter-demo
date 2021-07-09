# Entity: axiStreamToReal

## Diagram

![Diagram](axiStreamToReal.svg "Diagram")
## Description

(c) Copyright: OscillatorIMP Digital
Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
Creation date : 2016/10/27
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| DATA_SIZE    | natural | 32    |             |
## Ports

| Port name       | Direction | Type                                   | Description |
| --------------- | --------- | -------------------------------------- | ----------- |
| s00_axis_reset  | in        | std_logic                              |             |
| data_o          | out       | std_logic_vector(DATA_SIZE-1 downto 0) | output data |
| data_en_o       | out       | std_logic                              |             |
| data_clk_o      | out       | std_logic                              |             |
| data_rst_o      | out       | std_logic                              |             |
| s00_axis_aclk   | in        | std_logic                              | input data  |
| s00_axis_tdata  | in        | std_logic_vector(DATA_SIZE-1 downto 0) |             |
| s00_axis_tready | out       | std_logic                              |             |
| s00_axis_tvalid | in        | std_logic                              |             |
