# Entity: lut_Sine
## Diagram
![Diagram](lut_Sine.svg "Diagram")
## Generics
| Generic name  | Type     | Value | Description |
| ------------- | -------- | ----- | ----------- |
| REG_OUTPUT    | boolean  | TRUE  |             |
| MAX_AMPLITUDE | positive | 255   |             |
| POINTS        | positive | 4096  |             |
| OFFSET_DEG    | REAL     | 0.0   |             |
| QUARTERS      | positive | 4     |             |
## Ports
| Port name | Direction | Type                                                                        | Description |
| --------- | --------- | --------------------------------------------------------------------------- | ----------- |
| Clock     | in        | std_logic                                                                   |             |
| Input     | in        | std_logic_vector(log2ceilnz(POINTS) - 1 downto 0)                           |             |
| Output    | out       | std_logic_vector(log2ceilnz(MAX_AMPLITUDE + ((QUARTERS - 1) / 2)) downto 0) |             |
## Signals
| Name       | Type                           | Description |
| ---------- | ------------------------------ | ----------- |
| Output_nxt | std_logic_vector(Output'range) |             |
