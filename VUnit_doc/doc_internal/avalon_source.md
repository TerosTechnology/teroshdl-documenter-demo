# Entity: avalon_source
## Diagram
![Diagram](avalon_source.svg "Diagram")
## Generics
| Generic name | Type            | Value | Description |
| ------------ | --------------- | ----- | ----------- |
| source       | avalon_source_t |       |             |
## Ports
| Port name | Direction | Type                                             | Description |
| --------- | --------- | ------------------------------------------------ | ----------- |
| clk       | in        | std_logic                                        |             |
| ready     | in        | std_logic                                        |             |
| valid     | out       | std_logic                                        |             |
| sop       | out       | std_logic                                        |             |
| eop       | out       | std_logic                                        |             |
| data      | out       | std_logic_vector(data_length(source)-1 downto 0) |             |
## Processes
- main: _(  )_

