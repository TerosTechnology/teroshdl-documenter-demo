# Package: waveform
## Types
| Name                        | Type | Description |
| --------------------------- | ---- | ----------- |
| T_SIM_WAVEFORM_TUPLE_SL     |      |             |
| T_SIM_WAVEFORM_TUPLE_SLV_8  |      |             |
| T_SIM_WAVEFORM_TUPLE_SLV_16 |      |             |
| T_SIM_WAVEFORM_TUPLE_SLV_24 |      |             |
| T_SIM_WAVEFORM_TUPLE_SLV_32 |      |             |
| T_SIM_WAVEFORM_TUPLE_SLV_48 |      |             |
| T_SIM_WAVEFORM_TUPLE_SLV_64 |      |             |
| T_SIM_WAVEFORM_SL           |      |             |
| T_SIM_WAVEFORM_SLV_8        |      |             |
| T_SIM_WAVEFORM_SLV_16       |      |             |
| T_SIM_WAVEFORM_SLV_24       |      |             |
| T_SIM_WAVEFORM_SLV_32       |      |             |
| T_SIM_WAVEFORM_SLV_48       |      |             |
| T_SIM_WAVEFORM_SLV_64       |      |             |
## Functions
- simGenerateClock <font id="function_arguments">(		signal	 Clock			: out	std_logic;
		constant Frequency	: in	FREQ;
		constant Phase			: in	T_PHASE			:=	0 deg;
		constant DutyCycle	: in	T_DUTYCYCLE	:= 50 percent;
		constant Wander			: in	T_WANDER		:=	0 permil
	)</font> <font id="function_return">return ()</font>
- simGenerateClock <font id="function_arguments">(		constant TestID			: in	T_SIM_TEST_ID;
		signal	 Clock			: out	std_logic;
		constant Frequency	: in	FREQ;
		constant Phase			: in	T_PHASE			:=	0 deg;
		constant DutyCycle	: in	T_DUTYCYCLE	:= 50 percent;
		constant Wander			: in	T_WANDER		:=	0 permil
	)</font> <font id="function_return">return ()</font>
- simGenerateClock <font id="function_arguments">(		signal	 Clock			: out	std_logic;
		constant Period			: in	time;
		constant Phase			: in	T_PHASE			:=	0 deg;
		constant DutyCycle	: in	T_DUTYCYCLE	:= 50 percent;
		constant Wander			: in	T_WANDER		:=	0 permil
	)</font> <font id="function_return">return ()</font>
- simGenerateClock <font id="function_arguments">(		constant TestID			: in	T_SIM_TEST_ID;
		signal	 Clock			: out	std_logic;
		constant Period			: in	time;
		constant Phase			: in	T_PHASE			:=	0 deg;
		constant DutyCycle	: in	T_DUTYCYCLE	:= 50 percent;
		constant Wander			: in	T_WANDER		:=	0 permil
	)</font> <font id="function_return">return ()</font>
- simWaitUntilRisingEdge <font id="function_arguments">(signal Clock : in std_logic; constant Times : in positive)</font> <font id="function_return">return ()</font>
- simWaitUntilRisingEdge <font id="function_arguments">(constant TestID : in T_SIM_TEST_ID; signal Clock : in std_logic; constant Times : in positive)</font> <font id="function_return">return ()</font>
- simWaitUntilFallingEdge <font id="function_arguments">(signal Clock : in std_logic; constant Times : in positive)</font> <font id="function_return">return ()</font>
- simWaitUntilFallingEdge <font id="function_arguments">(constant TestID : in T_SIM_TEST_ID; signal Clock : in std_logic; constant Times : in positive)</font> <font id="function_return">return ()</font>
- simGenerateClock2 <font id="function_arguments">(constant TestID : in T_SIM_TEST_ID; signal Clock : out std_logic; signal Debug : out REAL; constant Period : in time)</font> <font id="function_return">return ()</font>
- simGenerateWaveform <font id="function_arguments">(		signal	 Wave					: out	boolean;
		constant Waveform			: in	T_SIM_WAVEFORM;
		constant InitialValue	: in	boolean					:= FALSE
	)</font> <font id="function_return">return ()</font>
- simGenerateWaveform <font id="function_arguments">(		constant TestID				: in	T_SIM_TEST_ID;
		signal	 Wave					: out	boolean;
		constant Waveform			: in	T_SIM_WAVEFORM;
		constant InitialValue	: in	boolean					:= FALSE
	)</font> <font id="function_return">return ()</font>
- simGenerateWaveform <font id="function_arguments">(		signal	 Wave					: out	std_logic;
		constant Waveform			: in	T_SIM_WAVEFORM;
		constant InitialValue	: in	std_logic				:= '0'
	)</font> <font id="function_return">return ()</font>
- simGenerateWaveform <font id="function_arguments">(		constant TestID				: in	T_SIM_TEST_ID;
		signal	 Wave					: out	std_logic;
		constant Waveform			: in	T_SIM_WAVEFORM;
		constant InitialValue	: in	std_logic				:= '0'
	)</font> <font id="function_return">return ()</font>
- simGenerateWaveform <font id="function_arguments">(		signal	 Wave					: out	std_logic;
		constant Waveform			: in	T_SIM_WAVEFORM_SL;
		constant InitialValue	: in	std_logic				:= '0'
	)</font> <font id="function_return">return ()</font>
- simGenerateWaveform <font id="function_arguments">(		constant TestID				: in	T_SIM_TEST_ID;
		signal	 Wave					: out	std_logic;
		constant Waveform			: in	T_SIM_WAVEFORM_SL;
		constant InitialValue	: in	std_logic				:= '0'
	)</font> <font id="function_return">return ()</font>
