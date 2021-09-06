# Package: com_pkg

- **File**: com_api.vhd
## Signals

| Name | Type      | Description |
| ---- | --------- | ----------- |
| net  | network_t |             |
## Functions
- destroy <font id="function_arguments">(actor : inout actor_t) </font> <font id="function_return">return ()</font>
</br>**Description**
 Destroy actor. Mailboxes are deallocated and dependent subscriptions are
 removed. Returns null_actor.

- reset_messenger <font id="function_arguments">()</font> <font id="function_return">return ()</font>
</br>**Description**
 Reset communication system. All actors are destroyed.

- resize_mailbox <font id="function_arguments">(actor : actor_t;<br><span style="padding-left:20px"> new_size : natural;<br><span style="padding-left:20px"> mailbox_id : mailbox_id_t := inbox) </font> <font id="function_return">return ()</font>
</br>**Description**
 Resize actor mailbox. Reducing size below the number of messages in the
 mailbox in runtime error

- send <font id="function_arguments">( signal net        : inout network_t;<br><span style="padding-left:20px"> constant receiver : in    actor_t;<br><span style="padding-left:20px"> variable msg      : inout msg_t;<br><span style="padding-left:20px"> constant timeout  : in    time := max_timeout) </font> <font id="function_return">return ()</font>
</br>**Description**
---------------------------------------------------------------------------
 Primary send and receive related subprograms

 All timeouts will result in a runtime error unless otherwise noted.
---------------------------------------------------------------------------
 Send message to receiver. Blocking if reciever or any subscriber inbox is
 full.

- send <font id="function_arguments">( signal net         : inout network_t;<br><span style="padding-left:20px"> constant receivers : in    actor_vec_t;<br><span style="padding-left:20px"> variable msg       : inout msg_t;<br><span style="padding-left:20px"> constant timeout   : in    time := max_timeout) </font> <font id="function_return">return ()</font>
</br>**Description**
 Send message to an array of receivers. Blocking if any reciever or any subscriber inbox is
 full.

- receive <font id="function_arguments">( signal net        : inout network_t;<br><span style="padding-left:20px"> constant receiver : in    actor_t;<br><span style="padding-left:20px"> variable msg      : inout msg_t;<br><span style="padding-left:20px"> constant timeout  : in    time := max_timeout) </font> <font id="function_return">return ()</font>
</br>**Description**
 Receive message sent to receiver. Returns oldest message or the first
 incoming if the inbox is empty. msg is initially deleted.

- receive <font id="function_arguments">( signal net         : inout network_t;<br><span style="padding-left:20px"> constant receivers : in    actor_vec_t;<br><span style="padding-left:20px"> variable msg       : inout msg_t;<br><span style="padding-left:20px"> constant timeout   : in    time := max_timeout) </font> <font id="function_return">return ()</font>
</br>**Description**
 Receive message sent to any of the receivers. Returns oldest message or the first
 incoming if the inboxes are empty. Receiver inboxes are emptied from left
 to right. msg is initially deleted.

- reply <font id="function_arguments">( signal net           : inout network_t;<br><span style="padding-left:20px"> variable request_msg : inout msg_t;<br><span style="padding-left:20px"> variable reply_msg   : inout msg_t;<br><span style="padding-left:20px"> constant timeout     : in    time := max_timeout) </font> <font id="function_return">return ()</font>
</br>**Description**
 Reply to request_msg with reply_msg. request_msg may be anonymous. Blocking if reciever
 or any subscriber inbox is full.

- receive_reply <font id="function_arguments">( signal net           : inout network_t;<br><span style="padding-left:20px"> variable request_msg : inout msg_t;<br><span style="padding-left:20px"> variable reply_msg   : inout msg_t;<br><span style="padding-left:20px"> constant timeout     : in    time := max_timeout) </font> <font id="function_return">return ()</font>
</br>**Description**
 Receive a reply_msg to request_msg. request_msg may be anonymous. reply_msg is initially deleted.

- publish <font id="function_arguments">( signal net       : inout network_t;<br><span style="padding-left:20px"> constant sender  : in    actor_t;<br><span style="padding-left:20px"> variable msg     : inout msg_t;<br><span style="padding-left:20px"> constant timeout : in    time := max_timeout) </font> <font id="function_return">return ()</font>
</br>**Description**
 Publish a message from sender to all its subscribers. Blocking if reciever or any subscriber inbox is
 full.

- acknowledge <font id="function_arguments">( signal net            : inout network_t;<br><span style="padding-left:20px"> variable request_msg  : inout msg_t;<br><span style="padding-left:20px"> constant positive_ack : in    boolean := true;<br><span style="padding-left:20px"> constant timeout      : in    time    := max_timeout) </font> <font id="function_return">return ()</font>
</br>**Description**
---------------------------------------------------------------------------
 Secondary send and receive related subprograms

 All timeouts will result in a runtime error unless otherwise noted.
---------------------------------------------------------------------------
 Positive or negative acknowledge of a request_msg. Same as a reply with a
 boolean reply message.

- receive_reply <font id="function_arguments">( signal net            : inout network_t;<br><span style="padding-left:20px"> variable request_msg  : inout msg_t;<br><span style="padding-left:20px"> variable positive_ack : out   boolean;<br><span style="padding-left:20px"> constant timeout      : in    time := max_timeout) </font> <font id="function_return">return ()</font>
</br>**Description**
 Receive positive or negative acknowledge for a request_msg. request_msg
 may be anonymous. reply_msg is initially deleted.

