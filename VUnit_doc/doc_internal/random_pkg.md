# Package: random_pkg
## Functions
- random_integer_vector_ptr <font id="function_arguments">(variable rnd : inout RandomPType;                                      variable integer_vector_ptr : inout integer_vector_ptr_t;
                                      length : natural;
                                      min_value : integer;
                                      max_value : integer)</font> <font id="function_return">return ()</font>
- random_integer_vector_ptr <font id="function_arguments">(variable rnd : inout RandomPType;                                      variable integer_vector_ptr : inout integer_vector_ptr_t;
                                      length : natural;
                                      bits_per_word : positive;
                                      is_signed : boolean)</font> <font id="function_return">return ()</font>
- random_integer_array <font id="function_arguments">(variable rnd : inout RandomPType;                                 variable integer_array : inout integer_array_t;
                                 width : natural := 1;
                                 height : natural := 1;
                                 depth : natural := 1;
                                 min_value : integer := 0;
                                 max_value : integer := 0)</font> <font id="function_return">return ()</font>
- random_integer_array <font id="function_arguments">(variable rnd : inout RandomPType;                                 variable integer_array : inout integer_array_t;
                                 width : natural := 1;
                                 height : natural := 1;
                                 depth : natural := 1;
                                 bits_per_word : integer := 1;
                                 is_signed : boolean := false)</font> <font id="function_return">return ()</font>
