# Package: sync_pkg
## Constants
| Name                      | Type       | Value                                  | Description |
| ------------------------- | ---------- | -------------------------------------- | ----------- |
| wait_until_idle_msg       | msg_type_t |  new_msg_type("wait until idle")       |             |
| wait_until_idle_reply_msg | msg_type_t |  new_msg_type("wait until idle reply") |             |
| wait_for_time_msg         | msg_type_t |  new_msg_type("wait for time")         |             |
## Functions
- wait_until_idle <font id="function_arguments">(signal net : inout network_t;                            handle     :       sync_handle_t)</font> <font id="function_return">return ()</font>
- wait_for_time <font id="function_arguments">(signal net : inout network_t;                          handle     :       sync_handle_t;
                          delay      :       delay_length)</font> <font id="function_return">return ()</font>
- handle_wait_until_idle <font id="function_arguments">(signal net        : inout network_t;                                   variable msg_type : inout msg_type_t;
                                   variable msg      : inout msg_t)</font> <font id="function_return">return ()</font>
- handle_wait_for_time <font id="function_arguments">(signal net        : inout network_t;                                 variable msg_type : inout msg_type_t;
                                 variable msg      : inout msg_t)</font> <font id="function_return">return ()</font>
- handle_sync_message <font id="function_arguments">(signal net        : inout network_t;                                variable msg_type : inout msg_type_t;
                                variable msg      : inout msg_t)</font> <font id="function_return">return ()</font>
