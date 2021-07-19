# Package: axi_slave_private_pkg

- **File**: axi_slave_private_pkg.vhd
## Types

| Name                | Type                                                           | Description |
| ------------------- | -------------------------------------------------------------- | ----------- |
| axi_burst_t         |                                                                |             |
| axi_slave_type_t    | (write_slave,<br><span style="padding-left:20px"> read_slave)  |             |
| axi_slave_private_t |                                                                |             |
## Functions
- main_loop <font id="function_arguments">(variable self : inout axi_slave_private_t;<br><span style="padding-left:20px"> signal net : inout network_t) </font> <font id="function_return">return ()</font>
- check_axi_resp <font id="function_arguments">(bus_handle : bus_master_t;<br><span style="padding-left:20px"> got,<br><span style="padding-left:20px"> expected : axi_resp_t;<br><span style="padding-left:20px"> msg : string) </font> <font id="function_return">return ()</font>
