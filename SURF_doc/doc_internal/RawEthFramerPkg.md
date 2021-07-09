# Package: RawEthFramerPkg

## Constants

| Name                  | Type                | Value                                                                                                                                                                                                          | Description                                                                                     |
| --------------------- | ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| ETH_BCF_C             | integer             |  2                                                                                                                                                                                                             |                                                                                                 |
| RAW_ETH_CONFIG_INIT_C | AxiStreamConfigType |  ssiAxiStreamConfig(8,<br><span style="padding-left:20px"> TKEEP_COMP_C,<br><span style="padding-left:20px"> TUSER_FIRST_LAST_C,<br><span style="padding-left:20px"> 8,<br><span style="padding-left:20px"> 3) | dataBytes = 8tKeepMode = TKEEP_COMP_C;tUserMode = TUSER_FIRST_LAST_C;tDestBits = 8tUserBits = 3 |
## Functions
- ssiGetUserBcf <font id="function_arguments">( axisConfig : AxiStreamConfigType;<br><span style="padding-left:20px"> axisMaster : AxiStreamMasterType) </font> <font id="function_return">return sl </font>
- ssiSetUserBcf <font id="function_arguments">( axisConfig : in    AxiStreamConfigType;<br><span style="padding-left:20px"> axisMaster : inout AxiStreamMasterType;<br><span style="padding-left:20px"> bcf        : in    sl) </font> <font id="function_return">return ()</font>
