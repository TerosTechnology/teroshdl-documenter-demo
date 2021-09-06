# Package: components

- **File**: components.vhdl
## Functions
- registered <font id="function_arguments">(signal Clock : std_logic;<br><span style="padding-left:20px"> constant IsRegistered : boolean) </font> <font id="function_return">return boolean </font>
- ffrs <font id="function_arguments">(q : std_logic;<br><span style="padding-left:20px">	rst : std_logic := '0';<br><span style="padding-left:20px"> set : std_logic := '0') </font> <font id="function_return">return std_logic </font>
</br>**Description**
 RS-FlipFlop with dominant rst
- ffsr <font id="function_arguments">(q : std_logic;<br><span style="padding-left:20px">	rst : std_logic := '0';<br><span style="padding-left:20px"> set : std_logic := '0') </font> <font id="function_return">return std_logic </font>
</br>**Description**
 RS-FlipFlop with dominant set
- ffdre <font id="function_arguments">(q : std_logic;<br><span style="padding-left:20px">					d : std_logic;<br><span style="padding-left:20px">				rst : std_logic := '0';<br><span style="padding-left:20px"> en : std_logic := '1';<br><span style="padding-left:20px"> constant INIT : std_logic := '0') </font> <font id="function_return">return std_logic </font>
</br>**Description**
 D-FlipFlop with reset and enable
- ffdre <font id="function_arguments">(q : std_logic_vector;<br><span style="padding-left:20px">	d : std_logic_vector;<br><span style="padding-left:20px">	rst : std_logic := '0';<br><span style="padding-left:20px"> en : std_logic := '1';<br><span style="padding-left:20px"> constant INIT : std_logic_vector := (0 to 0 => '0')) </font> <font id="function_return">return std_logic_vector </font>
</br>**Description**
 D-FlipFlop with reset and enable
- ffdse <font id="function_arguments">(q : std_logic;<br><span style="padding-left:20px">					d : std_logic;<br><span style="padding-left:20px">				set : std_logic := '0';<br><span style="padding-left:20px"> en : std_logic := '1') </font> <font id="function_return">return std_logic </font>
</br>**Description**
 D-FlipFlop with set and enable
- fftre <font id="function_arguments">(q : std_logic;<br><span style="padding-left:20px">					t : std_logic;<br><span style="padding-left:20px">				rst : std_logic := '0';<br><span style="padding-left:20px"> en : std_logic := '1';<br><span style="padding-left:20px"> constant INIT : std_logic := '0') </font> <font id="function_return">return std_logic </font>
</br>**Description**
 T-FlipFlop with reset and enable
- fftse <font id="function_arguments">(q : std_logic;<br><span style="padding-left:20px">					t : std_logic;<br><span style="padding-left:20px">				set : std_logic := '0';<br><span style="padding-left:20px"> en : std_logic := '1') </font> <font id="function_return">return std_logic </font>
</br>**Description**
 T-FlipFlop with set and enable
- upcounter_next <font id="function_arguments">(cnt : unsigned;<br><span style="padding-left:20px"> rst : std_logic := '0';<br><span style="padding-left:20px"> en : std_logic := '1';<br><span style="padding-left:20px"> constant INIT : natural := 0) </font> <font id="function_return">return unsigned </font>
</br>**Description**
 counter

- upcounter_equal <font id="function_arguments">(cnt : unsigned;<br><span style="padding-left:20px"> value : natural) </font> <font id="function_return">return std_logic </font>
- downcounter_next <font id="function_arguments">(cnt : signed;<br><span style="padding-left:20px"> rst : std_logic := '0';<br><span style="padding-left:20px"> en : std_logic := '1';<br><span style="padding-left:20px"> constant INIT : integer := 0) </font> <font id="function_return">return signed </font>
- downcounter_equal <font id="function_arguments">(cnt : signed;<br><span style="padding-left:20px"> value : integer) </font> <font id="function_return">return std_logic </font>
- downcounter_neg <font id="function_arguments">(cnt : signed) </font> <font id="function_return">return std_logic </font>
- shreg_left <font id="function_arguments">(q : std_logic_vector;<br><span style="padding-left:20px"> i : std_logic;<br><span style="padding-left:20px"> en : std_logic := '1') </font> <font id="function_return">return std_logic_vector </font>
</br>**Description**
 shiftregisters

- shreg_right <font id="function_arguments">(q : std_logic_vector;<br><span style="padding-left:20px"> i : std_logic;<br><span style="padding-left:20px"> en : std_logic := '1') </font> <font id="function_return">return std_logic_vector </font>
- rreg_left <font id="function_arguments">(q : std_logic_vector;<br><span style="padding-left:20px"> en : std_logic := '1') </font> <font id="function_return">return std_logic_vector </font>
</br>**Description**
 rotate registers

- rreg_right <font id="function_arguments">(q : std_logic_vector;<br><span style="padding-left:20px"> en : std_logic := '1') </font> <font id="function_return">return std_logic_vector </font>
- comp <font id="function_arguments">(value1 : std_logic_vector;<br><span style="padding-left:20px"> value2 : std_logic_vector) </font> <font id="function_return">return std_logic_vector </font>
</br>**Description**
 compare

- comp <font id="function_arguments">(value1 : unsigned;<br><span style="padding-left:20px"> value2 : unsigned) </font> <font id="function_return">return unsigned </font>
- comp <font id="function_arguments">(value1 : signed;<br><span style="padding-left:20px"> value2 : signed) </font> <font id="function_return">return signed </font>
- comp_allzero <font id="function_arguments">(value	: std_logic_vector) </font> <font id="function_return">return std_logic </font>
- comp_allzero <font id="function_arguments">(value	: unsigned) </font> <font id="function_return">return std_logic </font>
- comp_allzero <font id="function_arguments">(value	: signed) </font> <font id="function_return">return std_logic </font>
- comp_allone <font id="function_arguments">(value	: std_logic_vector) </font> <font id="function_return">return std_logic </font>
- comp_allone <font id="function_arguments">(value	: unsigned) </font> <font id="function_return">return std_logic </font>
- comp_allone <font id="function_arguments">(value	: signed) </font> <font id="function_return">return std_logic </font>
- mux <font id="function_arguments">(sel : std_logic;<br><span style="padding-left:20px"> sl0		: std_logic;<br><span style="padding-left:20px">				sl1		: std_logic) </font> <font id="function_return">return std_logic </font>
</br>**Description**
 multiplexing

- mux <font id="function_arguments">(sel : std_logic;<br><span style="padding-left:20px"> slv0	: std_logic_vector;<br><span style="padding-left:20px">	slv1	: std_logic_vector) </font> <font id="function_return">return std_logic_vector </font>
- mux <font id="function_arguments">(sel : std_logic;<br><span style="padding-left:20px"> us0		: unsigned;<br><span style="padding-left:20px">					us1		: unsigned) </font> <font id="function_return">return unsigned </font>
- mux <font id="function_arguments">(sel : std_logic;<br><span style="padding-left:20px"> s0		: signed;<br><span style="padding-left:20px">						s1		: signed) </font> <font id="function_return">return signed </font>
