# Package: axi_statistics_pkg

## Constants

| Name                | Type             | Value                                  | Description |
| ------------------- | ---------------- | -------------------------------------- | ----------- |
| null_axi_statistics | axi_statistics_t |  (p_count_by_burst_length => null_ptr) |             |
## Types

| Name             | Type | Description |
| ---------------- | ---- | ----------- |
| axi_statistics_t |      |             |
## Functions
- deallocate <font id="function_arguments">(variable stat : inout axi_statistics_t) </font> <font id="function_return">return ()</font>
**Description**
Free dynamically allocated memory
- add_burst_length <font id="function_arguments">(stat : axi_statistics_t;<br><span style="padding-left:20px"> burst_length : natural) </font> <font id="function_return">return ()</font>
- clear <font id="function_arguments">(stat : axi_statistics_t) </font> <font id="function_return">return ()</font>
