# Entity: pmod_SSD
## Diagram
![Diagram](pmod_SSD.svg "Diagram")
## Generics
| Generic name | Type | Value   | Description |
| ------------ | ---- | ------- | ----------- |
| CLOCK_FREQ   | FREQ | 100 MHz |             |
| REFRESH_RATE | FREQ | 1 kHz   |             |
## Ports
| Port name | Direction | Type                         | Description |
| --------- | --------- | ---------------------------- | ----------- |
| Clock     | in        | std_logic                    |             |
| Digit0    | in        | std_logic_vector(3 downto 0) |             |
| Digit1    | in        | std_logic_vector(3 downto 0) |             |
| SSD       | out       | T_PMOD_SSD_PINS              |             |
## Signals
| Name             | Type                                   | Description |
| ---------------- | -------------------------------------- | ----------- |
| RefreshTimer_rst | std_logic                              |             |
| RefreshTimer_s   | signed(REFRESHTIMER_BITS - 1 downto 0) |             |
| CathodeSelect_en | std_logic                              |             |
| CathodeSelect_r  | std_logic                              |             |
| Digit            | std_logic_vector(3 downto 0)           |             |
| Segments         | std_logic_vector(6 downto 0)           |             |
## Constants
| Name              | Type     | Value                                                  | Description |
| ----------------- | -------- | ------------------------------------------------------ | ----------- |
| REFRESHTIMER_MAX  | positive |  TimingToCycles(to_time(REFRESH_RATE), CLOCK_FREQ) - 1 |             |
| REFRESHTIMER_BITS | positive |  log2ceilnz(REFRESHTIMER_MAX) + 1                      |             |
