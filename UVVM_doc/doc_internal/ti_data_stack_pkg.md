# Package: ti_data_stack_pkg

- **File**: ti_data_stack_pkg.vhd
## Functions
- uvvm_stack_init <font id="function_arguments">( buffer_index          : natural;<br><span style="padding-left:20px"> buffer_size_in_bits   : natural ) </font> <font id="function_return">return ()</font>
</br>**Description**
----------------------------------------
 uvvm_stack_init
----------------------------------------
 This procedure allocates space in the buffer at the given buffer_idx.

  - Parameters: 
        - buffer_idx                    - The index of the stack (natural)
                                          that shall be initialized.  
        - buffer_size_in_bits (natural) - The size of the stack


- uvvm_stack_push <font id="function_arguments">( buffer_index          : natural;<br><span style="padding-left:20px"> data                  : std_logic_vector ) </font> <font id="function_return">return ()</font>
</br>**Description**
----------------------------------------
 uvvm_stack_push
----------------------------------------
 This procedure puts data into a stack with index buffer_idx.
 The size of the data is unconstrained, meaning that 
 it can be any size. Pushing data with a size that is
 larger than the stack size results in wrapping, i.e.,
 that when reaching the end the data remaining will over-
 write the data that was written first.
 
  - Parameters: 
        - buffer_idx - The index of the stack (natural) 
                       that shall be pushed to.  
        - data       - The data that shall be pushed (slv)


- uvvm_stack_flush <font id="function_arguments">( buffer_index          : natural ) </font> <font id="function_return">return ()</font>
</br>**Description**
----------------------------------------
 uvvm_stack_flush
----------------------------------------
 This procedure empties the stack given
 by buffer_idx.

  - Parameters: 
        - buffer_idx - The index of the stack (natural)
                       that shall be flushed.


