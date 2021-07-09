# Entity: cacode_g1_gen

## Diagram

![Diagram](cacode_g1_gen.svg "Diagram")
## Ports

| Port name | Direction | Type                         | Description |
| --------- | --------- | ---------------------------- | ----------- |
| clk       | in        | std_logic                    |             |
| reset     | in        | std_logic                    |             |
| tick_i    | in        | std_logic                    |             |
| prn_o     | out       | std_logic_vector(9 downto 0) | start       |
| bit_o     | out       | std_logic                    |             |
## Signals

| Name         | Type                         | Description |
| ------------ | ---------------------------- | ----------- |
| lfsr_s       | std_logic_vector(9 downto 0) |             |
|  lfsr_next_s | std_logic_vector(9 downto 0) |             |
| xor9_2       | std_logic                    |             |
## Processes
- unnamed: ( clk )
