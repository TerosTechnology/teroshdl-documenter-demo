# Package: bus_master_pkg

- **File**: bus_master_pkg.vhd
## Constants

| Name                | Type       | Value                                   | Description                                    |
| ------------------- | ---------- | --------------------------------------- | ---------------------------------------------- |
| bus_logger          | logger_t   |  get_logger("vunit_lib:bus_master_pkg") | Default logger object for bus master instances |
| bus_write_msg       | msg_type_t |  new_msg_type("write bus")              | Message type definitions, used by VC-instances |
| bus_read_msg        | msg_type_t |  new_msg_type("read bus")               |                                                |
| bus_burst_write_msg | msg_type_t |  new_msg_type("burst write bus")        |                                                |
| bus_burst_read_msg  | msg_type_t |  new_msg_type("burst read bus")         |                                                |
## Types

| Name         | Type | Description |
| ------------ | ---- | ----------- |
| bus_master_t |      |             |
## Functions
- get_logger <font id="function_arguments">(bus_handle : bus_master_t) </font> <font id="function_return">return logger_t </font>
**Description**
Return the logger used by the bus master
- write_bus <font id="function_arguments">(signal net : inout network_t;<br><span style="padding-left:20px"> constant bus_handle : bus_master_t;<br><span style="padding-left:20px"> constant address : std_logic_vector;<br><span style="padding-left:20px"> constant data : std_logic_vector;<br><span style="padding-left:20px"> constant byte_enable : std_logic_vector := "") </font> <font id="function_return">return ()</font>
**Description**
Blocking: Write the bus
- write_bus <font id="function_arguments">(signal net : inout network_t;<br><span style="padding-left:20px"> constant bus_handle : bus_master_t;<br><span style="padding-left:20px"> constant address : natural;<br><span style="padding-left:20px"> constant data : std_logic_vector;<br><span style="padding-left:20px"> constant byte_enable : std_logic_vector := "") </font> <font id="function_return">return ()</font>
- burst_write_bus <font id="function_arguments">(signal net : inout network_t;<br><span style="padding-left:20px"> constant bus_handle : bus_master_t;<br><span style="padding-left:20px"> constant address : std_logic_vector;<br><span style="padding-left:20px"> constant burst_length : positive;<br><span style="padding-left:20px"> constant data : queue_t) </font> <font id="function_return">return ()</font>
**Description**
Procedures for burst bus write: Caller is responsible for allocation anddeallocation of data queue. Procedure cunsumes burst_length data wordsfrom data queue. If data queue has less data words, all datawords are consumed and pop from empty queue error is raised.
- burst_write_bus <font id="function_arguments">(signal net : inout network_t;<br><span style="padding-left:20px"> constant bus_handle : bus_master_t;<br><span style="padding-left:20px"> constant address : natural;<br><span style="padding-left:20px"> constant burst_length : positive;<br><span style="padding-left:20px"> constant data : queue_t) </font> <font id="function_return">return ()</font>
- read_bus <font id="function_arguments">(signal net : inout network_t;<br><span style="padding-left:20px"> constant bus_handle : bus_master_t;<br><span style="padding-left:20px"> constant address : std_logic_vector;<br><span style="padding-left:20px"> variable reference : inout bus_reference_t) </font> <font id="function_return">return ()</font>
**Description**
Non blocking: Read the bus returning a reference to the future reply
- read_bus <font id="function_arguments">(signal net : inout network_t;<br><span style="padding-left:20px"> constant bus_handle : bus_master_t;<br><span style="padding-left:20px"> constant address : natural;<br><span style="padding-left:20px"> variable reference : inout bus_reference_t) </font> <font id="function_return">return ()</font>
- burst_read_bus <font id="function_arguments">(signal net : inout network_t;<br><span style="padding-left:20px"> constant bus_handle : bus_master_t;<br><span style="padding-left:20px"> constant address : std_logic_vector;<br><span style="padding-left:20px"> constant burst_length : positive;<br><span style="padding-left:20px"> variable reference : inout bus_reference_t) </font> <font id="function_return">return ()</font>
- burst_read_bus <font id="function_arguments">(signal net : inout network_t;<br><span style="padding-left:20px"> constant bus_handle : bus_master_t;<br><span style="padding-left:20px"> constant address : natural;<br><span style="padding-left:20px"> constant burst_length : positive;<br><span style="padding-left:20px"> variable reference : inout bus_reference_t) </font> <font id="function_return">return ()</font>
- await_read_bus_reply <font id="function_arguments">(signal net : inout network_t;<br><span style="padding-left:20px"> variable reference : inout bus_reference_t;<br><span style="padding-left:20px"> variable data : inout std_logic_vector) </font> <font id="function_return">return ()</font>
**Description**
Blocking: Await read bus reply data
- await_burst_read_bus_reply <font id="function_arguments">(signal net : inout network_t;<br><span style="padding-left:20px"> constant bus_handle : bus_master_t;<br><span style="padding-left:20px"> constant data : queue_t;<br><span style="padding-left:20px"> variable reference : inout bus_reference_t) </font> <font id="function_return">return ()</font>
**Description**
Procedure for burst read reply: Caller is responsible for allocation anddeallocation of data queue. Procedure pushes burst_length data wordsinto data queue.
- check_bus <font id="function_arguments">(signal net : inout network_t;<br><span style="padding-left:20px"> constant bus_handle : bus_master_t;<br><span style="padding-left:20px"> constant address : std_logic_vector;<br><span style="padding-left:20px"> constant expected : std_logic_vector;<br><span style="padding-left:20px"> constant msg : string := "") </font> <font id="function_return">return ()</font>
**Description**
Blocking: Read bus and check result against expected data
- check_bus <font id="function_arguments">(signal net : inout network_t;<br><span style="padding-left:20px"> constant bus_handle : bus_master_t;<br><span style="padding-left:20px"> constant address : natural;<br><span style="padding-left:20px"> constant expected : std_logic_vector;<br><span style="padding-left:20px"> constant msg : string := "") </font> <font id="function_return">return ()</font>
- read_bus <font id="function_arguments">(signal net : inout network_t;<br><span style="padding-left:20px"> constant bus_handle : bus_master_t;<br><span style="padding-left:20px"> constant address : std_logic_vector;<br><span style="padding-left:20px"> variable data : inout std_logic_vector) </font> <font id="function_return">return ()</font>
**Description**
Blocking: read bus with immediate reply
- read_bus <font id="function_arguments">(signal net : inout network_t;<br><span style="padding-left:20px"> constant bus_handle : bus_master_t;<br><span style="padding-left:20px"> constant address : natural;<br><span style="padding-left:20px"> variable data : inout std_logic_vector) </font> <font id="function_return">return ()</font>
- burst_read_bus <font id="function_arguments">(signal net : inout network_t;<br><span style="padding-left:20px"> constant bus_handle : bus_master_t;<br><span style="padding-left:20px"> constant address : std_logic_vector;<br><span style="padding-left:20px"> constant burst_length : positive;<br><span style="padding-left:20px"> constant data : queue_t) </font> <font id="function_return">return ()</font>
**Description**
Procedure for burst bus read: Caller is responsible for allocation anddeallocation of data queue. Procedure pushes burst_length data wordsinto data queue.
- burst_read_bus <font id="function_arguments">(signal net : inout network_t;<br><span style="padding-left:20px"> constant bus_handle : bus_master_t;<br><span style="padding-left:20px"> constant address : natural;<br><span style="padding-left:20px"> constant burst_length : positive;<br><span style="padding-left:20px"> constant data : queue_t) </font> <font id="function_return">return ()</font>
- wait_until_read_equals <font id="function_arguments">( signal net : inout network_t;<br><span style="padding-left:20px"> bus_handle   : bus_master_t;<br><span style="padding-left:20px"> addr         : std_logic_vector;<br><span style="padding-left:20px"> value        : std_logic_vector;<br><span style="padding-left:20px"> timeout      : delay_length := delay_length'high;<br><span style="padding-left:20px"> msg    : string       := "") </font> <font id="function_return">return ()</font>
**Description**
Blocking: Wait until a read from address equals the value usingstd_match If timeout is reached error with msg
- wait_until_read_bit_equals <font id="function_arguments">( signal net : inout network_t;<br><span style="padding-left:20px"> bus_handle   : bus_master_t;<br><span style="padding-left:20px"> addr         : std_logic_vector;<br><span style="padding-left:20px"> idx          : natural;<br><span style="padding-left:20px"> value        : std_logic;<br><span style="padding-left:20px"> timeout      : delay_length := delay_length'high;<br><span style="padding-left:20px"> msg    : string       := "") </font> <font id="function_return">return ()</font>
**Description**
Blocking: Wait until a read from address has the bit with thisindex set to value If timeout is reached error with msg
- wait_until_idle <font id="function_arguments">(signal net : inout network_t;<br><span style="padding-left:20px"> bus_handle : bus_master_t) </font> <font id="function_return">return ()</font>
**Description**
Wait until all operations scheduled before this command has finished
