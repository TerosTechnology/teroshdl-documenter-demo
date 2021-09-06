# Package: MessageListPkg

- **File**: MessageListPkg.vhd
## Types

| Name                 | Type | Description |
| -------------------- | ---- | ----------- |
| MessageStructPtrType |      |             |
| MessageStructType    |      |             |
## Functions
- SetMessage <font id="function_arguments">(variable Message : inout MessageStructPtrType;<br><span style="padding-left:20px"> Name : String) </font> <font id="function_return">return ()</font>
- WriteMessage <font id="function_arguments">(variable buf : inout line;<br><span style="padding-left:20px"> variable Message : inout MessageStructPtrType;<br><span style="padding-left:20px"> prefix : string := "") </font> <font id="function_return">return ()</font>
- WriteMessage <font id="function_arguments">(file f : text;<br><span style="padding-left:20px"> variable Message : inout MessageStructPtrType;<br><span style="padding-left:20px"> prefix : string := "") </font> <font id="function_return">return ()</font>
- GetMessageCount <font id="function_arguments">(variable Message : inout MessageStructPtrType;<br><span style="padding-left:20px"> variable Count : out integer) </font> <font id="function_return">return ()</font>
- DeallocateMessage <font id="function_arguments">(variable Message : inout MessageStructPtrType) </font> <font id="function_return">return ()</font>
