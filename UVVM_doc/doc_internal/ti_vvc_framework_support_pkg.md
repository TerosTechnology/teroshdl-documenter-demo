# Package: ti_vvc_framework_support_pkg
## Signals
| Name                                 | Type                                              | Description            |
| ------------------------------------ | ------------------------------------------------- | ---------------------- |
| VVC_BROADCAST                        | std_logic                                         |                        |
| global_trigger_vvc_activity_register | std_logic                                         |                        |
| global_awaiting_completion           | std_logic_vector(C_MAX_NUM_SEQUENCERS-1 downto 0) | ACK on global triggers |
## Constants
| Name                                          | Type                                                                                                                                   | Value                                                                                                                                                                                                                                                                                                     | Description |
| --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| C_VVC_NAME_MAX_LENGTH                         | natural                                                                                                                                |  C_MAX_VVC_NAME_LENGTH                                                                                                                                                                                                                                                                                    |             |
| C_BROADCAST_CMD_STRING_MAX_LENGTH             | natural                                                                                                                                |  300                                                                                                                                                                                                                                                                                                      |             |
| C_VVC_BROADCAST_CMD_DEFAULT                   | t_vvc_broadcast_cmd_record                                                                                                             |  (     operation           => NO_CMD,     msg_id              => NO_ID,     msg                 => (others => NUL),     proc_call           => (others => NUL),     quietness           => NON_QUIET,     delay               => 0 ns,     timeout             => 0 ns,     gen_integer         => -1   ) |             |
| C_DUT_IF_FIELD_CONFIG_DEFAULT                 | t_dut_if_field_config(dut_address(0 downto 0))                                                                                         |  (     dut_address                => (others => '0'),     dut_address_increment      => 0,     data_width                 => 8,     use_field                  => true,     field_description          => "default")                                                                                      |             |
| C_DUT_IF_FIELD_CONFIG_DIRECTION_ARRAY_DEFAULT | t_dut_if_field_config_direction_array(t_direction'low to t_direction'high)(0 to 0)(dut_address(0 downto 0), field_description(1 to 7)) |  (others => (others => C_DUT_IF_FIELD_CONFIG_DEFAULT))                                                                                                                                                                                                                                                    |             |
## Types
| Name                                  | Type                                                                                                                      | Description                                              |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| t_immediate_or_queued                 | (NO_command_type, IMMEDIATE, QUEUED)                                                                                      |                                                          |
| t_flag_record                         |                                                                                                                           |                                                          |
| t_uvvm_state                          | (IDLE, PHASE_A, PHASE_B, INIT_COMPLETED)                                                                                  |                                                          |
| t_lastness                            | (LAST, NOT_LAST)                                                                                                          |                                                          |
| t_broadcastable_cmd                   | (NO_CMD, ENABLE_LOG_MSG, DISABLE_LOG_MSG, FLUSH_COMMAND_QUEUE, INSERT_DELAY, AWAIT_COMPLETION, TERMINATE_CURRENT_COMMAND) |                                                          |
| t_vvc_broadcast_cmd_record            |                                                                                                                           |                                                          |
| t_vvc_operation                       | (TRANSMIT, RECEIVE)                                                                                                       | Type of operation to be executed by the VVC              |
| t_direction                           | (TRANSMIT, RECEIVE)                                                                                                       | Direction of the interface (used by the IF field config) |
| t_field_position                      | (FIRST, MIDDLE, LAST, FIRST_AND_LAST)                                                                                     | Position of a field within a packet                      |
| t_hvvc_to_bridge                      |                                                                                                                           |                                                          |
| t_bridge_to_hvvc                      |                                                                                                                           |                                                          |
| t_dut_if_field_config                 |                                                                                                                           |                                                          |
| t_dut_if_field_config_array           |                                                                                                                           |                                                          |
| t_dut_if_field_config_direction_array |                                                                                                                           |                                                          |
## Functions
- flag_handler <font id="function_arguments">(    signal flag : inout t_flag_record
  )</font> <font id="function_return">return ()</font>
**Description**
Flag handler is a general flag/semaphore handling mechanism between two separate processes/threadsThe idea is to allow one process to set a flag and another to reset it. The flag may then be used by both - or othersMay be used for a message from process 1 to process 2 with acknowledge; - like do-something & done, or valid & ack
- set_flag <font id="function_arguments">(    signal flag : inout t_flag_record
  )</font> <font id="function_return">return ()</font>
**Description**
Sets reset and is_active to 'Z' and pulses set_flag
- reset_flag <font id="function_arguments">(    signal flag : inout t_flag_record
  )</font> <font id="function_return">return ()</font>
**Description**
Sets set and is_active to 'Z' and pulses reset_flag
- await_uvvm_initialization <font id="function_arguments">(    constant dummy : in t_void
  )</font> <font id="function_return">return ()</font>
