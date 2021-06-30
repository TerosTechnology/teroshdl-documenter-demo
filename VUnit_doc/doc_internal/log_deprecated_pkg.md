# Package: log_deprecated_pkg

## Functions
- logger_init <font id="function_arguments">( variable logger : inout logger_t; default_src     :       string                  := ""; file_name       :       string                  := "log.csv"; display_format  :       deprecated_log_format_t := raw; file_format     :       deprecated_log_format_t := off; stop_level      :       log_level_t             := failure; separator       :       character               := ','; append          :       boolean                 := false) </font> <font id="function_return">return ()</font>
**Description**
* default_src sets the name of an uninitialized logger. Empty string names are not supported  and will be replaced with "anonymous<a unique number>". Changing logger  name of an already initialized logger is not allowed. In this case the  empty string is the only valid value.* Changing the separator and append parameters to non-default values is not  supported* The logger is configured with private display and file log handlers independent  of the predefined handlers used by default_logger
- logger_init <font id="function_arguments">( default_src    : string                  := ""; file_name      : string                  := "log.csv"; display_format : deprecated_log_format_t := raw; file_format    : deprecated_log_format_t := off; stop_level     : log_level_t             := failure; separator      : character               := ','; append         : boolean                 := false) </font> <font id="function_return">return ()</font>
**Description**
This logger_init is used to reinitialize the default_logger and its predefineddisplay and file handlers
- verbose <font id="function_arguments">(logger : logger_t; msg : string; line_num : natural := 0; file_name : string := "") </font> <font id="function_return">return ()</font>
**Description**
VERBOSE is alias for TRACE
- verbose <font id="function_arguments">(msg : string; line_num : natural := 0; file_name : string := "") </font> <font id="function_return">return ()</font>
