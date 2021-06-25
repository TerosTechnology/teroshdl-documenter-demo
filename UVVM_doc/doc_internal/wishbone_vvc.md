# Entity: wishbone_vvc
## Diagram
![Diagram](wishbone_vvc.svg "Diagram")
## Generics
| Generic name                             | Type                  | Value                         | Description |
| ---------------------------------------- | --------------------- | ----------------------------- | ----------- |
| GC_ADDR_WIDTH                            | integer               | 8                             |             |
| GC_DATA_WIDTH                            | integer               | 32                            |             |
| GC_INSTANCE_IDX                          | natural               | 1                             |             |
| GC_WISHBONE_BFM_CONFIG                   | t_wishbone_bfm_config | C_WISHBONE_BFM_CONFIG_DEFAULT |             |
| GC_CMD_QUEUE_COUNT_MAX                   | natural               | 1000                          |             |
| GC_CMD_QUEUE_COUNT_THRESHOLD             | natural               | 950                           |             |
| GC_CMD_QUEUE_COUNT_THRESHOLD_SEVERITY    | t_alert_level         | WARNING                       |             |
| GC_RESULT_QUEUE_COUNT_MAX                | natural               | 1000                          |             |
| GC_RESULT_QUEUE_COUNT_THRESHOLD          | natural               | 950                           |             |
| GC_RESULT_QUEUE_COUNT_THRESHOLD_SEVERITY | t_alert_level         | WARNING                       |             |
## Ports
| Port name              | Direction | Type          | Description |
| ---------------------- | --------- | ------------- | ----------- |
| clk                    | in        | std_logic     |             |
| wishbone_vvc_master_if | inout     | t_wishbone_if |             |
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

