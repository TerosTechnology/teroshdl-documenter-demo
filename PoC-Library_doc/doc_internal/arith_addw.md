# Entity: arith_addw
## Diagram
![Diagram](arith_addw.svg "Diagram")
## Generics
| Generic name | Type      | Value | Description |
| ------------ | --------- | ----- | ----------- |
| N            | positive  |       |             |
| K            | positive  |       |             |
| ARCH         | tArch     | AAM   |             |
| BLOCKING     | tBlocking | DFLT  |             |
| SKIPPING     | tSkipping | CCC   |             |
| P_INCLUSIVE  | boolean   | false |             |
## Ports
| Port name | Direction | Type                           | Description |
| --------- | --------- | ------------------------------ | ----------- |
| a         | in        | std_logic_vector(N-1 downto 0) |             |
| b         | in        | std_logic_vector(N-1 downto 0) |             |
| cin       | in        | std_logic                      |             |
| s         | out       | std_logic_vector(N-1 downto 0) |             |
| cout      | out       | std_logic                      |             |
## Signals
| Name | Type                           | Description |
| ---- | ------------------------------ | ----------- |
| g    | std_logic_vector(K-1 downto 1) |             |
| p    | std_logic_vector(K-1 downto 1) |             |
| c    | std_logic_vector(K-1 downto 1) |             |
## Constants
| Name             | Type                         | Value                                                | Description |
| ---------------- | ---------------------------- | ---------------------------------------------------- | ----------- |
| DEFAULT_BLOCKING | tBlocking_vector             |  (AAM => ASC, CAI => DESC, PAI => DESC, CCA => DESC) |             |
| BLOCKS           | integer_vector(K-1 downto 0) |  compute_blocks                                      |             |
## Types
| Name             | Type | Description |
| ---------------- | ---- | ----------- |
| tBlocking_vector |      |             |
| integer_vector   |      |             |
## Functions
