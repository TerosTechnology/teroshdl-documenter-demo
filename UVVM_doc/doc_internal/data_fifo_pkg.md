# Package: data_fifo_pkg

- **File**: data_fifo_pkg.vhd
## Functions
- uvvm_fifo_init <font id="function_arguments">( buffer_idx            : natural;<br><span style="padding-left:20px"> buffer_size_in_bits   : natural ) </font> <font id="function_return">return ()</font>
**Description**
----------------------------------------
 uvvm_fifo_init
----------------------------------------
 This procedure allocates space in the buffer at the given buffer_idx.

  - Parameters:
        - buffer_idx                    - The index of the FIFO (natural)
                                          that shall be initialized.
        - buffer_size_in_bits (natural) - The size of the FIFO


- uvvm_fifo_put <font id="function_arguments">( buffer_idx        : natural;<br><span style="padding-left:20px"> data              : std_logic_vector ) </font> <font id="function_return">return ()</font>
**Description**
----------------------------------------
 uvvm_fifo_put
----------------------------------------
 This procedure puts data into a FIFO with index buffer_idx.
 The size of the data is unconstrained, meaning that
 it can be any size. Pushing data with a size that is
 larger than the FIFO size results in wrapping, i.e.,
 that when reaching the end the data remaining will over-
 write the data that was written first.

  - Parameters:
        - buffer_idx - The index of the FIFO (natural)
                       that shall be pushed to.
        - data       - The data that shall be pushed (slv)


- uvvm_fifo_flush <font id="function_arguments">( buffer_idx            : natural ) </font> <font id="function_return">return ()</font>
**Description**
----------------------------------------
 uvvm_fifo_flush
----------------------------------------
 This procedure empties the FIFO given
 by buffer_idx.

  - Parameters:
        - buffer_idx - The index of the FIFO (natural)
                       that shall be flushed.


- uvvm_fifo_deallocate <font id="function_arguments">( dummy : t_void ) </font> <font id="function_return">return ()</font>
**Description**
----------------------------------------
 uvvm_fifo_deallocate
----------------------------------------
 This procedure deallocates all the FIFOs
 in the buffer.


