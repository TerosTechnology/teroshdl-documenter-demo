# Package: support_pkg
## Functions
- blocking_send_to_bridge <font id="function_arguments">(    signal   hvvc_to_bridge   : inout t_hvvc_to_bridge;
    signal   bridge_to_hvvc   : in  t_bridge_to_hvvc;
    constant data_words       : in  t_slv_array;
    constant dut_if_field_idx : in  integer;
    constant dut_if_field_pos : in  t_field_position;
    constant scope            : in  string;
    constant msg_id_panel     : in  t_msg_id_panel
  )</font> <font id="function_return">return ()</font>
- blocking_request_from_bridge <font id="function_arguments">(    signal   hvvc_to_bridge   : inout t_hvvc_to_bridge;
    signal   bridge_to_hvvc   : in  t_bridge_to_hvvc;
    constant num_data_words   : in  positive;
    constant dut_if_field_idx : in  integer;
    constant dut_if_field_pos : in  t_field_position;
    constant scope            : in  string;
    constant msg_id_panel     : in  t_msg_id_panel
  )</font> <font id="function_return">return ()</font>
- get_dut_address_config <font id="function_arguments">(    constant dut_if_field_config    : in  t_dut_if_field_config_direction_array;
    signal   hvvc_to_bridge         : in  t_hvvc_to_bridge;
    variable dut_address            : out unsigned;
    variable dut_address_increment  : out integer
  )</font> <font id="function_return">return ()</font>
- get_data_width_config <font id="function_arguments">(    constant dut_if_field_config : in  t_dut_if_field_config_direction_array;
    signal   hvvc_to_bridge      : in  t_hvvc_to_bridge;
    variable data_width          : out positive
  )</font> <font id="function_return">return ()</font>
