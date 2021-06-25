# Entity: uart_bclk
## Diagram
![Diagram](uart_bclk.svg "Diagram")
## Generics
| Generic name | Type | Value     | Description |
| ------------ | ---- | --------- | ----------- |
| CLOCK_FREQ   | FREQ | 100 MHz   |             |
| BAUDRATE     | BAUD | 115200 Bd |             |
## Ports
| Port name | Direction | Type      | Description |
| --------- | --------- | --------- | ----------- |
| clk       | in        | std_logic |             |
| rst       | in        | std_logic |             |
| bclk      | out       | std_logic |             |
| bclk_x8   | out       | std_logic |             |
## Signals
| Name        | Type                                         | Description |
| ----------- | -------------------------------------------- | ----------- |
| x8_cnt      | unsigned(BAUDRATE_COUNTER_BITS - 1 downto 0) |             |
| x1_cnt      | unsigned(2 downto 0)                         |             |
| x8_cnt_done | std_logic                                    |             |
| x1_cnt_done | std_logic                                    |             |
| bclk_r      | std_logic                                    |             |
| bclk_x8_r   | std_logic                                    |             |
## Constants
| Name                   | Type     | Value                                                             | Description |
| ---------------------- | -------- | ----------------------------------------------------------------- | ----------- |
| UART_OVERSAMPLING_RATE | positive |  8                                                                |             |
| TIME_UNIT_INTERVAL     | time     |  1 sec / (to_real(BAUDRATE, 1 Bd) * real(UART_OVERSAMPLING_RATE)) |             |
| BAUDRATE_COUNTER_MAX   | positive |  TimingToCycles(TIME_UNIT_INTERVAL, CLOCK_FREQ)                   |             |
| BAUDRATE_COUNTER_BITS  | positive |  log2ceilnz(BAUDRATE_COUNTER_MAX + 1)                             |             |
