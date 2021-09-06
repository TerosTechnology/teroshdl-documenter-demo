# Entity: IBUFDS_INTERMDISABLE_INT

- **File**: IBUFDS_INTERMDISABLE_INT.v
## Diagram

![Diagram](IBUFDS_INTERMDISABLE_INT.svg "Diagram")
## Generics

| Generic name    | Type | Value      | Description         |
| --------------- | ---- | ---------- | ------------------- |
| LOC             |      | "UNPLACED" |                     |
| DIFF_TERM       |      | "FALSE"    |  `ifdef XIL_TIMING  |
| DQS_BIAS        |      | "FALSE"    |                     |
| IBUF_LOW_PWR    |      | "TRUE"     |                     |
| IOSTANDARD      |      | "DEFAULT"  |                     |
| USE_IBUFDISABLE |      | "TRUE"     |                     |
## Ports

| Port name     | Direction | Type | Description |
| ------------- | --------- | ---- | ----------- |
| O             | output    |      |             |
| I             | input     |      |             |
| IB            | input     |      |             |
| IBUFDISABLE   | input     |      |             |
| INTERMDISABLE | input     |      |             |
## Constants

| Name        | Type | Value                      | Description |
| ----------- | ---- | -------------------------- | ----------- |
| MODULE_NAME |      | "IBUFDS_INTERMDISABLE_INT" |             |
