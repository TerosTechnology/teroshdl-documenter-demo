# Entity: IDELAYCTRL

- **File**: IDELAYCTRL.v
## Diagram

![Diagram](IDELAYCTRL.svg "Diagram")
## Description

An empty IDELAYCTRL model*/

## Ports

| Port name | Direction | Type | Description                              |
| --------- | --------- | ---- | ---------------------------------------- |
| RDY       | output    |      | goes high when delay has been calibrated |
| REFCLK    | input     |      | reference clock for setting tap delay    |
| RST       | input     |      | reset pulse for setting                  |
## Signals

| Name | Type | Description |
| ---- | ---- | ----------- |
| RDY  | reg  |             |
## Processes
- unnamed: ( @ (posedge REFCLK or posedge RST) )
  - **Type:** always
