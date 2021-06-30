# Package: td_target_support_pkg

## Signals

| Name            | Type      | Description            |
| --------------- | --------- | ---------------------- |
| global_vvc_ack  | std_logic | ACK on global triggers |
| global_vvc_busy | std_logic | ACK on global triggers |
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
- resolved <font id="function_arguments">( input_vector : t_vvc_target_record_drivers) </font> <font id="function_return">return t_vvc_target_record_unresolved </font>
- to_string <font id="function_arguments">( value         : t_vvc_target_record; vvc_instance  : integer   := -1; vvc_channel   : t_channel := NA ) </font> <font id="function_return">return string </font>
**Description**
to_string method for VVC name, instance and channel- If channel is set to NA, it will not be included in the string
- send_command_to_vvc <font id="function_arguments">(                  -- VVC dedicated shared command used  shared_vvc_cmd signal   vvc_target   : inout t_vvc_target_record; constant timeout      : in    time                 := std.env.resolution_limit; constant scope        : in    string               := C_VVC_CMD_SCOPE_DEFAULT; constant msg_id_panel : in    t_msg_id_panel       := shared_msg_id_panel ) </font> <font id="function_return">return ()</font>
**Description**
Sends command to VVC and waits for ACK or timeout- Logs with ID_UVVM_SEND_CMD when sending to VVC- Logs with ID_UVVM_CMD_ACK when ACK or timeout occurs
- set_vvc_target_defaults <font id="function_arguments">( constant  vvc_name  : in string; constant  scope     : in string := C_VVC_CMD_SCOPE_DEFAULT ) </font> <font id="function_return">return t_vvc_target_record </font>
**Description**
Returns a vvc target record with vvc_name and values specified in C_VVC_TARGET_RECORD_DEFAULT
- set_general_target_and_command_fields <font id="function_arguments">(   -- VVC dedicated shared command used  shared_vvc_cmd signal target               : inout t_vvc_target_record; constant vvc_instance_idx   : in integer; constant proc_call          : in string; constant msg                : in string; constant command_type       : in t_immediate_or_queued; constant operation          : in t_operation ) </font> <font id="function_return">return ()</font>
**Description**
Sets target index and channel, and updates shared_vvc_cmd
- set_general_target_and_command_fields <font id="function_arguments">(  -- VVC dedicated shared command used  shared_vvc_cmd signal target               : inout t_vvc_target_record; constant vvc_instance_idx   : in integer; constant vvc_channel        : in t_channel; constant proc_call          : in string; constant msg                : in string; constant command_type       : in t_immediate_or_queued; constant operation          : in t_operation ) </font> <font id="function_return">return ()</font>
**Description**
Sets target index and channel, and updates shared_vvc_cmd
- acknowledge_cmd <font id="function_arguments">( signal   vvc_ack      : inout std_logic; constant command_idx  : in natural ) </font> <font id="function_return">return ()</font>
**Description**
Drives global_vvc_ack signal (to '1') for 1 delta cycle, then sets it back to 'Z'.
- get_vvc_index_in_activity_register <font id="function_arguments">( signal   vvc_target                	    : in t_vvc_target_record; constant vvc_instance_idx          	    : in    integer; constant vvc_channel               	    : in    t_channel; variable vvc_idx_in_activity_register   : inout t_integer_array(0 to C_MAX_TB_VVC_NUM); variable num_vvc_instances              : inout natural range 0 to C_MAX_TB_VVC_NUM ) </font> <font id="function_return">return ()</font>
