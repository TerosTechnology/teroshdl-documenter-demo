# Package: gmii_bfm_pkg

- **File**: gmii_bfm_pkg.vhd
## Description

================================================================================================================================
================================================================================================================================

## Constants

| Name                      | Type              | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Description                                   |
| ------------------------- | ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| C_SCOPE                   | string            |  "GMII BFM"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                               |
| C_GMII_BFM_CONFIG_DEFAULT | t_gmii_bfm_config |  (     max_wait_cycles          => 12,<br><span style="padding-left:20px"> -- Standard minimum interpacket gap (Gigabith Ethernet)     max_wait_cycles_severity => ERROR,<br><span style="padding-left:20px">     clock_period             => -1 ns,<br><span style="padding-left:20px">     clock_period_margin      => 0 ns,<br><span style="padding-left:20px">     clock_margin_severity    => TB_ERROR,<br><span style="padding-left:20px">     setup_time               => -1 ns,<br><span style="padding-left:20px">     hold_time                => -1 ns,<br><span style="padding-left:20px">     bfm_sync                 => SYNC_ON_CLOCK_ONLY,<br><span style="padding-left:20px">     match_strictness         => MATCH_EXACT,<br><span style="padding-left:20px">     id_for_bfm               => ID_BFM   ) |  Define the default value for the BFM config  |
## Types

| Name              | Type | Description                                                |
| ----------------- | ---- | ---------------------------------------------------------- |
| t_gmii_tx_if      |      |  Interface record for BFM signals to DUT                   |
| t_gmii_rx_if      |      |  Interface record for BFM signals from DUT                 |
| t_gmii_bfm_config |      |  Configuration record to be assigned in the test harness.  |
## Functions
- init_gmii_if_signals <font id="function_arguments">()</font> <font id="function_return">return t_gmii_tx_if </font>
**Description**
==========================================================================================
 BFM procedures 
==========================================================================================
 This function returns a GMII interface with initialized signals.
 All input signals are initialized to 0
 All output signals are initialized to Z

- init_gmii_if_signals <font id="function_arguments">()</font> <font id="function_return">return t_gmii_rx_if </font>
- gmii_write <font id="function_arguments">( constant data_array   : in    t_slv_array;<br><span style="padding-left:20px"> constant msg          : in    string            := "";<br><span style="padding-left:20px"> signal   gmii_tx_if   : inout t_gmii_tx_if;<br><span style="padding-left:20px"> constant scope        : in    string            := C_SCOPE;<br><span style="padding-left:20px"> constant msg_id_panel : in    t_msg_id_panel    := shared_msg_id_panel;<br><span style="padding-left:20px"> constant config       : in    t_gmii_bfm_config := C_GMII_BFM_CONFIG_DEFAULT ) </font> <font id="function_return">return ()</font>
**Description**
-------------------------------------------------------------------------------------------
 GMII Write
 BFM -> DUT
-------------------------------------------------------------------------------------------

- gmii_read <font id="function_arguments">( variable data_array    : out   t_slv_array;<br><span style="padding-left:20px"> variable data_len      : out   natural;<br><span style="padding-left:20px"> constant msg           : in    string            := "";<br><span style="padding-left:20px"> signal   gmii_rx_if    : inout t_gmii_rx_if;<br><span style="padding-left:20px"> constant scope         : in    string            := C_SCOPE;<br><span style="padding-left:20px"> constant msg_id_panel  : in    t_msg_id_panel    := shared_msg_id_panel;<br><span style="padding-left:20px"> constant config        : in    t_gmii_bfm_config := C_GMII_BFM_CONFIG_DEFAULT;<br><span style="padding-left:20px"> constant ext_proc_call : in    string := ""  -- External proc_call. Overwrite if called from another BFM procedure ) </font> <font id="function_return">return ()</font>
**Description**
-------------------------------------------------------------------------------------------
 GMII Read
 DUT -> BFM
-------------------------------------------------------------------------------------------

- gmii_expect <font id="function_arguments">( constant data_exp     : in    t_slv_array;<br><span style="padding-left:20px"> constant msg          : in    string            := "";<br><span style="padding-left:20px"> signal   gmii_rx_if   : inout t_gmii_rx_if;<br><span style="padding-left:20px"> constant alert_level  : in    t_alert_level     := ERROR;<br><span style="padding-left:20px"> constant scope        : in    string            := C_SCOPE;<br><span style="padding-left:20px"> constant msg_id_panel : in    t_msg_id_panel    := shared_msg_id_panel;<br><span style="padding-left:20px"> constant config       : in    t_gmii_bfm_config := C_GMII_BFM_CONFIG_DEFAULT ) </font> <font id="function_return">return ()</font>
**Description**
-------------------------------------------------------------------------------------------
 GMII Expect
-------------------------------------------------------------------------------------------

