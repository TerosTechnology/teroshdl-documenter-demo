# Entity: arith_shifter_barrel
## Diagram
![Diagram](arith_shifter_barrel.svg "Diagram")
## Generics
| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| BITS         | positive | 32    |             |
## Ports
| Port name       | Direction | Type                                            | Description |
| --------------- | --------- | ----------------------------------------------- | ----------- |
| Input           | in        | std_logic_vector(BITS - 1 downto 0)             |             |
| ShiftAmount     | in        | std_logic_vector(log2ceilnz(BITS) - 1 downto 0) |             |
| ShiftRotate     | in        | std_logic                                       |             |
| LeftRight       | in        | std_logic                                       |             |
| ArithmeticLogic | in        | std_logic                                       |             |
| Output          | out       | std_logic_vector(BITS - 1 downto 0)             |             |
## Signals
| Name                | Type                                   | Description |
| ------------------- | -------------------------------------- | ----------- |
| IntermediateResults | T_INTERMEDIATE_VECTOR(STAGES downto 0) |             |
## Constants
| Name   | Type     | Value             | Description |
| ------ | -------- | ----------------- | ----------- |
| STAGES | positive |  log2ceilnz(BITS) |             |
## Types
| Name                  | Type | Description |
| --------------------- | ---- | ----------- |
| T_INTERMEDIATE_VECTOR |      |             |
