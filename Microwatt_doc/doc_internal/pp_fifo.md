# Entity: pp_fifo

- **File**: pp_fifo.vhd
## Diagram

![Diagram](pp_fifo.svg "Diagram")
## Description

The Potato Processor - A simple processor for FPGAs
(c) Kristian Klomsten Skordal 2014 - 2015 <kristian.skordal@wafflemail.net>
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| DEPTH        | natural | 64    |             |
| WIDTH        | natural | 32    |             |
## Ports

| Port name | Direction | Type                                 | Description    |
| --------- | --------- | ------------------------------------ | -------------- |
| clk       | in        | std_logic                            | Control lines: |
| reset     | in        | std_logic                            |                |
| full      | out       | std_logic                            | Status lines:  |
| empty     | out       | std_logic                            |                |
| data_in   | in        | std_logic_vector(WIDTH - 1 downto 0) | Data in:       |
| data_out  | out       | std_logic_vector(WIDTH - 1 downto 0) |                |
| push      | in        | std_logic                            |                |
| pop       | in        | std_logic                            |                |
## Signals

| Name    | Type         | Description |
| ------- | ------------ | ----------- |
| memory  | memory_array |             |
| top     | index_type   |             |
|  bottom | index_type   |             |
| prev_op | fifo_op      |             |
## Types

| Name         | Type                                                       | Description |
| ------------ | ---------------------------------------------------------- | ----------- |
| memory_array |                                                            |             |
| fifo_op      | (FIFO_POP,<br><span style="padding-left:20px"> FIFO_PUSH)  |             |
## Processes
- read: ( clk )
- write: ( clk )
- set_prev_op: ( clk )
