# Package: td_vvc_framework_common_methods_pkg
## Functions
- await_completion <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant vvc_channel               : in    t_channel;
    constant timeout                   : in    time;
    constant msg                       : in    string         := "";
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
- await_completion <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant timeout                   : in    time;
    constant msg                       : in    string         := "";
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
- await_completion <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant vvc_channel               : in    t_channel;
    constant wanted_idx                : in    integer;
    constant timeout                   : in    time;
    constant msg                       : in    string         := "";
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
- await_completion <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant wanted_idx                : in    integer;
    constant timeout                   : in    time;
    constant msg                       : in    string         := "";
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
- await_any_completion <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant vvc_channel               : in    t_channel;
    constant lastness                  : in    t_lastness;
    constant timeout                   : in    time           := 100 ns;
    constant msg                       : in    string         := "";
    constant awaiting_completion_idx   : in    natural        := 0;
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
- await_any_completion <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant lastness                  : in    t_lastness;
    constant timeout                   : in    time           := 100 ns;
    constant msg                       : in    string         := "";
    constant awaiting_completion_idx   : in    natural        := 0;
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
- await_any_completion <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant vvc_channel               : in    t_channel;
    constant wanted_idx                : in    integer;
    constant lastness                  : in    t_lastness;
    constant timeout                   : in    time           := 100 ns;
    constant msg                       : in    string         := "";
    constant awaiting_completion_idx   : in    natural        := 0;
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
- await_any_completion <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant wanted_idx                : in    integer;
    constant lastness                  : in    t_lastness;
    constant timeout                   : in    time           := 100 ns;
    constant msg                       : in    string         := "";
    constant awaiting_completion_idx   : in    natural        := 0;
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
- disable_log_msg <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant vvc_channel               : in    t_channel;
    constant msg_id                    : in    t_msg_id;
    constant msg                       : in    string         := "";
    constant quietness                 : in    t_quietness    := NON_QUIET;
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
- disable_log_msg <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant msg_id                    : in    t_msg_id;
    constant msg                       : in    string         := "";
    constant quietness                 : in    t_quietness    := NON_QUIET;
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
- enable_log_msg <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant vvc_channel               : in    t_channel;
    constant msg_id                    : in    t_msg_id;
    constant msg                       : in    string         := "";
    constant quietness                 : in    t_quietness    := NON_QUIET;
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
- enable_log_msg <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant msg_id                    : in    t_msg_id;
    constant msg                       : in    string         := "";
    constant quietness                 : in    t_quietness    := NON_QUIET;
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
- flush_command_queue <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant vvc_channel               : in    t_channel;
    constant msg                       : in    string         := "";
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
- flush_command_queue <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant msg                       : in    string         := "";
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
- fetch_result <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant vvc_channel               : in    t_channel;
    constant wanted_idx                : in    integer;
    variable result                    : out   t_vvc_result;
    variable fetch_is_accepted         : out   boolean;
    constant msg                       : in    string         := "";
    constant alert_level               : in    t_alert_level  := TB_ERROR;
    constant caller_name               : in    string         := "base_procedure";
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
- fetch_result <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant vvc_channel               : in    t_channel;
    constant wanted_idx                : in    integer;
    variable result                    : out   t_vvc_result;
    constant msg                       : in    string         := "";
    constant alert_level               : in    t_alert_level  := TB_ERROR;
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
- fetch_result <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant wanted_idx                : in    integer;
    variable result                    : out   t_vvc_result;
    variable fetch_is_accepted         : out   boolean;
    constant msg                       : in    string         := "";
    constant alert_level               : in    t_alert_level  := TB_ERROR;
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
- fetch_result <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant wanted_idx                : in    integer;
    variable result                    : out   t_vvc_result;
    constant msg                       : in    string         := "";
    constant alert_level               : in    t_alert_level  := TB_ERROR;
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
- insert_delay <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant vvc_channel               : in    t_channel;
    constant delay                     : in    natural;   in clock cycles
    constant msg                       : in    string         := "";
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
- insert_delay <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant delay                     : in    natural;   in clock cycles
    constant msg                       : in    string         := "";
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
- insert_delay <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant vvc_channel               : in    t_channel;
    constant delay                     : in    time;
    constant msg                       : in    string         := "";
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
- insert_delay <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant delay                     : in    time;
    constant msg                       : in    string         := "";
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
- terminate_current_command <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant vvc_channel               : in    t_channel      := NA;
    constant msg                       : in    string         := "";
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
- terminate_current_command <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant msg                       : in    string         := "";
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
- terminate_all_commands <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant vvc_channel               : in    t_channel      := NA;
    constant msg                       : in    string         := "";
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
- terminate_all_commands <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant msg                       : in    string         := "";
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