**Description**
Waits until uvvm has been initialized
- enable_log_msg <font id="function_arguments">(    signal VVC_BROADCAST        : inout std_logic;
    constant msg_id             : in t_msg_id;
    constant msg                : in string := "";
    constant quietness          : in t_quietness := NON_QUIET;
    constant scope              : in string      := C_VVC_CMD_SCOPE_DEFAULT
  )</font> <font id="function_return">return ()</font>
**Description**
Enables a log message for all VVCs
- disable_log_msg <font id="function_arguments">(    signal VVC_BROADCAST        : inout std_logic;
    constant msg_id             : in t_msg_id;
    constant msg                : in string := "";
    constant quietness          : in t_quietness := NON_QUIET;
    constant scope              : in string      := C_VVC_CMD_SCOPE_DEFAULT
  )</font> <font id="function_return">return ()</font>
**Description**
Disables a log message for all VVCs
- flush_command_queue <font id="function_arguments">(    signal VVC_BROADCAST        : inout std_logic;
    constant msg                : in string := "";
    constant scope              : in string := C_VVC_CMD_SCOPE_DEFAULT
  )</font> <font id="function_return">return ()</font>
**Description**
Flushes the command queue for all VVCs
- insert_delay <font id="function_arguments">(    signal VVC_BROADCAST        : inout std_logic;
    constant delay              : in natural;   in clock cycles
    constant msg                : in string  := "";
    constant scope              : in string  := C_VVC_CMD_SCOPE_DEFAULT
  )</font> <font id="function_return">return ()</font>
**Description**
Inserts delay into all VVCs (specified as number of clock cycles)
- insert_delay <font id="function_arguments">(    signal VVC_BROADCAST        : inout std_logic;
    constant delay              : in time;
    constant msg                : in string  := "";
    constant scope              : in string  := C_VVC_CMD_SCOPE_DEFAULT
  )</font> <font id="function_return">return ()</font>
**Description**
Inserts delay into all VVCs (specified as time)
- await_completion <font id="function_arguments">(    signal VVC_BROADCAST        : inout std_logic;
    constant timeout            : in time;
    constant msg                : in string  := "";
    constant scope              : in string  := C_VVC_CMD_SCOPE_DEFAULT
  )</font> <font id="function_return">return ()</font>
**Description**
Wait for all VVCs to finish (specified as time)
- terminate_current_command <font id="function_arguments">(    signal VVC_BROADCAST        : inout std_logic;
    constant msg                : in string  := "";
    constant scope              : in string  := C_VVC_CMD_SCOPE_DEFAULT
  )</font> <font id="function_return">return ()</font>
**Description**
terminates all current tasks
- terminate_all_commands <font id="function_arguments">(    signal VVC_BROADCAST        : inout std_logic;
    constant msg                : in string  := "";
    constant scope              : in string  := C_VVC_CMD_SCOPE_DEFAULT
  )</font> <font id="function_return">return ()</font>
**Description**
terminates all tasks
- transmit_broadcast <font id="function_arguments">(    signal VVC_BROADCAST        : inout std_logic;
    constant operation          : in t_broadcastable_cmd;
    constant proc_call          : in string;
    constant msg_id             : in t_msg_id;
    constant msg                : in string       := "";
    constant quietness          : in t_quietness  := NON_QUIET;
    constant delay              : in time         := 0 ns;
    constant delay_int          : in integer      := -1;
    constant timeout            : in time         := std.env.resolution_limit;
    constant scope              : in string       := C_VVC_CMD_SCOPE_DEFAULT
  )</font> <font id="function_return">return ()</font>
**Description**
Common broadcast transmission routine
- await_completion <font id="function_arguments">(    constant vvc_select    : in    t_vvc_select;
    variable vvc_info_list : inout t_vvc_info_list;
    constant timeout       : in    time;
    constant list_action   : in    t_list_action := CLEAR_LIST;
    constant msg           : in    string := "";
    constant scope         : in    string := C_VVC_CMD_SCOPE_DEFAULT
  )</font> <font id="function_return">return ()</font>
**Description**
Awaits completion of any VVC in the list or until timeout.
- await_completion <font id="function_arguments">(    constant vvc_select  : in    t_vvc_select;
    constant timeout     : in    time;
    constant list_action : in    t_list_action := CLEAR_LIST;
    constant msg         : in    string := "";
    constant scope       : in    string := C_VVC_CMD_SCOPE_DEFAULT
  )</font> <font id="function_return">return ()</font>
**Description**
Awaits completion of all the VVCs in the activity register or until timeout.
- activity_watchdog <font id="function_arguments">(    constant num_exp_vvc  : natural;
    constant timeout      : time;
    constant alert_level  : t_alert_level := TB_ERROR;
    constant msg          : string := "Activity_Watchdog"
  )</font> <font id="function_return">return ()</font>
**Description**
============================================================================Activity Watchdog============================================================================
