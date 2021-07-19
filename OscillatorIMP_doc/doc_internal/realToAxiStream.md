# Entity: realToAxiStream

- **File**: realToAxiStream.vhd
## Diagram

![Diagram](realToAxiStream.svg "Diagram")
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| DATA_SIZE    | natural | 32    |             |
## Ports

| Port name       | Direction | Type                                   | Description |
| --------------- | --------- | -------------------------------------- | ----------- |
| data_i          | in        | std_logic_vector(DATA_SIZE-1 downto 0) | input data  |
| data_en_i       | in        | std_logic                              |             |
| data_clk_i      | in        | std_logic                              |             |
| data_rst_i      | in        | std_logic                              |             |
| m00_axis_aclk   | in        | std_logic                              | output data |
| m00_axis_tdata  | out       | std_logic_vector(DATA_SIZE-1 downto 0) |             |
| m00_axis_tready | in        | std_logic                              |             |
| m00_axis_tvalid | out       | std_logic                              |             |
