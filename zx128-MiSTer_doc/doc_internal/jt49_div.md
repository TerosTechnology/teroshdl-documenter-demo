# Entity: jt49_div

- **File**: jt49_div.v
## Diagram

![Diagram](jt49_div.svg "Diagram")
## Description

 Th
 
## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| W            |      | 12    |             |
## Ports

| Port name | Direction | Type        | Description                                  |
| --------- | --------- | ----------- | -------------------------------------------- |
| clk       | input     | wire        | this is the divided down clock from the core |
| cen       | input     | wire        |                                              |
| rst_n     | input     | wire        |                                              |
| period    | input     | wire[W-1:0] |                                              |
| div       | output    |             |                                              |
## Signals

| Name  | Type         | Description |
| ----- | ------------ | ----------- |
| count | reg [W-1:0]  |             |
| one   | wire [W-1:0] |             |
## Processes
- unnamed: ( @(posedge clk, negedge rst_n ) )
