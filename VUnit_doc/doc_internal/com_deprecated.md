# Package: com_deprecated_pkg
## Constants
| Name            | Type         | Value          | Description |
| --------------- | ------------ | -------------- | ----------- |
| null_actor_c    | actor_t      |  null_actor    |             |
| no_message_id_c | message_id_t |  no_message_id |             |
| max_timeout_c   | time         |  max_timeout   |             |
## Functions
- destroy <font id="function_arguments">(actor     : inout actor_t; status : out com_status_t)</font> <font id="function_return">return ()</font>
- copy <font id="function_arguments">(src : inout message_ptr_t; dst : inout message_ptr_t)</font> <font id="function_return">return ()</font>
- delete <font id="function_arguments">(message : inout message_ptr_t)</font> <font id="function_return">return ()</font>
- send <font id="function_arguments">(    signal net            : inout network_t;
    constant receiver     : in    actor_t;
    variable message      : inout message_ptr_t;
    constant timeout      : in    time    := max_timeout_c;
    constant keep_message : in    boolean := true)</font> <font id="function_return">return ()</font>
- receive <font id="function_arguments">(    signal net        : inout network_t;
    constant receiver : in    actor_t;
    variable message  : inout message_ptr_t;
    constant timeout  : in    time := max_timeout_c)</font> <font id="function_return">return ()</font>
- reply <font id="function_arguments">(    signal net            : inout network_t;
    variable request      : inout message_ptr_t;
    variable message      : inout message_ptr_t;
    constant timeout      : in    time    := max_timeout_c;
    constant keep_message : in    boolean := true)</font> <font id="function_return">return ()</font>
- receive_reply <font id="function_arguments">(    signal net       : inout network_t;
    variable request : inout message_ptr_t;
    variable message : inout message_ptr_t;
    constant timeout : in    time := max_timeout_c)</font> <font id="function_return">return ()</font>
- send <font id="function_arguments">(    signal net            : inout network_t;
    constant receiver     : in    actor_t;
    variable message      : inout message_ptr_t;
    variable receipt      : out   receipt_t;
    constant timeout      : in    time    := max_timeout_c;
    constant keep_message : in    boolean := true)</font> <font id="function_return">return ()</font>
- reply <font id="function_arguments">(    signal net          : inout network_t;
    constant sender     : in    actor_t;
    constant receiver   : in    actor_t;
    constant request_id : in    message_id_t;
    constant payload    : in    string := "";
    variable receipt    : out   receipt_t;
    constant timeout    : in    time   := max_timeout_c)</font> <font id="function_return">return ()</font>
- reply <font id="function_arguments">(    signal net          : inout network_t;
    constant receiver   : in    actor_t;
    constant request_id : in    message_id_t;
    constant payload    : in    string := "";
    variable receipt    : out   receipt_t;
    constant timeout    : in    time   := max_timeout_c)</font> <font id="function_return">return ()</font>
- reply <font id="function_arguments">(    signal net            : inout network_t;
    constant receiver     : in    actor_t;
    variable message      : inout message_ptr_t;
    variable receipt      : out   receipt_t;
    constant timeout      : in    time    := max_timeout_c;
    constant keep_message : in    boolean := false)</font> <font id="function_return">return ()</font>
- receive_reply <font id="function_arguments">(    signal net          : inout network_t;
    constant receiver   : in    actor_t;
    constant request_id : in    message_id_t;
    variable message    : inout message_ptr_t;
    constant timeout    : in    time := max_timeout_c)</font> <font id="function_return">return ()</font>
- receive_reply <font id="function_arguments">(    signal net            : inout network_t;
    constant receiver     : in    actor_t;
    constant request_id   : in    message_id_t;
    variable positive_ack : out   boolean;
    variable status       : out   com_status_t;
    constant timeout      : in    time := max_timeout_c)</font> <font id="function_return">return ()</font>
- send <font id="function_arguments">(    signal net        : inout network_t;
    constant sender   : in    actor_t;
    constant receiver : in    actor_t;
    constant payload  : in    string := "";
    variable receipt  : out   receipt_t;
    constant timeout  : in    time   := max_timeout_c)</font> <font id="function_return">return ()</font>
