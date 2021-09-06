# Package: FileIO

- **File**: fileio.v93.vhdl
## Functions
- LogFile_Open <font id="function_arguments">(FileName : string;<br><span style="padding-left:20px"> OpenKind : T_LOGFILE_OPEN_KIND := WRITE_MODE) </font> <font id="function_return">return ()</font>
- LogFile_Open <font id="function_arguments">(Status : out FILE_OPEN_STATUS;<br><span style="padding-left:20px"> FileName : string;<br><span style="padding-left:20px"> OpenKind : T_LOGFILE_OPEN_KIND := WRITE_MODE) </font> <font id="function_return">return ()</font>
- LogFile_Print <font id="function_arguments">(str : string) </font> <font id="function_return">return ()</font>
- LogFile_PrintLine <font id="function_arguments">(str : string := "") </font> <font id="function_return">return ()</font>
- LogFile_Flush <font id="function_arguments">()</font> <font id="function_return">return ()</font>
- LogFile_Close <font id="function_arguments">()</font> <font id="function_return">return ()</font>
- StdOut_Print <font id="function_arguments">(str : string) </font> <font id="function_return">return ()</font>
**Description**
 StdOut
 ===========================================================================

- StdOut_PrintLine <font id="function_arguments">(str : string := "") </font> <font id="function_return">return ()</font>
- StdOut_Flush <font id="function_arguments">()</font> <font id="function_return">return ()</font>
