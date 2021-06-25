# Entity: T80_Reg
## Diagram
![Diagram](T80_Reg.svg "Diagram")
## Ports
| Port name | Direction | Type                           | Description |
| --------- | --------- | ------------------------------ | ----------- |
| Clk       | in        | std_logic                      |             |
| CEN       | in        | std_logic                      |             |
| WEH       | in        | std_logic                      |             |
| WEL       | in        | std_logic                      |             |
| AddrA     | in        | std_logic_vector(2 downto 0)   |             |
| AddrB     | in        | std_logic_vector(2 downto 0)   |             |
| AddrC     | in        | std_logic_vector(2 downto 0)   |             |
| DIH       | in        | std_logic_vector(7 downto 0)   |             |
| DIL       | in        | std_logic_vector(7 downto 0)   |             |
| DOAH      | out       | std_logic_vector(7 downto 0)   |             |
| DOAL      | out       | std_logic_vector(7 downto 0)   |             |
| DOBH      | out       | std_logic_vector(7 downto 0)   |             |
| DOBL      | out       | std_logic_vector(7 downto 0)   |             |
| DOCH      | out       | std_logic_vector(7 downto 0)   |             |
| DOCL      | out       | std_logic_vector(7 downto 0)   |             |
| DOR       | out       | std_logic_vector(127 downto 0) |             |
| DIRSet    | in        | std_logic                      |             |
| DIR       | in        | std_logic_vector(127 downto 0) |             |
## Signals
| Name  | Type                   | Description |
| ----- | ---------------------- | ----------- |
| RegsH | Register_Image(0 to 7) |             |
| RegsL | Register_Image(0 to 7) |             |
## Types
| Name           | Type | Description |
| -------------- | ---- | ----------- |
| Register_Image |      |             |
## Processes
- unnamed: _( Clk )_

