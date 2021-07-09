# Entity: add_constReal_synchronizer_vector

## Diagram

![Diagram](add_constReal_synchronizer_vector.svg "Diagram")
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| stages       | natural | 3     |             |
| DATA         | natural | 16    |             |
## Ports

| Port name | Direction | Type                              | Description |
| --------- | --------- | --------------------------------- | ----------- |
| clk_i     | in        | std_logic                         |             |
| bit_i     | in        | std_logic_vector(DATA-1 downto 0) |             |
| bit_o     | out       | std_logic_vector(DATA-1 downto 0) |             |
## Signals

| Name      | Type                         | Description |
| --------- | ---------------------------- | ----------- |
| flipflops | data_tab(stages -1 downto 0) |             |
## Types

| Name     | Type                                                           | Description |
| -------- | -------------------------------------------------------------- | ----------- |
| data_tab | array (natural range <>) of std_logic_vector(DATA-1 downto 0)  |             |
## Processes
- sync_proc: ( clk_i )
