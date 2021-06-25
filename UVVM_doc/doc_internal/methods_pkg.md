# Package: methods_pkg
## Constants
| Name           | Type   | Value            | Description |
| -------------- | ------ | ---------------- | ----------- |
| C_UVVM_VERSION | string |  "v2 2021.05.26" |             |
## Functions
- check_file_open_status <font id="function_arguments">(    constant status    : in file_open_status;
    constant file_name : in string;
    constant scope     : in string := C_SCOPE
    )</font> <font id="function_return">return ()</font>
**Description**
============================================================================File handling (that needs to use other utility methods)============================================================================
- set_alert_file_name <font id="function_arguments">(    constant file_name : string := C_ALERT_FILE_NAME
    )</font> <font id="function_return">return ()</font>
- set_alert_file_name <font id="function_arguments">(    constant file_name : string := C_ALERT_FILE_NAME;
    constant msg_id    : t_msg_id
    )</font> <font id="function_return">return ()</font>
**Description**
msg_id is unused. This is a deprecated overload
- set_log_file_name <font id="function_arguments">(    constant file_name : string := C_LOG_FILE_NAME
    )</font> <font id="function_return">return ()</font>
- set_log_file_name <font id="function_arguments">(    constant file_name : string := C_LOG_FILE_NAME;
    constant msg_id    : t_msg_id
    )</font> <font id="function_return">return ()</font>
**Description**
msg_id is unused. This is a deprecated overload
- log <font id="function_arguments">(    msg_id          : t_msg_id;
    msg             : string;
    scope           : string            := C_TB_SCOPE_DEFAULT;
    msg_id_panel    : t_msg_id_panel    := shared_msg_id_panel;
    log_destination : t_log_destination := shared_default_log_destination;
    log_file_name   : string            := C_LOG_FILE_NAME;
    open_mode       : file_open_kind    := append_mode
    )</font> <font id="function_return">return ()</font>
**Description**
============================================================================Log-related============================================================================
- log <font id="function_arguments">(    msg             : string;
    scope           : string            := C_TB_SCOPE_DEFAULT;
    msg_id_panel    : t_msg_id_panel    := shared_msg_id_panel;
    log_destination : t_log_destination := shared_default_log_destination;
    log_file_name   : string            := C_LOG_FILE_NAME;
    open_mode       : file_open_kind    := append_mode
    )</font> <font id="function_return">return ()</font>
- log_text_block <font id="function_arguments">(    msg_id              :       t_msg_id;
    variable text_block : inout line;
    formatting          :       t_log_format;   FORMATTED or UNFORMATTED
    msg_header          :       string               := "";
    scope               :       string               := C_TB_SCOPE_DEFAULT;
    msg_id_panel        :       t_msg_id_panel       := shared_msg_id_panel;
    log_if_block_empty  :       t_log_if_block_empty := WRITE_HDR_IF_BLOCK_EMPTY;
    log_destination     :       t_log_destination    := shared_default_log_destination;
    log_file_name       :       string               := C_LOG_FILE_NAME;
    open_mode           :       file_open_kind       := append_mode
    )</font> <font id="function_return">return ()</font>
- write_to_file <font id="function_arguments">(    file_name        :       string;
    open_mode        :       file_open_kind;
    variable my_line : inout line
    )</font> <font id="function_return">return ()</font>
- write_line_to_log_destination <font id="function_arguments">(    variable log_line        : inout line;
    constant log_destination : in    t_log_destination := shared_default_log_destination;
    constant log_file_name   : in    string            := C_LOG_FILE_NAME;
    constant open_mode       : in    file_open_kind    := append_mode
    )</font> <font id="function_return">return ()</font>
- enable_log_msg <font id="function_arguments">(    constant msg_id       :       t_msg_id;
    variable msg_id_panel : inout t_msg_id_panel;
    constant msg          :       string      := "";
    constant scope        :       string      := C_TB_SCOPE_DEFAULT;
    constant quietness    :       t_quietness := NON_QUIET
    )</font> <font id="function_return">return ()</font>
- enable_log_msg <font id="function_arguments">(    msg_id    : t_msg_id;
    msg       : string;
    quietness : t_quietness := NON_QUIET;
    scope     : string      := C_TB_SCOPE_DEFAULT
    )</font> <font id="function_return">return ()</font>
- enable_log_msg <font id="function_arguments">(    msg_id    : t_msg_id;
    quietness : t_quietness := NON_QUIET;
    scope     : string      := C_TB_SCOPE_DEFAULT
    )</font> <font id="function_return">return ()</font>
- disable_log_msg <font id="function_arguments">(    constant msg_id       :       t_msg_id;
    variable msg_id_panel : inout t_msg_id_panel;
    constant msg          :       string      := "";
    constant scope        :       string      := C_TB_SCOPE_DEFAULT;
    constant quietness    :       t_quietness := NON_QUIET
    )</font> <font id="function_return">return ()</font>
- disable_log_msg <font id="function_arguments">(    msg_id    : t_msg_id;
    msg       : string;
    quietness : t_quietness := NON_QUIET;
    scope     : string      := C_TB_SCOPE_DEFAULT
    )</font> <font id="function_return">return ()</font>
- disable_log_msg <font id="function_arguments">(    msg_id    : t_msg_id;
    quietness : t_quietness := NON_QUIET;
    scope     : string      := C_TB_SCOPE_DEFAULT
    )</font> <font id="function_return">return ()</font>
- set_log_destination <font id="function_arguments">(    constant log_destination : t_log_destination;
    constant quietness       : t_quietness := NON_QUIET
    )</font> <font id="function_return">return ()</font>
- alert <font id="function_arguments">(    constant alert_level : t_alert_level;
    constant msg         : string;
    constant scope       : string := C_TB_SCOPE_DEFAULT
    )</font> <font id="function_return">return ()</font>
**Description**
============================================================================Alert-related============================================================================
- note <font id="function_arguments">(    constant msg   : string;
    constant scope : string := C_TB_SCOPE_DEFAULT
    )</font> <font id="function_return">return ()</font>
**Description**
Dedicated alert-procedures all alert levels (less verbose - as 2 rather than 3 parameters...)
- tb_note <font id="function_arguments">(    constant msg   : string;
    constant scope : string := C_TB_SCOPE_DEFAULT
    )</font> <font id="function_return">return ()</font>
- warning <font id="function_arguments">(    constant msg   : string;
    constant scope : string := C_TB_SCOPE_DEFAULT
    )</font> <font id="function_return">return ()</font>
- tb_warning <font id="function_arguments">(    constant msg   : string;
    constant scope : string := C_TB_SCOPE_DEFAULT
    )</font> <font id="function_return">return ()</font>
- manual_check <font id="function_arguments">(    constant msg   : string;
    constant scope : string := C_TB_SCOPE_DEFAULT
    )</font> <font id="function_return">return ()</font>
- error <font id="function_arguments">(    constant msg   : string;
    constant scope : string := C_TB_SCOPE_DEFAULT
    )</font> <font id="function_return">return ()</font>
- tb_error <font id="function_arguments">(    constant msg   : string;
    constant scope : string := C_TB_SCOPE_DEFAULT
    )</font> <font id="function_return">return ()</font>
- failure <font id="function_arguments">(    constant msg   : string;
    constant scope : string := C_TB_SCOPE_DEFAULT
    )</font> <font id="function_return">return ()</font>
- tb_failure <font id="function_arguments">(    constant msg   : string;
    constant scope : string := C_TB_SCOPE_DEFAULT
    )</font> <font id="function_return">return ()</font>
- increment_expected_alerts <font id="function_arguments">(    constant alert_level : t_alert_level;
    constant number      : natural := 1;
    constant msg         : string  := "";
    constant scope       : string  := C_TB_SCOPE_DEFAULT
    )</font> <font id="function_return">return ()</font>
- report_alert_counters <font id="function_arguments">(    constant order : in t_order
    )</font> <font id="function_return">return ()</font>
- report_alert_counters <font id="function_arguments">(    constant dummy : in t_void
    )</font> <font id="function_return">return ()</font>
