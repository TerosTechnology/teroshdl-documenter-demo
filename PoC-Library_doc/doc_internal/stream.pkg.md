# Package: stream
## Constants
| Name                              | Type                       | Value                                                                                                                                                                                        | Description |
| --------------------------------- | -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| C_SIM_STREAM_MAX_PATTERN_COUNT    | positive                   |  128                                                                                                                                                                                         |             |
| C_SIM_STREAM_MAX_FRAMEGROUP_COUNT | positive                   |  8                                                                                                                                                                                           |             |
| C_SIM_STREAM_WORD_INDEX_BW        | positive                   |  log2ceilnz(C_SIM_STREAM_MAX_PATTERN_COUNT)                                                                                                                                                  |             |
| C_SIM_STREAM_FRAMEGROUP_INDEX_BW  | positive                   |  log2ceilnz(C_SIM_STREAM_MAX_FRAMEGROUP_COUNT)                                                                                                                                               |             |
| C_SIM_STREAM_WORD_8_EMPTY         | T_SIM_STREAM_WORD_8        |  (Valid => '0', Data => (others => 'U'),	SOF => '0', EOF	=> '0', Ready => '0', EOFG => FALSE)                                                                                                |             |
| C_SIM_STREAM_WORD_32_EMPTY        | T_SIM_STREAM_WORD_32       |  (Valid => '0', Data => (others => 'U'),	SOF => '0', EOF	=> '0', Ready => '0', EOFG => FALSE)                                                                                                |             |
| C_SIM_STREAM_WORD_8_INVALID       | T_SIM_STREAM_WORD_8        |  (Valid	=> '0', Data => (others => 'U'),	SOF => '0', EOF	=> '0', Ready => '0', EOFG => FALSE)                                                                                                |             |
| C_SIM_STREAM_WORD_32_INVALID      | T_SIM_STREAM_WORD_32       |  (Valid	=> '0', Data => (others => 'U'),	SOF => '0', EOF	=> '0', Ready => '0', EOFG => FALSE)                                                                                                |             |
| C_SIM_STREAM_WORD_8_ZERO          | T_SIM_STREAM_WORD_8        |  (Valid	=> '1', Data => (others => 'Z'),	SOF => '0', EOF	=> '0', Ready => '0', EOFG => FALSE)                                                                                                |             |
| C_SIM_STREAM_WORD_32_ZERO         | T_SIM_STREAM_WORD_32       |  (Valid	=> '1', Data => (others => 'Z'),	SOF => '0', EOF	=> '0', Ready => '0', EOFG => FALSE)                                                                                                |             |
| C_SIM_STREAM_WORD_8_UNDEF         | T_SIM_STREAM_WORD_8        |  (Valid	=> '1', Data => (others => 'U'),	SOF => '0', EOF	=> '0', Ready => '0', EOFG => FALSE)                                                                                                |             |
| C_SIM_STREAM_WORD_32_UNDEF        | T_SIM_STREAM_WORD_32       |  (Valid	=> '1', Data => (others => 'U'),	SOF => '0', EOF	=> '0', Ready => '0', EOFG => FALSE)                                                                                                |             |
| C_SIM_STREAM_FRAMEGROUP_8_EMPTY   | T_SIM_STREAM_FRAMEGROUP_8  |  ( 		Active						=> FALSE, 		Name							=> (others => C_POC_NUL), 		PrePause					=> 0, 		PostPause					=> 0, 		DataCount					=> 0, 		Data							=> (others => C_SIM_STREAM_WORD_8_EMPTY) 	)  |             |
| C_SIM_STREAM_FRAMEGROUP_32_EMPTY  | T_SIM_STREAM_FRAMEGROUP_32 |  ( 		Active						=> FALSE, 		Name							=> (others => C_POC_NUL), 		PrePause					=> 0, 		PostPause					=> 0, 		DataCount					=> 0, 		Data							=> (others => C_SIM_STREAM_WORD_32_EMPTY) 	) |             |
## Types
| Name                              | Type            | Description |
| --------------------------------- | --------------- | ----------- |
| T_SIM_STREAM_WORD_8               |                 |             |
| T_SIM_STREAM_WORD_32              |                 |             |
| T_SIM_DELAY_VECTOR                |                 |             |
| T_SIM_STREAM_WORD_VECTOR_8        |                 |             |
| T_SIM_STREAM_WORD_VECTOR_32       |                 |             |
| T_SIM_STREAM_DIRECTION            | (Send, RECEIVE) |             |
| T_SIM_STREAM_FRAMEGROUP_8         |                 |             |
| T_SIM_STREAM_FRAMEGROUP_32        |                 |             |
| T_SIM_STREAM_FRAMEGROUP_VECTOR_8  |                 |             |
| T_SIM_STREAM_FRAMEGROUP_VECTOR_32 |                 |             |
## Functions
- CountPatterns <font id="function_arguments">(Data : T_SIM_STREAM_WORD_VECTOR_8)</font> <font id="function_return">return natural</font>
- CountPatterns <font id="function_arguments">(Data : T_SIM_STREAM_WORD_VECTOR_32)</font> <font id="function_return">return natural</font>
- dat <font id="function_arguments">(slv		: T_SLV_8)</font> <font id="function_return">return T_SIM_STREAM_WORD_8</font>
- dat <font id="function_arguments">(slvv		: T_SLVV_8)</font> <font id="function_return">return T_SIM_STREAM_WORD_VECTOR_8</font>
- dat <font id="function_arguments">(slv		: T_SLV_32)</font> <font id="function_return">return T_SIM_STREAM_WORD_32</font>
- dat <font id="function_arguments">(slvv		: T_SLVV_32)</font> <font id="function_return">return T_SIM_STREAM_WORD_VECTOR_32</font>
- sof <font id="function_arguments">(slv		: T_SLV_8)</font> <font id="function_return">return T_SIM_STREAM_WORD_8</font>
- sof <font id="function_arguments">(slvv		: T_SLVV_8)</font> <font id="function_return">return T_SIM_STREAM_WORD_VECTOR_8</font>
- sof <font id="function_arguments">(slv		: T_SLV_32)</font> <font id="function_return">return T_SIM_STREAM_WORD_32</font>
- sof <font id="function_arguments">(slvv		: T_SLVV_32)</font> <font id="function_return">return T_SIM_STREAM_WORD_VECTOR_32</font>
- eof <font id="function_arguments">(slv		: T_SLV_8)</font> <font id="function_return">return T_SIM_STREAM_WORD_8</font>
- eof <font id="function_arguments">(slvv		: T_SLVV_8)</font> <font id="function_return">return T_SIM_STREAM_WORD_VECTOR_8</font>
- eof <font id="function_arguments">(slv		: T_SLV_32)</font> <font id="function_return">return T_SIM_STREAM_WORD_32</font>
- eof <font id="function_arguments">(slvv		: T_SLVV_32)</font> <font id="function_return">return T_SIM_STREAM_WORD_VECTOR_32</font>
- eof <font id="function_arguments">(stmw		: T_SIM_STREAM_WORD_8)</font> <font id="function_return">return T_SIM_STREAM_WORD_8</font>
- eof <font id="function_arguments">(stmwv	: T_SIM_STREAM_WORD_VECTOR_8)</font> <font id="function_return">return T_SIM_STREAM_WORD_VECTOR_8</font>
- eof <font id="function_arguments">(stmw		: T_SIM_STREAM_WORD_32)</font> <font id="function_return">return T_SIM_STREAM_WORD_32</font>
- eofg <font id="function_arguments">(stmw	: T_SIM_STREAM_WORD_8)</font> <font id="function_return">return T_SIM_STREAM_WORD_8</font>
- eofg <font id="function_arguments">(stmwv	: T_SIM_STREAM_WORD_VECTOR_8)</font> <font id="function_return">return T_SIM_STREAM_WORD_VECTOR_8</font>
- eofg <font id="function_arguments">(stmw	: T_SIM_STREAM_WORD_32)</font> <font id="function_return">return T_SIM_STREAM_WORD_32</font>
- to_string <font id="function_arguments">(stmw : T_SIM_STREAM_WORD_8)</font> <font id="function_return">return string</font>
- to_string <font id="function_arguments">(stmw : T_SIM_STREAM_WORD_32)</font> <font id="function_return">return string</font>
- sim_CRC8 <font id="function_arguments">(words		: T_SIM_STREAM_WORD_VECTOR_8)</font> <font id="function_return">return std_logic_vector</font>
