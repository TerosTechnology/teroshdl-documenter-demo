# Entity: tb_ram_master
## Diagram
![Diagram](tb_ram_master.svg "Diagram")
## Generics
| Generic name | Type   | Value | Description |
| ------------ | ------ | ----- | ----------- |
| runner_cfg   | string |       |             |
## Signals
| Name  | Type                          | Description |
| ----- | ----------------------------- | ----------- |
| clk   | std_logic                     |             |
| en    | std_logic                     |             |
| we    | std_logic_vector(3 downto 0)  |             |
| addr  | std_logic_vector(7 downto 0)  |             |
| wdata | std_logic_vector(31 downto 0) |             |
| rdata | std_logic_vector(31 downto 0) |             |
| start | boolean                       |             |
|  done | boolean                       |             |
## Constants
| Name                   | Type         | Value                                                                | Description |
| ---------------------- | ------------ | -------------------------------------------------------------------- | ----------- |
| latency                | integer      |  2                                                                   |             |
| num_back_to_back_reads | integer      |  64                                                                  |             |
| bus_handle             | bus_master_t |  new_bus(data_length => wdata'length, address_length => addr'length) |             |
## Processes
- main: _(  )_

- support: _(  )_

## Instantiations
- dut: work.ram_master
