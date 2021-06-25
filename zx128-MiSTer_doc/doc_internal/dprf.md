# Entity: dprf
## Diagram
![Diagram](dprf.svg "Diagram")
## Generics
| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| KB           |      | 0     |             |
## Ports
| Port name | Direction | Type                      | Description |
| --------- | --------- | ------------------------- | ----------- |
| clock     | input     | wire                      |             |
| ce1       | input     | wire                      |             |
| q1        | output    | [                7:0]     |             |
| a1        | input     | wire[$clog2(KB*1024)-1:0] |             |
| ce2       | input     | wire                      |             |
| we2       | input     | wire                      |             |
| d2        | input     | wire[                7:0] |             |
| q2        | output    | [                7:0]     |             |
| a2        | input     | wire[$clog2(KB*1024)-1:0] |             |
## Signals
| Name | Type     | Description |
| ---- | -------- | ----------- |
| dpr  | reg[7:0] |             |
## Processes
- unnamed: _( @(posedge clock) )_

- unnamed: _( @(posedge clock) )_

