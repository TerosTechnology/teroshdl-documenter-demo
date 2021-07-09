# Entity: cacode

## Diagram

![Diagram](cacode.svg "Diagram")
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| PERIOD_LEN   | natural | 1     |             |
## Ports

| Port name   | Direction | Type                          | Description |
| ----------- | --------- | ----------------------------- | ----------- |
| clk         | in        | std_logic                     |             |
| reset       | in        | std_logic                     |             |
| tick_i      | in        | std_logic                     |             |
| g1_full_o   | out       | std_logic_vector(9 downto 0)  | start       |
| cacode_o    | out       | std_logic_vector(9 downto 0)  |             |
| g1_o        | out       | std_logic                     |             |
| g2_o        | out       | std_logic                     |             |
| gold_code_o | out       | std_logic_vector(31 downto 0) |             |
## Signals

| Name            | Type                            | Description |
| --------------- | ------------------------------- | ----------- |
| g2_full_s       | std_logic_vector(9 downto 0)    |             |
| g1_s            | std_logic                       |             |
| s1_s            | std_logic_vector(31 downto 0)   |             |
|  s2_s           | std_logic_vector(31 downto 0)   |             |
|  s1_2_s         | std_logic_vector(31 downto 0)   |             |
| counter_s       | natural range 0 to PERIOD_LEN-1 | prescaler   |
|  counter_next_s | natural range 0 to PERIOD_LEN-1 | prescaler   |
| tick_s          | std_logic                       |             |
| load_en_s       | std_logic                       |             |
## Processes
- unnamed: ( clk )
## Instantiations

- gen_g1_inst: work.cacode_g1_gen
- gen_g2_inst: work.cacode_g2_gen