- request <font id="function_arguments">( signal net           : inout network_t;<br><span style="padding-left:20px"> constant receiver    : in    actor_t;<br><span style="padding-left:20px"> variable request_msg : inout msg_t;<br><span style="padding-left:20px"> variable reply_msg   : inout msg_t;<br><span style="padding-left:20px"> constant timeout     : in    time := max_timeout) </font> <font id="function_return">return ()</font>
</br>**Description**
 This request is the same as send of request_msg to receiver followed by a
 receive_reply of a reply_msg

- request <font id="function_arguments">( signal net            : inout network_t;<br><span style="padding-left:20px"> constant receiver     : in    actor_t;<br><span style="padding-left:20px"> variable request_msg  : inout msg_t;<br><span style="padding-left:20px"> variable positive_ack : out   boolean;<br><span style="padding-left:20px"> constant timeout      : in    time := max_timeout) </font> <font id="function_return">return ()</font>
</br>**Description**
 This request is the same as send of request_msg to receiver followed by a
 receive_reply of a positive or negative acknowledge.

- wait_for_message <font id="function_arguments">( signal net        : in  network_t;<br><span style="padding-left:20px"> constant receiver : in  actor_t;<br><span style="padding-left:20px"> variable status   : out com_status_t;<br><span style="padding-left:20px"> constant timeout  : in  time := max_timeout) </font> <font id="function_return">return ()</font>
</br>**Description**
---------------------------------------------------------------------------
 Low-level subprograms primarily used for handling timeout wihout error
---------------------------------------------------------------------------
 Wait for message sent to receiver. status = ok if message is
 received before the timeout, status = timeout otherwise.

- wait_for_message <font id="function_arguments">( signal net         : in  network_t;<br><span style="padding-left:20px"> constant receivers : in  actor_vec_t;<br><span style="padding-left:20px"> variable status    : out com_status_t;<br><span style="padding-left:20px"> constant timeout   : in  time := max_timeout) </font> <font id="function_return">return ()</font>
</br>**Description**
 Wait for message sent to any of the listed receivers. status = ok
 if message is received before the timeout, status = timeout otherwise.

- wait_for_reply <font id="function_arguments">( signal net           : inout network_t;<br><span style="padding-left:20px"> variable request_msg : inout msg_t;<br><span style="padding-left:20px"> variable status      : out   com_status_t;<br><span style="padding-left:20px"> constant timeout     : in    time := max_timeout) </font> <font id="function_return">return ()</font>
</br>**Description**
 Wait for reply to request_msg. status = ok
 if message is received before the timeout, status = timeout otherwise.

- get_message <font id="function_arguments">(signal net : inout network_t;<br><span style="padding-left:20px"> receiver : actor_t;<br><span style="padding-left:20px"> variable msg : inout msg_t) </font> <font id="function_return">return ()</font>
</br>**Description**
 Get oldest message from receiver inbox. Runtime error if inbox is empty.

- get_reply <font id="function_arguments">( signal net           : inout network_t;<br><span style="padding-left:20px"> variable request_msg : inout msg_t;<br><span style="padding-left:20px"> variable reply_msg : inout msg_t) </font> <font id="function_return">return ()</font>
</br>**Description**
 Get reply message to request_msg. Runtime error if reply message isn't available.

- subscribe <font id="function_arguments">( subscriber   : actor_t;<br><span style="padding-left:20px"> publisher    : actor_t;<br><span style="padding-left:20px"> traffic_type : subscription_traffic_type_t := published) </font> <font id="function_return">return ()</font>
</br>**Description**
---------------------------------------------------------------------------
 Subscriptions
---------------------------------------------------------------------------
 Make subscriber subscribe on the specified publisher and traffic type. For
 a description of the traffic types see com_types.vhd

- unsubscribe <font id="function_arguments">( subscriber   : actor_t;<br><span style="padding-left:20px"> publisher    : actor_t;<br><span style="padding-left:20px"> traffic_type : subscription_traffic_type_t := published) </font> <font id="function_return">return ()</font>
</br>**Description**
 Remove subscription on the given publisher and traffic type.

- deallocate <font id="function_arguments">(variable mailbox_state : inout mailbox_state_t) </font> <font id="function_return">return ()</font>
</br>**Description**
 Deallocate memory allocated to a mailbox state variable

- deallocate <font id="function_arguments">(variable actor_state : inout actor_state_t) </font> <font id="function_return">return ()</font>
</br>**Description**
 Deallocate memory allocated to a actor state variable

- deallocate <font id="function_arguments">(variable messenger_state : inout messenger_state_t) </font> <font id="function_return">return ()</font>
</br>**Description**
 Deallocate memory allocated to a messenger state variable

- allow_deprecated <font id="function_arguments">()</font> <font id="function_return">return ()</font>
</br>**Description**
---------------------------------------------------------------------------
 Misc
---------------------------------------------------------------------------
 Allow deprecated APIs

- allow_timeout <font id="function_arguments">()</font> <font id="function_return">return ()</font>
</br>**Description**
 Allow timeout in deprecated functionality. If not allowed timeouts will
 cause a runtime error.