- report_global_ctrl <font id="function_arguments">(    constant dummy : in t_void
    )</font> <font id="function_return">return ()</font>
- report_msg_id_panel <font id="function_arguments">(    constant dummy : in t_void
    )</font> <font id="function_return">return ()</font>
- set_alert_attention <font id="function_arguments">(    alert_level : t_alert_level;
    attention   : t_attention;
    msg         : string := ""
    )</font> <font id="function_return">return ()</font>
- set_alert_stop_limit <font id="function_arguments">(    alert_level : t_alert_level;
    value       : natural
    )</font> <font id="function_return">return ()</font>
- increment_alert_counter <font id="function_arguments">(    alert_level : t_alert_level;
    attention   : t_attention := REGARD;   regard, expect, ignore
    number      : natural     := 1
    )</font> <font id="function_return">return ()</font>
- increment_expected_alerts_and_stop_limit <font id="function_arguments">(    constant alert_level : t_alert_level;
    constant number      : natural := 1;
    constant msg         : string  := "";
    constant scope       : string  := C_TB_SCOPE_DEFAULT
    )</font> <font id="function_return">return ()</font>
- report_check_counters <font id="function_arguments">(    constant dummy : in t_void
    )</font> <font id="function_return">return ()</font>
- report_check_counters <font id="function_arguments">(    constant order : in t_order
    )</font> <font id="function_return">return ()</font>
- deprecate <font id="function_arguments">(    caller_name  : string;
    constant msg : string := ""
    )</font> <font id="function_return">return ()</font>
**Description**
============================================================================Deprecate message============================================================================
- matching_widths <font id="function_arguments">(    value1 : std_logic_vector;
    value2 : std_logic_vector
    )</font> <font id="function_return">return boolean</font>
**Description**
============================================================================Non time consuming checks============================================================================Matching if same width or only zeros in "extended width"
- matching_widths <font id="function_arguments">(    value1 : unsigned;
    value2 : unsigned
    )</font> <font id="function_return">return boolean</font>
- matching_widths <font id="function_arguments">(    value1 : signed;
    value2 : signed
    )</font> <font id="function_return">return boolean</font>
- check_value <font id="function_arguments">(    constant value        : boolean;
    constant alert_level  : t_alert_level;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_value()"
    )</font> <font id="function_return">return ()</font>
**Description**
overloads for procedure version of check_value (no return value)
- check_value <font id="function_arguments">(    constant value        : boolean;
    constant exp          : boolean;
    constant alert_level  : t_alert_level;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_value()"
    )</font> <font id="function_return">return ()</font>
- check_value <font id="function_arguments">(    constant value            : std_logic_vector;
    constant exp              : std_logic_vector;
    constant match_strictness : t_match_strictness;
    constant alert_level      : t_alert_level;
    constant msg              : string;
    constant scope            : string         := C_TB_SCOPE_DEFAULT;
    constant radix            : t_radix        := HEX_BIN_IF_INVALID;
    constant format           : t_format_zeros := KEEP_LEADING_0;
    constant msg_id           : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel     : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name      : string         := "check_value()";
    constant value_type       : string         := "slv"
    )</font> <font id="function_return">return ()</font>
- check_value <font id="function_arguments">(    constant value        : std_logic_vector;
    constant exp          : std_logic_vector;
    constant alert_level  : t_alert_level;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant radix        : t_radix        := HEX_BIN_IF_INVALID;
    constant format       : t_format_zeros := KEEP_LEADING_0;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_value()";
    constant value_type   : string         := "slv"
    )</font> <font id="function_return">return ()</font>
- check_value <font id="function_arguments">(    constant value            : unsigned;
    constant exp              : unsigned;
    constant match_strictness : t_match_strictness;
    constant alert_level      : t_alert_level;
    constant msg              : string;
    constant scope            : string         := C_TB_SCOPE_DEFAULT;
    constant radix            : t_radix        := HEX_BIN_IF_INVALID;
    constant format           : t_format_zeros := KEEP_LEADING_0;
    constant msg_id           : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel     : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name      : string         := "check_value()";
    constant value_type       : string         := "unsigned"
    )</font> <font id="function_return">return ()</font>
- check_value <font id="function_arguments">(    constant value        : unsigned;
    constant exp          : unsigned;
    constant alert_level  : t_alert_level;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant radix        : t_radix        := HEX_BIN_IF_INVALID;
    constant format       : t_format_zeros := KEEP_LEADING_0;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_value()";
    constant value_type   : string         := "unsigned"
    )</font> <font id="function_return">return ()</font>
- check_value <font id="function_arguments">(    constant value            : signed;
    constant exp              : signed;
    constant match_strictness : t_match_strictness;
    constant alert_level      : t_alert_level;
    constant msg              : string;
    constant scope            : string         := C_TB_SCOPE_DEFAULT;
    constant radix            : t_radix        := HEX_BIN_IF_INVALID;
    constant format           : t_format_zeros := KEEP_LEADING_0;
    constant msg_id           : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel     : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name      : string         := "check_value()";
    constant value_type       : string         := "signed"
    )</font> <font id="function_return">return ()</font>
- check_value <font id="function_arguments">(    constant value        : signed;
    constant exp          : signed;
    constant alert_level  : t_alert_level;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant radix        : t_radix        := HEX_BIN_IF_INVALID;
    constant format       : t_format_zeros := KEEP_LEADING_0;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_value()";
    constant value_type   : string         := "signed"
    )</font> <font id="function_return">return ()</font>
- check_value <font id="function_arguments">(    constant value        : std_logic;
    constant exp          : std_logic;
    constant alert_level  : t_alert_level;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_value()"
    )</font> <font id="function_return">return ()</font>
- check_value <font id="function_arguments">(    constant value            : std_logic;
    constant exp              : std_logic;
    constant match_strictness : t_match_strictness;
    constant alert_level      : t_alert_level;
    constant msg              : string;
    constant scope            : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id           : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel     : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name      : string         := "check_value()"
    )</font> <font id="function_return">return ()</font>
- check_value <font id="function_arguments">(    constant value        : integer;
    constant exp          : integer;
    constant alert_level  : t_alert_level;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_value()"
    )</font> <font id="function_return">return ()</font>
- check_value <font id="function_arguments">(    constant value        : real;
    constant exp          : real;
    constant alert_level  : t_alert_level;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_value()"
    )</font> <font id="function_return">return ()</font>
- check_value <font id="function_arguments">(    constant value        : time;
    constant exp          : time;
    constant alert_level  : t_alert_level;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_value()"
    )</font> <font id="function_return">return ()</font>
- check_value <font id="function_arguments">(    constant value        : string;
    constant exp          : string;
    constant alert_level  : t_alert_level;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_value()"
    )</font> <font id="function_return">return ()</font>
- check_value <font id="function_arguments">(    constant value            : t_slv_array;
    constant exp              : t_slv_array;
    constant match_strictness : t_match_strictness;
    constant alert_level      : t_alert_level;
    constant msg              : string;
    constant scope            : string         := C_TB_SCOPE_DEFAULT;
    constant radix            : t_radix        := HEX_BIN_IF_INVALID;
    constant format           : t_format_zeros := KEEP_LEADING_0;
    constant msg_id           : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel     : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name      : string         := "check_value()";
    constant value_type       : string         := "t_slv_array"
    )</font> <font id="function_return">return ()</font>
- check_value <font id="function_arguments">(    constant value        : t_slv_array;
    constant exp          : t_slv_array;
    constant alert_level  : t_alert_level;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant radix        : t_radix        := HEX_BIN_IF_INVALID;
    constant format       : t_format_zeros := KEEP_LEADING_0;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_value()";
    constant value_type   : string         := "t_slv_array"
    )</font> <font id="function_return">return ()</font>
