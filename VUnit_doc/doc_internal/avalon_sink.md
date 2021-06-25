# Entity: avalon_sink
## Diagram
![Diagram](avalon_sink.svg "Diagram")
## Generics
| Generic name | Type          | Value | Description |
| ------------ | ------------- | ----- | ----------- |
| sink         | avalon_sink_t |       |             |
## Ports
| Port name | Direction | Type                                           | Description |
| --------- | --------- | ---------------------------------------------- | ----------- |
| clk       | in        | std_logic                                      |             |
| ready     | out       | std_logic                                      |             |
| valid     | in        | std_logic                                      |             |
| sop       | in        | std_logic                                      |             |
| eop       | in        | std_logic                                      |             |
| data      | in        | std_logic_vector(data_length(sink)-1 downto 0) |             |
## Processes
- main: _(  )_

