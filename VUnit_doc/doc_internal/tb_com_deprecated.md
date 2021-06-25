# Entity: tb_com_deprecated
## Diagram
![Diagram](tb_com_deprecated.svg "Diagram")
## Generics
| Generic name | Type   | Value | Description |
| ------------ | ------ | ----- | ----------- |
| runner_cfg   | string |       |             |
## Signals
| Name                            | Type                     | Description |
| ------------------------------- | ------------------------ | ----------- |
| hello_world_received            | boolean                  |             |
|  start_receiver                 | boolean                  |             |
|  start_server                   | boolean                  |             |
| 
    start_server2              | boolean                  |             |
|  start_server3                  | boolean                  |             |
|  start_server5                  | boolean                  |             |
| 
    start_subscribers          | boolean                  |             |
| start_limited_inbox             | boolean                  |             |
|  start_limited_inbox_subscriber | boolean                  |             |
| 
    limited_inbox_actor_done   | boolean                  |             |
| hello_subscriber_received       | std_logic_vector(1 to 2) |             |
## Constants
| Name       | Type     | Value                        | Description |
| ---------- | -------- | ---------------------------- | ----------- |
| com_logger | logger_t |  get_logger("vunit_lib:com") |             |
## Processes
- test_runner: _(  )_

- receiver: _(  )_

- server: _(  )_

- server2: _(  )_

- server3: _(  )_

- server5: _(  )_

- limited_inbox_actor: _(  )_

- limited_inbox_subscriber: _(  )_

