# Entity: dv_ctrl

- **File**: dv_random.v
## Diagram

![Diagram](dv_random.svg "Diagram")
## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| N            |      | 5000  |             |
## Ports

| Port name      | Direction | Type   | Description            |
| -------------- | --------- | ------ | ---------------------- |
| nreset         | input     |        | async active low reset |
| clk            | input     |        | main clock             |
| output [N-1:0] | input     | [15:0] |                        |
| test_done      | input     |        | test is done           |
## Signals

| Name   | Type | Description          |
| ------ | ---- | -------------------- |
| nreset | reg  | signal declarations  |
| clk    | reg  |                      |
| start  | reg  |                      |
## Processes
- unnamed: ( @* )
  - **Type:** always
</br>**Description**
finish circuitry 
- unnamed: (  )
  - **Type:** always
</br>**Description**
Clock generator 
