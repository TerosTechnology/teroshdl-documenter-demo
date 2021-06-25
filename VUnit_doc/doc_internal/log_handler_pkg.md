# Package: log_handler_pkg
## Constants
| Name             | Type          | Value                 | Description                           |
| ---------------- | ------------- | --------------------- | ------------------------------------- |
| null_log_handler | log_handler_t |  (p_data => null_ptr) |                                       |
| stdout_file_name | string        |  ">1"                 | File name used by the display handler |
| null_file_name   | string        |  ""                   |                                       |
## Types
| Name                    | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Description                                |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| deprecated_log_format_t | (      The raw log format contains just the message without any other information     raw,       The level log format contains the level and message     level,       The verbose log format contains all information     verbose,       The csv format contains all information in machine readable format     csv,       Deprecated value not supported by new interfaces but kept for backward      compatibility reasons. NOT for new designs     off) |                                            |
| log_handler_t           |                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Log handler record, all fields are private |
| log_handler_vec_t       |                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                            |
## Functions
- set_format <font id="function_arguments">(log_handler : log_handler_t;                       format : log_format_t;
                       use_color : boolean := false)</font> <font id="function_return">return ()</font>
**Description**
Set the format to be used by the log handler
- get_format <font id="function_arguments">(constant log_handler : in log_handler_t;                       variable format : out log_format_t;
                       variable use_color : out boolean)</font> <font id="function_return">return ()</font>
**Description**
Get the format used by the log handler
- update_max_logger_name_length <font id="function_arguments">(log_handler : log_handler_t; value : natural)</font> <font id="function_return">return ()</font>
- log_to_handler <font id="function_arguments">(log_handler : log_handler_t;                           logger_name : string;
                           msg : string;
                           log_level : log_level_t;
                           log_time : time;
                           sequence_number : natural;
                           line_num : natural := 0;
                           file_name : string := "")</font> <font id="function_return">return ()</font>
- init_log_handler <font id="function_arguments">(log_handler : log_handler_t;                             format : log_format_t;
                             file_name : string;
                             use_color : boolean := false)</font> <font id="function_return">return ()</font>
