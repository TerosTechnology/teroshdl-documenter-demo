# Package: axi_lite_master_pkg

- **File**: axi_lite_master_pkg.vhd
## Constants

| Name               | Type       | Value                           | Description |
| ------------------ | ---------- | ------------------------------- | ----------- |
| axi_lite_read_msg  | msg_type_t |  new_msg_type("read axi lite")  |             |
| axi_lite_write_msg | msg_type_t |  new_msg_type("write axi lite") |             |
## Functions
- write_axi_lite <font id="function_arguments">(signal net : inout network_t;<br><span style="padding-left:20px"> constant bus_handle : bus_master_t;<br><span style="padding-left:20px"> constant address : std_logic_vector;<br><span style="padding-left:20px"> constant data : std_logic_vector;<br><span style="padding-left:20px"> constant expected_bresp : axi_resp_t := axi_resp_okay;<br><span style="padding-left:20px"> constant byte_enable : std_logic_vector := "") </font> <font id="function_return">return ()</font>
</br>**Description**
 Blocking: Write the bus

- read_axi_lite <font id="function_arguments">(signal net : inout network_t;<br><span style="padding-left:20px"> constant bus_handle : bus_master_t;<br><span style="padding-left:20px"> constant address : std_logic_vector;<br><span style="padding-left:20px"> constant expected_rresp : axi_resp_t := axi_resp_okay;<br><span style="padding-left:20px"> variable reference : inout bus_reference_t) </font> <font id="function_return">return ()</font>
</br>**Description**
 Non blocking: Read the bus returning a reference to the future reply

- read_axi_lite <font id="function_arguments">(signal net : inout network_t;<br><span style="padding-left:20px"> constant bus_handle : bus_master_t;<br><span style="padding-left:20px"> constant address : std_logic_vector;<br><span style="padding-left:20px"> constant expected_rresp : axi_resp_t := axi_resp_okay;<br><span style="padding-left:20px"> variable data : inout std_logic_vector) </font> <font id="function_return">return ()</font>
</br>**Description**
 Blocking: read bus with immediate reply

- check_axi_lite <font id="function_arguments">(signal net : inout network_t;<br><span style="padding-left:20px"> constant bus_handle : bus_master_t;<br><span style="padding-left:20px"> constant address : std_logic_vector;<br><span style="padding-left:20px"> constant expected_rresp : axi_resp_t := axi_resp_okay;<br><span style="padding-left:20px"> constant expected : std_logic_vector;<br><span style="padding-left:20px"> constant msg : string := "") </font> <font id="function_return">return ()</font>
</br>**Description**
 Blocking: Read bus and check result against expected data

- is_read <font id="function_arguments">(msg_type : msg_type_t) </font> <font id="function_return">return boolean </font>
- is_write <font id="function_arguments">(msg_type : msg_type_t) </font> <font id="function_return">return boolean </font>
- is_axi_lite_msg <font id="function_arguments">(msg_type : msg_type_t) </font> <font id="function_return">return boolean </font>
