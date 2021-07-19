# Package: proj_package

- **File**: proj_package.sv
## Description

MICRON TECHNOLOGY, INC. - CONFIDENTIAL AND PROPRIETARY INFORMATION
 

## Constants

| Name      | Type | Value | Description |
| --------- | ---- | ----- | ----------- |
| DEF_CCD_L |      | 6     |             |
## Functions
- project_dut_config <font id="function_arguments">(inout UTYPE_dutconfig dut_config)</font> <font id="function_return">return (void)</font>
- GetCWLSpeedRange <font id="function_arguments">(input UTYPE_DutModeConfig dut_mode_config,<br><span style="padding-left:20px">)</font> <font id="function_return">return (void)</font>
- GetCLSpeedRange <font id="function_arguments">(input UTYPE_DutModeConfig dut_mode_config,<br><span style="padding-left:20px"> output UTYPE_TS slowest,<br><span style="padding-left:20px"> output UTYPE_TS fastest,<br><span style="padding-left:20px"> output UTYPE_TS)</font> <font id="function_return">return (void)</font>
- GetCLSpeedRange3DS <font id="function_arguments">(input UTYPE_DutModeConfig dut_mode_config,<br><span style="padding-left:20px"> output UTYPE_TS slowest,<br><span style="padding-left:20px"> output UTYPE_TS fastest,<br><span style="padding-left:20px"> output UTYPE_TS)</font> <font id="function_return">return (void)</font>
- GettCCD_LSpeed <font id="function_arguments">(input UTYPE_DutModeConfig dut_mode_config,<br><span style="padding-left:20px"> input UTYPE_TS)</font> <font id="function_return">return (int)</font>
- GetMintWR <font id="function_arguments">(input UTYPE_DutModeConfig dut_mode_config,<br><span style="padding-left:20px"> int tWRc,<br><span style="padding-left:20px"> int)</font> <font id="function_return">return (int)</font>
- GettWR_CRC_DMSpeed <font id="function_arguments">(input UTYPE_DutModeConfig dut_mode_config,<br><span style="padding-left:20px"> input UTYPE_TS)</font> <font id="function_return">return (UTYPE_delay_write_crc_dm)</font>
- GetCWLSpeedRange_locked <font id="function_arguments">(input UTYPE_DutModeConfig dut_mode_)</font> <font id="function_return">return (void)</font>
- GettCCD_LSpeed_locked <font id="function_arguments">(input UTYPE_DutModeConfig dut_mode_config,<br><span style="padding-left:20px"> input UTYPE_TS ts,<br><span style="padding-left:20px"> input int)</font> <font id="function_return">return (int)</font>
- ppr_available <font id="function_arguments">(input UTYPE_dutconfig dut_config)</font> <font id="function_return">return (bit)</font>
- sppr_available <font id="function_arguments">(input UTYPE_dutconfig dut_config)</font> <font id="function_return">return (bit)</font>
