# Entity: wishbone_master
## Diagram
![Diagram](wishbone_master.svg "Diagram")
## Generics
| Generic name            | Type                  | Value | Description |
| ----------------------- | --------------------- | ----- | ----------- |
| bus_handle              | bus_master_t          |       |             |
| strobe_high_probability | real range 0.0 to 1.0 | 1.0   |             |
## Ports
| Port name | Direction | Type             | Description |
| --------- | --------- | ---------------- | ----------- |
| clk       | in        | std_logic        |             |
| adr       | out       | std_logic_vector |             |
| dat_i     | in        | std_logic_vector |             |
| dat_o     | out       | std_logic_vector |             |
| sel       | out       | std_logic_vector |             |
| cyc       | out       | std_logic        |             |
| stb       | out       | std_logic        |             |
| we        | out       | std_logic        |             |
| stall     | in        | std_logic        |             |
| ack       | in        | std_logic        |             |
## Signals
| Name        | Type      | Description |
| ----------- | --------- | ----------- |
| start_cycle | std_logic |             |
| end_cycle   | std_logic |             |
| cycle       | boolean   |             |
## Constants
| Name                | Type       | Value                              | Description |
| ------------------- | ---------- | ---------------------------------- | ----------- |
| rd_request_queue    | queue_t    |  new_queue                         |             |
| wr_request_queue    | queue_t    |  new_queue                         |             |
| acknowledge_queue   | queue_t    |  new_queue                         |             |
| bus_ack_msg         | msg_type_t |  new_msg_type("wb master ack msg") |             |
| wb_master_ack_actor | actor_t    |  new_actor                         |             |
## Processes
- main: _(  )_

- p_cycle: _(  )_

- acknowledge: _(  )_