- check_value <font id="function_arguments">(    constant value            : t_signed_array;
    constant exp              : t_signed_array;
    constant match_strictness : t_match_strictness;
    constant alert_level      : t_alert_level;
    constant msg              : string;
    constant scope            : string         := C_TB_SCOPE_DEFAULT;
    constant radix            : t_radix        := HEX_BIN_IF_INVALID;
    constant format           : t_format_zeros := KEEP_LEADING_0;
    constant msg_id           : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel     : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name      : string         := "check_value()";
    constant value_type       : string         := "t_signed_array"
    )</font> <font id="function_return">return ()</font>
- check_value <font id="function_arguments">(    constant value        : t_signed_array;
    constant exp          : t_signed_array;
    constant alert_level  : t_alert_level;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant radix        : t_radix        := HEX_BIN_IF_INVALID;
    constant format       : t_format_zeros := KEEP_LEADING_0;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_value()";
    constant value_type   : string         := "t_signed_array"
    )</font> <font id="function_return">return ()</font>
- check_value <font id="function_arguments">(    constant value            : t_unsigned_array;
    constant exp              : t_unsigned_array;
    constant match_strictness : t_match_strictness;
    constant alert_level      : t_alert_level;
    constant msg              : string;
    constant scope            : string         := C_TB_SCOPE_DEFAULT;
    constant radix            : t_radix        := HEX_BIN_IF_INVALID;
    constant format           : t_format_zeros := KEEP_LEADING_0;
    constant msg_id           : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel     : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name      : string         := "check_value()";
    constant value_type       : string         := "t_unsigned_array"
    )</font> <font id="function_return">return ()</font>
- check_value <font id="function_arguments">(    constant value        : t_unsigned_array;
    constant exp          : t_unsigned_array;
    constant alert_level  : t_alert_level;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant radix        : t_radix        := HEX_BIN_IF_INVALID;
    constant format       : t_format_zeros := KEEP_LEADING_0;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_value()";
    constant value_type   : string         := "t_unsigned_array"
    )</font> <font id="function_return">return ()</font>
- check_value <font id="function_arguments">(    constant value        : boolean;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_value()"
    )</font> <font id="function_return">return ()</font>
**Description**
Procedure overloads for check_value without mandatory alert_level
- check_value <font id="function_arguments">(    constant value        : boolean;
    constant exp          : boolean;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_value()"
    )</font> <font id="function_return">return ()</font>
- check_value <font id="function_arguments">(    constant value            : std_logic_vector;
    constant exp              : std_logic_vector;
    constant match_strictness : t_match_strictness;
    constant msg              : string;
    constant scope            : string         := C_TB_SCOPE_DEFAULT;
    constant radix            : t_radix        := HEX_BIN_IF_INVALID;
    constant format           : t_format_zeros := KEEP_LEADING_0;
    constant msg_id           : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel     : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name      : string         := "check_value()";
    constant value_type       : string         := "slv"
    )</font> <font id="function_return">return ()</font>
- check_value <font id="function_arguments">(    constant value        : std_logic_vector;
    constant exp          : std_logic_vector;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant radix        : t_radix        := HEX_BIN_IF_INVALID;
    constant format       : t_format_zeros := KEEP_LEADING_0;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_value()";
    constant value_type   : string         := "slv"
    )</font> <font id="function_return">return ()</font>
- check_value <font id="function_arguments">(    constant value            : unsigned;
    constant exp              : unsigned;
    constant match_strictness : t_match_strictness;
    constant msg              : string;
    constant scope            : string         := C_TB_SCOPE_DEFAULT;
    constant radix            : t_radix        := HEX_BIN_IF_INVALID;
    constant format           : t_format_zeros := KEEP_LEADING_0;
    constant msg_id           : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel     : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name      : string         := "check_value()";
    constant value_type       : string         := "unsigned"
    )</font> <font id="function_return">return ()</font>
- check_value <font id="function_arguments">(    constant value        : unsigned;
    constant exp          : unsigned;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant radix        : t_radix        := HEX_BIN_IF_INVALID;
    constant format       : t_format_zeros := KEEP_LEADING_0;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_value()";
    constant value_type   : string         := "unsigned"
    )</font> <font id="function_return">return ()</font>
- check_value <font id="function_arguments">(    constant value            : signed;
    constant exp              : signed;
    constant match_strictness : t_match_strictness;
    constant msg              : string;
    constant scope            : string         := C_TB_SCOPE_DEFAULT;
    constant radix            : t_radix        := HEX_BIN_IF_INVALID;
    constant format           : t_format_zeros := KEEP_LEADING_0;
    constant msg_id           : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel     : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name      : string         := "check_value()";
    constant value_type       : string         := "signed"
    )</font> <font id="function_return">return ()</font>
- check_value <font id="function_arguments">(    constant value        : signed;
    constant exp          : signed;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant radix        : t_radix        := HEX_BIN_IF_INVALID;
    constant format       : t_format_zeros := KEEP_LEADING_0;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_value()";
    constant value_type   : string         := "signed"
    )</font> <font id="function_return">return ()</font>
- check_value <font id="function_arguments">(    constant value        : std_logic;
    constant exp          : std_logic;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_value()"
    )</font> <font id="function_return">return ()</font>
- check_value <font id="function_arguments">(    constant value            : std_logic;
    constant exp              : std_logic;
    constant match_strictness : t_match_strictness;
    constant msg              : string;
    constant scope            : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id           : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel     : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name      : string         := "check_value()"
    )</font> <font id="function_return">return ()</font>
- check_value <font id="function_arguments">(    constant value        : integer;
    constant exp          : integer;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_value()"
    )</font> <font id="function_return">return ()</font>
- check_value <font id="function_arguments">(    constant value        : real;
    constant exp          : real;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_value()"
    )</font> <font id="function_return">return ()</font>
- check_value <font id="function_arguments">(    constant value        : time;
    constant exp          : time;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_value()"
    )</font> <font id="function_return">return ()</font>
- check_value <font id="function_arguments">(    constant value        : string;
    constant exp          : string;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_value()"
    )</font> <font id="function_return">return ()</font>
- check_value <font id="function_arguments">(    constant value            : t_slv_array;
    constant exp              : t_slv_array;
    constant match_strictness : t_match_strictness;
    constant msg              : string;
    constant scope            : string         := C_TB_SCOPE_DEFAULT;
    constant radix            : t_radix        := HEX_BIN_IF_INVALID;
    constant format           : t_format_zeros := KEEP_LEADING_0;
    constant msg_id           : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel     : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name      : string         := "check_value()";
    constant value_type       : string         := "t_slv_array"
    )</font> <font id="function_return">return ()</font>
- check_value <font id="function_arguments">(    constant value        : t_slv_array;
    constant exp          : t_slv_array;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant radix        : t_radix        := HEX_BIN_IF_INVALID;
    constant format       : t_format_zeros := KEEP_LEADING_0;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_value()";
    constant value_type   : string         := "t_slv_array"
    )</font> <font id="function_return">return ()</font>
- check_value <font id="function_arguments">(    constant value            : t_signed_array;
    constant exp              : t_signed_array;
    constant match_strictness : t_match_strictness;
    constant msg              : string;
    constant scope            : string         := C_TB_SCOPE_DEFAULT;
    constant radix            : t_radix        := HEX_BIN_IF_INVALID;
    constant format           : t_format_zeros := KEEP_LEADING_0;
    constant msg_id           : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel     : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name      : string         := "check_value()";
    constant value_type       : string         := "t_signed_array"
    )</font> <font id="function_return">return ()</font>
- check_value <font id="function_arguments">(    constant value        : t_signed_array;
    constant exp          : t_signed_array;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant radix        : t_radix        := HEX_BIN_IF_INVALID;
    constant format       : t_format_zeros := KEEP_LEADING_0;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_value()";
    constant value_type   : string         := "t_signed_array"
    )</font> <font id="function_return">return ()</font>
- check_value <font id="function_arguments">(    constant value            : t_unsigned_array;
    constant exp              : t_unsigned_array;
    constant match_strictness : t_match_strictness;
    constant msg              : string;
    constant scope            : string         := C_TB_SCOPE_DEFAULT;
    constant radix            : t_radix        := HEX_BIN_IF_INVALID;
    constant format           : t_format_zeros := KEEP_LEADING_0;
    constant msg_id           : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel     : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name      : string         := "check_value()";
    constant value_type       : string         := "t_unsigned_array"
    )</font> <font id="function_return">return ()</font>
