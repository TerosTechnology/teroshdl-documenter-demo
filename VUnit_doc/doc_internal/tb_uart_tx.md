# Entity: tb_uart_tx
## Diagram
![Diagram](tb_uart_tx.svg "Diagram")
## Generics
| Generic name | Type   | Value | Description |
| ------------ | ------ | ----- | ----------- |
| runner_cfg   | string |       |             |
## Signals
| Name   | Type                         | Description |
| ------ | ---------------------------- | ----------- |
| clk    | std_logic                    |             |
| tx     | std_logic                    |             |
| tready | std_logic                    |             |
| tvalid | std_Logic                    |             |
| tdata  | std_logic_vector(7 downto 0) |             |
## Constants
| Name           | Type                | Value                                                                                                                             | Description |
| -------------- | ------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| baud_rate      | integer             |  115200                                                                                                                           |             |
| clk_period     | integer             |  20                                                                                                                               |             |
| cycles_per_bit | integer             |  50 * 10**6 / baud_rate                                                                                                           |             |
| uart_bfm       | uart_slave_t        |  new_uart_slave(initial_baud_rate => baud_rate,                                                      data_length => tdata'length) |             |
| uart_stream    | stream_slave_t      |  as_stream(uart_bfm)                                                                                                              |             |
| axi_stream_bfm | axi_stream_master_t |  new_axi_stream_master(data_length => tdata'length)                                                                               |             |
| axi_stream     | stream_master_t     |  as_stream(axi_stream_bfm)                                                                                                        |             |
## Processes
- main: _(  )_

## Instantiations
- dut: uart_lib.uart_tx
- uart_slave_bfm: vunit_lib.uart_slave
- axi_stream_master_bfm: vunit_lib.axi_stream_master
