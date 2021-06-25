# Package: axi_stream_pkg
## Constants
| Name                                | Type                          | Value                                                                                                                                                                                                                                                                                                                                                                | Description                                                                                                                                             |
| ----------------------------------- | ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| null_stall_config                   | stall_config_t                |  (     stall_probability => 0.0,     min_stall_cycles  => 0,     max_stall_cycles  => 0     )                                                                                                                                                                                                                                                                        |                                                                                                                                                         |
| null_axi_stream_protocol_checker    | axi_stream_protocol_checker_t |  (     p_type        => null_component,     p_actor       => null_actor,     p_data_length => 0,     p_id_length   => 0,     p_dest_length => 0,     p_user_length => 0,     p_logger      => null_logger,     p_max_waits   => 0   )                                                                                                                                |                                                                                                                                                         |
| default_axi_stream_protocol_checker | axi_stream_protocol_checker_t |  (     p_type        => default_component,     p_actor       => null_actor,     p_data_length => 0,     p_id_length   => 0,     p_dest_length => 0,     p_user_length => 0,     p_logger      => null_logger,     p_max_waits   => 0   )                                                                                                                             | The default protocol checker is used to specify that the checkerconfiguration is defined by the parent component into which the checker isinstantiated. |
| null_axi_stream_monitor             | axi_stream_monitor_t          |  (     p_type             => null_component,     p_actor            => null_actor,     p_data_length      => 0,     p_id_length        => 0,     p_dest_length      => 0,     p_user_length      => 0,     p_logger           => null_logger,     p_protocol_checker => null_axi_stream_protocol_checker   )                                                         |                                                                                                                                                         |
| default_axi_stream_monitor          | axi_stream_monitor_t          |  (     p_type             => default_component,     p_actor            => null_actor,     p_data_length      => 0,     p_id_length        => 0,     p_dest_length      => 0,     p_user_length      => 0,     p_logger           => null_logger,     p_protocol_checker => null_axi_stream_protocol_checker   )                                                      | The default monitor is used to specify that the monitorconfiguration is defined by the parent component into which the monitor isinstantiated.          |
| null_axi_stream_master              | axi_stream_master_t           |  (     p_actor            => null_actor,     p_data_length      => 0,     p_id_length        => 0,     p_dest_length      => 0,     p_user_length      => 0,     p_stall_config     => null_stall_config,     p_logger           => null_logger,     p_monitor          => null_axi_stream_monitor,     p_protocol_checker => null_axi_stream_protocol_checker     ) |                                                                                                                                                         |
| null_axi_stream_slave               | axi_stream_slave_t            |  (     p_actor            => null_actor,     p_data_length      => 0,     p_id_length        => 0,     p_dest_length      => 0,     p_user_length      => 0,     p_stall_config     => null_stall_config,     p_logger           => null_logger,     p_monitor          => null_axi_stream_monitor,     p_protocol_checker => null_axi_stream_protocol_checker     ) |                                                                                                                                                         |
| axi_stream_logger                   | logger_t                      |  get_logger("vunit_lib:axi_stream_pkg")                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                         |
| axi_stream_checker                  | checker_t                     |  new_checker(axi_stream_logger)                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                         |
| push_axi_stream_msg                 | msg_type_t                    |  new_msg_type("push axi stream")                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                         |
| pop_axi_stream_msg                  | msg_type_t                    |  new_msg_type("pop axi stream")                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                         |
| check_axi_stream_msg                | msg_type_t                    |  new_msg_type("check axi stream")                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                         |
| axi_stream_transaction_msg          | msg_type_t                    |  new_msg_type("axi stream transaction")                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                         |
## Types
| Name                          | Type                                                  | Description |
| ----------------------------- | ----------------------------------------------------- | ----------- |
| stall_config_t                |                                                       |             |
| axi_stream_component_type_t   | (null_component, default_component, custom_component) |             |
| axi_stream_protocol_checker_t |                                                       |             |
| axi_stream_monitor_t          |                                                       |             |
| axi_stream_master_t           |                                                       |             |
| axi_stream_slave_t            |                                                       |             |
| axi_stream_transaction_t      |                                                       |             |
## Functions
- push_axi_stream <font id="function_arguments">(      signal net : inout network_t;
      axi_stream : axi_stream_master_t;
      tdata      : std_logic_vector;
      tlast      : std_logic        := '1';
      tkeep      : std_logic_vector := "";
      tstrb      : std_logic_vector := "";
      tid        : std_logic_vector := "";
      tdest      : std_logic_vector := "";
      tuser      : std_logic_vector := ""
    )</font> <font id="function_return">return ()</font>
