# Package: integer_vector_ptr_pool_pkg

- **File**: integer_vector_ptr_pool_pkg.vhd
## Constants

| Name                         | Type                      | Value                   | Description |
| ---------------------------- | ------------------------- | ----------------------- | ----------- |
| null_integer_vector_ptr_pool | integer_vector_ptr_pool_t |  (others => null_queue) |             |
## Types

| Name                      | Type | Description |
| ------------------------- | ---- | ----------- |
| integer_vector_ptr_pool_t |      |             |
## Functions
- recycle <font id="function_arguments">( pool         : integer_vector_ptr_pool_t;<br><span style="padding-left:20px"> variable ptr : inout integer_vector_ptr_t ) </font> <font id="function_return">return ()</font>
