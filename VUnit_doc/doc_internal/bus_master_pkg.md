# Package: bus_master_pkg
## Constants
| Name                | Type       | Value                                   | Description |
| ------------------- | ---------- | --------------------------------------- | ----------- |
| bus_logger          | logger_t   |  get_logger("vunit_lib:bus_master_pkg") |             |
| bus_write_msg       | msg_type_t |  new_msg_type("write bus")              |             |
| bus_read_msg        | msg_type_t |  new_msg_type("read bus")               |             |
| bus_burst_write_msg | msg_type_t |  new_msg_type("burst write bus")        |             |
| bus_burst_read_msg  | msg_type_t |  new_msg_type("burst read bus")         |             |
## Types
| Name         | Type | Description |
| ------------ | ---- | ----------- |
| bus_master_t |      |             |
## Functions
- get_logger <font id="function_arguments">(bus_handle : bus_master_t)</font> <font id="function_return">return logger_t</font>
- write_bus <font id="function_arguments">(signal net : inout network_t;                      constant bus_handle : bus_master_t;
                      constant address : std_logic_vector;
                      constant data : std_logic_vector;
                       default byte enable is all bytes
                      constant byte_enable : std_logic_vector := "")</font> <font id="function_return">return ()</font>
- write_bus <font id="function_arguments">(signal net : inout network_t;                      constant bus_handle : bus_master_t;
                      constant address : natural;
                      constant data : std_logic_vector;
                       default byte enable is all bytes
                      constant byte_enable : std_logic_vector := "")</font> <font id="function_return">return ()</font>
- burst_write_bus <font id="function_arguments">(signal net : inout network_t;                      constant bus_handle : bus_master_t;
                      constant address : std_logic_vector;
                      constant burst_length : positive;
                      constant data : queue_t)</font> <font id="function_return">return ()</font>
- burst_write_bus <font id="function_arguments">(signal net : inout network_t;                      constant bus_handle : bus_master_t;
                      constant address : natural;
                      constant burst_length : positive;
                      constant data : queue_t)</font> <font id="function_return">return ()</font>
- read_bus <font id="function_arguments">(signal net : inout network_t;                     constant bus_handle : bus_master_t;
                     constant address : std_logic_vector;
                     variable reference : inout bus_reference_t)</font> <font id="function_return">return ()</font>
- read_bus <font id="function_arguments">(signal net : inout network_t;                     constant bus_handle : bus_master_t;
                     constant address : natural;
                     variable reference : inout bus_reference_t)</font> <font id="function_return">return ()</font>
- burst_read_bus <font id="function_arguments">(signal net : inout network_t;                      constant bus_handle : bus_master_t;
                      constant address : std_logic_vector;
                      constant burst_length : positive;
                      variable reference : inout bus_reference_t)</font> <font id="function_return">return ()</font>
- burst_read_bus <font id="function_arguments">(signal net : inout network_t;                      constant bus_handle : bus_master_t;
                      constant address : natural;
                      constant burst_length : positive;
                      variable reference : inout bus_reference_t)</font> <font id="function_return">return ()</font>
- await_read_bus_reply <font id="function_arguments">(signal net : inout network_t;                                 variable reference : inout bus_reference_t;
                                 variable data : inout std_logic_vector)</font> <font id="function_return">return ()</font>
- await_burst_read_bus_reply <font id="function_arguments">(signal net : inout network_t;                                 constant bus_handle : bus_master_t;
                                 constant data : queue_t;
                                 variable reference : inout bus_reference_t)</font> <font id="function_return">return ()</font>
- check_bus <font id="function_arguments">(signal net : inout network_t;                      constant bus_handle : bus_master_t;
                      constant address : std_logic_vector;
                      constant expected : std_logic_vector;
                      constant msg : string := "")</font> <font id="function_return">return ()</font>
- check_bus <font id="function_arguments">(signal net : inout network_t;                      constant bus_handle : bus_master_t;
                      constant address : natural;
                      constant expected : std_logic_vector;
                      constant msg : string := "")</font> <font id="function_return">return ()</font>
- read_bus <font id="function_arguments">(signal net : inout network_t;                     constant bus_handle : bus_master_t;
                     constant address : std_logic_vector;
                     variable data : inout std_logic_vector)</font> <font id="function_return">return ()</font>
- read_bus <font id="function_arguments">(signal net : inout network_t;                     constant bus_handle : bus_master_t;
                     constant address : natural;
                     variable data : inout std_logic_vector)</font> <font id="function_return">return ()</font>
- burst_read_bus <font id="function_arguments">(signal net : inout network_t;                      constant bus_handle : bus_master_t;
                      constant address : std_logic_vector;
                      constant burst_length : positive;
                      constant data : queue_t)</font> <font id="function_return">return ()</font>
- burst_read_bus <font id="function_arguments">(signal net : inout network_t;                      constant bus_handle : bus_master_t;
                      constant address : natural;
                      constant burst_length : positive;
                      constant data : queue_t)</font> <font id="function_return">return ()</font>
- wait_until_read_equals <font id="function_arguments">(    signal net : inout network_t;
    bus_handle   : bus_master_t;
    addr         : std_logic_vector;
    value        : std_logic_vector;
    timeout      : delay_length := delay_length'high;
    msg    : string       := "")</font> <font id="function_return">return ()</font>
- wait_until_read_bit_equals <font id="function_arguments">(    signal net : inout network_t;
    bus_handle   : bus_master_t;
    addr         : std_logic_vector;
    idx          : natural;
    value        : std_logic;
    timeout      : delay_length := delay_length'high;
    msg    : string       := "")</font> <font id="function_return">return ()</font>
- wait_until_idle <font id="function_arguments">(signal net : inout network_t;                            bus_handle : bus_master_t)</font> <font id="function_return">return ()</font>
