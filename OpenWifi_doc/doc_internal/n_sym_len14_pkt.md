# Entity: n_sym_len14_pkt

- **File**: n_sym_len14_pkt.v
## Diagram

![Diagram](n_sym_len14_pkt.svg "Diagram")
## Description

Xianjun jiao. putaoshu@msn.com; xianjun.jiao@imec.be;
 
## Ports

| Port name | Direction | Type       | Description |
| --------- | --------- | ---------- | ----------- |
| ht_flag   | input     | wire       |             |
| rate_mcs  | input     | wire [3:0] |             |
| n_sym     | output    | wire [2:0] |             |
## Signals

| Name                 | Type      | Description |
| -------------------- | --------- | ----------- |
| num_data_ofdm_symbol | reg [2:0] |             |
## Processes
- unnamed: ( @( ht_flag, rate_mcs ) )
