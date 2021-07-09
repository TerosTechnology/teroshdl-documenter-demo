# Entity: crc32_tx

## Diagram

![Diagram](crc32_tx.svg "Diagram")
## Ports

| Port name | Direction | Type       | Description |
| --------- | --------- | ---------- | ----------- |
| rst       | input     | wire       |             |
| clk       | input     | wire       |             |
| crc_en    | input     | wire       |             |
| data_in   | input     | wire [3:0] |             |
| crc_out   | output    | [31:0]     |             |
## Signals

| Name      | Type       | Description |
| --------- | ---------- | ----------- |
| idx       | wire [3:0] |             |
| crc_table | reg [31:0] |             |
## Processes
- unnamed: ( @(*) )
- unnamed: ( @(posedge clk) )
