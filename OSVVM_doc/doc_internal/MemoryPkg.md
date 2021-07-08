# Package: MemoryPkg

## Constants

| Name                     | Type           | Value              | Description |
| ------------------------ | -------------- | ------------------ | ----------- |
| OSVVM_MEMORY_ALERTLOG_ID | AlertLogIDType |  OSVVM_ALERTLOG_ID |             |
## Types

| Name              | Type                                      | Description |
| ----------------- | ----------------------------------------- | ----------- |
| MemoryIDType      |                                           |             |
| MemoryIDArrayType | array (integer range <>) of MemoryIDType  |             |
| MemoryPType       |                                           |             |
## Functions
- MemWrite <font id="function_arguments">( ID    : MemoryIDType ;<br><span style="padding-left:20px"> Addr  : std_logic_vector ;<br><span style="padding-left:20px"> Data  : std_logic_vector ) </font> <font id="function_return">return ()</font>
- MemRead <font id="function_arguments">( ID    : in MemoryIDType ;<br><span style="padding-left:20px"> Addr  : in  std_logic_vector ;<br><span style="padding-left:20px"> Data  : out std_logic_vector ) </font> <font id="function_return">return ()</font>
- MemErase <font id="function_arguments">(ID : in MemoryIDType) </font> <font id="function_return">return ()</font>
- FileReadH <font id="function_arguments">(    -- Hexadecimal File Read ID           : MemoryIDType ;<br><span style="padding-left:20px"> FileName     : string ;<br><span style="padding-left:20px"> StartAddr    : std_logic_vector ;<br><span style="padding-left:20px"> EndAddr      : std_logic_vector ) </font> <font id="function_return">return ()</font>
- FileReadH <font id="function_arguments">( ID           : MemoryIDType ;<br><span style="padding-left:20px"> FileName     : string ;<br><span style="padding-left:20px"> StartAddr    : std_logic_vector ) </font> <font id="function_return">return ()</font>
- FileReadH <font id="function_arguments">( ID           : MemoryIDType ;<br><span style="padding-left:20px"> FileName     : string ) </font> <font id="function_return">return ()</font>
- FileReadB <font id="function_arguments">(    -- Binary File Read ID           : MemoryIDType ;<br><span style="padding-left:20px"> FileName     : string ;<br><span style="padding-left:20px"> StartAddr    : std_logic_vector ;<br><span style="padding-left:20px"> EndAddr      : std_logic_vector ) </font> <font id="function_return">return ()</font>
- FileReadB <font id="function_arguments">( ID           : MemoryIDType ;<br><span style="padding-left:20px"> FileName     : string ;<br><span style="padding-left:20px"> StartAddr    : std_logic_vector ) </font> <font id="function_return">return ()</font>
- FileReadB <font id="function_arguments">( ID           : MemoryIDType ;<br><span style="padding-left:20px"> FileName     : string ) </font> <font id="function_return">return ()</font>
- FileWriteH <font id="function_arguments">(    -- Hexadecimal File Write ID           : MemoryIDType ;<br><span style="padding-left:20px"> FileName     : string ;<br><span style="padding-left:20px"> StartAddr    : std_logic_vector ;<br><span style="padding-left:20px"> EndAddr      : std_logic_vector ) </font> <font id="function_return">return ()</font>
- FileWriteH <font id="function_arguments">( ID           : MemoryIDType ;<br><span style="padding-left:20px"> FileName     : string ;<br><span style="padding-left:20px"> StartAddr    : std_logic_vector ) </font> <font id="function_return">return ()</font>
- FileWriteH <font id="function_arguments">( ID           : MemoryIDType ;<br><span style="padding-left:20px"> FileName     : string ) </font> <font id="function_return">return ()</font>
- FileWriteB <font id="function_arguments">(    -- Binary File Write ID           : MemoryIDType ;<br><span style="padding-left:20px"> FileName     : string ;<br><span style="padding-left:20px"> StartAddr    : std_logic_vector ;<br><span style="padding-left:20px"> EndAddr      : std_logic_vector ) </font> <font id="function_return">return ()</font>
- FileWriteB <font id="function_arguments">( ID           : MemoryIDType ;<br><span style="padding-left:20px"> FileName     : string ;<br><span style="padding-left:20px"> StartAddr    : std_logic_vector ) </font> <font id="function_return">return ()</font>
- FileWriteB <font id="function_arguments">( ID           : MemoryIDType ;<br><span style="padding-left:20px"> FileName     : string ) </font> <font id="function_return">return ()</font>
