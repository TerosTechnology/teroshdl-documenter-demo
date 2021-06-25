# Entity: tb_wishbone_master
## Diagram
![Diagram](tb_wishbone_master.svg "Diagram")
## Generics
| Generic name   | Type   | Value | Description |
| -------------- | ------ | ----- | ----------- |
| runner_cfg     | string |       |             |
| encoded_tb_cfg | string |       |             |
## Signals
| Name  | Type                                             | Description |
| ----- | ------------------------------------------------ | ----------- |
| clk   | std_logic                                        |             |
| adr   | std_logic_vector(tb_cfg.adr_width-1 downto 0)    |             |
| dat_i | std_logic_vector(tb_cfg.dat_width-1 downto 0)    |             |
| dat_o | std_logic_vector(tb_cfg.dat_width-1 downto 0)    |             |
| sel   | std_logic_vector(tb_cfg.dat_width/8 -1 downto 0) |             |
| cyc   | std_logic                                        |             |
| stb   | std_logic                                        |             |
| we    | std_logic                                        |             |
| stall | std_logic                                        |             |
| ack   | std_logic                                        |             |
## Constants
| Name           | Type             | Value                                                                                                                                       | Description |
| -------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| tb_cfg         | tb_cfg_t         |  decode(encoded_tb_cfg)                                                                                                                     |             |
| master_logger  | logger_t         |  get_logger("master")                                                                                                                       |             |
| tb_logger      | logger_t         |  get_logger("tb")                                                                                                                           |             |
| bus_handle     | bus_master_t     |  new_bus(data_length => tb_cfg.dat_width,       address_length => tb_cfg.adr_width, logger => master_logger)                                |             |
| memory         | memory_t         |  new_memory                                                                                                                                 |             |
| buf            | buffer_t         |  allocate(memory, tb_cfg.num_cycles * sel'length)                                                                                           |             |
| wishbone_slave | wishbone_slave_t |  new_wishbone_slave(     memory => memory,     ack_high_probability => tb_cfg.ack_prob,     stall_high_probability => tb_cfg.stall_prob   ) |             |
## Types
| Name     | Type | Description |
| -------- | ---- | ----------- |
| tb_cfg_t |      |             |
## Functions
## Processes
- main_stim: _(  )_

## Instantiations
- dut: work.wishbone_master
