# Entity: rom

- **File**: rom.v
## Diagram

![Diagram](rom.svg "Diagram")
## Description

-------------------------------------------------------------------------------------------------

## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| KB           |      | 0     |             |
| FN           |      | ""    |             |
## Ports

| Port name | Direction | Type                      | Description |
| --------- | --------- | ------------------------- | ----------- |
| clock     | input     | wire                      |             |
| ce        | input     | wire                      |             |
| q         | output    | [                7:0]     |             |
| a         | input     | wire[$clog2(KB*1024)-1:0] |             |
## Signals

| Name | Type     | Description                                                                                         |
| ---- | -------- | --------------------------------------------------------------------------------------------------- |
| rom  | reg[7:0] | -------------------------------------------------------------------------------------------------  |
## Processes
- unnamed: ( @(posedge clock) )
  - **Type:** always
