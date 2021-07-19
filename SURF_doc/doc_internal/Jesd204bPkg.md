# Package: Jesd204bPkg

- **File**: Jesd204bPkg.vhd
## Constants

| Name                      | Type             | Value                                                                                                                                                                                                                                                                                                                                                                                         | Description                                                   |
| ------------------------- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| GT_WORD_SIZE_C            | positive         |  4                                                                                                                                                                                                                                                                                                                                                                                            |                                                               |
| K_CHAR_C                  | slv(7 downto 0)  |  x"BC"                                                                                                                                                                                                                                                                                                                                                                                        | 8B10B characters (8-bit values)K.28.5                         |
| R_CHAR_C                  | slv(7 downto 0)  |  x"1C"                                                                                                                                                                                                                                                                                                                                                                                        | K.28.0                                                        |
| A_CHAR_C                  | slv(7 downto 0)  |  x"7C"                                                                                                                                                                                                                                                                                                                                                                                        | K.28.3                                                        |
| F_CHAR_C                  | slv(7 downto 0)  |  x"FC"                                                                                                                                                                                                                                                                                                                                                                                        | K.28.7                                                        |
| SYSRF_DLY_WIDTH_C         | positive         |  8                                                                                                                                                                                                                                                                                                                                                                                            | Register or counter widths                                    |
| RX_STAT_WIDTH_C           | positive         |  19 + 2*GT_WORD_SIZE_C                                                                                                                                                                                                                                                                                                                                                                        |                                                               |
| TX_STAT_WIDTH_C           | positive         |  6                                                                                                                                                                                                                                                                                                                                                                                            |                                                               |
| AXI_PACKET_SIZE_DEFAULT_C | slv(23 downto 0) |  x"00_01_00"                                                                                                                                                                                                                                                                                                                                                                                  | AXI packet size at power up                                   |
| PER_STEP_WIDTH_C          | positive         |  16                                                                                                                                                                                                                                                                                                                                                                                           | TX specificRamp step or square wave period slv width (max 16) |
| JESD_PRBS_TAPS_C          | NaturalArray     |  (0 => 14,<br><span style="padding-left:20px"> 1 => 15)                                                                                                                                                                                                                                                                                                                                       | Scrambler/Descrambler PBRS taps for 1 + x^14 + x^15           |
| JESD_GT_RX_LANE_INIT_C    | jesdGtRxLaneType |  (       data      => (others => '0'),<br><span style="padding-left:20px">       dataK     => (others => '0'),<br><span style="padding-left:20px">       dispErr   => (others => '0'),<br><span style="padding-left:20px">       decErr    => (others => '0'),<br><span style="padding-left:20px">       rstDone   => '0',<br><span style="padding-left:20px">       cdrStable => '0'       ) |                                                               |
| JESD_GT_TX_LANE_INIT_C    | jesdGtTxLaneType |  (       data  => (others => '0'),<br><span style="padding-left:20px">       dataK => (others => '0'))                                                                                                                                                                                                                                                                                        |                                                               |
## Types

