# Package: rgmii_bfm_pkg

- **File**: rgmii_bfm_pkg.vhd
## Description

================================================================================================================================
================================================================================================================================

## Constants

| Name                       | Type               | Value                                                                                                                                                                                                                                                                                                                                                                                                                                   | Description                                   |
| -------------------------- | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| C_SCOPE                    | string             |  "RGMII BFM"                                                                                                                                                                                                                                                                                                                                                                                                                            |                                               |
| C_RGMII_BFM_CONFIG_DEFAULT | t_rgmii_bfm_config |  (     max_wait_cycles          => 10,<br><span style="padding-left:20px">     max_wait_cycles_severity => ERROR,<br><span style="padding-left:20px">     clock_period             => -1 ns,<br><span style="padding-left:20px">     rx_clock_skew            => -1 ns,<br><span style="padding-left:20px">     match_strictness         => MATCH_EXACT,<br><span style="padding-left:20px">     id_for_bfm               => ID_BFM   ) |  Define the default value for the BFM config  |
## Types

| Name               | Type | Description                                                |
| ------------------ | ---- | ---------------------------------------------------------- |
| t_rgmii_tx_if      |      |  Interface record for BFM signals to DUT                   |
| t_rgmii_rx_if      |      |  Interface record for BFM signals from DUT                 |
| t_rgmii_bfm_config |      |  Configuration record to be assigned in the test harness.  |
## Functions
- init_rgmii_if_signals <font id="function_arguments">()</font> <font id="function_return">return t_rgmii_tx_if </font>
</br>**Description**
==========================================================================================
 BFM procedures 
==========================================================================================
 This function returns an RGMII interface with initialized signals.
 All input signals are initialized to 0
 All output signals are initialized to Z

- init_rgmii_if_signals <font id="function_arguments">()</font> <font id="function_return">return t_rgmii_rx_if </font>
- rgmii_write <font id="function_arguments">( constant data_array   : in    t_byte_array;<br><span style="padding-left:20px"> constant msg          : in    string             := "";<br><span style="padding-left:20px"> signal   rgmii_tx_if  : inout t_rgmii_tx_if;<br><span style="padding-left:20px"> constant scope        : in    string             := C_SCOPE;<br><span style="padding-left:20px"> constant msg_id_panel : in    t_msg_id_panel     := shared_msg_id_panel;<br><span style="padding-left:20px"> constant config       : in    t_rgmii_bfm_config := C_RGMII_BFM_CONFIG_DEFAULT ) </font> <font id="function_return">return ()</font>
</br>**Description**
-------------------------------------------------------------------------------------------
 RGMII Write
 BFM -> DUT
-------------------------------------------------------------------------------------------

- rgmii_read <font id="function_arguments">( variable data_array    : out   t_byte_array;<br><span style="padding-left:20px"> variable data_len      : out   natural;<br><span style="padding-left:20px"> constant msg           : in    string             := "";<br><span style="padding-left:20px"> signal   rgmii_rx_if   : inout t_rgmii_rx_if;<br><span style="padding-left:20px"> constant scope         : in    string             := C_SCOPE;<br><span style="padding-left:20px"> constant msg_id_panel  : in    t_msg_id_panel     := shared_msg_id_panel;<br><span style="padding-left:20px"> constant config        : in    t_rgmii_bfm_config := C_RGMII_BFM_CONFIG_DEFAULT;<br><span style="padding-left:20px"> constant ext_proc_call : in    string := ""  -- External proc_call. Overwrite if called from another BFM procedure ) </font> <font id="function_return">return ()</font>
</br>**Description**
-------------------------------------------------------------------------------------------
 RGMII Read
 DUT -> BFM
-------------------------------------------------------------------------------------------

- rgmii_expect <font id="function_arguments">( constant data_exp     : in    t_byte_array;<br><span style="padding-left:20px"> constant msg          : in    string             := "";<br><span style="padding-left:20px"> signal   rgmii_rx_if  : inout t_rgmii_rx_if;<br><span style="padding-left:20px"> constant alert_level  : in    t_alert_level      := ERROR;<br><span style="padding-left:20px"> constant scope        : in    string             := C_SCOPE;<br><span style="padding-left:20px"> constant msg_id_panel : in    t_msg_id_panel     := shared_msg_id_panel;<br><span style="padding-left:20px"> constant config       : in    t_rgmii_bfm_config := C_RGMII_BFM_CONFIG_DEFAULT ) </font> <font id="function_return">return ()</font>
</br>**Description**
-------------------------------------------------------------------------------------------
 RGMII Expect
-------------------------------------------------------------------------------------------

