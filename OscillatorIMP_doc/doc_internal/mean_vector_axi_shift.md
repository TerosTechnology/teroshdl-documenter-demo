# Entity: mean_vector_axi_shift

- **File**: mean_vector_axi_shift.vhd
## Diagram

![Diagram](mean_vector_axi_shift.svg "Diagram")
## Description

(c) Copyright: OscillatorIMP Digital
Author : Gwenhael Goavec-Merou<gwenhael.goavec-merou@trabucayre.com>
2013-2019
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| SHIFT_SIZE   | natural | 10    |             |
| DATA_I_SIZE  | natural | 32    |             |
| DATA_O_SIZE  | natural | 34    |             |
## Ports

| Port name | Direction | Type                                     | Description |
| --------- | --------- | ---------------------------------------- | ----------- |
| shift_i   | in        | std_logic_vector(SHIFT_SIZE-1 downto 0)  |             |
| data_i    | in        | std_logic_vector(DATA_I_SIZE-1 downto 0) |             |
| data_o    | out       | std_logic_vector(DATA_O_SIZE-1 downto 0) |             |
## Signals

| Name      | Type      | Description |
| --------- | --------- | ----------- |
| array_val | mux_array |             |
## Constants

| Name   | Type    | Value          | Description |
| ------ | ------- | -------------- | ----------- |
| MUX_SZ | natural |  2**SHIFT_SIZE |             |
## Types

| Name      | Type | Description |
| --------- | ---- | ----------- |
| mux_array |      |             |
