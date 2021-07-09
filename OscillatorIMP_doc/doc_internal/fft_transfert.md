# Entity: fft_transfert

## Diagram

![Diagram](fft_transfert.svg "Diagram")
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| ADDR_SIZE    | natural | 10    |             |
| DATA_SIZE    | natural | 32    |             |
## Ports

| Port name       | Direction | Type                                   | Description    |
| --------------- | --------- | -------------------------------------- | -------------- |
| clk_i           | in        | std_logic                              | Syscon signals |
| rst_i           | in        | std_logic                              |                |
| transmit_en_o   | in        | std_logic                              |                |
| done_transmit_o | out       | std_logic                              |                |
| res_re_i        | in        | std_logic_vector(DATA_SIZE-1 downto 0) | in             |
| res_im_i        | in        | std_logic_vector(DATA_SIZE-1 downto 0) |                |
| res_addr_o      | out       | std_logic_vector(ADDR_SIZE-1 downto 0) |                |
| res_re_o        | out       | std_logic_vector(DATA_SIZE-1 downto 0) | results        |
| res_im_o        | out       | std_logic_vector(DATA_SIZE-1 downto 0) |                |
| res_en_o        | out       | std_logic                              |                |
## Signals

| Name          | Type                                   | Description |
| ------------- | -------------------------------------- | ----------- |
| result_addr_s | std_logic_vector(ADDR_SIZE-1 downto 0) |             |
| transmit_en_s | std_logic                              |             |
|  old_tx_en_s  | std_logic                              |             |
| tx_en_s       | std_logic                              |             |
## Processes
- unnamed: ( clk_i )
