# Package: memory_utils_pkg
## Functions
- write_integer_vector_ptr <font id="function_arguments">(memory : memory_t;                                     base_address : natural;
                                     integer_vector_ptr : integer_vector_ptr_t;
                                     bytes_per_word : natural range 1 to 4 := 4;
                                     endian : endianness_arg_t := default_endian)</font> <font id="function_return">return ()</font>
**Description**
Write integer vector pointer to memory address
- set_expected_integer_vector_ptr <font id="function_arguments">(memory : memory_t;                                            base_address : natural;
                                            integer_vector_ptr : integer_vector_ptr_t;
                                            bytes_per_word : natural range 1 to 4 := 4;
                                            endian : endianness_arg_t := default_endian)</font> <font id="function_return">return ()</font>
**Description**
Set expected integer vector pointer data at memory address
- write_integer_array <font id="function_arguments">(memory : memory_t;                                base_address : natural;
                                integer_array : integer_array_t;
                                stride_in_bytes : natural := 0;  0 stride means use image width
                                endian : endianness_arg_t := default_endian)</font> <font id="function_return">return ()</font>
**Description**
Write integer array to memory address
- set_expected_integer_array <font id="function_arguments">(memory : memory_t;                                       base_address : natural;
                                       integer_array : integer_array_t;
                                       stride_in_bytes : natural := 0;  0 stride means use image width
                                       endian : endianness_arg_t := default_endian)</font> <font id="function_return">return ()</font>
**Description**
Set integer_array as expected data
