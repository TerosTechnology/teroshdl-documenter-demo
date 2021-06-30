# Package: TbUtilPkg

## Constants

| Name             | Type      | Value                     | Description |
| ---------------- | --------- | ------------------------- | ----------- |
| CLK_ACTIVE       | std_logic |  '1'                      |             |
| t_sim_resolution | time      |  std.env.resolution_limit | VHDL-2008   |
## Functions
- OneHot <font id="function_arguments">( constant A : in std_logic_vector ) </font> <font id="function_return">return boolean </font>
- ZeroOneHot <font id="function_arguments">( constant A : in std_logic_vector ) </font> <font id="function_return">return boolean </font>
- IfElse <font id="function_arguments">(Expr : boolean ; A, B : std_logic_vector) </font> <font id="function_return">return std_logic_vector </font>
- IfElse <font id="function_arguments">(Expr : boolean ; A, B : integer) </font> <font id="function_return">return integer </font>
- RequestTransaction <font id="function_arguments">( signal Rdy  : Out std_logic ; signal Ack  : In  std_logic ) </font> <font id="function_return">return ()</font>
- WaitForTransaction <font id="function_arguments">( signal Clk  : In  std_logic ; signal Rdy  : In  std_logic ; signal Ack  : Out std_logic ) </font> <font id="function_return">return ()</font>
- RequestTransaction <font id="function_arguments">( signal Rdy  : Out bit ; signal Ack  : In  bit ) </font> <font id="function_return">return ()</font>
- WaitForTransaction <font id="function_arguments">( signal Clk  : In  std_logic ; signal Rdy  : In  bit ; signal Ack  : Out bit ) </font> <font id="function_return">return ()</font>
- RequestTransaction <font id="function_arguments">( signal Rdy     : InOut RdyType ; signal Ack     : In    AckType ) </font> <font id="function_return">return ()</font>
- WaitForTransaction <font id="function_arguments">( signal Clk      : In    std_logic ; signal Rdy      : In    RdyType ; signal Ack      : InOut AckType ) </font> <font id="function_return">return ()</font>
- WaitForTransaction <font id="function_arguments">( signal   Clk       : In  std_logic ; signal   Rdy       : In  std_logic ; signal   Ack       : Out std_logic ; signal   TimeOut   : In  std_logic ; constant Polarity  : In  std_logic := '1' ) </font> <font id="function_return">return ()</font>
- WaitForTransactionOrIrq <font id="function_arguments">( signal Clk     : In  std_logic ; signal Rdy     : In  std_logic ; signal IntReq  : In  std_logic ) </font> <font id="function_return">return ()</font>
**Description**
Variation for model that stops waiting when IntReq is assertedIntended for models that need to switch between instruction streamssuch as a CPU when interrupt is pending
- StartTransaction <font id="function_arguments">( signal Ack : Out std_logic ) </font> <font id="function_return">return ()</font>
**Description**
Set Ack to Model starting value
- FinishTransaction <font id="function_arguments">( signal Ack : Out std_logic ) </font> <font id="function_return">return ()</font>
**Description**
Set Ack to Model finishing value
- TransactionPending <font id="function_arguments">( signal Rdy : In  std_logic ) </font> <font id="function_return">return boolean </font>
**Description**
If a transaction is pending, return true
- WaitForTransaction <font id="function_arguments">( signal Rdy : In  std_logic ; signal Ack : Out std_logic ) </font> <font id="function_return">return ()</font>
**Description**
Variation for clockless models
- Toggle <font id="function_arguments">( signal Sig        : InOut std_logic ; constant DelayVal : time ) </font> <font id="function_return">return ()</font>
- Toggle <font id="function_arguments">( signal Sig : InOut std_logic ) </font> <font id="function_return">return ()</font>
- ToggleHS <font id="function_arguments">( signal Sig : InOut std_logic ) </font> <font id="function_return">return ()</font>
- IsToggle <font id="function_arguments">( signal Sig : In std_logic ) </font> <font id="function_return">return boolean </font>
- WaitForToggle <font id="function_arguments">( signal Sig : In std_logic ) </font> <font id="function_return">return ()</font>
- Toggle <font id="function_arguments">( signal Sig : InOut bit ; constant DelayVal : time ) </font> <font id="function_return">return ()</font>
**Description**
Bit type versions
- Toggle <font id="function_arguments">( signal Sig : InOut bit ) </font> <font id="function_return">return ()</font>
- ToggleHS <font id="function_arguments">( signal Sig : InOut bit ) </font> <font id="function_return">return ()</font>
- IsToggle <font id="function_arguments">( signal Sig : In bit ) </font> <font id="function_return">return boolean </font>
- WaitForToggle <font id="function_arguments">( signal Sig : In bit ) </font> <font id="function_return">return ()</font>
- Increment <font id="function_arguments">( signal Sig : InOut integer ; constant RollOverValue : in integer := 0) </font> <font id="function_return">return ()</font>
**Description**
Integer type versions
- Increment <font id="function_arguments">(constant Sig : in integer ; constant Amount : in integer := 1) </font> <font id="function_return">return integer </font>
- WaitForToggle <font id="function_arguments">( signal Sig : In integer ) </font> <font id="function_return">return ()</font>
- WaitForBarrier <font id="function_arguments">( signal Sig : InOut std_logic ) </font> <font id="function_return">return ()</font>
- WaitForBarrier <font id="function_arguments">( signal Sig : InOut std_logic ; signal TimeOut : std_logic ; constant Polarity : in std_logic := '1') </font> <font id="function_return">return ()</font>
- WaitForBarrier <font id="function_arguments">( signal Sig : InOut std_logic ; constant TimeOut : time ) </font> <font id="function_return">return ()</font>
- resolved_barrier <font id="function_arguments">( s : integer_vector ) </font> <font id="function_return">return integer </font>
**Description**
resolved_barrier : summing resolution used in conjunction with integer based barriers
- WaitForBarrier <font id="function_arguments">( signal Sig : InOut integer ) </font> <font id="function_return">return ()</font>
**Description**
Usage of integer barriers requires resolved_barrier. Initialization to 1 recommended, but not required  signal barrier1 : resolved_barrier integer := 1 ;     -- using the resolution function  signal barrier2 : integer_barrier := 1 ;              -- using the subtype that already applies the resolution function
- WaitForBarrier <font id="function_arguments">( signal Sig : InOut integer ; signal TimeOut : std_logic ; constant Polarity : in std_logic := '1') </font> <font id="function_return">return ()</font>
- WaitForBarrier <font id="function_arguments">( signal Sig : InOut integer ; constant TimeOut : time ) </font> <font id="function_return">return ()</font>
- WaitForBarrier2 <font id="function_arguments">( signal SyncOut : out std_logic ; signal SyncIn : in  std_logic ) </font> <font id="function_return">return ()</font>
**Description**
Using separate signals
- WaitForBarrier2 <font id="function_arguments">( signal SyncOut : out std_logic ; signal SyncInV : in  std_logic_vector ) </font> <font id="function_return">return ()</font>
- WaitForClock <font id="function_arguments">( signal Clk : in std_logic ;  constant Delay : in time ) </font> <font id="function_return">return ()</font>
- WaitForClock <font id="function_arguments">( signal Clk : in std_logic ;  constant NumberOfClocks : in integer := 1) </font> <font id="function_return">return ()</font>
- WaitForClock <font id="function_arguments">( signal Clk : in std_logic ;  signal Enable : in boolean ) </font> <font id="function_return">return ()</font>
- WaitForClock <font id="function_arguments">( signal Clk : in std_logic ;  signal Enable : in std_logic ; constant Polarity : std_logic := '1' ) </font> <font id="function_return">return ()</font>
- WaitForLevel <font id="function_arguments">( signal A : in boolean ) </font> <font id="function_return">return ()</font>
- WaitForLevel <font id="function_arguments">( signal A : in std_logic ; Polarity : std_logic := '1' ) </font> <font id="function_return">return ()</font>
- CreateClock <font id="function_arguments">( signal   Clk        : inout std_logic ; constant Period     : time ; constant DutyCycle  : real := 0.5 ) </font> <font id="function_return">return ()</font>
- CheckClockPeriod <font id="function_arguments">( constant AlertLogID : AlertLogIDType ; signal   Clk        : in  std_logic ; constant Period     : time ; constant ClkName    : string := "Clock" ; constant HowMany    : integer := 5 ) </font> <font id="function_return">return ()</font>
- CheckClockPeriod <font id="function_arguments">( signal   Clk        : in  std_logic ; constant Period     : time ; constant ClkName    : string := "Clock" ; constant HowMany    : integer := 5 ) </font> <font id="function_return">return ()</font>
- CreateReset <font id="function_arguments">( signal   Reset       : out std_logic ; constant ResetActive : in  std_logic ; signal   Clk         : in  std_logic ; constant Period      :     time ; constant tpd         :     time ) </font> <font id="function_return">return ()</font>
- LogReset <font id="function_arguments">( constant AlertLogID  : AlertLogIDType ; signal   Reset       : in  std_logic ; constant ResetActive : in  std_logic ; constant ResetName   : in  string := "Reset" ; constant LogLevel    : in  LogType := ALWAYS ) </font> <font id="function_return">return ()</font>
- LogReset <font id="function_arguments">( signal   Reset       : in  std_logic ; constant ResetActive : in  std_logic ; constant ResetName   : in  string := "Reset" ; constant LogLevel    : in  LogType := ALWAYS ) </font> <font id="function_return">return ()</font>
- WaitForAck <font id="function_arguments">( signal Ack : In  std_logic ) </font> <font id="function_return">return ()</font>
- StrobeAck <font id="function_arguments">( signal Ack : Out std_logic ) </font> <font id="function_return">return ()</font>