- check_value <font id="function_arguments">(    constant value        : t_unsigned_array;
    constant exp          : t_unsigned_array;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant radix        : t_radix        := HEX_BIN_IF_INVALID;
    constant format       : t_format_zeros := KEEP_LEADING_0;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_value()";
    constant value_type   : string         := "t_unsigned_array"
    )</font> <font id="function_return">return ()</font>
- check_value_in_range <font id="function_arguments">(    constant value        : integer;
    constant min_value    : integer;
    constant max_value    : integer;
    constant alert_level  : t_alert_level;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_value_in_range()"
    )</font> <font id="function_return">return ()</font>
**Description**
Procedure overloads for check_value_in_range
- check_value_in_range <font id="function_arguments">(    constant value        : unsigned;
    constant min_value    : unsigned;
    constant max_value    : unsigned;
    constant alert_level  : t_alert_level;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_value_in_range()"
    )</font> <font id="function_return">return ()</font>
- check_value_in_range <font id="function_arguments">(    constant value        : signed;
    constant min_value    : signed;
    constant max_value    : signed;
    constant alert_level  : t_alert_level;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_value_in_range()"
    )</font> <font id="function_return">return ()</font>
- check_value_in_range <font id="function_arguments">(    constant value        : time;
    constant min_value    : time;
    constant max_value    : time;
    constant alert_level  : t_alert_level;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_value_in_range()"
    )</font> <font id="function_return">return ()</font>
- check_value_in_range <font id="function_arguments">(    constant value        : real;
    constant min_value    : real;
    constant max_value    : real;
    constant alert_level  : t_alert_level;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_value_in_range()"
    )</font> <font id="function_return">return ()</font>
- check_value_in_range <font id="function_arguments">(    constant value        : integer;
    constant min_value    : integer;
    constant max_value    : integer;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_value_in_range()"
    )</font> <font id="function_return">return ()</font>
**Description**
Procedure overloads for check_value_in_range without mandatory alert_level
- check_value_in_range <font id="function_arguments">(    constant value        : unsigned;
    constant min_value    : unsigned;
    constant max_value    : unsigned;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_value_in_range()"
    )</font> <font id="function_return">return ()</font>
- check_value_in_range <font id="function_arguments">(    constant value        : signed;
    constant min_value    : signed;
    constant max_value    : signed;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_value_in_range()"
    )</font> <font id="function_return">return ()</font>
- check_value_in_range <font id="function_arguments">(    constant value        : time;
    constant min_value    : time;
    constant max_value    : time;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_value_in_range()"
    )</font> <font id="function_return">return ()</font>
- check_value_in_range <font id="function_arguments">(    constant value        : real;
    constant min_value    : real;
    constant max_value    : real;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_value_in_range()"
    )</font> <font id="function_return">return ()</font>
- check_stable <font id="function_arguments">(    signal target         : boolean;
    constant stable_req   : time;
    constant alert_level  : t_alert_level;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_stable()";
    constant value_type   : string         := "boolean"
    )</font> <font id="function_return">return ()</font>
**Description**
Check_stable
- check_stable <font id="function_arguments">(    signal target         : in  std_logic_vector;
    constant stable_req   : in  time;
    constant alert_level  : in  t_alert_level;
    variable success      : out boolean;
    constant msg          : in  string;
    constant scope        : in  string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : in  t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : in  t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : in  string         := "check_stable()";
    constant value_type   : in  string         := "slv"
    )</font> <font id="function_return">return ()</font>
- check_stable <font id="function_arguments">(    signal target         : std_logic_vector;
    constant stable_req   : time;
    constant alert_level  : t_alert_level;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_stable()";
    constant value_type   : string         := "slv"
    )</font> <font id="function_return">return ()</font>
- check_stable <font id="function_arguments">(    signal target         : unsigned;
    constant stable_req   : time;
    constant alert_level  : t_alert_level;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_stable()";
    constant value_type   : string         := "unsigned"
    )</font> <font id="function_return">return ()</font>
- check_stable <font id="function_arguments">(    signal target         : signed;
    constant stable_req   : time;
    constant alert_level  : t_alert_level;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_stable()";
    constant value_type   : string         := "signed"
    )</font> <font id="function_return">return ()</font>
- check_stable <font id="function_arguments">(    signal target         : std_logic;
    constant stable_req   : time;
    constant alert_level  : t_alert_level;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_stable()";
    constant value_type   : string         := "std_logic"
    )</font> <font id="function_return">return ()</font>
- check_stable <font id="function_arguments">(    signal target         : integer;
    constant stable_req   : time;
    constant alert_level  : t_alert_level;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_stable()";
    constant value_type   : string         := "integer"
    )</font> <font id="function_return">return ()</font>
- check_stable <font id="function_arguments">(    signal target         : real;
    constant stable_req   : time;
    constant alert_level  : t_alert_level;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_stable()";
    constant value_type   : string         := "real"
    )</font> <font id="function_return">return ()</font>
- check_stable <font id="function_arguments">(    signal target         : boolean;
    constant stable_req   : time;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_stable()";
    constant value_type   : string         := "boolean"
    )</font> <font id="function_return">return ()</font>
**Description**
Procedure overloads for check_stable without mandatory alert_level
- check_stable <font id="function_arguments">(    signal target         : std_logic_vector;
    constant stable_req   : time;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_stable()";
    constant value_type   : string         := "slv"
    )</font> <font id="function_return">return ()</font>
- check_stable <font id="function_arguments">(    signal target         : unsigned;
    constant stable_req   : time;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_stable()";
    constant value_type   : string         := "unsigned"
    )</font> <font id="function_return">return ()</font>
- check_stable <font id="function_arguments">(    signal target         : signed;
    constant stable_req   : time;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_stable()";
    constant value_type   : string         := "signed"
    )</font> <font id="function_return">return ()</font>
- check_stable <font id="function_arguments">(    signal target         : std_logic;
    constant stable_req   : time;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_stable()";
    constant value_type   : string         := "std_logic"
    )</font> <font id="function_return">return ()</font>
- check_stable <font id="function_arguments">(    signal target         : integer;
    constant stable_req   : time;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_stable()";
    constant value_type   : string         := "integer"
    )</font> <font id="function_return">return ()</font>
- check_stable <font id="function_arguments">(    signal target         : real;
    constant stable_req   : time;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant caller_name  : string         := "check_stable()";
    constant value_type   : string         := "real"
    )</font> <font id="function_return">return ()</font>
- random <font id="function_arguments">(    variable v_seed1  : inout positive;
    variable v_seed2  : inout positive;
    variable v_target : inout std_logic_vector
    )</font> <font id="function_return">return ()</font>
- random <font id="function_arguments">(    variable v_seed1  : inout positive;
    variable v_seed2  : inout positive;
    variable v_target : inout std_logic
    )</font> <font id="function_return">return ()</font>
- random <font id="function_arguments">(    constant min_value :       integer;
    constant max_value :       integer;
    variable v_seed1   : inout positive;
    variable v_seed2   : inout positive;
    variable v_target  : inout integer
    )</font> <font id="function_return">return ()</font>
- random <font id="function_arguments">(    constant min_value :       real;
    constant max_value :       real;
    variable v_seed1   : inout positive;
    variable v_seed2   : inout positive;
    variable v_target  : inout real
    )</font> <font id="function_return">return ()</font>
- random <font id="function_arguments">(    constant min_value :       time;
    constant max_value :       time;
    variable v_seed1   : inout positive;
    variable v_seed2   : inout positive;
    variable v_target  : inout time
    )</font> <font id="function_return">return ()</font>
- randomize <font id="function_arguments">(    constant seed1 : positive;
    constant seed2 : positive;
    constant msg   : string := "randomizing seeds";
    constant scope : string := C_TB_SCOPE_DEFAULT
    )</font> <font id="function_return">return ()</font>
