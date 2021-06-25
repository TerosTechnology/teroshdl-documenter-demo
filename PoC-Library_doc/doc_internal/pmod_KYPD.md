# Entity: pmod_KYPD
## Diagram
![Diagram](pmod_KYPD.svg "Diagram")
## Generics
| Generic name | Type | Value   | Description |
| ------------ | ---- | ------- | ----------- |
| CLOCK_FREQ   | FREQ | 100 MHz |             |
| SCAN_FREQ    | FREQ | 1 kHz   |             |
| BOUNCE_TIME  | time | 10 ms   |             |
## Ports
| Port name | Direction | Type                         | Description |
| --------- | --------- | ---------------------------- | ----------- |
| Clock     | in        | std_logic                    |             |
| Reset     | in        | std_logic                    |             |
| Keys      | out       | T_PMOD_KYPD_KEYPAD           |             |
| Columns_n | out       | std_logic_vector(3 downto 0) |             |
| Rows_n    | in        | std_logic_vector(3 downto 0) |             |
## Signals
| Name             | Type                          | Description |
| ---------------- | ----------------------------- | ----------- |
| ColumnVector     | std_logic_vector(3 downto 0)  |             |
| RowVector        | std_logic_vector(3 downto 0)  |             |
| KeyPadMatrix     | T_SLM(3 downto 0, 3 downto 0) |             |
| KeyPadMatrix_slv | std_logic_vector(15 downto 0) |             |
| KeyPadVector     | std_logic_vector(15 downto 0) |             |
| KeyPad           | T_SLM(3 downto 0, 3 downto 0) |             |
## Instantiations
- scanner: PoC.io_KeyPadScanner
- debounce: PoC.io_Debounce
