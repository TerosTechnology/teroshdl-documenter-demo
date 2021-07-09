# Entity: switchReal_synch

## Diagram

![Diagram](switchReal_synch.svg "Diagram")
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| stages       | natural | 3     |             |
## Ports

| Port name | Direction | Type      | Description |
| --------- | --------- | --------- | ----------- |
| clk_i     | in        | std_logic |             |
| bit_i     | in        | std_logic |             |
| bit_o     | out       | std_logic |             |
## Signals

| Name      | Type                                 | Description |
| --------- | ------------------------------------ | ----------- |
| flipflops | std_logic_vector(stages -1 downto 0) |             |
## Processes
- sync_proc: ( clk_i )
