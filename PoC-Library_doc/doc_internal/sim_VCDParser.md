# Package: sim_VCDParser

- **File**: sim_VCDParser.vhdl
## Functions
- VCD_ReadHeader <font id="function_arguments">(file VCDFile : TEXT;<br><span style="padding-left:20px"> VCDLine : inout T_VCDLINE) </font> <font id="function_return">return ()</font>
- VCD_ReadLine <font id="function_arguments">(file VCDFile : TEXT;<br><span style="padding-left:20px"> VCDLine : out string) </font> <font id="function_return">return ()</font>
- VCD_Read_StdLogic <font id="function_arguments">(VCDLine : string;<br><span style="padding-left:20px"> signal sl : out std_logic;<br><span style="padding-left:20px"> WaveName : string) </font> <font id="function_return">return ()</font>
- VCD_Read_StdLogicVector <font id="function_arguments">(VCDLine : string;<br><span style="padding-left:20px"> signal slv : out std_logic_vector;<br><span style="padding-left:20px"> WaveName : string;<br><span style="padding-left:20px"> def : std_logic := '0') </font> <font id="function_return">return ()</font>
