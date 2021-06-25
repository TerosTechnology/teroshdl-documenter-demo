# Entity: axistream_vvc
## Diagram
![Diagram](axistream_vvc.svg "Diagram")
## Generics
| Generic name                             | Type                   | Value                          | Description |
| ---------------------------------------- | ---------------------- | ------------------------------ | ----------- |
| GC_VVC_IS_MASTER                         | boolean                |                                |             |
| GC_DATA_WIDTH                            | integer                |                                |             |
| GC_USER_WIDTH                            | integer                | 1                              |             |
| GC_ID_WIDTH                              | integer                | 1                              |             |
| GC_DEST_WIDTH                            | integer                | 1                              |             |
| GC_INSTANCE_IDX                          | natural                |                                |             |
| GC_PACKETINFO_QUEUE_COUNT_MAX            | natural                | 1                              |             |
| GC_AXISTREAM_BFM_CONFIG                  | t_axistream_bfm_config | C_AXISTREAM_BFM_CONFIG_DEFAULT |             |
| GC_CMD_QUEUE_COUNT_MAX                   | natural                | 1000                           |             |
| GC_CMD_QUEUE_COUNT_THRESHOLD             | natural                | 950                            |             |
| GC_CMD_QUEUE_COUNT_THRESHOLD_SEVERITY    | t_alert_level          | warning                        |             |
| GC_RESULT_QUEUE_COUNT_MAX                | natural                | 1000                           |             |
| GC_RESULT_QUEUE_COUNT_THRESHOLD          | natural                | 950                            |             |
| GC_RESULT_QUEUE_COUNT_THRESHOLD_SEVERITY | t_alert_level          | WARNING                        |             |
## Ports
| Port name        | Direction | Type           | Description |
| ---------------- | --------- | -------------- | ----------- |
| clk              | in        | std_logic      |             |
| axistream_vvc_if | inout     | t_axistream_if |             |
## Signals
| Name                               | Type          | Description |
| ---------------------------------- | ------------- | ----------- |
| executor_is_busy                   | boolean       |             |
| queue_is_increasing                | boolean       |             |
| last_cmd_idx_executed              | natural       |             |
| terminate_current_cmd              | t_flag_record |             |
| entry_num_in_vvc_activity_register | integer       |             |
## Constants
| Name         | Type         | Value                                                        | Description |
| ------------ | ------------ | ------------------------------------------------------------ | ----------- |
| C_SCOPE      | string       |  C_VVC_NAME & "," & to_string(GC_INSTANCE_IDX)               |             |
| C_VVC_LABELS | t_vvc_labels |  assign_vvc_labels(C_SCOPE, C_VVC_NAME, GC_INSTANCE_IDX, NA) |             |
## Functions
- get_msg_id_panel <font id="function_arguments">(    constant command    : in t_vvc_cmd_record;
    constant vvc_config : in t_vvc_config
  )</font> <font id="function_return">return t_msg_id_panel</font>
## Processes
- cmd_interpreter: _(  )_

- cmd_executor: _(  )_

