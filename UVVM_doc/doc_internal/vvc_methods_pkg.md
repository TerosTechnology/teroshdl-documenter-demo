# Package: vvc_methods_pkg
## Signals
| Name          | Type                | Description |
| ------------- | ------------------- | ----------- |
| WISHBONE_VVCT | t_vvc_target_record |             |
## Constants
| Name                               | Type               | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Description                       |
| ---------------------------------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| C_VVC_NAME                         | string             |  "WISHBONE_VVC"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                   |
| C_WISHBONE_INTER_BFM_DELAY_DEFAULT | t_inter_bfm_delay  |  (     delay_type                          => NO_DELAY,     delay_in_time                       => 0 ns,     inter_bfm_delay_violation_severity  => WARNING   )                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Type found in UVVM-Util types_pkg |
| C_WISHBONE_VVC_CONFIG_DEFAULT      | t_vvc_config       |  (     inter_bfm_delay                       => C_WISHBONE_INTER_BFM_DELAY_DEFAULT,     cmd_queue_count_max                   => C_CMD_QUEUE_COUNT_MAX,     cmd_queue_count_threshold             => C_CMD_QUEUE_COUNT_THRESHOLD,     cmd_queue_count_threshold_severity    => C_CMD_QUEUE_COUNT_THRESHOLD_SEVERITY,     result_queue_count_max                => C_RESULT_QUEUE_COUNT_MAX,     result_queue_count_threshold_severity => C_RESULT_QUEUE_COUNT_THRESHOLD_SEVERITY,     result_queue_count_threshold          => C_RESULT_QUEUE_COUNT_THRESHOLD,     bfm_config                            => C_WISHBONE_BFM_CONFIG_DEFAULT,     msg_id_panel                          => C_VVC_MSG_ID_PANEL_DEFAULT,     parent_msg_id_panel                   => C_VVC_MSG_ID_PANEL_DEFAULT   ) |                                   |
| C_VVC_STATUS_DEFAULT               | t_vvc_status       |  (     current_cmd_idx      => 0,     previous_cmd_idx     => 0,     pending_cmd_cnt      => 0   )                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                   |
| C_TRANSACTION_INFO_DEFAULT         | t_transaction_info |  (     -- Example:     operation           =>  NO_OPERATION,     addr                => (others => '0'),     data                => (others => '0'),     msg                 => (others => ' ')   )                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                   |
## Types
| Name                     | Type | Description                                                           |
| ------------------------ | ---- | --------------------------------------------------------------------- |
| t_vvc_config             |      |                                                                       |
| t_vvc_config_array       |      |                                                                       |
| t_vvc_status             |      |                                                                       |
| t_vvc_status_array       |      |                                                                       |
| t_transaction_info       |      | Transaction information to include in the wave view during simulation |
| t_transaction_info_array |      |                                                                       |
## Functions
- wishbone_write <font id="function_arguments">(    signal   VVCT                : inout t_vvc_target_record;
    constant vvc_instance_idx    : in    integer;
    constant addr                : in    unsigned;
    constant data                : in    std_logic_vector;
    constant msg                 : in    string;
    constant scope               : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel : in    t_msg_id_panel := C_UNUSED_MSG_ID_PANEL  Only intended for usage by parent HVVCs
  )</font> <font id="function_return">return ()</font>
- wishbone_read <font id="function_arguments">(    signal   VVCT                : inout t_vvc_target_record;
    constant vvc_instance_idx    : in    integer;
    constant addr                : in    unsigned;
    constant data_routing        : in    t_data_routing;
    constant msg                 : in    string;
    constant scope               : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel : in    t_msg_id_panel := C_UNUSED_MSG_ID_PANEL  Only intended for usage by parent HVVCs
  )</font> <font id="function_return">return ()</font>
- wishbone_read <font id="function_arguments">(    signal   VVCT                : inout t_vvc_target_record;
    constant vvc_instance_idx    : in    integer;
    constant addr                : in    unsigned;
    constant msg                 : in    string;
    constant scope               : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel : in    t_msg_id_panel := C_UNUSED_MSG_ID_PANEL  Only intended for usage by parent HVVCs
  )</font> <font id="function_return">return ()</font>
- wishbone_check <font id="function_arguments">(    signal   VVCT                : inout t_vvc_target_record;
    constant vvc_instance_idx    : in    integer;
    constant addr                : in    unsigned;
    constant data                : in    std_logic_vector;
    constant msg                 : in    string;
    constant alert_level         : in    t_alert_level  := ERROR;
    constant scope               : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel : in    t_msg_id_panel := C_UNUSED_MSG_ID_PANEL  Only intended for usage by parent HVVCs
  )</font> <font id="function_return">return ()</font>
- update_vvc_activity_register <font id="function_arguments">( signal global_trigger_vvc_activity_register : inout std_logic;                                          variable vvc_status                         : inout t_vvc_status;
                                          constant activity                           : in    t_activity;
                                          constant entry_num_in_vvc_activity_register : in    integer;
                                          constant last_cmd_idx_executed              : in    natural;
                                          constant command_queue_is_empty             : in    boolean;
                                          constant scope                              : in    string := C_VVC_NAME)</font> <font id="function_return">return ()</font>
- pad_wishbone_sb <font id="function_arguments">(    constant data : in std_logic_vector
  )</font> <font id="function_return">return std_logic_vector</font>
