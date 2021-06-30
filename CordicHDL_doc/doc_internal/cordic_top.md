# Entity: cordic_top

## Diagram

![Diagram](cordic_top.svg "Diagram")
## Description

 Standard library.
 Implementation of cordic.
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| g_MODE       | integer | 1     |             |
## Ports

| Port name  | Direction | Type                           | Description      |
| ---------- | --------- | ------------------------------ | ---------------- |
| clk        | in        | std_logic                      |  Clock.          |
| dv_in      | in        | std_logic                      |  Data valid in.  |
| data_0_in  | in        | std_logic_vector (19 downto 0) |  Data 0 in.      |
| data_1_in  | in        | std_logic_vector (19 downto 0) |  Data 1 in.      |
| data_0_out | out       | std_logic_vector (19 downto 0) |  Data 0 out.     |
| data_1_out | out       | std_logic_vector (19 downto 0) |  Data 1 out.     |
| dv_out     | out       | std_logic                      |  Data valid out. |
