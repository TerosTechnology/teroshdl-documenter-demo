# Entity: ethernet_tx_vvc
## Diagram
![Diagram](ethernet_tx_vvc.svg "Diagram")
## Generics
| Generic name                             | Type                                  | Value                                         | Description |
| ---------------------------------------- | ------------------------------------- | --------------------------------------------- | ----------- |
| GC_INSTANCE_IDX                          | natural                               |                                               |             |
| GC_CHANNEL                               | t_channel                             |                                               |             |
| GC_PHY_INTERFACE                         | t_interface                           |                                               |             |
| GC_PHY_VVC_INSTANCE_IDX                  | natural                               |                                               |             |
| GC_PHY_MAX_ACCESS_TIME                   | time                                  | 1 us                                          |             |
| GC_DUT_IF_FIELD_CONFIG                   | t_dut_if_field_config_direction_array | C_DUT_IF_FIELD_CONFIG_DIRECTION_ARRAY_DEFAULT |             |
| GC_ETHERNET_PROTOCOL_CONFIG              | t_ethernet_protocol_config            | C_ETHERNET_PROTOCOL_CONFIG_DEFAULT            |             |
| GC_CMD_QUEUE_COUNT_MAX                   | natural                               | 1000                                          |             |
| GC_CMD_QUEUE_COUNT_THRESHOLD             | natural                               | 950                                           |             |
| GC_CMD_QUEUE_COUNT_THRESHOLD_SEVERITY    | t_alert_level                         | WARNING                                       |             |
| GC_RESULT_QUEUE_COUNT_MAX                | natural                               | 1000                                          |             |
| GC_RESULT_QUEUE_COUNT_THRESHOLD          | natural                               | 950                                           |             |
| GC_RESULT_QUEUE_COUNT_THRESHOLD_SEVERITY | t_alert_level                         | WARNING                                       |             |
## Signals
| Name                               | Type                                                                 | Description |
| ---------------------------------- | -------------------------------------------------------------------- | ----------- |
| executor_is_busy                   | boolean                                                              |             |
| queue_is_increasing                | boolean                                                              |             |
| last_cmd_idx_executed              | natural                                                              |             |
| terminate_current_cmd              | t_flag_record                                                        |             |
| hvvc_to_bridge                     | t_hvvc_to_bridge(data_words(0 to C_MAX_PACKET_LENGTH-1)(7 downto 0)) |             |
| bridge_to_hvvc                     | t_bridge_to_hvvc(data_words(0 to C_MAX_PACKET_LENGTH-1)(7 downto 0)) |             |
| entry_num_in_vvc_activity_register | integer                                                              |             |
## Constants
| Name         | Type         | Value                                                                | Description |
| ------------ | ------------ | -------------------------------------------------------------------- | ----------- |
| C_SCOPE      | string       |  C_VVC_NAME & "," & to_string(GC_INSTANCE_IDX)                       |             |
| C_VVC_LABELS | t_vvc_labels |  assign_vvc_labels(C_SCOPE, C_VVC_NAME, GC_INSTANCE_IDX, GC_CHANNEL) |             |
## Processes
- cmd_interpreter: _(  )_

- cmd_executor: _(  )_

