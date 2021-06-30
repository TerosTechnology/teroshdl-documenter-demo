# Entity: spi

## Diagram

![Diagram](spi.svg "Diagram")
## Ports

| Port name | Direction | Type      | Description |
| --------- | --------- | --------- | ----------- |
| clock     | input     | wire      |             |
| ce        | input     | wire      |             |
| tx        | input     | wire      |             |
| rx        | input     | wire      |             |
| d         | input     | wire[7:0] |             |
| q         | output    | wire[7:0] |             |
| ck        | output    | wire      |             |
| miso      | input     | wire      |             |
| mosi      | output    | wire      |             |
## Signals

| Name  | Type     | Description |
| ----- | -------- | ----------- |
| md    | reg[7:0] |             |
| sd    | reg[7:0] |             |
| count | reg[4:0] |             |
## Processes
- unnamed: ( @(posedge clock) )
