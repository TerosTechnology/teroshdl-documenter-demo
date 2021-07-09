# Entity: pwm_cpt

## Diagram

![Diagram](pwm_cpt.svg "Diagram")
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| CPT_SIZE     | natural | 32    |             |
## Ports

| Port name | Direction | Type                                  | Description |
| --------- | --------- | ------------------------------------- | ----------- |
| clk_i     | in        | std_logic                             |             |
| reset_i   | in        | std_logic                             |             |
| enable_i  | in        | std_logic                             |             |
| max_cpt_i | in        | std_logic_vector(CPT_SIZE-1 downto 0) |             |
| tick_o    | out       | std_logic                             |             |
## Signals

| Name       | Type                          | Description |
| ---------- | ----------------------------- | ----------- |
| cpt_s      | unsigned(CPT_SIZE-1 downto 0) |             |
|  max_cpt_s | unsigned(CPT_SIZE-1 downto 0) |             |
| clr_cpt_s  | std_logic                     |             |
|  rst_s     | std_logic                     |             |
## Processes
- prescaler: ( clk_i )