- randomise <font id="function_arguments">(    constant seed1 : positive;
    constant seed2 : positive;
    constant msg   : string := "randomising seeds";
    constant scope : string := C_TB_SCOPE_DEFAULT
    )</font> <font id="function_return">return ()</font>
- convert_byte_array_to_slv <font id="function_arguments">(    constant byte_array      : t_byte_array;
    constant byte_endianness : t_byte_endianness
    )</font> <font id="function_return">return std_logic_vector</font>
- convert_slv_to_byte_array <font id="function_arguments">(    constant slv             : std_logic_vector;
    constant byte_endianness : t_byte_endianness
    )</font> <font id="function_return">return t_byte_array</font>
- convert_byte_array_to_slv_array <font id="function_arguments">(    constant byte_array      : t_byte_array;
    constant bytes_in_word   : natural;
    constant byte_endianness : t_byte_endianness := LOWER_BYTE_LEFT
    )</font> <font id="function_return">return t_slv_array</font>
- convert_slv_array_to_byte_array <font id="function_arguments">(    constant slv_array       : t_slv_array;
    constant byte_endianness : t_byte_endianness := LOWER_BYTE_LEFT
    )</font> <font id="function_return">return t_byte_array</font>
- convert_slv_array_to_byte_array <font id="function_arguments">(      constant slv_array        : t_slv_array;
      constant ascending        : boolean           := false;
      constant byte_endianness  : t_byte_endianness := FIRST_BYTE_LEFT
    )</font> <font id="function_return">return t_byte_array</font>
- reverse_vector <font id="function_arguments">(    constant value : std_logic_vector
    )</font> <font id="function_return">return std_logic_vector</font>
- log2 <font id="function_arguments">(    constant num : positive
    )</font> <font id="function_return">return natural</font>
- matching_values <font id="function_arguments">(    constant value1           : in std_logic_vector;
    constant value2           : in std_logic_vector;
    constant match_strictness : in t_match_strictness := MATCH_STD
    )</font> <font id="function_return">return boolean</font>
**Description**
Warning! This function should NOT be used outside the UVVM library.         Function is only included to support internal functionality.         The function can be removed without notification.
- await_change <font id="function_arguments">(    signal target         : boolean;
    constant min_time     : time;
    constant max_time     : time;
    constant alert_level  : t_alert_level;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant value_type   : string         := "boolean"
    )</font> <font id="function_return">return ()</font>
**Description**
============================================================================Time consuming checks============================================================================
- await_change <font id="function_arguments">(    signal target         : std_logic;
    constant min_time     : time;
    constant max_time     : time;
    constant alert_level  : t_alert_level;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant value_type   : string         := "std_logic"
    )</font> <font id="function_return">return ()</font>
- await_change <font id="function_arguments">(    signal target         : std_logic_vector;
    constant min_time     : time;
    constant max_time     : time;
    constant alert_level  : t_alert_level;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant value_type   : string         := "slv"
    )</font> <font id="function_return">return ()</font>
- await_change <font id="function_arguments">(    signal target         : unsigned;
    constant min_time     : time;
    constant max_time     : time;
    constant alert_level  : t_alert_level;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant value_type   : string         := "unsigned"
    )</font> <font id="function_return">return ()</font>
- await_change <font id="function_arguments">(    signal target         : signed;
    constant min_time     : time;
    constant max_time     : time;
    constant alert_level  : t_alert_level;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant value_type   : string         := "signed"
    )</font> <font id="function_return">return ()</font>
- await_change <font id="function_arguments">(    signal target         : integer;
    constant min_time     : time;
    constant max_time     : time;
    constant alert_level  : t_alert_level;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant value_type   : string         := "integer"
    )</font> <font id="function_return">return ()</font>
- await_change <font id="function_arguments">(    signal target         : real;
    constant min_time     : time;
    constant max_time     : time;
    constant alert_level  : t_alert_level;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant value_type   : string         := "real"
    )</font> <font id="function_return">return ()</font>
- await_change <font id="function_arguments">(    signal target         : boolean;
    constant min_time     : time;
    constant max_time     : time;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant value_type   : string         := "boolean"
    )</font> <font id="function_return">return ()</font>
**Description**
Procedure overloads for await_change without mandatory alert_level
- await_change <font id="function_arguments">(    signal target         : std_logic;
    constant min_time     : time;
    constant max_time     : time;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant value_type   : string         := "std_logic"
    )</font> <font id="function_return">return ()</font>
- await_change <font id="function_arguments">(    signal target         : std_logic_vector;
    constant min_time     : time;
    constant max_time     : time;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant value_type   : string         := "slv"
    )</font> <font id="function_return">return ()</font>
- await_change <font id="function_arguments">(    signal target         : unsigned;
    constant min_time     : time;
    constant max_time     : time;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant value_type   : string         := "unsigned"
    )</font> <font id="function_return">return ()</font>
- await_change <font id="function_arguments">(    signal target         : signed;
    constant min_time     : time;
    constant max_time     : time;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant value_type   : string         := "signed"
    )</font> <font id="function_return">return ()</font>
- await_change <font id="function_arguments">(    signal target         : integer;
    constant min_time     : time;
    constant max_time     : time;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant value_type   : string         := "integer"
    )</font> <font id="function_return">return ()</font>
- await_change <font id="function_arguments">(    signal target         : real;
    constant min_time     : time;
    constant max_time     : time;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel;
    constant value_type   : string         := "real"
    )</font> <font id="function_return">return ()</font>
