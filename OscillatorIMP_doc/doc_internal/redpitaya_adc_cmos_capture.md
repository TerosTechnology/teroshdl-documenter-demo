# Entity: redpitaya_adc_cmos_capture

- **File**: redpitaya_adc_cmos_capture.vhd
## Diagram

![Diagram](redpitaya_adc_cmos_capture.svg "Diagram")
## Generics

| Generic name                   | Type    | Value | Description |
| ------------------------------ | ------- | ----- | ----------- |
| ADC_SIZE                       | natural | 14    |             |
| CLOCK_DUTY_CYCLE_STABILIZER_EN | boolean | true  |             |
## Ports

| Port name    | Direction | Type                                  | Description   |
| ------------ | --------- | ------------------------------------- | ------------- |
| clk_in_i     | in        | std_logic                             | redpitaya_adc |
| resetn       | in        | std_logic                             |               |
| clk_cdcs     | out       | std_logic                             |               |
| adc_data_a_i | in        | std_logic_vector(ADC_SIZE-1 downto 0) | a/d cmos      |
| adc_data_b_i | in        | std_logic_vector(ADC_SIZE-1 downto 0) |               |
| adc_data_en  | out       | std_logic                             | adc dat       |
| adc_data_a   | out       | std_logic_vector(ADC_SIZE-1 downto 0) |               |
| adc_data_b   | out       | std_logic_vector(ADC_SIZE-1 downto 0) |               |
## Signals

| Name      | Type                                  | Description |
| --------- | ------------------------------------- | ----------- |
| data_a_s  | std_logic_vector(ADC_SIZE-1 downto 0) |             |
|  data_b_s | std_logic_vector(ADC_SIZE-1 downto 0) |             |
## Processes
- latch_d: ( clk_in_i, resetn )
