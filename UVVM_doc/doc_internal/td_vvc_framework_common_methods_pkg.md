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
**Description**
See description above
- await_completion <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant vvc_channel               : in    t_channel;
    constant wanted_idx                : in    integer;
    constant timeout                   : in    time;
    constant msg                       : in    string         := "";
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
**Description**
VVC interpreter IMMEDIATE command- Awaits completion of the specified command 'wanted_idx' in the queue for the specified VVC, or  until timeout.
- await_completion <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant wanted_idx                : in    integer;
    constant timeout                   : in    time;
    constant msg                       : in    string         := "";
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
**Description**
See description above
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
**Description**
VVC interpreter IMMEDIATE command- Waits for the first of multiple VVCs to finish :  - Awaits completion of all commands in the queue for the specified VVC, or  - until global_awaiting_completion /= '1' (any of the other involved VVCs completed).
- await_any_completion <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant lastness                  : in    t_lastness;
    constant timeout                   : in    time           := 100 ns;
    constant msg                       : in    string         := "";
    constant awaiting_completion_idx   : in    natural        := 0;
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
**Description**
Overload without vvc_channel
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
**Description**
Overload with wanted_idx- Awaits completion of the specified command 'wanted_idx' in the queue for the specified VVC, or  - until global_awaiting_completion /= '1' (any of the other involved VVCs completed).
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
**Description**
Overload without vvc_channel
- disable_log_msg <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant vvc_channel               : in    t_channel;
    constant msg_id                    : in    t_msg_id;
    constant msg                       : in    string         := "";
    constant quietness                 : in    t_quietness    := NON_QUIET;
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
**Description**
VVC interpreter IMMEDIATE command- Disables the specified msg_id for the VVC
- disable_log_msg <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant msg_id                    : in    t_msg_id;
    constant msg                       : in    string         := "";
    constant quietness                 : in    t_quietness    := NON_QUIET;
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
**Description**
See description above
- enable_log_msg <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant vvc_channel               : in    t_channel;
    constant msg_id                    : in    t_msg_id;
    constant msg                       : in    string         := "";
    constant quietness                 : in    t_quietness    := NON_QUIET;
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
**Description**
VVC interpreter IMMEDIATE command- Enables the specified msg_id for the VVC
- enable_log_msg <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant msg_id                    : in    t_msg_id;
    constant msg                       : in    string         := "";
    constant quietness                 : in    t_quietness    := NON_QUIET;
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
**Description**
See description above
- flush_command_queue <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant vvc_channel               : in    t_channel;
    constant msg                       : in    string         := "";
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
**Description**
VVC interpreter IMMEDIATE command- Flushes the command queue of the specified VVC
- flush_command_queue <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant msg                       : in    string         := "";
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
**Description**
See description above
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
**Description**
VVC interpreter IMMEDIATE command- Fetches result from a VVC- Requires that result is available (i.e. already executed in respective VVC)- Logs with ID ID_UVVM_CMD_RESULTThe 'result' parameter is of type t_vvc_result tosupport that the BFM returns something other than a std_logic_vector.
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
**Description**
-- Same as above but without fetch_is_accepted.-- Will trigger alert with alert_level if not OK.
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
**Description**
-- - This version does not use vvc_channel.-- - Fetches result from a VVC-- - Requires that result is available (i.e. already executed in respective VVC)-- - Logs with ID ID_UVVM_CMD_RESULT
- fetch_result <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant wanted_idx                : in    integer;
    variable result                    : out   t_vvc_result;
    constant msg                       : in    string         := "";
    constant alert_level               : in    t_alert_level  := TB_ERROR;
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
**Description**
-- Same as above but without fetch_is_accepted.-- Will trigger alert with alert_level if not OK.
- insert_delay <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant vvc_channel               : in    t_channel;
    constant delay                     : in    natural;   in clock cycles
    constant msg                       : in    string         := "";
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
**Description**
VVC executor QUEUED command- Inserts delay for 'delay' clock cycles
- insert_delay <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant delay                     : in    natural;   in clock cycles
    constant msg                       : in    string         := "";
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
**Description**
See description above
- insert_delay <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant vvc_channel               : in    t_channel;
    constant delay                     : in    time;
    constant msg                       : in    string         := "";
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
**Description**
VVC executor QUEUED command- Inserts delay for a given time
- insert_delay <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant delay                     : in    time;
    constant msg                       : in    string         := "";
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
**Description**
See description above
- terminate_current_command <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant vvc_channel               : in    t_channel      := NA;
    constant msg                       : in    string         := "";
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
**Description**
VVC interpreter IMMEDIATE command- Terminates the current command being processed in the VVC executor
- terminate_current_command <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant msg                       : in    string         := "";
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
**Description**
Overload without VVC channel
- terminate_all_commands <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant vvc_channel               : in    t_channel      := NA;
    constant msg                       : in    string         := "";
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
**Description**
VVC interpreter IMMEDIATE command- Terminates the current command being processed in the VVC executor, and  flushes the command queue
- terminate_all_commands <font id="function_arguments">(    signal   vvc_target                : inout t_vvc_target_record;
    constant vvc_instance_idx          : in    integer;
    constant msg                       : in    string         := "";
    constant scope                     : in    string         := C_VVC_CMD_SCOPE_DEFAULT;
    constant parent_msg_id_panel       : in    t_msg_id_panel := shared_msg_id_panel UVVM: temporary fix for HVVC, replace for C_UNUSED_MSG_ID_PANEL in v3.0
  )</font> <font id="function_return">return ()</font>
**Description**
Overload without VVC channel
