# Entity: keyboard

- **File**: keyboard.v
## Diagram

![Diagram](keyboard.svg "Diagram")
## Ports

| Port name | Direction | Type      | Description |
| --------- | --------- | --------- | ----------- |
| clock     | input     | wire      |             |
| pressed   | input     | wire      |             |
| strobe    | input     | wire      |             |
| code      | input     | wire[7:0] |             |
| f6        | output    |           |             |
| f5        | output    |           |             |
| q         | output    | wire[4:0] |             |
| a         | input     | wire[7:0] |             |
## Signals

| Name | Type     | Description |
| ---- | -------- | ----------- |
| key  | reg[4:0] |             |
## Processes
- unnamed: ( @(posedge clock) )
