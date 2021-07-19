# Entity: cplx_conj

- **File**: cplx_conj.v
## Diagram

![Diagram](cplx_conj.svg "Diagram")
## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| DATA_SIZE    |      | 16    |             |
## Ports

| Port name  | Direction | Type            | Description |
| ---------- | --------- | --------------- | ----------- |
| data_i_i   | input     | [DATA_SIZE-1:0] | input data  |
| data_q_i   | input     | [DATA_SIZE-1:0] |             |
| data_en_i  | input     |                 |             |
| data_sof_i | input     |                 |             |
| data_eof_i | input     |                 |             |
| data_rst_i | input     |                 |             |
| data_clk_i | input     |                 |             |
| data_i_o   | output    | [DATA_SIZE-1:0] | output data |
| data_q_o   | output    | [DATA_SIZE-1:0] |             |
| data_en_o  | output    |                 |             |
| data_sof_o | output    |                 |             |
| data_eof_o | output    |                 |             |
| data_rst_o | output    |                 |             |
| data_clk_o | output    |                 |             |
