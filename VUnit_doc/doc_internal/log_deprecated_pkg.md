# Package: log_deprecated_pkg
## Functions
- logger_init <font id="function_arguments">(    variable logger : inout logger_t;
    default_src     :       string                  := "";
    file_name       :       string                  := "log.csv";
    display_format  :       deprecated_log_format_t := raw;
    file_format     :       deprecated_log_format_t := off;
    stop_level      :       log_level_t             := failure;
    separator       :       character               := ',';
    append          :       boolean                 := false)</font> <font id="function_return">return ()</font>
- logger_init <font id="function_arguments">(    default_src    : string                  := "";
    file_name      : string                  := "log.csv";
    display_format : deprecated_log_format_t := raw;
    file_format    : deprecated_log_format_t := off;
    stop_level     : log_level_t             := failure;
    separator      : character               := ',';
    append         : boolean                 := false)</font> <font id="function_return">return ()</font>
- verbose <font id="function_arguments">(logger : logger_t;                    msg : string;
                    line_num : natural := 0;
                    file_name : string := "")</font> <font id="function_return">return ()</font>
- verbose <font id="function_arguments">(msg : string;                    line_num : natural := 0;
                    file_name : string := "")</font> <font id="function_return">return ()</font>
