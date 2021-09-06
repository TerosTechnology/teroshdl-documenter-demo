# Entity: tsf_timer

- **File**: tsf_timer.v
## Diagram

![Diagram](tsf_timer.svg "Diagram")
## Description

 Xianjun jiao. putaoshu@msn.com; xianjun.jiao@imec.be;

## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| TIMER_WIDTH  | integer | 64    |             |
## Ports

| Port name        | Direction | Type                        | Description                               |
| ---------------- | --------- | --------------------------- | ----------------------------------------- |
| clk              | input     | wire                        |                                           |
| rstn             | input     | wire                        |                                           |
| tsf_load_control | input     | wire                        | rising edge will load load_val into timer |
| tsf_load_val     | input     | wire  [(TIMER_WIDTH-1) : 0] |                                           |
| tsf_runtime_val  | output    | [(TIMER_WIDTH-1) : 0]       |                                           |
| tsf_pulse_1M     | output    |                             |                                           |
## Signals

| Name                 | Type      | Description |
| -------------------- | --------- | ----------- |
| counter_1M           | reg [7:0] |             |
| tsf_load_control_reg | reg       |             |
## Processes
- unnamed: ( @( posedge clk ) )
  - **Type:** always
