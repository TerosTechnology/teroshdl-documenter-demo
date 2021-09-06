# Entity: tb_user_guide

- **File**: tb_user_guide.vhd
## Diagram

![Diagram](tb_user_guide.svg "Diagram")
## Description

 This Source Code Form is subject to the terms of the Mozilla Public
 License, v. 2.0. If a copy of the MPL was not distributed with this file,
 You can obtain one at http://mozilla.org/MPL/2.0/.

 Copyright (c) 2014-2021, Lars Asplund lars.anders.asplund@gmail.com
## Generics

| Generic name | Type   | Value | Description |
| ------------ | ------ | ----- | ----------- |
| runner_cfg   | string |       |             |
## Signals

| Name    | Type                 | Description |
| ------- | -------------------- | ----------- |
| clk     | std_logic            |             |
| op_a    | unsigned(7 downto 0) |             |
|  op_b   | unsigned(7 downto 0) |             |
| sum     | unsigned(8 downto 0) |             |
| dv_in   | std_logic            |             |
|  dv_out | std_logic            |             |
## Constants

| Name           | Type                | Value                                                                                 | Description |
| -------------- | ------------------- | ------------------------------------------------------------------------------------- | ----------- |
| driver         | actor_t             |  new_actor("driver")                                                                  |             |
| monitor        | actor_t             |  new_actor("monitor")                                                                 |             |
| master_channel | actor_t             |  new_actor("driver channel")                                                          |             |
| slave_channel  | actor_t             |  new_actor("monitor channel")                                                         |             |
| add_msg        | msg_type_t          |  new_msg_type("add")                                                                  |             |
| sum_msg        | msg_type_t          |  new_msg_type("sum")                                                                  |             |
| my_receiver    | actor_t             |  new_actor("my receiver")                                                             |             |
| test_sequencer | actor_t             |  new_actor("test sequencer")                                                          |             |
| channels       | actor_vec_t(1 to 2) |  (new_actor("channel 1"),<br><span style="padding-left:20px"> new_actor("channel 2")) |             |
| clk_period     | time                |  10 ns                                                                                |             |
## Processes
- test_runner: (  )
- my_receiver_process: (  )
- multiple_channel_process: (  )
- driver_process: (  )
- monitor_process: (  )
- scoreboard_process: (  )
## Instantiations

- memory_bfm: work.memory_bfm
- adder: lib.adder
