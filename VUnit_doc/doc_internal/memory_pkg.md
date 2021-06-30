# Package: memory_pkg

## Constants

| Name          | Type     | Value                                                                                                                                                                                                                                      | Description           |
| ------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------- |
| null_memory   | memory_t |  (p_logger => null_logger,                                       p_check_permissions => boolean'low,                                       p_default_endian => endianness_t'low,                                       others => null_ptr) |                       |
| memory_logger | logger_t |  get_logger("vunit_lib:memory_pkg")                                                                                                                                                                                                        | Default memory logger |
| null_buffer   | buffer_t |  (p_memory_ref => null_memory,                                       p_name => null_string_ptr,                                       p_address => natural'low,                                       p_num_bytes => natural'low)          |                       |
## Types

| Name             | Type                                                | Description                                      |
| ---------------- | --------------------------------------------------- | ------------------------------------------------ |
| endianness_arg_t | (little_endian, big_endian, default_endian)         |                                                  |
| memory_t         |                                                     | Memory model object                              |
| permissions_t    | (no_access, write_only, read_only, read_and_write)  |                                                  |
| buffer_t         |                                                     | Reference to an allocated buffer with the memory |
## Functions
- clear <font id="function_arguments">(memory : memory_t) </font> <font id="function_return">return ()</font>
**Description**
Empties the memory by removing all data and permissions
- write_byte <font id="function_arguments">(memory : memory_t; address : natural; byte : byte_t) </font> <font id="function_return">return ()</font>
- write_word <font id="function_arguments">(memory : memory_t; address : natural; word : std_logic_vector; endian : endianness_arg_t := default_endian) </font> <font id="function_return">return ()</font>
- write_integer <font id="function_arguments">(memory : memory_t; address : natural; word : integer; bytes_per_word : natural range 1 to 4 := 4; endian : endianness_arg_t := default_endian) </font> <font id="function_return">return ()</font>
**Description**
Write integer
- set_permissions <font id="function_arguments">(memory : memory_t; address : natural; permissions : permissions_t) </font> <font id="function_return">return ()</font>
- clear_expected_byte <font id="function_arguments">(memory : memory_t; address : natural) </font> <font id="function_return">return ()</font>
- set_expected_byte <font id="function_arguments">(memory : memory_t; address : natural; expected : byte_t) </font> <font id="function_return">return ()</font>
- set_expected_word <font id="function_arguments">(memory : memory_t; address : natural; expected : std_logic_vector; endian : endianness_arg_t := default_endian) </font> <font id="function_return">return ()</font>
- set_expected_integer <font id="function_arguments">(memory : memory_t; address : natural; expected : integer; bytes_per_word : natural range 1 to 4 := 4; endian : endianness_arg_t := default_endian) </font> <font id="function_return">return ()</font>
- check_expected_was_written <font id="function_arguments">(memory : memory_t; address : natural; num_bytes : natural) </font> <font id="function_return">return ()</font>
**Description**
Check that all expected bytes within address range was writtenwith correct value
- check_expected_was_written <font id="function_arguments">(memory : memory_t) </font> <font id="function_return">return ()</font>
**Description**
Check that all expected bytes within the entire memory was writtenwith correct value
- check_expected_was_written <font id="function_arguments">(buf : buffer_t) </font> <font id="function_return">return ()</font>
**Description**
Check that all expected bytes was written with correct value in buffer
- write_byte_unchecked <font id="function_arguments">(memory : memory_t; address : natural; byte : byte_t) </font> <font id="function_return">return ()</font>
**Description**
Perform write of one byte without running any address or data checks
