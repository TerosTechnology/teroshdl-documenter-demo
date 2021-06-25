# Entity: ocram_sdp
## Diagram
![Diagram](ocram_sdp.svg "Diagram")
## Generics
| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| A_BITS       | positive |       |             |
| D_BITS       | positive |       |             |
| FILENAME     | string   | ""    |             |
## Ports
| Port name | Direction | Type                                | Description |
| --------- | --------- | ----------------------------------- | ----------- |
| rclk      | in        | std_logic                           |             |
| rce       | in        | std_logic                           |             |
| wclk      | in        | std_logic                           |             |
| wce       | in        | std_logic                           |             |
| we        | in        | std_logic                           |             |
| ra        | in        | unsigned(A_BITS-1 downto 0)         |             |
| wa        | in        | unsigned(A_BITS-1 downto 0)         |             |
| d         | in        | std_logic_vector(D_BITS-1 downto 0) |             |
| q         | out       | std_logic_vector(D_BITS-1 downto 0) |             |
## Constants
| Name  | Type     | Value      | Description |
| ----- | -------- | ---------- | ----------- |
| DEPTH | positive |  2**A_BITS |             |
