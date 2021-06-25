# Entity: axis_buffer
## Diagram
![Diagram](axis_buffer.svg "Diagram")
## Generics
| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| data_width   | integer | 32    |             |
| fifo_depth   | integer | 0     |             |
## Ports
| Port name    | Direction | Type                                        | Description |
| ------------ | --------- | ------------------------------------------- | ----------- |
| s_axis_clk   | in        | std_logic                                   |             |
| s_axis_rstn  | in        | std_logic                                   |             |
| s_axis_rdy   | out       | std_logic                                   |             |
| s_axis_data  | in        | std_logic_vector(data_width-1 downto 0)     |             |
| s_axis_valid | in        | std_logic                                   |             |
| s_axis_strb  | in        | std_logic_vector((data_width/8)-1 downto 0) |             |
| s_axis_last  | in        | std_logic                                   |             |
| m_axis_clk   | in        | std_logic                                   |             |
| m_axis_rstn  | in        | std_logic                                   |             |
| m_axis_valid | out       | std_logic                                   |             |
| m_axis_data  | out       | std_logic_vector(data_width-1 downto 0)     |             |
| m_axis_rdy   | in        | std_logic                                   |             |
| m_axis_strb  | out       | std_logic_vector((data_width/8)-1 downto 0) |             |
| m_axis_last  | out       | std_logic                                   |             |
## Signals
| Name   | Type                                               | Description |
| ------ | -------------------------------------------------- | ----------- |
| r      | std_logic                                          |             |
|  e     | std_logic                                          |             |
|  f     | std_logic                                          |             |
|  wr    | std_logic                                          |             |
|  rd    | std_logic                                          |             |
|  valid | std_logic                                          |             |
| d      | std_logic_vector(data_width+data_width/8 downto 0) |             |
|  q     | std_logic_vector(data_width+data_width/8 downto 0) |             |
## Processes
- unnamed: _( m_axis_clk )_

## Instantiations
- fifo: work.fifo
