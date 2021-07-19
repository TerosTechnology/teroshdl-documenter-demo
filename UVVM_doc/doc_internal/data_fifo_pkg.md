# Package: data_fifo_pkg

- **File**: data_fifo_pkg.vhd
## Functions
- uvvm_fifo_init <font id="function_arguments">( buffer_idx            : natural;<br><span style="padding-left:20px"> buffer_size_in_bits   : natural ) </font> <font id="function_return">return ()</font>
- uvvm_fifo_put <font id="function_arguments">( buffer_idx        : natural;<br><span style="padding-left:20px"> data              : std_logic_vector ) </font> <font id="function_return">return ()</font>
- uvvm_fifo_flush <font id="function_arguments">( buffer_idx            : natural ) </font> <font id="function_return">return ()</font>
- uvvm_fifo_deallocate <font id="function_arguments">( dummy : t_void ) </font> <font id="function_return">return ()</font>