- send <font id="function_arguments">(    signal net        : inout network_t;
    constant receiver : in    actor_t;
    constant payload  : in    string := "";
    variable receipt  : out   receipt_t;
    constant timeout  : in    time   := max_timeout_c)</font> <font id="function_return">return ()</font>
- request <font id="function_arguments">(    signal net               : inout network_t;
    constant sender          : in    actor_t;
    constant receiver        : in    actor_t;
    constant request_payload : in    string := "";
    variable reply_message   : inout message_ptr_t;
    constant timeout         : in    time   := max_timeout_c)</font> <font id="function_return">return ()</font>
- request <font id="function_arguments">(    signal net               : inout network_t;
    constant receiver        : in    actor_t;
    variable request_message : inout message_ptr_t;
    variable reply_message   : inout message_ptr_t;
    constant timeout         : in    time    := max_timeout_c;
    constant keep_message    : in    boolean := false)</font> <font id="function_return">return ()</font>
- request <font id="function_arguments">(    signal net               : inout network_t;
    constant receiver        : in    actor_t;
    variable request_message : inout message_ptr_t;
    variable positive_ack    : out   boolean;
    constant timeout         : in    time    := max_timeout_c;
    constant keep_message    : in    boolean := false)</font> <font id="function_return">return ()</font>
- publish <font id="function_arguments">(    signal net            : inout network_t;
    variable message      : inout message_ptr_t;
    constant timeout      : in    time    := max_timeout_c;
    constant keep_message : in    boolean := false)</font> <font id="function_return">return ()</font>
- request <font id="function_arguments">(    signal net               : inout network_t;
    constant sender          : in    actor_t;
    constant receiver        : in    actor_t;
    constant request_payload : in    string := "";
    variable positive_ack    : out   boolean;
    variable status          : out   com_status_t;
    constant timeout         : in    time   := max_timeout_c)</font> <font id="function_return">return ()</font>
- request <font id="function_arguments">(    signal net               : inout network_t;
    constant receiver        : in    actor_t;
    variable request_message : inout message_ptr_t;
    variable positive_ack    : out   boolean;
    variable status          : out   com_status_t;
    constant timeout         : in    time    := max_timeout_c;
    constant keep_message    : in    boolean := false)</font> <font id="function_return">return ()</font>
- publish <font id="function_arguments">(    signal net       : inout network_t;
    constant sender  : in    actor_t;
    constant payload : in    string := "";
    variable status  : out   com_status_t;
    constant timeout : in    time   := max_timeout_c)</font> <font id="function_return">return ()</font>
- publish <font id="function_arguments">(    signal net            : inout network_t;
    variable message      : inout message_ptr_t;
    variable status       : out   com_status_t;
    constant timeout      : in    time    := max_timeout_c;
    constant keep_message : in    boolean := false)</font> <font id="function_return">return ()</font>
- acknowledge <font id="function_arguments">(    signal net            : inout network_t;
    constant sender       : in    actor_t;
    constant receiver     : in    actor_t;
    constant request_id   : in    message_id_t;
    constant positive_ack : in    boolean := true;
    variable receipt      : out   receipt_t;
    constant timeout      : in    time    := max_timeout_c)</font> <font id="function_return">return ()</font>
- acknowledge <font id="function_arguments">(    signal net            : inout network_t;
    constant receiver     : in    actor_t;
    constant request_id   : in    message_id_t;
    constant positive_ack : in    boolean := true;
    variable receipt      : out   receipt_t;
    constant timeout      : in    time    := max_timeout_c)</font> <font id="function_return">return ()</font>
- wait_for_messages <font id="function_arguments">(    signal net               : in  network_t;
    constant receiver        : in  actor_t;
    variable status          : out com_status_t;
    constant receive_timeout : in  time := max_timeout_c)</font> <font id="function_return">return ()</font>
- subscribe <font id="function_arguments">(    constant subscriber : in  actor_t;
    constant publisher  : in  actor_t;
    variable status     : out com_status_t)</font> <font id="function_return">return ()</font>
- unsubscribe <font id="function_arguments">(    constant subscriber : in  actor_t;
    constant publisher  : in  actor_t;
    variable status     : out com_status_t)</font> <font id="function_return">return ()</font>
