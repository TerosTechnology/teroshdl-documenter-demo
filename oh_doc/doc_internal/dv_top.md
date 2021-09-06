# Entity: dv_top

- **File**: dv_top.v
## Diagram

![Diagram](dv_top.svg "Diagram")
## Generics

| Generic name | Type | Value   | Description       |
| ------------ | ---- | ------- | ----------------- |
| N            |      | 1       | static variables  |
| IDW          |      | 12      |                   |
| AW           |      | 32      |                   |
| PW           |      | 2*AW+40 |                   |
## Signals

| Name        | Type            | Description                    |
| ----------- | --------------- | ------------------------------ |
| r           | integer         | local variables                |
| dv_coreid   | wire [IDW-1:0]  |                                |
| vdd         | wire [N*N-1:0]  |                                |
| vss         | wire            |                                |
| clkout      | wire            |                                |
| dut_active  | wire            |                                |
| dut_wait    | wire [N-1:0]    |                                |
| dut_access  | wire [N-1:0]    |                                |
| dut_packet  | wire [N*PW-1:0] |                                |
| clk1        | wire            | From dv_ctrl of dv_ctrl.v      |
| clk2        | wire            | From dv_ctrl of dv_ctrl.v      |
| nreset      | wire            | From dv_ctrl of dv_ctrl.v      |
| start       | wire            | From dv_ctrl of dv_ctrl.v      |
| stim_access | wire [N-1:0]    | From dv_driver of dv_driver.v  |
| stim_done   | wire            | From dv_driver of dv_driver.v  |
| stim_packet | wire [N*PW-1:0] | From dv_driver of dv_driver.v  |
| stim_wait   | wire [N-1:0]    | From dv_driver of dv_driver.v  |
## Instantiations

- dv_ctrl: dv_ctrl
</br>**Description**
optimize later

