# Entity: sysid_rom

- **File**: sysid_rom.v
## Diagram

![Diagram](sysid_rom.svg "Diagram")
## Generics

| Generic name  | Type | Value                   | Description |
| ------------- | ---- | ----------------------- | ----------- |
| ROM_WIDTH     |      | 32                      |             |
| ROM_ADDR_BITS |      | 6                       |             |
| PATH_TO_FILE  |      | "path_to_mem_init_file" |             |
## Ports

| Port name | Direction | Type                | Description |
| --------- | --------- | ------------------- | ----------- |
| clk       | input     |                     |             |
| rom_addr  | input     | [ROM_ADDR_BITS-1:0] |             |
| rom_data  | output    | [ROM_WIDTH-1:0]     |             |
## Signals

| Name    | Type                | Description |
| ------- | ------------------- | ----------- |
| lut_rom | reg [ROM_WIDTH-1:0] |             |
## Processes
- unnamed: ( @(posedge clk) )
  - **Type:** always
