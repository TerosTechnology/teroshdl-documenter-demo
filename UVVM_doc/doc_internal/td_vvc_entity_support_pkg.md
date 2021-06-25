# Package: td_vvc_entity_support_pkg
## Types
| Name         | Type | Description |
| ------------ | ---- | ----------- |
| t_vvc_labels |      |             |
## Functions
- assign_vvc_labels <font id="function_arguments">(    scope        : string;
    vvc_name     : string;
    instance_idx : integer;
    channel      : t_channel
    )</font> <font id="function_return">return t_vvc_labels</font>
- vvc_constructor <font id="function_arguments">(    constant scope                                 : in string;
    constant instance_idx                          : in natural;
    variable vvc_config                            : inout t_vvc_config;
    variable command_queue                         : inout work.td_cmd_queue_pkg.t_generic_queue;
    variable result_queue                          : inout work.td_result_queue_pkg.t_generic_queue;
    constant bfm_config                            : in t_bfm_config;
    constant cmd_queue_count_max                   : in natural;
    constant cmd_queue_count_threshold             : in natural;
    constant cmd_queue_count_threshold_severity    : in t_alert_level;
    constant result_queue_count_max                : in natural;
    constant result_queue_count_threshold          : in natural;
    constant result_queue_count_threshold_severity : in t_alert_level
  )</font> <font id="function_return">return ()</font>
- initialize_interpreter <font id="function_arguments">(    signal terminate_current_cmd      : out t_flag_record;
    signal global_awaiting_completion : out std_logic_vector(C_MAX_NUM_SEQUENCERS-1 downto 0)
    )</font> <font id="function_return">return ()</font>
- get_msg_id_panel <font id="function_arguments">(    constant command    : in t_vvc_cmd_record;
    constant vvc_config : in t_vvc_config
  )</font> <font id="function_return">return t_msg_id_panel</font>
- await_cmd_from_sequencer <font id="function_arguments">(    constant vvc_labels        : in    t_vvc_labels;
    constant vvc_config        : in    t_vvc_config;
    signal VVCT                : in    t_vvc_target_record;
    signal VVC_BROADCAST       : inout std_logic;
    signal global_vvc_busy     : inout std_logic;
    signal vvc_ack             : out   std_logic;
    variable output_vvc_cmd    : out   t_vvc_cmd_record;
    constant msg_id_panel      : in    t_msg_id_panel := shared_msg_id_panel UVVM: unused, remove in v3.0
    )</font> <font id="function_return">return ()</font>
- await_cmd_from_sequencer <font id="function_arguments">(    constant vvc_labels        : in t_vvc_labels;
    constant vvc_config        : in t_vvc_config;
    signal VVCT                : in t_vvc_target_record;
    signal VVC_BROADCAST       : inout std_logic;
    signal global_vvc_busy     : inout std_logic;
    signal vvc_ack             : out std_logic;
    constant shared_vvc_cmd    : in t_vvc_cmd_record;
    variable output_vvc_cmd    : out t_vvc_cmd_record
    )</font> <font id="function_return">return ()</font>
- put_command_on_queue <font id="function_arguments">(    constant command             : in t_vvc_cmd_record;
    variable command_queue       : inout work.td_cmd_queue_pkg.t_generic_queue;
    variable vvc_status          : inout t_vvc_status;
    signal   queue_is_increasing : out   boolean
    )</font> <font id="function_return">return ()</font>
- interpreter_await_completion <font id="function_arguments">(    constant command                              : in t_vvc_cmd_record;
    variable command_queue                        : inout work.td_cmd_queue_pkg.t_generic_queue;
    constant vvc_config                           : in t_vvc_config;
    signal executor_is_busy                       : in boolean;
    constant vvc_labels                           : in t_vvc_labels;
    signal last_cmd_idx_executed                  : in natural;
    constant await_completion_pending_msg_id      : in t_msg_id := ID_IMMEDIATE_CMD_WAIT;
    constant await_completion_finished_msg_id     : in t_msg_id := ID_IMMEDIATE_CMD
    )</font> <font id="function_return">return ()</font>
