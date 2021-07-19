# Entity: ram

- **File**: ram.v
## Diagram

![Diagram](ram.svg "Diagram")
## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| KB           |      | 0     |             |
## Ports

| Port name | Direction | Type                      | Description |
| --------- | --------- | ------------------------- | ----------- |
| clock     | input     | wire                      |             |
| ce        | input     | wire                      |             |
| we        | input     | wire                      |             |
| d         | input     | wire[                7:0] |             |
| q         | output    | [                7:0]     |             |
| a         | input     | wire[$clog2(KB*1024)-1:0] |             |
## Signals

| Name | Type     | Description |
| ---- | -------- | ----------- |
| ram  | reg[7:0] |             |
## Processes
- unnamed: ( @(posedge clock) )
