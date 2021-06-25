# Entity: fifo_glue
## Diagram
![Diagram](fifo_glue.svg "Diagram")
## Generics
| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| D_BITS       | positive |       |             |
## Ports
| Port name | Direction | Type                                | Description |
| --------- | --------- | ----------------------------------- | ----------- |
| clk       | in        | std_logic                           |             |
| rst       | in        | std_logic                           |             |
| put       | in        | std_logic                           |             |
| di        | in        | std_logic_vector(D_BITS-1 downto 0) |             |
| ful       | out       | std_logic                           |             |
| vld       | out       | std_logic                           |             |
| do        | out       | std_logic_vector(D_BITS-1 downto 0) |             |
| got       | in        | std_logic                           |             |
## Signals
| Name   | Type                                | Description |
| ------ | ----------------------------------- | ----------- |
| A      | std_logic_vector(D_BITS-1 downto 0) |             |
|  B     | std_logic_vector(D_BITS-1 downto 0) |             |
| Full   | std_logic                           |             |
|  Avail | std_logic                           |             |
## Processes
- unnamed: _( clk )_

