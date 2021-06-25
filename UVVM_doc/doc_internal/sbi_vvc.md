# Entity: sbi_vvc
## Diagram
![Diagram](sbi_vvc.svg "Diagram")
## Generics
| Generic name                             | Type                                         | Value                    | Description |
| ---------------------------------------- | -------------------------------------------- | ------------------------ | ----------- |
| GC_ADDR_WIDTH                            | integer range 1 to C_VVC_CMD_ADDR_MAX_LENGTH | 8                        |             |
| GC_DATA_WIDTH                            | integer range 1 to C_VVC_CMD_DATA_MAX_LENGTH | 32                       |             |
| GC_INSTANCE_IDX                          | natural                                      | 1                        |             |
| GC_SBI_CONFIG                            | t_sbi_bfm_config                             | C_SBI_BFM_CONFIG_DEFAULT |             |
| GC_CMD_QUEUE_COUNT_MAX                   | natural                                      | 1000                     |             |
| GC_CMD_QUEUE_COUNT_THRESHOLD             | natural                                      | 950                      |             |
| GC_CMD_QUEUE_COUNT_THRESHOLD_SEVERITY    | t_alert_level                                | warning                  |             |
| GC_RESULT_QUEUE_COUNT_MAX                | natural                                      | 1000                     |             |
| GC_RESULT_QUEUE_COUNT_THRESHOLD          | natural                                      | 950                      |             |
| GC_RESULT_QUEUE_COUNT_THRESHOLD_SEVERITY | t_alert_level                                | warning                  |             |
## Ports
| Port name         | Direction | Type                                                                                                                                                                                     | Description |
| ----------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| clk               | in        | std_logic                                                                                                                                                                                |             |
| sbi_vvc_master_if | inout     | t_sbi_if(addr(GC_ADDR_WIDTH-1 downto 0),                                        wdata(GC_DATA_WIDTH-1 downto 0),                                        rdata(GC_DATA_WIDTH-1 downto 0)) |             |
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

