# Entity: arith_cca
## Diagram
![Diagram](arith_cca.svg "Diagram")
## Generics
| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| N            | positive |       |             |
| L            | natural  |       |             |
| X            | natural  | 0     |             |
## Ports
| Port name | Direction | Type                           | Description |
| --------- | --------- | ------------------------------ | ----------- |
| a         | in        | std_logic_vector(N-1 downto 0) |             |
| b         | in        | std_logic_vector(N-1 downto 0) |             |
| c         | in        | std_logic                      |             |
| s         | out       | std_logic_vector(N-1 downto 0) |             |
## Constants
| Name   | Type    | Value              | Description |
| ------ | ------- | ------------------ | ----------- |
| LEVELS | tLevels |  compact           |             |
| CCA    | boolean |  LEVELS'length > 1 |             |
## Types
| Name    | Type | Description |
| ------- | ---- | ----------- |
| tLevel  |      |             |
| tLevels |      |             |
## Functions
- compact <font id="function_arguments">()</font> <font id="function_return">return tLevels</font>
