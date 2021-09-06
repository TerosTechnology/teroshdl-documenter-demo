# Package: log_deprecated_pkg

- **File**: log_deprecated_pkg.vhd
## Functions
- logger_init <font id="function_arguments">( variable logger : inout logger_t;<br><span style="padding-left:20px"> default_src     :       string                  := "";<br><span style="padding-left:20px"> file_name       :       string                  := "log.csv";<br><span style="padding-left:20px"> display_format  :       deprecated_log_format_t := raw;<br><span style="padding-left:20px"> file_format     :       deprecated_log_format_t := off;<br><span style="padding-left:20px"> stop_level      :       log_level_t             := failure;<br><span style="padding-left:20px"> separator       :       character               := ',<br><span style="padding-left:20px">';<br><span style="padding-left:20px"> append          :       boolean                 := false) </font> <font id="function_return">return ()</font>
</br>**Description**
 Deprecated interface to better support legacy testbenches. Calls to this
 procedure will be mapped to contemporary functionality using best effort:

 * default_src sets the name of an uninitialized logger. Empty string names are not supported
   and will be replaced with "anonymous<a unique number>". Changing logger
   name of an already initialized logger is not allowed. In this case the
   empty string is the only valid value.
 * Changing the separator and append parameters to non-default values is not
   supported
 * The logger is configured with private display and file log handlers independent
   of the predefined handlers used by default_logger

- logger_init <font id="function_arguments">( default_src    : string                  := "";<br><span style="padding-left:20px"> file_name      : string                  := "log.csv";<br><span style="padding-left:20px"> display_format : deprecated_log_format_t := raw;<br><span style="padding-left:20px"> file_format    : deprecated_log_format_t := off;<br><span style="padding-left:20px"> stop_level     : log_level_t             := failure;<br><span style="padding-left:20px"> separator      : character               := ',<br><span style="padding-left:20px">';<br><span style="padding-left:20px"> append         : boolean                 := false) </font> <font id="function_return">return ()</font>
</br>**Description**
 This logger_init is used to reinitialize the default_logger and its predefined
 display and file handlers

- verbose <font id="function_arguments">(logger : logger_t;<br><span style="padding-left:20px"> msg : string;<br><span style="padding-left:20px"> line_num : natural := 0;<br><span style="padding-left:20px"> file_name : string := "") </font> <font id="function_return">return ()</font>
</br>**Description**
 VERBOSE is alias for TRACE

- verbose <font id="function_arguments">(msg : string;<br><span style="padding-left:20px"> line_num : natural := 0;<br><span style="padding-left:20px"> file_name : string := "") </font> <font id="function_return">return ()</font>
