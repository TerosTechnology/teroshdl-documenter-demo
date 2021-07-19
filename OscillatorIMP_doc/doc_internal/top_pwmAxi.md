# Entity: top_pwmaxi

- **File**: top_pwmAxi.vhd
## Diagram

![Diagram](top_pwmAxi.svg "Diagram")
## Ports

| Port name   | Direction | Type                          | Description |
| ----------- | --------- | ----------------------------- | ----------- |
| clk_i       | in        | std_logic                     |             |
| rst_i       | in        | std_logic                     |             |
| enable_i    | in        | std_logic                     | conf        |
| duty_i      | in        | std_logic_vector(31 downto 0) |             |
| period_i    | in        | std_logic_vector(31 downto 0) |             |
| prescaler_i | in        | std_logic_vector(31 downto 0) |             |
| pwm1_o      | out       | std_logic                     | out         |
| pwm2_o      | out       | std_logic                     |             |
## Instantiations

- dutInvertN: work.pwm_logic
- dutInvert: work.pwm_logic
