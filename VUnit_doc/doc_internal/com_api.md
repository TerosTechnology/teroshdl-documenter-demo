# Package: com_pkg
## Signals
| Name | Type      | Description |
| ---- | --------- | ----------- |
| net  | network_t |             |
## Functions
- destroy <font id="function_arguments">(actor : inout actor_t)</font> <font id="function_return">return ()</font>
**Description**
Destroy actor. Mailboxes are deallocated and dependent subscriptions areremoved. Returns null_actor.
- reset_messenger <font id="function_arguments">()</font> <font id="function_return">return ()</font>
**Description**
Reset communication system. All actors are destroyed.
- resize_mailbox <font id="function_arguments">(actor : actor_t; new_size : natural; mailbox_id : mailbox_id_t := inbox)</font> <font id="function_return">return ()</font>
**Description**
Resize actor mailbox. Reducing size below the number of messages in themailbox in runtime error
- send <font id="function_arguments">(    signal net        : inout network_t;
    constant receiver : in    actor_t;
    variable msg      : inout msg_t;
    constant timeout  : in    time := max_timeout)</font> <font id="function_return">return ()</font>
**Description**
Send message to receiver. Blocking if reciever or any subscriber inbox isfull.
- send <font id="function_arguments">(    signal net         : inout network_t;
    constant receivers : in    actor_vec_t;
    variable msg       : inout msg_t;
    constant timeout   : in    time := max_timeout)</font> <font id="function_return">return ()</font>
**Description**
Send message to an array of receivers. Blocking if any reciever or any subscriber inbox isfull.
- receive <font id="function_arguments">(    signal net        : inout network_t;
    constant receiver : in    actor_t;
    variable msg      : inout msg_t;
    constant timeout  : in    time := max_timeout)</font> <font id="function_return">return ()</font>
**Description**
Receive message sent to receiver. Returns oldest message or the firstincoming if the inbox is empty. msg is initially deleted.
- receive <font id="function_arguments">(    signal net         : inout network_t;
    constant receivers : in    actor_vec_t;
    variable msg       : inout msg_t;
    constant timeout   : in    time := max_timeout)</font> <font id="function_return">return ()</font>
**Description**
Receive message sent to any of the receivers. Returns oldest message or the firstincoming if the inboxes are empty. Receiver inboxes are emptied from leftto right. msg is initially deleted.
- reply <font id="function_arguments">(    signal net           : inout network_t;
    variable request_msg : inout msg_t;
    variable reply_msg   : inout msg_t;
    constant timeout     : in    time := max_timeout)</font> <font id="function_return">return ()</font>
**Description**
Reply to request_msg with reply_msg. request_msg may be anonymous. Blocking if recieveror any subscriber inbox is full.
- receive_reply <font id="function_arguments">(    signal net           : inout network_t;
    variable request_msg : inout msg_t;
    variable reply_msg   : inout msg_t;
    constant timeout     : in    time := max_timeout)</font> <font id="function_return">return ()</font>
**Description**
Receive a reply_msg to request_msg. request_msg may be anonymous. reply_msg is initially deleted.
- publish <font id="function_arguments">(    signal net       : inout network_t;
    constant sender  : in    actor_t;
    variable msg     : inout msg_t;
    constant timeout : in    time := max_timeout)</font> <font id="function_return">return ()</font>
**Description**
Publish a message from sender to all its subscribers. Blocking if reciever or any subscriber inbox isfull.
- acknowledge <font id="function_arguments">(    signal net            : inout network_t;
    variable request_msg  : inout msg_t;
    constant positive_ack : in    boolean := true;
    constant timeout      : in    time    := max_timeout)</font> <font id="function_return">return ()</font>
**Description**
Positive or negative acknowledge of a request_msg. Same as a reply with aboolean reply message.
- receive_reply <font id="function_arguments">(    signal net            : inout network_t;
    variable request_msg  : inout msg_t;
    variable positive_ack : out   boolean;
    constant timeout      : in    time := max_timeout)</font> <font id="function_return">return ()</font>
