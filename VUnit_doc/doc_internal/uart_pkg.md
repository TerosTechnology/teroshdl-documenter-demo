# Package: uart_pkg

## Constants

| Name                   | Type       | Value                               | Description |
| ---------------------- | ---------- | ----------------------------------- | ----------- |
| default_baud_rate      | natural    |  115200                             |             |
| default_idle_state     | std_logic  |  '1'                                |             |
| default_data_length    | positive   |  8                                  |             |
| uart_set_baud_rate_msg | msg_type_t |  new_msg_type("uart set baud rate") |             |
## Types

| Name          | Type | Description |
| ------------- | ---- | ----------- |
| uart_master_t |      |             |
| uart_slave_t  |      |             |
## Functions
- set_baud_rate <font id="function_arguments">(signal net : inout network_t;<br><span style="padding-left:20px"> uart_master : uart_master_t;<br><span style="padding-left:20px"> baud_rate : natural) </font> <font id="function_return">return ()</font>
**Description**
Set the baud rate [bits/s]
- set_baud_rate <font id="function_arguments">(signal net : inout network_t;<br><span style="padding-left:20px"> uart_slave : uart_slave_t;<br><span style="padding-left:20px"> baud_rate : natural) </font> <font id="function_return">return ()</font>
