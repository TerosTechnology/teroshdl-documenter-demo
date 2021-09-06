# Entity: dv_top

- **File**: dv_stimulus.v
## Diagram

![Diagram](dv_stimulus.svg "Diagram")
## Generics

| Generic name | Type | Value | Description            |
| ------------ | ---- | ----- | ---------------------- |
| DW           |      | 64    |  Memory width          |
| MAW          |      | 15    |  Memory address width  |
## Signals

| Name        | Type          | Description                  |
| ----------- | ------------- | ---------------------------- |
| filename    | reg [1023:0]  | regs/wires                   |
| ext_packet  | wire [DW-1:0] |                              |
| nreset      | wire          | From dv_ctrl of dv_ctrl.v    |
| start       | wire          | From dv_ctrl of dv_ctrl.v    |
| stim_access | wire          | From stimulus of stimulus.v  |
| stim_done   | wire          | From stimulus of stimulus.v  |
| stim_packet | wire [DW-1:0] | From stimulus of stimulus.v  |
| vdd         | wire          | From dv_ctrl of dv_ctrl.v    |
| vss         | wire          | From dv_ctrl of dv_ctrl.v    |
## Instantiations

- dv_ctrl: dv_ctrl
</br>**Description**
Reset and clocks