**Description**
Receive positive or negative acknowledge for a request_msg. request_msgmay be anonymous. reply_msg is initially deleted.
- request <font id="function_arguments">(    signal net           : inout network_t;
    constant receiver    : in    actor_t;
    variable request_msg : inout msg_t;
    variable reply_msg   : inout msg_t;
    constant timeout     : in    time := max_timeout)</font> <font id="function_return">return ()</font>
**Description**
This request is the same as send of request_msg to receiver followed by areceive_reply of a reply_msg
- request <font id="function_arguments">(    signal net            : inout network_t;
    constant receiver     : in    actor_t;
    variable request_msg  : inout msg_t;
    variable positive_ack : out   boolean;
    constant timeout      : in    time := max_timeout)</font> <font id="function_return">return ()</font>
**Description**
This request is the same as send of request_msg to receiver followed by areceive_reply of a positive or negative acknowledge.
- wait_for_message <font id="function_arguments">(    signal net        : in  network_t;
    constant receiver : in  actor_t;
    variable status   : out com_status_t;
    constant timeout  : in  time := max_timeout)</font> <font id="function_return">return ()</font>
**Description**
Wait for message sent to receiver. status = ok if message isreceived before the timeout, status = timeout otherwise.
- wait_for_message <font id="function_arguments">(    signal net         : in  network_t;
    constant receivers : in  actor_vec_t;
    variable status    : out com_status_t;
    constant timeout   : in  time := max_timeout)</font> <font id="function_return">return ()</font>
**Description**
Wait for message sent to any of the listed receivers. status = okif message is received before the timeout, status = timeout otherwise.
- wait_for_reply <font id="function_arguments">(    signal net           : inout network_t;
    variable request_msg : inout msg_t;
    variable status      : out   com_status_t;
    constant timeout     : in    time := max_timeout)</font> <font id="function_return">return ()</font>
**Description**
Wait for reply to request_msg. status = okif message is received before the timeout, status = timeout otherwise.
- get_message <font id="function_arguments">(signal net : inout network_t; receiver : actor_t; variable msg : inout msg_t)</font> <font id="function_return">return ()</font>
**Description**
Get oldest message from receiver inbox. Runtime error if inbox is empty.
- get_reply <font id="function_arguments">(    signal net           : inout network_t;
    variable request_msg : inout msg_t;
    variable reply_msg : inout msg_t)</font> <font id="function_return">return ()</font>
**Description**
Get reply message to request_msg. Runtime error if reply message isn't available.
- subscribe <font id="function_arguments">(    subscriber   : actor_t;
    publisher    : actor_t;
    traffic_type : subscription_traffic_type_t := published)</font> <font id="function_return">return ()</font>
**Description**
Make subscriber subscribe on the specified publisher and traffic type. Fora description of the traffic types see com_types.vhd
- unsubscribe <font id="function_arguments">(    subscriber   : actor_t;
    publisher    : actor_t;
    traffic_type : subscription_traffic_type_t := published)</font> <font id="function_return">return ()</font>
**Description**
Remove subscription on the given publisher and traffic type.
- deallocate <font id="function_arguments">(variable mailbox_state : inout mailbox_state_t)</font> <font id="function_return">return ()</font>
**Description**
Deallocate memory allocated to a mailbox state variable
- deallocate <font id="function_arguments">(variable actor_state : inout actor_state_t)</font> <font id="function_return">return ()</font>
**Description**
Deallocate memory allocated to a actor state variable
- deallocate <font id="function_arguments">(variable messenger_state : inout messenger_state_t)</font> <font id="function_return">return ()</font>
**Description**
Deallocate memory allocated to a messenger state variable
- allow_deprecated <font id="function_arguments">()</font> <font id="function_return">return ()</font>
**Description**
Allow deprecated APIs
- allow_timeout <font id="function_arguments">()</font> <font id="function_return">return ()</font>
**Description**
Allow timeout in deprecated functionality. If not allowed timeouts willcause a runtime error.
