# Package: signal_checker_pkg
## Constants
| Name       | Type       | Value                   | Description                      |
| ---------- | ---------- | ----------------------- | -------------------------------- |
| expect_msg | msg_type_t |  new_msg_type("expect") | Private message type definitions |
## Types
| Name             | Type | Description |
| ---------------- | ---- | ----------- |
| signal_checker_t |      |             |
## Functions
- expect <font id="function_arguments">(signal net : inout network_t;                   signal_checker : signal_checker_t;
                   value : std_logic_vector;
                   event_time : delay_length;
                   margin : delay_length := 0 ns)</font> <font id="function_return">return ()</font>
**Description**
Add one value to the expect queueAllow event to occur within event_time += margin including end points
- wait_until_idle <font id="function_arguments">(signal net : inout network_t;                            signal_checker : signal_checker_t)</font> <font id="function_return">return ()</font>
**Description**
Wait until all expected values have been checked
