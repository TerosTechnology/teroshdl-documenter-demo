# Package: MemoryPkg

## Constants

| Name                     | Type           | Value              | Description |
| ------------------------ | -------------- | ------------------ | ----------- |
| OSVVM_MEMORY_ALERTLOG_ID | AlertLogIDType |  OSVVM_ALERTLOG_ID |             |
## Types

| Name              | Type | Description |
| ----------------- | ---- | ----------- |
| MemoryIDType      |      |             |
| MemoryIDArrayType |      |             |
| MemoryPType       |      |             |
## Functions
- MemWrite <font id="function_arguments">( ID    : MemoryIDType ; Addr  : std_logic_vector ; Data  : std_logic_vector ) </font> <font id="function_return">return ()</font>
- MemRead <font id="function_arguments">( ID    : in MemoryIDType ; Addr  : in  std_logic_vector ; Data  : out std_logic_vector ) </font> <font id="function_return">return ()</font>
- MemErase <font id="function_arguments">(ID : in MemoryIDType) </font> <font id="function_return">return ()</font>
- FileReadH <font id="function_arguments">(    -- Hexadecimal File Read ID           : MemoryIDType ; FileName     : string ; StartAddr    : std_logic_vector ; EndAddr      : std_logic_vector ) </font> <font id="function_return">return ()</font>
- FileReadH <font id="function_arguments">( ID           : MemoryIDType ; FileName     : string ; StartAddr    : std_logic_vector ) </font> <font id="function_return">return ()</font>
- FileReadH <font id="function_arguments">( ID           : MemoryIDType ; FileName     : string ) </font> <font id="function_return">return ()</font>
- FileReadB <font id="function_arguments">(    -- Binary File Read ID           : MemoryIDType ; FileName     : string ; StartAddr    : std_logic_vector ; EndAddr      : std_logic_vector ) </font> <font id="function_return">return ()</font>
- FileReadB <font id="function_arguments">( ID           : MemoryIDType ; FileName     : string ; StartAddr    : std_logic_vector ) </font> <font id="function_return">return ()</font>
- FileReadB <font id="function_arguments">( ID           : MemoryIDType ; FileName     : string ) </font> <font id="function_return">return ()</font>
- FileWriteH <font id="function_arguments">(    -- Hexadecimal File Write ID           : MemoryIDType ; FileName     : string ; StartAddr    : std_logic_vector ; EndAddr      : std_logic_vector ) </font> <font id="function_return">return ()</font>
- FileWriteH <font id="function_arguments">( ID           : MemoryIDType ; FileName     : string ; StartAddr    : std_logic_vector ) </font> <font id="function_return">return ()</font>
- FileWriteH <font id="function_arguments">( ID           : MemoryIDType ; FileName     : string ) </font> <font id="function_return">return ()</font>
- FileWriteB <font id="function_arguments">(    -- Binary File Write ID           : MemoryIDType ; FileName     : string ; StartAddr    : std_logic_vector ; EndAddr      : std_logic_vector ) </font> <font id="function_return">return ()</font>
- FileWriteB <font id="function_arguments">( ID           : MemoryIDType ; FileName     : string ; StartAddr    : std_logic_vector ) </font> <font id="function_return">return ()</font>
- FileWriteB <font id="function_arguments">( ID           : MemoryIDType ; FileName     : string ) </font> <font id="function_return">return ()</font>
