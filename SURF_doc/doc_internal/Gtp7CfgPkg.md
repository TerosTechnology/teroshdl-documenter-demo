# Package: Gtp7CfgPkg

- **File**: Gtp7CfgPkg.vhd
## Constants

| Name                     | Type         | Value                                                                                                                                                            | Description |
| ------------------------ | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| QPLL_REFCLK_DIV_VALIDS_C | IntegerArray |  (1,<br><span style="padding-left:20px"> 2)                                                                                                                      |             |
| QPLL_FBDIV_VALIDS_C      | IntegerArray |  (1,<br><span style="padding-left:20px"> 2,<br><span style="padding-left:20px"> 3,<br><span style="padding-left:20px"> 4,<br><span style="padding-left:20px"> 5) |             |
| QPLL_FBDIV_45_VALIDS_C   | IntegerArray |  (4,<br><span style="padding-left:20px"> 5)                                                                                                                      |             |
| QPLL_OUT_DIV_VALIDS_C    | IntegerArray |  (1,<br><span style="padding-left:20px"> 2,<br><span style="padding-left:20px"> 4,<br><span style="padding-left:20px"> 8)                                        |             |
| QPLL_LOW_C               | real         |  1.6E9                                                                                                                                                           |             |
| QPLL_HIGH_C              | real         |  3.3E9                                                                                                                                                           |             |
## Types

| Name            | Type | Description |
| --------------- | ---- | ----------- |
| Gtp7QPllCfgType |      |             |
## Functions
- getGtp7QPllCfg <font id="function_arguments">(refClkFreq : real;<br><span style="padding-left:20px"> lineRate : real) </font> <font id="function_return">return Gtp7QPllCfgType </font>
- ite <font id="function_arguments">(i : boolean;<br><span style="padding-left:20px"> t : Gtp7QPllCfgType;<br><span style="padding-left:20px"> e : Gtp7QPllCfgType) </font> <font id="function_return">return Gtp7QPllCfgType </font>
