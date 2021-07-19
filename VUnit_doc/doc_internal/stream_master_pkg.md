# Package: stream_master_pkg

- **File**: stream_master_pkg.vhd
## Constants

| Name            | Type       | Value                        | Description                                                        |
| --------------- | ---------- | ---------------------------- | ------------------------------------------------------------------ |
| stream_push_msg | msg_type_t |  new_msg_type("stream push") | Message type definitions used by VC implementing stream master VCI |
## Types

| Name            | Type | Description |
| --------------- | ---- | ----------- |
| stream_master_t |      |             |
## Functions
- push_stream <font id="function_arguments">(signal net : inout network_t;<br><span style="padding-left:20px"> stream : stream_master_t;<br><span style="padding-left:20px"> data : std_logic_vector;<br><span style="padding-left:20px"> last : boolean := false) </font> <font id="function_return">return ()</font>
**Description**
Push a data value to the stream
