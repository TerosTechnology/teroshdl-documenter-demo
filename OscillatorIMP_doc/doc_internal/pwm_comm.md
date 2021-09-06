# Entity: pwm_comm

- **File**: pwm_comm.vhd
## Diagram

![Diagram](pwm_comm.svg "Diagram")
## Generics

| Generic name   | Type    | Value | Description |
| -------------- | ------- | ----- | ----------- |
| id             | natural | 1     |             |
| COUNTER_SIZE   | natural | 32    |             |
| AXI_DATA_WIDTH | integer | 32    |             |
## Ports

| Port name   | Direction | Type                                        | Description    |
| ----------- | --------- | ------------------------------------------- | -------------- |
| reset       | in        | std_logic                                   | Syscon signals |
| clk         | in        | std_logic                                   |                |
| addr_i      | in        | std_logic_vector(2 downto 0)                | axi signals    |
| write_en_i  | in        | std_logic                                   |                |
| writedata   | in        | std_logic_vector(AXI_DATA_WIDTH-1 downto 0) |                |
| read_en_i   | in        | std_logic                                   |                |
| read_ack_o  | out       | std_logic                                   |                |
| readdata    | out       | std_logic_vector(AXI_DATA_WIDTH-1 downto 0) |                |
| enable_o    | out       | std_logic                                   | out signals    |
| invert_o    | out       | std_logic                                   |                |
| prescaler_o | out       | std_logic_vector(COUNTER_SIZE-1 downto 0)   |                |
| duty_o      | out       | std_logic_vector(COUNTER_SIZE-1 downto 0)   |                |
| period_o    | out       | std_logic_vector(COUNTER_SIZE-1 downto 0)   |                |
## Signals

| Name        | Type                                        | Description |
| ----------- | ------------------------------------------- | ----------- |
| enable_s    | std_logic                                   |             |
|  invert_s   | std_logic                                   |             |
| duty_s      | std_logic_vector(COUNTER_SIZE-1 downto 0)   |             |
| period_s    | std_logic_vector(COUNTER_SIZE-1 downto 0)   |             |
| prescaler_s | std_logic_vector(COUNTER_SIZE-1 downto 0)   |             |
| readdata_s  | std_logic_vector(AXI_DATA_WIDTH-1 downto 0) |             |
| writedata_s | std_logic_vector(COUNTER_SIZE-1 downto 0)   |             |
## Constants

| Name          | Type                         | Value  | Description |
| ------------- | ---------------------------- | ------ | ----------- |
| REG_ID        | std_logic_vector(2 downto 0) |  "000" |             |
| REG_CTRL      | std_logic_vector(2 downto 0) |  "001" |             |
| REG_DUTY      | std_logic_vector(2 downto 0) |  "010" |             |
| REG_PERIOD    | std_logic_vector(2 downto 0) |  "011" |             |
| REG_PRESCALER | std_logic_vector(2 downto 0) |  "100" |             |
## Processes
- write_bloc: ( clk )
</br>**Description**
 manage register 
- read_bloc: ( clk, reset )
