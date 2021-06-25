# Entity: tb_avalon_slave
## Diagram
![Diagram](tb_avalon_slave.svg "Diagram")
## Generics
| Generic name   | Type   | Value | Description |
| -------------- | ------ | ----- | ----------- |
| runner_cfg     | string |       |             |
| encoded_tb_cfg | string |       |             |
## Signals
| Name          | Type                                                  | Description |
| ------------- | ----------------------------------------------------- | ----------- |
| clk           | std_logic                                             |             |
| address       | std_logic_vector(tb_cfg.address_width-1 downto 0)     |             |
| writedata     | std_logic_vector(tb_cfg.data_width-1 downto 0)        |             |
| readdata      | std_logic_vector(tb_cfg.data_width-1 downto 0)        |             |
| byteenable    | std_logic_vector(tb_cfg.data_width/8 -1 downto 0)     |             |
| burstcount    | std_logic_vector(tb_cfg.burstcount_width -1 downto 0) |             |
| write         | std_logic                                             |             |
| read          | std_logic                                             |             |
| waitrequest   | std_logic                                             |             |
| readdatavalid | std_logic                                             |             |
| wr_ack_cnt    | natural range 0 to tb_cfg.num_cycles                  |             |
| rd_ack_cnt    | natural range 0 to tb_cfg.num_cycles                  |             |
## Constants
| Name         | Type           | Value                                                                                                                                                                                                             | Description |
| ------------ | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| tb_cfg       | tb_cfg_t       |  decode(encoded_tb_cfg)                                                                                                                                                                                           |             |
| tb_logger    | logger_t       |  get_logger("tb")                                                                                                                                                                                                 |             |
| memory       | memory_t       |  new_memory                                                                                                                                                                                                       |             |
| buf          | buffer_t       |  allocate(memory, tb_cfg.num_cycles * byteenable'length)                                                                                                                                                          |             |
| avalon_slave | avalon_slave_t |        new_avalon_slave(memory => memory,         name => "avmm_vc",         readdatavalid_high_probability => tb_cfg.readdatavalid_prob,         waitrequest_high_probability => tb_cfg.waitrequest_prob       ) |             |
## Types
| Name     | Type | Description |
| -------- | ---- | ----------- |
| tb_cfg_t |      |             |
## Functions
## Processes
- main_stim: _(  )_

- rd_ack: _(  )_

## Instantiations
- dut_slave: work.avalon_slave
