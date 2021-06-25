# Package: sim_VCDParser
## Functions
- VCD_ReadHeader <font id="function_arguments">(file VCDFile : TEXT; VCDLine : inout T_VCDLINE)</font> <font id="function_return">return ()</font>
- VCD_ReadLine <font id="function_arguments">(file VCDFile : TEXT; VCDLine : out string)</font> <font id="function_return">return ()</font>
- VCD_Read_StdLogic <font id="function_arguments">(VCDLine : string; signal sl : out std_logic; WaveName : string)</font> <font id="function_return">return ()</font>
- VCD_Read_StdLogicVector <font id="function_arguments">(VCDLine : string; signal slv : out std_logic_vector; WaveName : string; def : std_logic := '0')</font> <font id="function_return">return ()</font>
