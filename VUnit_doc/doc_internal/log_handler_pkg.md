# Package: log_handler_pkg

- **File**: log_handler_pkg.vhd
## Constants

| Name             | Type          | Value                 | Description                             |
| ---------------- | ------------- | --------------------- | --------------------------------------- |
| null_log_handler | log_handler_t |  (p_data => null_ptr) |                                         |
| stdout_file_name | string        |  ">1"                 |  File name used by the display handler  |
| null_file_name   | string        |  ""                   |                                         |
## Types

| Name                    | Type                                                                                                                                                                                  | Description                                  |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| deprecated_log_format_t | ( raw,<br><span style="padding-left:20px">  level,<br><span style="padding-left:20px">  verbose,<br><span style="padding-left:20px">  csv,<br><span style="padding-left:20px">  off)  |                                              |
| log_handler_t           |                                                                                                                                                                                       |  Log handler record, all fields are private  |
| log_handler_vec_t       | array (natural range <>) of log_handler_t                                                                                                                                             |                                              |
## Functions
- set_format <font id="function_arguments">(log_handler : log_handler_t;<br><span style="padding-left:20px"> format : log_format_t;<br><span style="padding-left:20px"> use_color : boolean := false) </font> <font id="function_return">return ()</font>
</br>**Description**
 Set the format to be used by the log handler

- get_format <font id="function_arguments">(constant log_handler : in log_handler_t;<br><span style="padding-left:20px"> variable format : out log_format_t;<br><span style="padding-left:20px"> variable use_color : out boolean) </font> <font id="function_return">return ()</font>
</br>**Description**
 Get the format used by the log handler

- update_max_logger_name_length <font id="function_arguments">(log_handler : log_handler_t;<br><span style="padding-left:20px"> value : natural) </font> <font id="function_return">return ()</font>
- log_to_handler <font id="function_arguments">(log_handler : log_handler_t;<br><span style="padding-left:20px"> logger_name : string;<br><span style="padding-left:20px"> msg : string;<br><span style="padding-left:20px"> log_level : log_level_t;<br><span style="padding-left:20px"> log_time : time;<br><span style="padding-left:20px"> sequence_number : natural;<br><span style="padding-left:20px"> line_num : natural := 0;<br><span style="padding-left:20px"> file_name : string := "") </font> <font id="function_return">return ()</font>
- init_log_handler <font id="function_arguments">(log_handler : log_handler_t;<br><span style="padding-left:20px"> format : log_format_t;<br><span style="padding-left:20px"> file_name : string;<br><span style="padding-left:20px"> use_color : boolean := false) </font> <font id="function_return">return ()</font>
