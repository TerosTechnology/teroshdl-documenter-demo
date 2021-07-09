# Entity: ltc2145_cmos_capture

## Diagram

![Diagram](ltc2145_cmos_capture.svg "Diagram")
## Generics

| Generic name                   | Type    | Value | Description |
| ------------------------------ | ------- | ----- | ----------- |
| CLOCK_DUTY_CYCLE_STABILIZER_EN | boolean | false |             |
## Ports

| Port name    | Direction | Type                          | Description |
| ------------ | --------- | ----------------------------- | ----------- |
| clk_in_i     | in        | std_logic                     | ltc2145     |
| resetn       | in        | std_logic                     |             |
| clk_cdcs     | out       | std_logic                     |             |
| adc_data_a_i | in        | std_logic_vector(13 downto 0) | a/d cmos    |
| adc_data_b_i | in        | std_logic_vector(13 downto 0) |             |
| adc_clk_o    | out       | std_logic                     | adc dat     |
| adc_data_en  | out       | std_logic                     |             |
| adc_data_a   | out       | std_logic_vector(13 downto 0) |             |
| adc_data_b   | out       | std_logic_vector(13 downto 0) |             |
## Signals

| Name      | Type                          | Description |
| --------- | ----------------------------- | ----------- |
| data_a_s  | std_logic_vector(13 downto 0) |             |
|  data_b_s | std_logic_vector(13 downto 0) |             |
## Processes
- latch_d: ( clk_in_i, resetn )
