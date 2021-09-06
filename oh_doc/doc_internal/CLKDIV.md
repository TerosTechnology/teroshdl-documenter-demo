# Entity: CLKDIV

- **File**: CLKDIV.v
## Diagram

![Diagram](CLKDIV.svg "Diagram")
## Ports

| Port name | Direction | Type  | Description                            |
| --------- | --------- | ----- | -------------------------------------- |
| clkin     | input     |       | Input clock                            |
| divcfg    | input     | [3:0] | Divide factor (1-128)                  |
| reset     | input     |       | Counter init                           |
| clkout    | output    |       | Divided clock phase aligned with clkin |
## Signals

| Name          | Type      | Description |
| ------------- | --------- | ----------- |
| clkout_reg    | reg       |             |
| counter       | reg [7:0] |             |
| divcfg_dec    | reg [7:0] |             |
| divcfg_reg    | reg [3:0] |             |
| div_bp        | wire      |             |
| posedge_match | wire      |             |
| negedge_match | wire      |             |
## Processes
- unnamed: ( @ (divcfg[3:0]) )
  - **Type:** always
</br>**Description**
 ###################  # Decode divcfg  ################### 
- unnamed: ( @ (posedge clkin or posedge reset) )
  - **Type:** always
- unnamed: ( @ (posedge clkin or posedge reset) )
  - **Type:** always
