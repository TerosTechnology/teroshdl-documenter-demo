# Entity: T80_MCode
## Diagram
![Diagram](T80_MCode.svg "Diagram")
## Generics
| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| Mode         | integer | 0     |             |
| Flag_C       | integer | 0     |             |
| Flag_N       | integer | 1     |             |
| Flag_P       | integer | 2     |             |
| Flag_X       | integer | 3     |             |
| Flag_H       | integer | 4     |             |
| Flag_Y       | integer | 5     |             |
| Flag_Z       | integer | 6     |             |
| Flag_S       | integer | 7     |             |
## Ports
| Port name   | Direction | Type                         | Description |
| ----------- | --------- | ---------------------------- | ----------- |
| IR          | in        | std_logic_vector(7 downto 0) |             |
| ISet        | in        | std_logic_vector(1 downto 0) |             |
| MCycle      | in        | std_logic_vector(2 downto 0) |             |
| F           | in        | std_logic_vector(7 downto 0) |             |
| NMICycle    | in        | std_logic                    |             |
| IntCycle    | in        | std_logic                    |             |
| XY_State    | in        | std_logic_vector(1 downto 0) |             |
| MCycles     | out       | std_logic_vector(2 downto 0) |             |
| TStates     | out       | std_logic_vector(2 downto 0) |             |
| Prefix      | out       | std_logic_vector(1 downto 0) |             |
| Inc_PC      | out       | std_logic                    |             |
| Inc_WZ      | out       | std_logic                    |             |
| IncDec_16   | out       | std_logic_vector(3 downto 0) |             |
| Read_To_Reg | out       | std_logic                    |             |
| Read_To_Acc | out       | std_logic                    |             |
| Set_BusA_To | out       | std_logic_vector(3 downto 0) |             |
| Set_BusB_To | out       | std_logic_vector(3 downto 0) |             |
| ALU_Op      | out       | std_logic_vector(3 downto 0) |             |
| Save_ALU    | out       | std_logic                    |             |
| PreserveC   | out       | std_logic                    |             |
| Arith16     | out       | std_logic                    |             |
| Set_Addr_To | out       | std_logic_vector(2 downto 0) |             |
| IORQ        | out       | std_logic                    |             |
| Jump        | out       | std_logic                    |             |
| JumpE       | out       | std_logic                    |             |
| JumpXY      | out       | std_logic                    |             |
| Call        | out       | std_logic                    |             |
| RstP        | out       | std_logic                    |             |
| LDZ         | out       | std_logic                    |             |
| LDW         | out       | std_logic                    |             |
| LDSPHL      | out       | std_logic                    |             |
| Special_LD  | out       | std_logic_vector(2 downto 0) |             |
| ExchangeDH  | out       | std_logic                    |             |
| ExchangeRp  | out       | std_logic                    |             |
| ExchangeAF  | out       | std_logic                    |             |
| ExchangeRS  | out       | std_logic                    |             |
| I_DJNZ      | out       | std_logic                    |             |
| I_CPL       | out       | std_logic                    |             |
| I_CCF       | out       | std_logic                    |             |
| I_SCF       | out       | std_logic                    |             |
| I_RETN      | out       | std_logic                    |             |
| I_BT        | out       | std_logic                    |             |
| I_BC        | out       | std_logic                    |             |
| I_BTR       | out       | std_logic                    |             |
| I_RLD       | out       | std_logic                    |             |
| I_RRD       | out       | std_logic                    |             |
| I_INRC      | out       | std_logic                    |             |
| SetWZ       | out       | std_logic_vector(1 downto 0) |             |
| SetDI       | out       | std_logic                    |             |
| SetEI       | out       | std_logic                    |             |
| IMode       | out       | std_logic_vector(1 downto 0) |             |
| Halt        | out       | std_logic                    |             |
| NoRead      | out       | std_logic                    |             |
| Write       | out       | std_logic                    |             |
| XYbit_undoc | out       | std_logic                    |             |
## Functions
- is_cc_true <font id="function_arguments">(		F : std_logic_vector(7 downto 0);
		cc : bit_vector(2 downto 0)
		)</font> <font id="function_return">return boolean</font>
## Processes
- unnamed: _( IR, ISet, MCycle, F, NMICycle, IntCycle, XY_State )_

