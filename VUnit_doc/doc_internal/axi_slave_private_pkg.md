# Package: axi_slave_private_pkg

## Types

| Name                | Type                       | Description |
| ------------------- | -------------------------- | ----------- |
| axi_burst_t         |                            |             |
| axi_slave_type_t    | (write_slave, read_slave)  |             |
| axi_slave_private_t |                            |             |
## Functions
- main_loop <font id="function_arguments">(variable self : inout axi_slave_private_t; signal net : inout network_t) </font> <font id="function_return">return ()</font>
- check_axi_resp <font id="function_arguments">(bus_handle : bus_master_t; got, expected : axi_resp_t; msg : string) </font> <font id="function_return">return ()</font>
