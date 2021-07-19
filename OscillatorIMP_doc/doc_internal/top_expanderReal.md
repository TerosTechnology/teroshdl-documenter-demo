# Entity: top_expanderreal

- **File**: top_expanderReal.vhd
## Diagram

![Diagram](top_expanderReal.svg "Diagram")
## Ports

| Port name | Direction | Type                          | Description |
| --------- | --------- | ----------------------------- | ----------- |
| clk_i     | in        | std_logic                     |             |
| rst_i     | in        | std_logic                     |             |
| data_en_i | in        | std_logic                     | in          |
| data_i    | in        | std_logic_vector(15 downto 0) |             |
| data_o    | out       | std_logic_vector(7 downto 0)  | out         |
| data_en_o | out       | std_logic                     |             |
## Instantiations

- shift_same_inst: work.expanderReal
