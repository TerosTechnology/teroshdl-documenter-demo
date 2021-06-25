# Entity: sobel_x
## Diagram
![Diagram](sobel_x.svg "Diagram")
## Generics
| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| data_width   | natural |       |             |
## Ports
| Port name     | Direction | Type                            | Description |
| ------------- | --------- | ------------------------------- | ----------- |
| clk           | in        | std_logic                       |             |
| input_tvalid  | in        | std_logic                       |             |
| input_tlast   | in        | std_logic                       |             |
| input_tdata   | in        | unsigned(data_width-1 downto 0) |             |
| output_tvalid | out       | std_logic                       |             |
| output_tlast  | out       | std_logic                       |             |
| output_tdata  | out       | signed(data_width downto 0)     |             |
## Processes
- main: _(  )_

