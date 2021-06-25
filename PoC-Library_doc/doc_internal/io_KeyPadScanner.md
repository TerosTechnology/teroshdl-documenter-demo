# Entity: io_KeyPadScanner
## Diagram
![Diagram](io_KeyPadScanner.svg "Diagram")
## Generics
| Generic name            | Type     | Value   | Description |
| ----------------------- | -------- | ------- | ----------- |
| CLOCK_FREQ              | FREQ     | 100 MHz |             |
| SCAN_FREQ               | FREQ     | 1 kHz   |             |
| ROWS                    | positive | 4       |             |
| COLUMNS                 | positive | 4       |             |
| ADD_INPUT_SYNCHRONIZERS | boolean  | TRUE    |             |
## Ports
| Port name    | Direction | Type                                           | Description |
| ------------ | --------- | ---------------------------------------------- | ----------- |
| Clock        | in        | std_logic                                      |             |
| Reset        | in        | std_logic                                      |             |
| KeyPadMatrix | out       | T_SLM(COLUMNS - 1 downto 0, ROWS - 1 downto 0) |             |
| ColumnVector | out       | std_logic_vector(COLUMNS - 1 downto 0)         |             |
| RowVector    | in        | std_logic_vector(ROWS - 1 downto 0)            |             |
## Signals
| Name            | Type                                           | Description |
| --------------- | ---------------------------------------------- | ----------- |
| ColumnTimer_rst | std_logic                                      |             |
| ColumnTimer_s   | signed(COLUMNTIMER_BITS - 1 downto 0)          |             |
| ColumnSelect_en | std_logic                                      |             |
| ColumnSelect_d  | std_logic_vector(COLUMNS - 1 downto 0)         |             |
| Rows_sync       | std_logic_vector(ROWS - 1 downto 0)            |             |
| KeyPadMatrix_r  | T_SLM(COLUMNS - 1 downto 0, ROWS - 1 downto 0) |             |
## Constants
| Name             | Type     | Value                                                | Description |
| ---------------- | -------- | ---------------------------------------------------- | ----------- |
| SHIFT_FREQ       | FREQ     |  SCAN_FREQ * COLUMNS                                 |             |
| COLUMNTIMER_MAX  | positive |  TimingToCycles(to_time(SHIFT_FREQ), CLOCK_FREQ) - 1 |             |
| COLUMNTIMER_BITS | positive |  log2ceilnz(COLUMNTIMER_MAX) + 1                     |             |
