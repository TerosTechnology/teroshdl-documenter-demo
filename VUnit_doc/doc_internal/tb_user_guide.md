# Entity: tb_user_guide
## Diagram
![Diagram](tb_user_guide.svg "Diagram")
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
| Name           | Type                | Value                                             | Description |
| -------------- | ------------------- | ------------------------------------------------- | ----------- |
| driver         | actor_t             |  new_actor("driver")                              |             |
| monitor        | actor_t             |  new_actor("monitor")                             |             |
| master_channel | actor_t             |  new_actor("driver channel")                      |             |
| slave_channel  | actor_t             |  new_actor("monitor channel")                     |             |
| add_msg        | msg_type_t          |  new_msg_type("add")                              |             |
| sum_msg        | msg_type_t          |  new_msg_type("sum")                              |             |
| my_receiver    | actor_t             |  new_actor("my receiver")                         |             |
| test_sequencer | actor_t             |  new_actor("test sequencer")                      |             |
| channels       | actor_vec_t(1 to 2) |  (new_actor("channel 1"), new_actor("channel 2")) |             |
| clk_period     | time                |  10 ns                                            |             |
## Processes
- test_runner: _(  )_

- my_receiver_process: _(  )_

- multiple_channel_process: _(  )_

- driver_process: _(  )_

- monitor_process: _(  )_

- scoreboard_process: _(  )_

## Instantiations
- memory_bfm: work.memory_bfm
- adder: lib.adder
