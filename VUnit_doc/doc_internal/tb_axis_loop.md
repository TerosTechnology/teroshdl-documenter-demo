# Entity: tb_axis_loop

- **File**: tb_axis_loop.vhd
## Diagram

![Diagram](tb_axis_loop.svg "Diagram")
## Description

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this file,
You can obtain one at http://mozilla.org/MPL/2.0/.
Copyright (c) 2014-2021, Lars Asplund lars.anders.asplund@gmail.com
This testbench is a Minimum Working Example (MWE) of VUnit's resources to read/write CSV files and to verify
AXI4-Stream components. A CSV file that contains comma separated integers is read from `data_path & csv_i`, and it is
sent row by row to an AXI4-Stream Slave. The AXI4-Stream Slave is expected to be connected to an AXI4-Stream Master
either directly or (preferredly) through a FIFO, thus composing a loopback. Therefore, as data is pushed to the
AXI4-Stream Slave interface, the output is read from the AXI4-Stream Master interface and it is saved to
`data_path & csv_o`.
AXI Stream VC's optional 'stall' feature is used for generating random stalls in the interfaces. In this example,
a 5% of probability to stall for a duration of 1 to 10 cycles is defined.
## Generics

| Generic name | Type   | Value          | Description |
| ------------ | ------ | -------------- | ----------- |
| runner_cfg   | string |                |             |
| tb_path      | string |                |             |
| csv_i        | string | "data/in.csv"  |             |
| csv_o        | string | "data/out.csv" |             |
## Signals

| Name   | Type      | Description              |
| ------ | --------- | ------------------------ |
| clk    | std_logic | tb signals and variables |
|  rst   | std_logic | tb signals and variables |
|  rstn  | std_logic | tb signals and variables |
| start  | boolean   |                          |
|  done  | boolean   |                          |
|  saved | boolean   |                          |
## Constants

| Name              | Type                | Value                                                                                                                                                                                                                    | Description                        |
| ----------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------- |
| clk_period        | time                |  20 ns                                                                                                                                                                                                                   |                                    |
| data_width        | natural             |  32                                                                                                                                                                                                                      |                                    |
| master_axi_stream | axi_stream_master_t |  new_axi_stream_master(     data_length => data_width,<br><span style="padding-left:20px">     stall_config => new_stall_config(0.05,<br><span style="padding-left:20px"> 1,<br><span style="padding-left:20px"> 10)   ) | AXI4Stream Verification Components |
| slave_axi_stream  | axi_stream_slave_t  |  new_axi_stream_slave(     data_length => data_width,<br><span style="padding-left:20px">     stall_config => new_stall_config(0.05,<br><span style="padding-left:20px"> 1,<br><span style="padding-left:20px"> 10)   )  |                                    |
| m_I               | integer_array_t     |  load_csv(tb_path & csv_i)                                                                                                                                                                                               |                                    |
| m_O               | integer_array_t     |  new_2d(width(m_I),<br><span style="padding-left:20px"> height(m_I),<br><span style="padding-left:20px"> data_width,<br><span style="padding-left:20px"> true)                                                           |                                    |
## Processes
- main: (  )
- stimuli: (  )
- save: (  )
## Instantiations

- uut_vc: work.vc_axis