- interpreter_await_any_completion <font id="function_arguments">(    constant command                              : in t_vvc_cmd_record;
    variable command_queue                        : inout work.td_cmd_queue_pkg.t_generic_queue;
    constant vvc_config                           : in t_vvc_config;
    signal executor_is_busy                       : in boolean;
    constant vvc_labels                           : in t_vvc_labels;
    signal last_cmd_idx_executed                  : in natural;
    signal global_awaiting_completion             : inout std_logic_vector;  Handshake with other VVCs performing await_any_completion
    constant await_completion_pending_msg_id      : in t_msg_id := ID_IMMEDIATE_CMD_WAIT;
    constant await_completion_finished_msg_id     : in t_msg_id := ID_IMMEDIATE_CMD
    )</font> <font id="function_return">return ()</font>
- interpreter_flush_command_queue <font id="function_arguments">(    constant command            : in t_vvc_cmd_record;
    variable command_queue      : inout work.td_cmd_queue_pkg.t_generic_queue;
    constant vvc_config         : in t_vvc_config;
    variable vvc_status         : inout t_vvc_status;
    constant vvc_labels         : in t_vvc_labels
    )</font> <font id="function_return">return ()</font>
- interpreter_terminate_current_command <font id="function_arguments">(    constant command              : in t_vvc_cmd_record;
    constant vvc_config           : in t_vvc_config;
    constant vvc_labels           : in t_vvc_labels;
    signal terminate_current_cmd  : inout t_flag_record;
    constant executor_is_busy     : in boolean := true
    )</font> <font id="function_return">return ()</font>
- interpreter_fetch_result <font id="function_arguments">(    variable result_queue           : inout work.td_result_queue_pkg.t_generic_queue;
    constant command                : in t_vvc_cmd_record;
    constant vvc_config             : in t_vvc_config;
    constant vvc_labels             : in t_vvc_labels;
    constant last_cmd_idx_executed  : in natural;
    variable shared_vvc_response    : inout work.vvc_cmd_pkg.t_vvc_response
    )</font> <font id="function_return">return ()</font>
- initialize_executor <font id="function_arguments">(    signal terminate_current_cmd  : inout t_flag_record
    )</font> <font id="function_return">return ()</font>
- fetch_command_and_prepare_executor <font id="function_arguments">(    variable command             : inout t_vvc_cmd_record;
    variable command_queue       : inout work.td_cmd_queue_pkg.t_generic_queue;
    constant vvc_config          : in    t_vvc_config;
    variable vvc_status          : inout t_vvc_status;
    signal   queue_is_increasing : in    boolean;
    signal   executor_is_busy    : inout boolean;
    constant vvc_labels          : in    t_vvc_labels;
    constant msg_id_panel        : in    t_msg_id_panel := shared_msg_id_panel; UVVM: unused, remove in v3.0
    constant executor_id         : in    t_msg_id := ID_CMD_EXECUTOR;
    constant executor_wait_id    : in    t_msg_id := ID_CMD_EXECUTOR_WAIT
    )</font> <font id="function_return">return ()</font>
- store_result <font id="function_arguments">(    variable result_queue  : inout work.td_result_queue_pkg.t_generic_queue;
    constant cmd_idx       : in natural;
    constant result        : in t_vvc_result
    )</font> <font id="function_return">return ()</font>
- insert_inter_bfm_delay_if_requested <font id="function_arguments">(    constant vvc_config                         : in t_vvc_config;
    constant command_is_bfm_access              : in boolean;
    constant timestamp_start_of_last_bfm_access : in time;
    constant timestamp_end_of_last_bfm_access   : in time;
    constant msg_id_panel                       : in t_msg_id_panel;
    constant scope                              : in string          := C_SCOPE
  )</font> <font id="function_return">return ()</font>
- insert_inter_bfm_delay_if_requested <font id="function_arguments">(    constant vvc_config                           : in t_vvc_config;
    constant command_is_bfm_access                : in boolean;
    constant timestamp_start_of_last_bfm_access   : in time;
    constant timestamp_end_of_last_bfm_access     : in time;
    constant scope                                : in string := C_SCOPE
  )</font> <font id="function_return">return ()</font>
- broadcast_cmd_to_shared_cmd <font id="function_arguments">(    constant broadcast_cmd : t_broadcastable_cmd
  )</font> <font id="function_return">return t_operation</font>
- get_command_type_from_operation <font id="function_arguments">(    constant broadcast_cmd : t_broadcastable_cmd
  )</font> <font id="function_return">return t_immediate_or_queued</font>
- populate_shared_vvc_cmd_with_broadcast <font id="function_arguments">(    variable output_vvc_cmd   : out t_vvc_cmd_record;
    constant scope            : in  string := C_SCOPE
  )</font> <font id="function_return">return ()</font>
