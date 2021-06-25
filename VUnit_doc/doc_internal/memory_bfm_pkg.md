# Package: memory_bfm_pkg
## Constants
| Name                       | Type       | Value                                   | Description |
| -------------------------- | ---------- | --------------------------------------- | ----------- |
| write_msg                  | msg_type_t |  new_msg_type("write")                  |             |
| write_with_acknowledge_msg | msg_type_t |  new_msg_type("write with acknowledge") |             |
| read_msg                   | msg_type_t |  new_msg_type("read")                   |             |
| read_reply_msg             | msg_type_t |  new_msg_type("read reply")             |             |
| actor                      | actor_t    |  new_actor("memory BFM")                |             |
| memory_bfm_logger          | logger_t   |  get_logger("memory BFM")               |             |
## Functions
- write <font id="function_arguments">(    signal net       : inout network_t;
    constant address : in    unsigned(7 downto 0);
    constant data    : in    std_logic_vector(7 downto 0))</font> <font id="function_return">return ()</font>
- blocking_write <font id="function_arguments">(    signal net       : inout network_t;
    constant address : in    unsigned(7 downto 0);
    constant data    : in    std_logic_vector(7 downto 0))</font> <font id="function_return">return ()</font>
- read <font id="function_arguments">(    signal net       : inout network_t;
    constant address : in    unsigned(7 downto 0);
    variable future  : out   msg_t)</font> <font id="function_return">return ()</font>
- get <font id="function_arguments">(    signal net      : inout network_t;
    variable future : inout msg_t;
    variable data   : out   std_logic_vector(7 downto 0))</font> <font id="function_return">return ()</font>
- read <font id="function_arguments">(    signal net       : inout network_t;
    constant address : in    unsigned(7 downto 0);
    variable data    : out   std_logic_vector(7 downto 0))</font> <font id="function_return">return ()</font>
