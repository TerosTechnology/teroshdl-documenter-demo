# Entity: tb_axi_lite_master
## Diagram
![Diagram](tb_axi_lite_master.svg "Diagram")
## Generics
| Generic name | Type   | Value | Description |
| ------------ | ------ | ----- | ----------- |
| runner_cfg   | string |       |             |
## Signals
| Name    | Type                          | Description |
| ------- | ----------------------------- | ----------- |
| clk     | std_logic                     |             |
| arready | std_logic                     |             |
| arvalid | std_logic                     |             |
| araddr  | std_logic_vector(31 downto 0) |             |
| rready  | std_logic                     |             |
| rvalid  | std_logic                     |             |
| rdata   | std_logic_vector(15 downto 0) |             |
| rresp   | std_logic_vector(1 downto 0)  |             |
| awready | std_logic                     |             |
| awvalid | std_logic                     |             |
| awaddr  | std_logic_vector(31 downto 0) |             |
| wready  | std_logic                     |             |
| wvalid  | std_logic                     |             |
| wdata   | std_logic_vector(15 downto 0) |             |
| wstrb   | std_logic_vector(1 downto 0)  |             |
| bvalid  | std_logic                     |             |
| bready  | std_logic                     |             |
| bresp   | std_logic_vector(1 downto 0)  |             |
| start   | boolean                       |             |
|  done   | boolean                       |             |
## Constants
| Name             | Type         | Value                                                                                                                  | Description |
| ---------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------- | ----------- |
| num_random_tests | integer      |  128                                                                                                                   |             |
| bus_handle       | bus_master_t |  new_bus(data_length => wdata'length,                                                 address_length => awaddr'length) |             |
## Processes
- main: _(  )_

- support: _(  )_

## Instantiations
- dut: work.axi_lite_master
