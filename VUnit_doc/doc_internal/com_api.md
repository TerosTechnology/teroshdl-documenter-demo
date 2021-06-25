# Package: com_pkg
## Signals
| Name | Type      | Description |
| ---- | --------- | ----------- |
| net  | network_t |             |
## Functions
- destroy <font id="function_arguments">(actor : inout actor_t)</font> <font id="function_return">return ()</font>
- reset_messenger <font id="function_arguments">()</font> <font id="function_return">return ()</font>
- resize_mailbox <font id="function_arguments">(actor : actor_t; new_size : natural; mailbox_id : mailbox_id_t := inbox)</font> <font id="function_return">return ()</font>
- send <font id="function_arguments">(    signal net        : inout network_t;
    constant receiver : in    actor_t;
    variable msg      : inout msg_t;
    constant timeout  : in    time := max_timeout)</font> <font id="function_return">return ()</font>
- send <font id="function_arguments">(    signal net         : inout network_t;
    constant receivers : in    actor_vec_t;
    variable msg       : inout msg_t;
    constant timeout   : in    time := max_timeout)</font> <font id="function_return">return ()</font>
- receive <font id="function_arguments">(    signal net        : inout network_t;
    constant receiver : in    actor_t;
    variable msg      : inout msg_t;
    constant timeout  : in    time := max_timeout)</font> <font id="function_return">return ()</font>
- receive <font id="function_arguments">(    signal net         : inout network_t;
    constant receivers : in    actor_vec_t;
    variable msg       : inout msg_t;
    constant timeout   : in    time := max_timeout)</font> <font id="function_return">return ()</font>
- reply <font id="function_arguments">(    signal net           : inout network_t;
    variable request_msg : inout msg_t;
    variable reply_msg   : inout msg_t;
    constant timeout     : in    time := max_timeout)</font> <font id="function_return">return ()</font>
- receive_reply <font id="function_arguments">(    signal net           : inout network_t;
    variable request_msg : inout msg_t;
    variable reply_msg   : inout msg_t;
    constant timeout     : in    time := max_timeout)</font> <font id="function_return">return ()</font>
- publish <font id="function_arguments">(    signal net       : inout network_t;
    constant sender  : in    actor_t;
    variable msg     : inout msg_t;
    constant timeout : in    time := max_timeout)</font> <font id="function_return">return ()</font>
- acknowledge <font id="function_arguments">(    signal net            : inout network_t;
    variable request_msg  : inout msg_t;
    constant positive_ack : in    boolean := true;
    constant timeout      : in    time    := max_timeout)</font> <font id="function_return">return ()</font>
- receive_reply <font id="function_arguments">(    signal net            : inout network_t;
    variable request_msg  : inout msg_t;
    variable positive_ack : out   boolean;
    constant timeout      : in    time := max_timeout)</font> <font id="function_return">return ()</font>
- request <font id="function_arguments">(    signal net           : inout network_t;
    constant receiver    : in    actor_t;
    variable request_msg : inout msg_t;
    variable reply_msg   : inout msg_t;
    constant timeout     : in    time := max_timeout)</font> <font id="function_return">return ()</font>
- request <font id="function_arguments">(    signal net            : inout network_t;
    constant receiver     : in    actor_t;
    variable request_msg  : inout msg_t;
    variable positive_ack : out   boolean;
    constant timeout      : in    time := max_timeout)</font> <font id="function_return">return ()</font>
- wait_for_message <font id="function_arguments">(    signal net        : in  network_t;
    constant receiver : in  actor_t;
    variable status   : out com_status_t;
    constant timeout  : in  time := max_timeout)</font> <font id="function_return">return ()</font>
- wait_for_message <font id="function_arguments">(    signal net         : in  network_t;
    constant receivers : in  actor_vec_t;
    variable status    : out com_status_t;
    constant timeout   : in  time := max_timeout)</font> <font id="function_return">return ()</font>
- wait_for_reply <font id="function_arguments">(    signal net           : inout network_t;
    variable request_msg : inout msg_t;
    variable status      : out   com_status_t;
    constant timeout     : in    time := max_timeout)</font> <font id="function_return">return ()</font>
- get_message <font id="function_arguments">(signal net : inout network_t; receiver : actor_t; variable msg : inout msg_t)</font> <font id="function_return">return ()</font>
- get_reply <font id="function_arguments">(    signal net           : inout network_t;
    variable request_msg : inout msg_t;
    variable reply_msg : inout msg_t)</font> <font id="function_return">return ()</font>
- subscribe <font id="function_arguments">(    subscriber   : actor_t;
    publisher    : actor_t;
    traffic_type : subscription_traffic_type_t := published)</font> <font id="function_return">return ()</font>
- unsubscribe <font id="function_arguments">(    subscriber   : actor_t;
    publisher    : actor_t;
    traffic_type : subscription_traffic_type_t := published)</font> <font id="function_return">return ()</font>
- deallocate <font id="function_arguments">(variable mailbox_state : inout mailbox_state_t)</font> <font id="function_return">return ()</font>
- deallocate <font id="function_arguments">(variable actor_state : inout actor_state_t)</font> <font id="function_return">return ()</font>
- deallocate <font id="function_arguments">(variable messenger_state : inout messenger_state_t)</font> <font id="function_return">return ()</font>
- allow_deprecated <font id="function_arguments">()</font> <font id="function_return">return ()</font>
- allow_timeout <font id="function_arguments">()</font> <font id="function_return">return ()</font>