| Name                  | Type                                                                                                                | Description |
| --------------------- | ------------------------------------------------------------------------------------------------------------------- | ----------- |
| jesdGtRxLaneType      |                                                                                                                     |             |
| jesdGtTxLaneType      |                                                                                                                     |             |
| jesdGtRxLaneTypeArray | array (natural range <>) of jesdGtRxLaneType                                                                        | Arrays      |
| jesdGtTxLaneTypeArray | array (natural range <>) of jesdGtTxLaneType                                                                        |             |
| fixLatDataArray       | array (natural range <>) of slv((GT_WORD_SIZE_C*8+GT_WORD_SIZE_C*2)-1 downto 0)                                     |             |
| sampleDataArray       | array (natural range <>) of slv((GT_WORD_SIZE_C*8)-1 downto 0)                                                      |             |
| sampleDataVectorArray | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv((GT_WORD_SIZE_C*8)-1 downto 0)  |             |
| rxStatuRegisterArray  | array (natural range <>) of slv((RX_STAT_WIDTH_C)-1 downto 0)                                                       |             |
| txStatuRegisterArray  | array (natural range <>) of slv((TX_STAT_WIDTH_C)-1 downto 0)                                                       |             |
| alignTxArray          | array (natural range <>) of slv((GT_WORD_SIZE_C)-1 downto 0)                                                        |             |
## Functions
- detKcharFunc <font id="function_arguments">(data_slv : slv;<br><span style="padding-left:20px"> charisk_slv : slv;<br><span style="padding-left:20px"> bytes_int : positive) </font> <font id="function_return">return std_logic </font>
**Description**
Detect K character
- varIndexOutFunc <font id="function_arguments">(shft_slv : slv;<br><span style="padding-left:20px"> index_slv : slv) </font> <font id="function_return">return std_logic </font>
**Description**
Output variable index from SLV (use in variable length shift register)
- detectPosFuncSwap <font id="function_arguments">(data_slv : slv;<br><span style="padding-left:20px"> charisk_slv : slv;<br><span style="padding-left:20px"> bytes_int : positive) </font> <font id="function_return">return std_logic_vector </font>
**Description**
Detect position of first non K character (Swapped)
- detectPosFunc <font id="function_arguments">(data_slv : slv;<br><span style="padding-left:20px"> charisk_slv : slv;<br><span style="padding-left:20px"> bytes_int : positive) </font> <font id="function_return">return std_logic_vector </font>
**Description**
Detect position of first non K character
- byteSwapSlv <font id="function_arguments">(data_slv : slv;<br><span style="padding-left:20px"> bytes_int : positive) </font> <font id="function_return">return std_logic_vector </font>
**Description**
Byte swap slv (bytes int 2 or 4)
- endianSwapSlv <font id="function_arguments">(data_slv : slv;<br><span style="padding-left:20px"> bytes_int : positive) </font> <font id="function_return">return std_logic_vector </font>
**Description**
Swap little and big endians (bytes int 2 or 4)
- JesdDataAlign <font id="function_arguments">(data_slv : slv;<br><span style="padding-left:20px"> position_slv : slv;<br><span style="padding-left:20px"> bytes_int : positive) </font> <font id="function_return">return std_logic_vector </font>
**Description**
Align the data within the data buffer according to the position of the byte alignment word
- JesdCharAlign <font id="function_arguments">(char_slv : slv;<br><span style="padding-left:20px"> position_slv : slv;<br><span style="padding-left:20px"> bytes_int : positive) </font> <font id="function_return">return std_logic_vector </font>
**Description**
Align the character within the buffer according to the position of the byte alignment word
- slvToInt <font id="function_arguments">(data_slv : slv) </font> <font id="function_return">return integer </font>
**Description**
Convert standard logic vector to integer
- intToSlv <font id="function_arguments">(data_int : integer;<br><span style="padding-left:20px"> bytes_int : positive) </font> <font id="function_return">return std_logic_vector </font>
**Description**
Convert integer to standard logic vector
- outSampleZero <font id="function_arguments">(F_int : positive;<br><span style="padding-left:20px"> bytes_int : positive) </font> <font id="function_return">return std_logic_vector </font>
**Description**
Output offset binary zero
- invSigned <font id="function_arguments">(input : slv) </font> <font id="function_return">return std_logic_vector </font>
**Description**
Invert functionsInvert signed
- invData <font id="function_arguments">(data    : slv;<br><span style="padding-left:20px"> F_int : positive;<br><span style="padding-left:20px"> bytes_int : positive) </font> <font id="function_return">return std_logic_vector </font>
- jesdScrambler <font id="function_arguments">( dataIn  : in    slv(15 downto 0);<br><span style="padding-left:20px"> lfsrIn  : in    slv(14 downto 0);<br><span style="padding-left:20px"> dataOut : inout slv(15 downto 0);<br><span style="padding-left:20px"> lfsrOut : inout slv(14 downto 0)) </font> <font id="function_return">return ()</font>
