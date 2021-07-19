# Package: OsvvmGlobalPkg

- **File**: OsvvmGlobalPkg.vhd
## Constants

| Name                            | Type             | Value            | Description                |
| ------------------------------- | ---------------- | ---------------- | -------------------------- |
| OSVVM_DEFAULT_ALERT_PREFIX      | string           |  "%% Alert"      | Defaults for String values |
| OSVVM_DEFAULT_LOG_PREFIX        | string           |  "%% Log  "      |                            |
| OSVVM_DEFAULT_WRITE_PREFIX      | string           |  "%% "           |                            |
| OSVVM_DEFAULT_DONE_NAME         | string           |  "DONE"          |                            |
| OSVVM_DEFAULT_PASS_NAME         | string           |  "PASSED"        |                            |
| OSVVM_DEFAULT_FAIL_NAME         | string           |  "FAILED"        |                            |
| OSVVM_STRING_INIT_PARM_DETECT   | string           |  NUL & NUL & NUL |                            |
| OSVVM_STRING_USE_DEFAULT        | string           |  NUL & ""        |                            |
| OSVVM_DEFAULT_WRITE_PASS_FAIL   | OsvvmOptionsType |  FALSE           | Coverage Settings          |
| OSVVM_DEFAULT_WRITE_BIN_INFO    | OsvvmOptionsType |  TRUE            |                            |
| OSVVM_DEFAULT_WRITE_COUNT       | OsvvmOptionsType |  TRUE            |                            |
| OSVVM_DEFAULT_WRITE_ANY_ILLEGAL | OsvvmOptionsType |  FALSE           |                            |
## Types

| Name             | Type                                                                                                                                                                                                                                                         | Description |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| OsvvmOptionsType | (OPT_INIT_PARM_DETECT,<br><span style="padding-left:20px"> OPT_USE_DEFAULT,<br><span style="padding-left:20px"> DISABLED,<br><span style="padding-left:20px"> FALSE,<br><span style="padding-left:20px"> ENABLED,<br><span style="padding-left:20px"> TRUE)  |             |
| OptionsPType     |                                                                                                                                                                                                                                                              |             |
## Functions
- IsEnabled <font id="function_arguments">(A : OsvvmOptionsType) </font> <font id="function_return">return boolean </font>
**Description**
Requires that TRUE is last and ENABLED is 2nd to last
- to_OsvvmOptionsType <font id="function_arguments">(A : boolean) </font> <font id="function_return">return OsvvmOptionsType </font>
- SetOsvvmGlobalOptions <font id="function_arguments">( WritePassFail   : OsvvmOptionsType := OPT_INIT_PARM_DETECT ;<br><span style="padding-left:20px"> WriteBinInfo    : OsvvmOptionsType := OPT_INIT_PARM_DETECT ;<br><span style="padding-left:20px"> WriteCount      : OsvvmOptionsType := OPT_INIT_PARM_DETECT ;<br><span style="padding-left:20px"> WriteAnyIllegal : OsvvmOptionsType := OPT_INIT_PARM_DETECT ;<br><span style="padding-left:20px"> WritePrefix     : string := OSVVM_STRING_INIT_PARM_DETECT ;<br><span style="padding-left:20px"> DoneName        : string := OSVVM_STRING_INIT_PARM_DETECT ;<br><span style="padding-left:20px"> PassName        : string := OSVVM_STRING_INIT_PARM_DETECT ;<br><span style="padding-left:20px"> FailName        : string := OSVVM_STRING_INIT_PARM_DETECT ) </font> <font id="function_return">return ()</font>
- ResolveOsvvmOption <font id="function_arguments">(A,<br><span style="padding-left:20px"> B,<br><span style="padding-left:20px"> C : OsvvmOptionsType) </font> <font id="function_return">return OsvvmOptionsType </font>
**Description**
Accessor Functions
- ResolveOsvvmOption <font id="function_arguments">(A,<br><span style="padding-left:20px"> B,<br><span style="padding-left:20px"> C,<br><span style="padding-left:20px"> D : OsvvmOptionsType) </font> <font id="function_return">return OsvvmOptionsType </font>
- IsOsvvmStringSet <font id="function_arguments">(A : string) </font> <font id="function_return">return boolean </font>
- ResolveOsvvmOption <font id="function_arguments">(A,<br><span style="padding-left:20px"> B : string) </font> <font id="function_return">return string </font>
- ResolveOsvvmOption <font id="function_arguments">(A,<br><span style="padding-left:20px"> B,<br><span style="padding-left:20px"> C : string) </font> <font id="function_return">return string </font>
- ResolveOsvvmOption <font id="function_arguments">(A,<br><span style="padding-left:20px"> B,<br><span style="padding-left:20px"> C,<br><span style="padding-left:20px"> D : string) </font> <font id="function_return">return string </font>
- OsvvmDeallocate <font id="function_arguments">()</font> <font id="function_return">return ()</font>
