# Entity: IBUFDS_IBUFDISABLE

- **File**: IBUFDS_IBUFDISABLE.v
## Diagram

![Diagram](IBUFDS_IBUFDISABLE.svg "Diagram")
## Generics

| Generic name    | Type | Value      | Description         |
| --------------- | ---- | ---------- | ------------------- |
| LOC             |      | "UNPLACED" |                     |
| DIFF_TERM       |      | "FALSE"    |  `ifdef XIL_TIMING  |
| DQS_BIAS        |      | "FALSE"    |                     |
| IBUF_LOW_PWR    |      | "TRUE"     |                     |
| IOSTANDARD      |      | "DEFAULT"  |                     |
| SIM_DEVICE      |      | "7SERIES"  |                     |
| USE_IBUFDISABLE |      | "TRUE"     |                     |
## Ports

| Port name   | Direction | Type | Description |
| ----------- | --------- | ---- | ----------- |
| O           | output    |      |             |
| I           | input     |      |             |
| IB          | input     |      |             |
| IBUFDISABLE | input     |      |             |
## Constants

| Name        | Type | Value                | Description |
| ----------- | ---- | -------------------- | ----------- |
| MODULE_NAME |      | "IBUFDS_IBUFDISABLE" |             |