- simGenerateWaveform <font id="function_arguments">(		signal	 Wave					: out	T_SLV_8;
		constant Waveform			: in	T_SIM_WAVEFORM_SLV_8;
		constant InitialValue	: in	T_SLV_8					:= (others => '0')
	)</font> <font id="function_return">return ()</font>
- simGenerateWaveform <font id="function_arguments">(		constant TestID				: in	T_SIM_TEST_ID;
		signal	 Wave					: out	T_SLV_8;
		constant Waveform			: in	T_SIM_WAVEFORM_SLV_8;
		constant InitialValue	: in	T_SLV_8					:= (others => '0')
	)</font> <font id="function_return">return ()</font>
- simGenerateWaveform <font id="function_arguments">(		signal	 Wave					: out	T_SLV_16;
		constant Waveform			: in	T_SIM_WAVEFORM_SLV_16;
		constant InitialValue	: in	T_SLV_16				:= (others => '0')
	)</font> <font id="function_return">return ()</font>
- simGenerateWaveform <font id="function_arguments">(		constant TestID				: in	T_SIM_TEST_ID;
		signal	 Wave					: out	T_SLV_16;
		constant Waveform			: in	T_SIM_WAVEFORM_SLV_16;
		constant InitialValue	: in	T_SLV_16				:= (others => '0')
	)</font> <font id="function_return">return ()</font>
- simGenerateWaveform <font id="function_arguments">(		signal	 Wave					: out	T_SLV_24;
		constant Waveform			: in	T_SIM_WAVEFORM_SLV_24;
		constant InitialValue	: in	T_SLV_24				:= (others => '0')
	)</font> <font id="function_return">return ()</font>
- simGenerateWaveform <font id="function_arguments">(		constant TestID				: in	T_SIM_TEST_ID;
		signal	 Wave					: out	T_SLV_24;
		constant Waveform			: in	T_SIM_WAVEFORM_SLV_24;
		constant InitialValue	: in	T_SLV_24				:= (others => '0')
	)</font> <font id="function_return">return ()</font>
- simGenerateWaveform <font id="function_arguments">(		signal	 Wave					: out	T_SLV_32;
		constant Waveform			: in	T_SIM_WAVEFORM_SLV_32;
		constant InitialValue	: in	T_SLV_32				:= (others => '0')
	)</font> <font id="function_return">return ()</font>
- simGenerateWaveform <font id="function_arguments">(		constant TestID				: in	T_SIM_TEST_ID;
		signal	 Wave					: out	T_SLV_32;
		constant Waveform			: in	T_SIM_WAVEFORM_SLV_32;
		constant InitialValue	: in	T_SLV_32				:= (others => '0')
	)</font> <font id="function_return">return ()</font>
- simGenerateWaveform <font id="function_arguments">(		signal	 Wave					: out	T_SLV_48;
		constant Waveform			: in	T_SIM_WAVEFORM_SLV_48;
		constant InitialValue	: in	T_SLV_48				:= (others => '0')
	)</font> <font id="function_return">return ()</font>
- simGenerateWaveform <font id="function_arguments">(		constant TestID				: in	T_SIM_TEST_ID;
		signal	 Wave					: out	T_SLV_48;
		constant Waveform			: in	T_SIM_WAVEFORM_SLV_48;
		constant InitialValue	: in	T_SLV_48				:= (others => '0')
	)</font> <font id="function_return">return ()</font>
- simGenerateWaveform <font id="function_arguments">(		signal	 Wave					: out	T_SLV_64;
		constant Waveform			: in	T_SIM_WAVEFORM_SLV_64;
		constant InitialValue	: in	T_SLV_64				:= (others => '0')
	)</font> <font id="function_return">return ()</font>
- simGenerateWaveform <font id="function_arguments">(		constant TestID				: in	T_SIM_TEST_ID;
		signal	 Wave					: out	T_SLV_64;
		constant Waveform			: in	T_SIM_WAVEFORM_SLV_64;
		constant InitialValue	: in	T_SLV_64				:= (others => '0')
	)</font> <font id="function_return">return ()</font>
- to_waveform <font id="function_arguments">(bv : bit_vector; Delay : time)</font> <font id="function_return">return T_SIM_WAVEFORM</font>
- to_waveform <font id="function_arguments">(slv : std_logic_vector; Delay : time)</font> <font id="function_return">return T_SIM_WAVEFORM_SL</font>
- to_waveform <font id="function_arguments">(slvv : T_SLVV_8; Delay : time)</font> <font id="function_return">return T_SIM_WAVEFORM_SLV_8</font>
- to_waveform <font id="function_arguments">(slvv : T_SLVV_16; Delay : time)</font> <font id="function_return">return T_SIM_WAVEFORM_SLV_16</font>
- to_waveform <font id="function_arguments">(slvv : T_SLVV_24; Delay : time)</font> <font id="function_return">return T_SIM_WAVEFORM_SLV_24</font>
- to_waveform <font id="function_arguments">(slvv : T_SLVV_32; Delay : time)</font> <font id="function_return">return T_SIM_WAVEFORM_SLV_32</font>
- to_waveform <font id="function_arguments">(slvv : T_SLVV_48; Delay : time)</font> <font id="function_return">return T_SIM_WAVEFORM_SLV_48</font>
- to_waveform <font id="function_arguments">(slvv : T_SLVV_64; Delay : time)</font> <font id="function_return">return T_SIM_WAVEFORM_SLV_64</font>
- simGenerateWaveform_Reset <font id="function_arguments">(constant Pause : time := 0 ns; ResetPulse : time := 10 ns)</font> <font id="function_return">return T_SIM_WAVEFORM</font>
