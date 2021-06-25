# Entity: fifo_shift
## Diagram
![Diagram](fifo_shift.svg "Diagram")
## Generics
| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| D_BITS       | positive |       |             |
| MIN_DEPTH    | positive |       |             |
## Ports
| Port name | Direction | Type                                | Description |
| --------- | --------- | ----------------------------------- | ----------- |
| clk       | in        | std_logic                           |             |
| rst       | in        | std_logic                           |             |
| put       | in        | std_logic                           |             |
| din       | in        | std_logic_vector(D_BITS-1 downto 0) |             |
| ful       | out       | std_logic                           |             |
| got       | in        | std_logic                           |             |
| dout      | out       | std_logic_vector(D_BITS-1 downto 0) |             |
| vld       | out       | std_logic                           |             |
## Signals
| Name | Type                                     | Description |
| ---- | ---------------------------------------- | ----------- |
| Dat  | tData(0 to MIN_DEPTH-1)                  |             |
| Ptr  | unsigned(log2ceilnz(MIN_DEPTH) downto 0) |             |
## Types
| Name  | Type | Description |
| ----- | ---- | ----------- |
| tData |      |             |
## Processes
- unnamed: _( clk )_

- unnamed: _( clk )_

