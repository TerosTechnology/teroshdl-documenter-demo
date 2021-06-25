# Entity: T80_ALU
## Diagram
![Diagram](T80_ALU.svg "Diagram")
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
| Port name | Direction | Type                          | Description |
| --------- | --------- | ----------------------------- | ----------- |
| Arith16   | in        | std_logic                     |             |
| Z16       | in        | std_logic                     |             |
| WZ        | in        | std_logic_vector(15 downto 0) |             |
| XY_State  | in        | std_logic_vector(1 downto 0)  |             |
| ALU_Op    | in        | std_logic_vector(3 downto 0)  |             |
| IR        | in        | std_logic_vector(5 downto 0)  |             |
| ISet      | in        | std_logic_vector(1 downto 0)  |             |
| BusA      | in        | std_logic_vector(7 downto 0)  |             |
| BusB      | in        | std_logic_vector(7 downto 0)  |             |
| F_In      | in        | std_logic_vector(7 downto 0)  |             |
| Q         | out       | std_logic_vector(7 downto 0)  |             |
| F_Out     | out       | std_logic_vector(7 downto 0)  |             |
## Signals
| Name        | Type                         | Description |
| ----------- | ---------------------------- | ----------- |
| UseCarry    | std_logic                    |             |
| Carry7_v    | std_logic                    |             |
| Overflow_v  | std_logic                    |             |
| HalfCarry_v | std_logic                    |             |
| Carry_v     | std_logic                    |             |
| Q_v         | std_logic_vector(7 downto 0) |             |
| BitMask     | std_logic_vector(7 downto 0) |             |
## Functions
- AddSub <font id="function_arguments">(A        : std_logic_vector;					 B        : std_logic_vector;
					 Sub      : std_logic;
					 Carry_In : std_logic;
			  signal Res      : out std_logic_vector;
			  signal Carry    : out std_logic)</font> <font id="function_return">return ()</font>
## Processes
- unnamed: _( Carry_v, Carry7_v, Q_v )_

- unnamed: _( Arith16, ALU_OP, F_In, BusA, BusB, IR, Q_v, Carry_v, HalfCarry_v, OverFlow_v, BitMask, ISet, Z16, WZ, XY_State )_

