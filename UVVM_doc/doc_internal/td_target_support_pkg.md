# Package: td_target_support_pkg
## Signals
| Name            | Type      | Description |
| --------------- | --------- | ----------- |
| global_vvc_ack  | std_logic |             |
| global_vvc_busy | std_logic |             |
## Constants
| Name                        | Type                           | Value                                                                                                                                             | Description |
| --------------------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| C_VVC_TARGET_RECORD_DEFAULT | t_vvc_target_record_unresolved |  (     trigger            =>  'L',     vvc_name           =>  (others => '?'),     vvc_instance_idx   =>  -1,     vvc_channel        =>  NA     ) |             |
| C_VVC_INDEX_NOT_FOUND       | integer                        |  -1                                                                                                                                               |             |
## Types
| Name                           | Type | Description |
| ------------------------------ | ---- | ----------- |
| t_vvc_target_record_unresolved |      |             |
| t_vvc_target_record_drivers    |      |             |
## Functions
- resolved <font id="function_arguments">( input_vector : t_vvc_target_record_drivers)</font> <font id="function_return">return t_vvc_target_record_unresolved</font>
- to_string <font id="function_arguments">(    value         : t_vvc_target_record;
    vvc_instance  : integer   := -1;
    vvc_channel   : t_channel := NA
  )</font> <font id="function_return">return string</font>
- send_command_to_vvc <font id="function_arguments">(                   VVC dedicated shared command used  shared_vvc_cmd    signal   vvc_target   : inout t_vvc_target_record;
    constant timeout      : in    time                 := std.env.resolution_limit;
    constant scope        : in    string               := C_VVC_CMD_SCOPE_DEFAULT;
    constant msg_id_panel : in    t_msg_id_panel       := shared_msg_id_panel
  )</font> <font id="function_return">return ()</font>
- set_vvc_target_defaults <font id="function_arguments">(    constant  vvc_name  : in string;
    constant  scope     : in string := C_VVC_CMD_SCOPE_DEFAULT
  )</font> <font id="function_return">return t_vvc_target_record</font>
- set_general_target_and_command_fields <font id="function_arguments">(    VVC dedicated shared command used  shared_vvc_cmd    signal target               : inout t_vvc_target_record;
    constant vvc_instance_idx   : in integer;
    constant proc_call          : in string;
    constant msg                : in string;
    constant command_type       : in t_immediate_or_queued;
    constant operation          : in t_operation
  )</font> <font id="function_return">return ()</font>
- set_general_target_and_command_fields <font id="function_arguments">(   VVC dedicated shared command used  shared_vvc_cmd    signal target               : inout t_vvc_target_record;
    constant vvc_instance_idx   : in integer;
    constant vvc_channel        : in t_channel;
    constant proc_call          : in string;
    constant msg                : in string;
    constant command_type       : in t_immediate_or_queued;
    constant operation          : in t_operation
  )</font> <font id="function_return">return ()</font>
- acknowledge_cmd <font id="function_arguments">(    signal   vvc_ack      : inout std_logic;
    constant command_idx  : in natural
  )</font> <font id="function_return">return ()</font>
- get_vvc_index_in_activity_register <font id="function_arguments">(    signal   vvc_target                	    : in t_vvc_target_record;
    constant vvc_instance_idx          	    : in    integer;
    constant vvc_channel               	    : in    t_channel;
    variable vvc_idx_in_activity_register   : inout t_integer_array(0 to C_MAX_TB_VVC_NUM);
    variable num_vvc_instances              : inout natural range 0 to C_MAX_TB_VVC_NUM
    )</font> <font id="function_return">return ()</font>
