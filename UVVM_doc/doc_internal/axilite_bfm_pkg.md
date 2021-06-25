# Package: axilite_bfm_pkg
## Constants
| Name                         | Type                 | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Description |
| ---------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| C_SCOPE                      | string               |  "AXILITE_BFM"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |             |
| C_AXILITE_BFM_CONFIG_DEFAULT | t_axilite_bfm_config |  (     max_wait_cycles             => 10,     max_wait_cycles_severity    => TB_FAILURE,     clock_period                => -1 ns,     clock_period_margin         => 0 ns,     clock_margin_severity       => TB_ERROR,     setup_time                  => -1 ns,     hold_time                   => -1 ns,     bfm_sync                    => SYNC_ON_CLOCK_ONLY,     match_strictness            => MATCH_EXACT,     expected_response           => OKAY,     expected_response_severity  => TB_FAILURE,     protection_setting          => UNPRIVILEGED_NONSECURE_DATA,     num_aw_pipe_stages          => 1,     num_w_pipe_stages           => 1,     num_ar_pipe_stages          => 1,     num_r_pipe_stages           => 1,     num_b_pipe_stages           => 1,     id_for_bfm                  => ID_BFM,     id_for_bfm_wait             => ID_BFM_WAIT,     id_for_bfm_poll             => ID_BFM_POLL     ) |             |
## Types
| Name                             | Type                                                                                                                                                                                                                                                                                 | Description                                              |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------- |
| t_xresp                          | (     OKAY,      SLVERR,      DECERR,      EXOKAY   )                                                                                                                                                                                                                                | EXOKAY not supported for AXI-Lite, will raise TB_FAILURE |
| t_axprot                         | (     UNPRIVILEGED_NONSECURE_DATA,     UNPRIVILEGED_NONSECURE_INSTRUCTION,     UNPRIVILEGED_SECURE_DATA,     UNPRIVILEGED_SECURE_INSTRUCTION,     PRIVILEGED_NONSECURE_DATA,     PRIVILEGED_NONSECURE_INSTRUCTION,     PRIVILEGED_SECURE_DATA,     PRIVILEGED_SECURE_INSTRUCTION   ) |                                                          |
| t_axilite_bfm_config             |                                                                                                                                                                                                                                                                                      | Configuration record to be assigned in the test harness. |
| t_axilite_write_address_channel  |                                                                                                                                                                                                                                                                                      | AXI-Lite Interface signals                               |
| t_axilite_write_data_channel     |                                                                                                                                                                                                                                                                                      |                                                          |
| t_axilite_write_response_channel |                                                                                                                                                                                                                                                                                      |                                                          |
| t_axilite_read_address_channel   |                                                                                                                                                                                                                                                                                      |                                                          |
| t_axilite_read_data_channel      |                                                                                                                                                                                                                                                                                      |                                                          |
| t_axilite_if                     |                                                                                                                                                                                                                                                                                      |                                                          |
## Functions
- init_axilite_if_signals <font id="function_arguments">(    addr_width : natural;
    data_width : natural
    )</font> <font id="function_return">return t_axilite_if</font>
**Description**
- This function returns an AXILITE interface with initialized signals.- All AXILITE input signals are initialized to 0- All AXILITE output signals are initialized to Z- awprot and arprot are initialized to UNPRIVILEGED_NONSECURE_DATA
- axilite_write <font id="function_arguments">(    constant addr_value         : in    unsigned;
    constant data_value         : in    std_logic_vector;
    constant msg                : in    string;
    signal   clk                : in    std_logic;
    signal   axilite_if         : inout t_axilite_if;
    constant scope              : in    string                := C_SCOPE;
    constant msg_id_panel       : in    t_msg_id_panel        := shared_msg_id_panel;
    constant config             : in    t_axilite_bfm_config  := C_AXILITE_BFM_CONFIG_DEFAULT
    )</font> <font id="function_return">return ()</font>
**Description**
This procedure writes data to the AXILITE interface specified in axilite_if- The protection setting is set to UNPRIVILEGED_NONSECURE_DATA in this procedure- The byte enable input is set to 1 for all bytes in this procedure- When the write is completed, a log message is issued with log ID id_for_bfm
- axilite_write <font id="function_arguments">(    constant addr_value         : in    unsigned;
    constant data_value         : in    std_logic_vector;
    constant byte_enable        : in    std_logic_vector;
    constant msg                : in    string;
    signal   clk                : in    std_logic;
    signal   axilite_if         : inout t_axilite_if;
    constant scope              : in    string                := C_SCOPE;
    constant msg_id_panel       : in    t_msg_id_panel        := shared_msg_id_panel;
    constant config             : in    t_axilite_bfm_config  := C_AXILITE_BFM_CONFIG_DEFAULT
    )</font> <font id="function_return">return ()</font>
**Description**
This procedure writes data to the AXILITE interface specified in axilite_if- When the write is completed, a log message is issued with log ID id_for_bfm
- axilite_read <font id="function_arguments">(    constant addr_value     : in  unsigned;
    variable data_value     : out std_logic_vector;
    constant msg            : in  string;
    signal   clk            : in std_logic;
    signal   axilite_if     : inout t_axilite_if;
    constant scope          : in  string                := C_SCOPE;
    constant msg_id_panel   : in  t_msg_id_panel        := shared_msg_id_panel;
    constant config         : in  t_axilite_bfm_config := C_AXILITE_BFM_CONFIG_DEFAULT;
    constant ext_proc_call  : in  string                    := ""   External proc_call. Overwrite if called from another BFM procedure
    )</font> <font id="function_return">return ()</font>
**Description**
This procedure reads data from the AXILITE interface specified in axilite_if,and returns the read data in data_value.
- axilite_check <font id="function_arguments">(    constant addr_value         : in  unsigned;
    constant data_exp           : in  std_logic_vector;
    constant msg                : in  string;
    signal   clk                : in std_logic;
    signal   axilite_if         : inout t_axilite_if;
    constant alert_level        : in  t_alert_level         := error;
    constant scope              : in  string                := C_SCOPE;
    constant msg_id_panel       : in  t_msg_id_panel        := shared_msg_id_panel;
    constant config             : in  t_axilite_bfm_config  := C_AXILITE_BFM_CONFIG_DEFAULT
    )</font> <font id="function_return">return ()</font>
**Description**
This procedure reads data from the AXILITE interface specified in axilite_if,and compares it to the data in data_exp.- If the received data inconsistent with data_exp, an alert with severity  alert_level is issued.- If the received data was correct, a log message with ID id_for_bfm is issued.
- axprot_to_slv <font id="function_arguments">(    axprot : t_axprot
  )</font> <font id="function_return">return std_logic_vector</font>
- xresp_to_slv <font id="function_arguments">(    constant axilite_response_status : in  t_xresp;
    constant scope                   : in  string           := C_SCOPE;
    constant msg_id_panel            : in  t_msg_id_panel   := shared_msg_id_panel
  )</font> <font id="function_return">return std_logic_vector</font>