- pop_axi_stream <font id="function_arguments">(      signal net : inout network_t;
      axi_stream : axi_stream_slave_t;
      variable tdata : out std_logic_vector;
      variable tlast : out std_logic;
      variable tkeep : out std_logic_vector;
      variable tstrb : out std_logic_vector;
      variable tid   : out std_logic_vector;
      variable tdest : out std_logic_vector;
      variable tuser : out std_logic_vector
    )</font> <font id="function_return">return ()</font>
**Description**
Blocking: pop a value from the axi stream
- pop_axi_stream <font id="function_arguments">(      signal net : inout network_t;
      axi_stream : axi_stream_slave_t;
      variable tdata : out std_logic_vector;
      variable tlast : out std_logic
    )</font> <font id="function_return">return ()</font>
- pop_axi_stream <font id="function_arguments">(signal net : inout network_t;                           axi_stream : axi_stream_slave_t;
                           variable reference : inout axi_stream_reference_t)</font> <font id="function_return">return ()</font>
**Description**
Non-blocking: pop a value from the axi stream to be read in the future
- await_pop_axi_stream_reply <font id="function_arguments">(      signal net : inout network_t;
      variable reference : inout axi_stream_reference_t;
      variable tdata     : out std_logic_vector;
      variable tlast     : out std_logic;
      variable tkeep     : out std_logic_vector;
      variable tstrb     : out std_logic_vector;
      variable tid       : out std_logic_vector;
      variable tdest     : out std_logic_vector;
      variable tuser     : out std_logic_vector
    )</font> <font id="function_return">return ()</font>
**Description**
Blocking: Wait for reply to non-blocking pop
- await_pop_axi_stream_reply <font id="function_arguments">(      signal net : inout network_t;
      variable reference : inout axi_stream_reference_t;
      variable tdata     : out std_logic_vector;
      variable tlast     : out std_logic
    )</font> <font id="function_return">return ()</font>
- check_axi_stream <font id="function_arguments">(      signal net : inout network_t;
      axi_stream   : axi_stream_slave_t;
      expected : std_logic_vector;
      tlast    : std_logic        := '1';
      tkeep    : std_logic_vector := "";
      tstrb    : std_logic_vector := "";
      tid      : std_logic_vector := "";
      tdest    : std_logic_vector := "";
      tuser    : std_logic_vector := "";
      msg      : string           := "";
      blocking : boolean          := true
    )</font> <font id="function_return">return ()</font>
**Description**
Blocking: read axi stream and check result against expected value
- push_axi_stream_transaction <font id="function_arguments">(msg : msg_t; axi_stream_transaction : axi_stream_transaction_t)</font> <font id="function_return">return ()</font>
- pop_axi_stream_transaction <font id="function_arguments">(    constant msg                    : in msg_t;
    variable axi_stream_transaction : out axi_stream_transaction_t
  )</font> <font id="function_return">return ()</font>
- handle_axi_stream_transaction <font id="function_arguments">(    variable msg_type        : inout msg_type_t;
    variable msg             : inout msg_t;
    variable axi_transaction : out axi_stream_transaction_t)</font> <font id="function_return">return ()</font>
- new_stall_config <font id="function_arguments">(    stall_probability : real range 0.0 to 1.0;
    min_stall_cycles  : natural;
    max_stall_cycles  : natural
  )</font> <font id="function_return">return stall_config_t</font>
