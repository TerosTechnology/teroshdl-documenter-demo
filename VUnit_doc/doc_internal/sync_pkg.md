# Package: sync_pkg

- **File**: sync_pkg.vhd
## Constants

| Name                      | Type       | Value                                  | Description                                                                |
| ------------------------- | ---------- | -------------------------------------- | -------------------------------------------------------------------------- |
| wait_until_idle_msg       | msg_type_t |  new_msg_type("wait until idle")       |  Message type definitions used by VC implementing the synchronization VCI  |
| wait_until_idle_reply_msg | msg_type_t |  new_msg_type("wait until idle reply") |                                                                            |
| wait_for_time_msg         | msg_type_t |  new_msg_type("wait for time")         |                                                                            |
## Functions
- wait_until_idle <font id="function_arguments">(signal net : inout network_t;<br><span style="padding-left:20px"> handle     :       sync_handle_t) </font> <font id="function_return">return ()</font>
**Description**
 Blocking: Wait until all operations requested from the VC have been finished

- wait_for_time <font id="function_arguments">(signal net : inout network_t;<br><span style="padding-left:20px"> handle     :       sync_handle_t;<br><span style="padding-left:20px"> delay      :       delay_length) </font> <font id="function_return">return ()</font>
**Description**
 Non-blocking: Make VC wait for a delay before starting the next operation

- handle_wait_until_idle <font id="function_arguments">(signal net        : inout network_t;<br><span style="padding-left:20px"> variable msg_type : inout msg_type_t;<br><span style="padding-left:20px"> variable msg      : inout msg_t) </font> <font id="function_return">return ()</font>
**Description**
 Standard implementation of wait_until_idle VCI which may be used by VC

- handle_wait_for_time <font id="function_arguments">(signal net        : inout network_t;<br><span style="padding-left:20px"> variable msg_type : inout msg_type_t;<br><span style="padding-left:20px"> variable msg      : inout msg_t) </font> <font id="function_return">return ()</font>
**Description**
 Standard implementation of wait_for_time VCI which may be used by VC

- handle_sync_message <font id="function_arguments">(signal net        : inout network_t;<br><span style="padding-left:20px"> variable msg_type : inout msg_type_t;<br><span style="padding-left:20px"> variable msg      : inout msg_t) </font> <font id="function_return">return ()</font>
**Description**
 Standard implementation of synchronization VCI which may be used by VC