- await_value <font id="function_arguments">(    signal target         : boolean;
    constant exp          : boolean;
    constant min_time     : time;
    constant max_time     : time;
    constant alert_level  : t_alert_level;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
**Description**
Await Value procedures
- await_value <font id="function_arguments">(    signal target             : std_logic;
    constant exp              : std_logic;
    constant match_strictness : t_match_strictness;
    constant min_time         : time;
    constant max_time         : time;
    constant alert_level      : t_alert_level;
    constant msg              : string;
    constant scope            : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id           : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel     : t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- await_value <font id="function_arguments">(    signal target         : std_logic;
    constant exp          : std_logic;
    constant min_time     : time;
    constant max_time     : time;
    constant alert_level  : t_alert_level;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- await_value <font id="function_arguments">(    signal target             : in  std_logic_vector;
    constant exp              : in  std_logic_vector;
    constant match_strictness : in  t_match_strictness;
    constant min_time         : in  time;
    constant max_time         : in  time;
    constant alert_level      : in  t_alert_level;
    variable success          : out boolean;
    constant msg              : in  string;
    constant scope            : in  string         := C_TB_SCOPE_DEFAULT;
    constant radix            : in  t_radix        := HEX_BIN_IF_INVALID;
    constant format           : in  t_format_zeros := SKIP_LEADING_0;
    constant msg_id           : in  t_msg_id       := ID_POS_ACK;
    constant msg_id_panel     : in  t_msg_id_panel := shared_msg_id_panel;
    constant caller_name      : in  string         := ""
    )</font> <font id="function_return">return ()</font>
- await_value <font id="function_arguments">(    signal target             : std_logic_vector;
    constant exp              : std_logic_vector;
    constant match_strictness : t_match_strictness;
    constant min_time         : time;
    constant max_time         : time;
    constant alert_level      : t_alert_level;
    constant msg              : string;
    constant scope            : string         := C_TB_SCOPE_DEFAULT;
    constant radix            : t_radix        := HEX_BIN_IF_INVALID;
    constant format           : t_format_zeros := SKIP_LEADING_0;
    constant msg_id           : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel     : t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- await_value <font id="function_arguments">(    signal target         : std_logic_vector;
    constant exp          : std_logic_vector;
    constant min_time     : time;
    constant max_time     : time;
    constant alert_level  : t_alert_level;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant radix        : t_radix        := HEX_BIN_IF_INVALID;
    constant format       : t_format_zeros := SKIP_LEADING_0;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- await_value <font id="function_arguments">(    signal target         : unsigned;
    constant exp          : unsigned;
    constant min_time     : time;
    constant max_time     : time;
    constant alert_level  : t_alert_level;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant radix        : t_radix        := HEX_BIN_IF_INVALID;
    constant format       : t_format_zeros := SKIP_LEADING_0;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- await_value <font id="function_arguments">(    signal target         : signed;
    constant exp          : signed;
    constant min_time     : time;
    constant max_time     : time;
    constant alert_level  : t_alert_level;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant radix        : t_radix        := HEX_BIN_IF_INVALID;
    constant format       : t_format_zeros := SKIP_LEADING_0;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- await_value <font id="function_arguments">(    signal target         : integer;
    constant exp          : integer;
    constant min_time     : time;
    constant max_time     : time;
    constant alert_level  : t_alert_level;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- await_value <font id="function_arguments">(    signal target         : real;
    constant exp          : real;
    constant min_time     : time;
    constant max_time     : time;
    constant alert_level  : t_alert_level;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- await_value <font id="function_arguments">(    signal target         : boolean;
    constant exp          : boolean;
    constant min_time     : time;
    constant max_time     : time;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
**Description**
Await Value Overloads without Mandatory Alert_Level
- await_value <font id="function_arguments">(    signal target             : std_logic;
    constant exp              : std_logic;
    constant match_strictness : t_match_strictness;
    constant min_time         : time;
    constant max_time         : time;
    constant msg              : string;
    constant scope            : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id           : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel     : t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- await_value <font id="function_arguments">(    signal target         : std_logic;
    constant exp          : std_logic;
    constant min_time     : time;
    constant max_time     : time;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- await_value <font id="function_arguments">(    signal target             : std_logic_vector;
    constant exp              : std_logic_vector;
    constant match_strictness : t_match_strictness;
    constant min_time         : time;
    constant max_time         : time;
    constant msg              : string;
    constant scope            : string         := C_TB_SCOPE_DEFAULT;
    constant radix            : t_radix        := HEX_BIN_IF_INVALID;
    constant format           : t_format_zeros := SKIP_LEADING_0;
    constant msg_id           : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel     : t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- await_value <font id="function_arguments">(    signal target         : std_logic_vector;
    constant exp          : std_logic_vector;
    constant min_time     : time;
    constant max_time     : time;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant radix        : t_radix        := HEX_BIN_IF_INVALID;
    constant format       : t_format_zeros := SKIP_LEADING_0;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- await_value <font id="function_arguments">(    signal target         : unsigned;
    constant exp          : unsigned;
    constant min_time     : time;
    constant max_time     : time;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant radix        : t_radix        := HEX_BIN_IF_INVALID;
    constant format       : t_format_zeros := SKIP_LEADING_0;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- await_value <font id="function_arguments">(    signal target         : signed;
    constant exp          : signed;
    constant min_time     : time;
    constant max_time     : time;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant radix        : t_radix        := HEX_BIN_IF_INVALID;
    constant format       : t_format_zeros := SKIP_LEADING_0;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- await_value <font id="function_arguments">(    signal target         : integer;
    constant exp          : integer;
    constant min_time     : time;
    constant max_time     : time;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- await_value <font id="function_arguments">(    signal target         : real;
    constant exp          : real;
    constant min_time     : time;
    constant max_time     : time;
    constant msg          : string;
    constant scope        : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel : t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- await_stable <font id="function_arguments">(    signal target            : boolean;
    constant stable_req      : time;     Minimum stable requirement
    constant stable_req_from : t_from_point_in_time;   Which point in time stable_req starts
    constant timeout         : time;     Timeout if stable_req not achieved
    constant timeout_from    : t_from_point_in_time;   Which point in time the timeout starts
    constant alert_level     : t_alert_level;
    constant msg             : string;
    constant scope           : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id          : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel    : t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
**Description**
Await Stable Procedures
- await_stable <font id="function_arguments">(    signal target            : std_logic;
    constant stable_req      : time;     Minimum stable requirement
    constant stable_req_from : t_from_point_in_time;   Which point in time stable_req starts
    constant timeout         : time;     Timeout if stable_req not achieved
    constant timeout_from    : t_from_point_in_time;   Which point in time the timeout starts
    constant alert_level     : t_alert_level;
    constant msg             : string;
    constant scope           : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id          : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel    : t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- await_stable <font id="function_arguments">(    signal target            : in  std_logic_vector;
    constant stable_req      : in  time;     Minimum stable requirement
    constant stable_req_from : in  t_from_point_in_time;   Which point in time stable_req starts
    constant timeout         : in  time;     Timeout if stable_req not achieved
    constant timeout_from    : in  t_from_point_in_time;   Which point in time the timeout starts
    constant alert_level     : in  t_alert_level;
    variable success         : out boolean;
    constant msg             : in  string;
    constant scope           : in  string         := C_TB_SCOPE_DEFAULT;
    constant msg_id          : in  t_msg_id       := ID_POS_ACK;
    constant msg_id_panel    : in  t_msg_id_panel := shared_msg_id_panel;
    constant caller_name     : in  string         := ""
    )</font> <font id="function_return">return ()</font>
- await_stable <font id="function_arguments">(    signal target            : std_logic_vector;
    constant stable_req      : time;     Minimum stable requirement
    constant stable_req_from : t_from_point_in_time;   Which point in time stable_req starts
    constant timeout         : time;     Timeout if stable_req not achieved
    constant timeout_from    : t_from_point_in_time;   Which point in time the timeout starts
    constant alert_level     : t_alert_level;
    constant msg             : string;
    constant scope           : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id          : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel    : t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- await_stable <font id="function_arguments">(    signal target            : unsigned;
    constant stable_req      : time;     Minimum stable requirement
    constant stable_req_from : t_from_point_in_time;   Which point in time stable_req starts
    constant timeout         : time;     Timeout if stable_req not achieved
    constant timeout_from    : t_from_point_in_time;   Which point in time the timeout starts
    constant alert_level     : t_alert_level;
    constant msg             : string;
    constant scope           : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id          : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel    : t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- await_stable <font id="function_arguments">(    signal target            : signed;
    constant stable_req      : time;     Minimum stable requirement
    constant stable_req_from : t_from_point_in_time;   Which point in time stable_req starts
    constant timeout         : time;     Timeout if stable_req not achieved
    constant timeout_from    : t_from_point_in_time;   Which point in time the timeout starts
    constant alert_level     : t_alert_level;
    constant msg             : string;
    constant scope           : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id          : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel    : t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- await_stable <font id="function_arguments">(    signal target            : integer;
    constant stable_req      : time;     Minimum stable requirement
    constant stable_req_from : t_from_point_in_time;   Which point in time stable_req starts
    constant timeout         : time;     Timeout if stable_req not achieved
    constant timeout_from    : t_from_point_in_time;   Which point in time the timeout starts
    constant alert_level     : t_alert_level;
    constant msg             : string;
    constant scope           : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id          : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel    : t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- await_stable <font id="function_arguments">(    signal target            : real;
    constant stable_req      : time;     Minimum stable requirement
    constant stable_req_from : t_from_point_in_time;   Which point in time stable_req starts
    constant timeout         : time;     Timeout if stable_req not achieved
    constant timeout_from    : t_from_point_in_time;   Which point in time the timeout starts
    constant alert_level     : t_alert_level;
    constant msg             : string;
    constant scope           : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id          : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel    : t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- await_stable <font id="function_arguments">(    signal target            : boolean;
    constant stable_req      : time;     Minimum stable requirement
    constant stable_req_from : t_from_point_in_time;   Which point in time stable_req starts
    constant timeout         : time;     Timeout if stable_req not achieved
    constant timeout_from    : t_from_point_in_time;   Which point in time the timeout starts
    constant msg             : string;
    constant scope           : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id          : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel    : t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
**Description**
Await Stable Procedures without Mandatory Alert_LevelAwait Stable Procedures
- await_stable <font id="function_arguments">(    signal target            : std_logic;
    constant stable_req      : time;     Minimum stable requirement
    constant stable_req_from : t_from_point_in_time;   Which point in time stable_req starts
    constant timeout         : time;     Timeout if stable_req not achieved
    constant timeout_from    : t_from_point_in_time;   Which point in time the timeout starts
    constant msg             : string;
    constant scope           : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id          : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel    : t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- await_stable <font id="function_arguments">(    signal target            : std_logic_vector;
    constant stable_req      : time;     Minimum stable requirement
    constant stable_req_from : t_from_point_in_time;   Which point in time stable_req starts
    constant timeout         : time;     Timeout if stable_req not achieved
    constant timeout_from    : t_from_point_in_time;   Which point in time the timeout starts
    constant msg             : string;
    constant scope           : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id          : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel    : t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- await_stable <font id="function_arguments">(    signal target            : unsigned;
    constant stable_req      : time;     Minimum stable requirement
    constant stable_req_from : t_from_point_in_time;   Which point in time stable_req starts
    constant timeout         : time;     Timeout if stable_req not achieved
    constant timeout_from    : t_from_point_in_time;   Which point in time the timeout starts
    constant msg             : string;
    constant scope           : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id          : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel    : t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- await_stable <font id="function_arguments">(    signal target            : signed;
    constant stable_req      : time;     Minimum stable requirement
    constant stable_req_from : t_from_point_in_time;   Which point in time stable_req starts
    constant timeout         : time;     Timeout if stable_req not achieved
    constant timeout_from    : t_from_point_in_time;   Which point in time the timeout starts
    constant msg             : string;
    constant scope           : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id          : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel    : t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- await_stable <font id="function_arguments">(    signal target            : integer;
    constant stable_req      : time;     Minimum stable requirement
    constant stable_req_from : t_from_point_in_time;   Which point in time stable_req starts
    constant timeout         : time;     Timeout if stable_req not achieved
    constant timeout_from    : t_from_point_in_time;   Which point in time the timeout starts
    constant msg             : string;
    constant scope           : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id          : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel    : t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- await_stable <font id="function_arguments">(    signal target            : real;
    constant stable_req      : time;     Minimum stable requirement
    constant stable_req_from : t_from_point_in_time;   Which point in time stable_req starts
    constant timeout         : time;     Timeout if stable_req not achieved
    constant timeout_from    : t_from_point_in_time;   Which point in time the timeout starts
    constant msg             : string;
    constant scope           : string         := C_TB_SCOPE_DEFAULT;
    constant msg_id          : t_msg_id       := ID_POS_ACK;
    constant msg_id_panel    : t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- gen_pulse <font id="function_arguments">(    signal target           : inout std_logic;
    constant pulse_value    :       std_logic;
    constant pulse_duration :       time;
    constant blocking_mode  :       t_blocking_mode;
    constant msg            :       string;
    constant scope          :       string         := C_TB_SCOPE_DEFAULT;
    constant msg_id         :       t_msg_id       := ID_GEN_PULSE;
    constant msg_id_panel   :       t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- gen_pulse <font id="function_arguments">(    signal target           : inout std_logic;
    constant pulse_duration :       time;
    constant blocking_mode  :       t_blocking_mode;
    constant msg            :       string;
    constant scope          :       string         := C_TB_SCOPE_DEFAULT;
    constant msg_id         :       t_msg_id       := ID_GEN_PULSE;
    constant msg_id_panel   :       t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- gen_pulse <font id="function_arguments">(    signal target           : inout std_logic;
    constant pulse_value    :       std_logic;
    constant pulse_duration :       time;
    constant msg            :       string;
    constant scope          :       string         := C_TB_SCOPE_DEFAULT;
    constant msg_id         :       t_msg_id       := ID_GEN_PULSE;
    constant msg_id_panel   :       t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- gen_pulse <font id="function_arguments">(    signal target           : inout std_logic;
    constant pulse_duration :       time;
    constant msg            :       string;
    constant scope          :       string         := C_TB_SCOPE_DEFAULT;
    constant msg_id         :       t_msg_id       := ID_GEN_PULSE;
    constant msg_id_panel   :       t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- gen_pulse <font id="function_arguments">(    signal target         : inout std_logic;
    constant pulse_value  :       std_logic;
    signal clock_signal   :       std_logic;
    constant num_periods  :       natural;
    constant msg          :       string;
    constant scope        :       string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       :       t_msg_id       := ID_GEN_PULSE;
    constant msg_id_panel :       t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- gen_pulse <font id="function_arguments">(    signal target         : inout std_logic;
    signal clock_signal   :       std_logic;
    constant num_periods  :       natural;
    constant msg          :       string;
    constant scope        :       string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       :       t_msg_id       := ID_GEN_PULSE;
    constant msg_id_panel :       t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- gen_pulse <font id="function_arguments">(    signal target           : inout boolean;
    constant pulse_value    :       boolean;
    constant pulse_duration :       time;
    constant blocking_mode  :       t_blocking_mode;
    constant msg            :       string;
    constant scope          :       string         := C_TB_SCOPE_DEFAULT;
    constant msg_id         :       t_msg_id       := ID_GEN_PULSE;
    constant msg_id_panel   :       t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- gen_pulse <font id="function_arguments">(    signal target           : inout boolean;
    constant pulse_duration :       time;
    constant blocking_mode  :       t_blocking_mode;
    constant msg            :       string;
    constant scope          :       string         := C_TB_SCOPE_DEFAULT;
    constant msg_id         :       t_msg_id       := ID_GEN_PULSE;
    constant msg_id_panel   :       t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- gen_pulse <font id="function_arguments">(    signal target           : inout boolean;
    constant pulse_value    :       boolean;
    constant pulse_duration :       time;
    constant msg            :       string;
    constant scope          :       string         := C_TB_SCOPE_DEFAULT;
    constant msg_id         :       t_msg_id       := ID_GEN_PULSE;
    constant msg_id_panel   :       t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- gen_pulse <font id="function_arguments">(    signal target           : inout boolean;
    constant pulse_duration :       time;
    constant msg            :       string;
    constant scope          :       string         := C_TB_SCOPE_DEFAULT;
    constant msg_id         :       t_msg_id       := ID_GEN_PULSE;
    constant msg_id_panel   :       t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- gen_pulse <font id="function_arguments">(    signal target         : inout boolean;
    constant pulse_value  :       boolean;
    signal clock_signal   :       std_logic;
    constant num_periods  :       natural;
    constant msg          :       string;
    constant scope        :       string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       :       t_msg_id       := ID_GEN_PULSE;
    constant msg_id_panel :       t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- gen_pulse <font id="function_arguments">(    signal target         : inout boolean;
    signal clock_signal   :       std_logic;
    constant num_periods  :       natural;
    constant msg          :       string;
    constant scope        :       string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       :       t_msg_id       := ID_GEN_PULSE;
    constant msg_id_panel :       t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- gen_pulse <font id="function_arguments">(    signal target           : inout std_logic_vector;
    constant pulse_value    :       std_logic_vector;
    constant pulse_duration :       time;
    constant blocking_mode  :       t_blocking_mode;
    constant msg            :       string;
    constant scope          :       string         := C_TB_SCOPE_DEFAULT;
    constant msg_id         :       t_msg_id       := ID_GEN_PULSE;
    constant msg_id_panel   :       t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- gen_pulse <font id="function_arguments">(    signal target           : inout std_logic_vector;
    constant pulse_duration :       time;
    constant blocking_mode  :       t_blocking_mode;
    constant msg            :       string;
    constant scope          :       string         := C_TB_SCOPE_DEFAULT;
    constant msg_id         :       t_msg_id       := ID_GEN_PULSE;
    constant msg_id_panel   :       t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- gen_pulse <font id="function_arguments">(    signal target           : inout std_logic_vector;
    constant pulse_value    :       std_logic_vector;
    constant pulse_duration :       time;
    constant msg            :       string;
    constant scope          :       string         := C_TB_SCOPE_DEFAULT;
    constant msg_id         :       t_msg_id       := ID_GEN_PULSE;
    constant msg_id_panel   :       t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- gen_pulse <font id="function_arguments">(    signal target           : inout std_logic_vector;
    constant pulse_duration :       time;
    constant msg            :       string;
    constant scope          :       string         := C_TB_SCOPE_DEFAULT;
    constant msg_id         :       t_msg_id       := ID_GEN_PULSE;
    constant msg_id_panel   :       t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- gen_pulse <font id="function_arguments">(    signal target         : inout std_logic_vector;
    constant pulse_value  :       std_logic_vector;
    signal clock_signal   :       std_logic;
    constant num_periods  :       natural;
    constant msg          :       string;
    constant scope        :       string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       :       t_msg_id       := ID_GEN_PULSE;
    constant msg_id_panel :       t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- gen_pulse <font id="function_arguments">(    signal target         : inout std_logic_vector;
    signal clock_signal   :       std_logic;
    constant num_periods  :       natural;
    constant msg          :       string;
    constant scope        :       string         := C_TB_SCOPE_DEFAULT;
    constant msg_id       :       t_msg_id       := ID_GEN_PULSE;
    constant msg_id_panel :       t_msg_id_panel := shared_msg_id_panel
    )</font> <font id="function_return">return ()</font>
- clock_generator <font id="function_arguments">(    signal clock_signal            : inout std_logic;
    constant clock_period          : in    time;
    constant clock_high_percentage : in    natural range 1 to 99 := 50
    )</font> <font id="function_return">return ()</font>
- clock_generator <font id="function_arguments">(    signal clock_signal      : inout std_logic;
    constant clock_period    : in    time;
    constant clock_high_time : in    time
    )</font> <font id="function_return">return ()</font>
**Description**
Overloaded version with duty cycle in time
- clock_generator <font id="function_arguments">(    signal clock_signal            : inout std_logic;
    signal clock_count             : inout natural;
    constant clock_period          : in    time;
    constant clock_high_percentage : in    natural range 1 to 99 := 50
    )</font> <font id="function_return">return ()</font>
**Description**
Overloaded version with clock count
- clock_generator <font id="function_arguments">(    signal clock_signal      : inout std_logic;
    signal clock_count       : inout natural;
    constant clock_period    : in    time;
    constant clock_high_time : in    time
    )</font> <font id="function_return">return ()</font>
**Description**
Overloaded version with clock count and duty cycle in time
- clock_generator <font id="function_arguments">(    signal clock_signal            : inout std_logic;
    signal clock_ena               : in    boolean;
    constant clock_period          : in    time;
    constant clock_name            : in    string;
    constant clock_high_percentage : in    natural range 1 to 99 := 50
    )</font> <font id="function_return">return ()</font>
**Description**
Overloaded version with clock enable and clock name
- clock_generator <font id="function_arguments">(    signal clock_signal      : inout std_logic;
    signal clock_ena         : in    boolean;
    constant clock_period    : in    time;
    constant clock_name      : in    string;
    constant clock_high_time : in    time
    )</font> <font id="function_return">return ()</font>
**Description**
Overloaded version with clock enable, clock nameand duty cycle in time.
- clock_generator <font id="function_arguments">(    signal clock_signal            : inout std_logic;
    signal clock_ena               : in    boolean;
    signal clock_count             : out   natural;
    constant clock_period          : in    time;
    constant clock_name            : in    string;
    constant clock_high_percentage : in    natural range 1 to 99 := 50
    )</font> <font id="function_return">return ()</font>
**Description**
Overloaded version with clock enable, clock nameand clock count
- clock_generator <font id="function_arguments">(    signal clock_signal      : inout std_logic;
    signal clock_ena         : in    boolean;
    signal clock_count       : out   natural;
    constant clock_period    : in    time;
    constant clock_name      : in    string;
    constant clock_high_time : in    time
    )</font> <font id="function_return">return ()</font>
**Description**
Overloaded version with clock enable, clock name,clock count and duty cycle in time.
- adjustable_clock_generator <font id="function_arguments">(    signal clock_signal          : inout std_logic;
    signal clock_ena             : in    boolean;
    constant clock_period        : in    time;
    signal clock_high_percentage : in    natural range 0 to 100
    )</font> <font id="function_return">return ()</font>
- adjustable_clock_generator <font id="function_arguments">(    signal clock_signal          : inout std_logic;
    signal clock_ena             : in    boolean;
    constant clock_period        : in    time;
    constant clock_name          : in    string;
    signal clock_high_percentage : in    natural range 0 to 100
    )</font> <font id="function_return">return ()</font>
- adjustable_clock_generator <font id="function_arguments">(    signal clock_signal          : inout std_logic;
    signal clock_ena             : in    boolean;
    signal clock_count           : out   natural;
    constant clock_period        : in    time;
    constant clock_name          : in    string;
    signal clock_high_percentage : in    natural range 0 to 100
    )</font> <font id="function_return">return ()</font>
**Description**
Overloaded version with clock enable, clock nameand clock count
- deallocate_line_if_exists <font id="function_arguments">(    variable line_to_be_deallocated : inout line
    )</font> <font id="function_return">return ()</font>
- block_flag <font id="function_arguments">(    constant flag_name                : in string;
    constant msg                      : in string;
    constant already_blocked_severity : in t_alert_level := warning;
    constant scope                    : in string        := C_TB_SCOPE_DEFAULT
    )</font> <font id="function_return">return ()</font>
**Description**
============================================================================Synchronization methods============================================================================method to block a global flag with the name flag_name
- unblock_flag <font id="function_arguments">(    constant flag_name : in    string;
    constant msg       : in    string;
    signal trigger     : inout std_logic;   Parameter must be global_trigger as method await_unblock_flag() uses that global signal to detect unblocking.
    constant scope     : in    string := C_TB_SCOPE_DEFAULT
    )</font> <font id="function_return">return ()</font>
**Description**
method to unblock a global flag with the name flag_name
- await_unblock_flag <font id="function_arguments">(    constant flag_name        : in string;
    constant timeout          : in time;
    constant msg              : in string;
    constant flag_returning   : in t_flag_returning := KEEP_UNBLOCKED;
    constant timeout_severity : in t_alert_level    := error;
    constant scope            : in string           := C_TB_SCOPE_DEFAULT
    )</font> <font id="function_return">return ()</font>
**Description**
method to wait for the global flag with the name flag_name
- await_barrier <font id="function_arguments">(    signal barrier_signal     : inout std_logic;
    constant timeout          : in    time;
    constant msg              : in    string;
    constant timeout_severity : in    t_alert_level := error;
    constant scope            : in    string        := C_TB_SCOPE_DEFAULT
    )</font> <font id="function_return">return ()</font>
- await_semaphore_in_delta_cycles <font id="function_arguments">(    variable semaphore : inout t_protected_semaphore
    )</font> <font id="function_return">return ()</font>
**Description**
tries to lock the semaphore for C_NUM_SEMAPHORE_LOCK_TRIES in adaptations_pkg
- release_semaphore <font id="function_arguments">(    variable semaphore : inout t_protected_semaphore
    )</font> <font id="function_return">return ()</font>
**Description**
releases the semaphore
- watchdog_timer <font id="function_arguments">(    signal watchdog_ctrl : in t_watchdog_ctrl;
    constant timeout     :    time;
    constant alert_level :    t_alert_level := error;
    constant msg         :    string        := ""
    )</font> <font id="function_return">return ()</font>
**Description**
============================================================================Watchdog-related============================================================================
- extend_watchdog <font id="function_arguments">(    signal watchdog_ctrl : inout t_watchdog_ctrl;
    constant time_extend :       time := 0 ns
    )</font> <font id="function_return">return ()</font>
- reinitialize_watchdog <font id="function_arguments">(    signal watchdog_ctrl : inout t_watchdog_ctrl;
    constant timeout     :       time
    )</font> <font id="function_return">return ()</font>
- terminate_watchdog <font id="function_arguments">(    signal watchdog_ctrl : inout t_watchdog_ctrl
    )</font> <font id="function_return">return ()</font>
