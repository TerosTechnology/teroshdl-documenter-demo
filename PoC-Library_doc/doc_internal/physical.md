# Package: physical
## Constants
| Name                               | Type    | Value | Description |
| ---------------------------------- | ------- | ----- | ----------- |
| C_PHYSICAL_REPORT_TIMING_DEVIATION | boolean |  TRUE |             |
## Types
| Name      | Type | Description |
| --------- | ---- | ----------- |
| FREQ      |      |             |
| BAUD      |      |             |
| MEMORY    |      |             |
| T_TIMEVEC |      |             |
| T_FREQVEC |      |             |
| T_BAUDVEC |      |             |
| T_MEMVEC  |      |             |
## Functions
- to_time <font id="function_arguments">(f : FREQ)</font> <font id="function_return">return time</font>
- to_freq <font id="function_arguments">(p : time)</font> <font id="function_return">return FREQ</font>
- to_freq <font id="function_arguments">(br : BAUD)</font> <font id="function_return">return FREQ</font>
- to_baud <font id="function_arguments">(str : string)</font> <font id="function_return">return BAUD</font>
- div <font id="function_arguments">(a : time; b : time)</font> <font id="function_return">return real</font>
- div <font id="function_arguments">(a : FREQ; b : FREQ)</font> <font id="function_return">return real</font>
- ite <font id="function_arguments">(cond : boolean; value1 : time;	value2 : time)</font> <font id="function_return">return time</font>
- ite <font id="function_arguments">(cond : boolean; value1 : FREQ;	value2 : FREQ)</font> <font id="function_return">return FREQ</font>
- ite <font id="function_arguments">(cond : boolean; value1 : BAUD;	value2 : BAUD)</font> <font id="function_return">return BAUD</font>
- ite <font id="function_arguments">(cond : boolean; value1 : MEMORY;	value2 : MEMORY)</font> <font id="function_return">return MEMORY</font>
- tmin <font id="function_arguments">(arg1 : time; arg2 : time)</font> <font id="function_return">return time</font>
- fmin <font id="function_arguments">(arg1 : FREQ; arg2 : FREQ)</font> <font id="function_return">return FREQ</font>
- bmin <font id="function_arguments">(arg1 : BAUD; arg2 : BAUD)</font> <font id="function_return">return BAUD</font>
- mmin <font id="function_arguments">(arg1 : MEMORY; arg2 : MEMORY)</font> <font id="function_return">return MEMORY</font>
- tmax <font id="function_arguments">(arg1 : time; arg2 : time)</font> <font id="function_return">return time</font>
- fmax <font id="function_arguments">(arg1 : FREQ; arg2 : FREQ)</font> <font id="function_return">return FREQ</font>
- bmax <font id="function_arguments">(arg1 : BAUD; arg2 : BAUD)</font> <font id="function_return">return BAUD</font>
- mmax <font id="function_arguments">(arg1 : MEMORY; arg2 : MEMORY)</font> <font id="function_return">return MEMORY</font>
- tmin <font id="function_arguments">(vec : T_TIMEVEC)</font> <font id="function_return">return time</font>
- fmin <font id="function_arguments">(vec : T_FREQVEC)</font> <font id="function_return">return FREQ</font>
- bmin <font id="function_arguments">(vec : T_BAUDVEC)</font> <font id="function_return">return BAUD</font>
- mmin <font id="function_arguments">(vec : T_MEMVEC)</font> <font id="function_return">return MEMORY</font>
- tmax <font id="function_arguments">(vec : T_TIMEVEC)</font> <font id="function_return">return time</font>
- fmax <font id="function_arguments">(vec : T_FREQVEC)</font> <font id="function_return">return FREQ</font>
- bmax <font id="function_arguments">(vec : T_BAUDVEC)</font> <font id="function_return">return BAUD</font>
- mmax <font id="function_arguments">(vec : T_MEMVEC)</font> <font id="function_return">return MEMORY</font>
- tsum <font id="function_arguments">(vec : T_TIMEVEC)</font> <font id="function_return">return time</font>
- fsum <font id="function_arguments">(vec : T_FREQVEC)</font> <font id="function_return">return FREQ</font>
- bsum <font id="function_arguments">(vec : T_BAUDVEC)</font> <font id="function_return">return BAUD</font>
- msum <font id="function_arguments">(vec : T_MEMVEC)</font> <font id="function_return">return MEMORY</font>
- fs2Time <font id="function_arguments">(t_fs : integer)</font> <font id="function_return">return time</font>
- ps2Time <font id="function_arguments">(t_ps : integer)</font> <font id="function_return">return time</font>
- ns2Time <font id="function_arguments">(t_ns : integer)</font> <font id="function_return">return time</font>
- us2Time <font id="function_arguments">(t_us : integer)</font> <font id="function_return">return time</font>
- ms2Time <font id="function_arguments">(t_ms : integer)</font> <font id="function_return">return time</font>
- sec2Time <font id="function_arguments">(t_sec : integer)</font> <font id="function_return">return time</font>
- fs2Time <font id="function_arguments">(t_fs : REAL)</font> <font id="function_return">return time</font>
- ps2Time <font id="function_arguments">(t_ps : REAL)</font> <font id="function_return">return time</font>
- ns2Time <font id="function_arguments">(t_ns : REAL)</font> <font id="function_return">return time</font>
- us2Time <font id="function_arguments">(t_us : REAL)</font> <font id="function_return">return time</font>
- ms2Time <font id="function_arguments">(t_ms : REAL)</font> <font id="function_return">return time</font>
- sec2Time <font id="function_arguments">(t_sec : REAL)</font> <font id="function_return">return time</font>
- Hz2Time <font id="function_arguments">(f_Hz : natural)</font> <font id="function_return">return time</font>
- kHz2Time <font id="function_arguments">(f_kHz : natural)</font> <font id="function_return">return time</font>
- MHz2Time <font id="function_arguments">(f_MHz : natural)</font> <font id="function_return">return time</font>
- GHz2Time <font id="function_arguments">(f_GHz : natural)</font> <font id="function_return">return time</font>
- Hz2Time <font id="function_arguments">(f_Hz : REAL)</font> <font id="function_return">return time</font>
- kHz2Time <font id="function_arguments">(f_kHz : REAL)</font> <font id="function_return">return time</font>
- MHz2Time <font id="function_arguments">(f_MHz : REAL)</font> <font id="function_return">return time</font>
- GHz2Time <font id="function_arguments">(f_GHz : REAL)</font> <font id="function_return">return time</font>
- Hz2Freq <font id="function_arguments">(f_Hz : natural)</font> <font id="function_return">return FREQ</font>
- kHz2Freq <font id="function_arguments">(f_kHz : natural)</font> <font id="function_return">return FREQ</font>
- MHz2Freq <font id="function_arguments">(f_MHz : natural)</font> <font id="function_return">return FREQ</font>
- GHz2Freq <font id="function_arguments">(f_GHz : natural)</font> <font id="function_return">return FREQ</font>
- Hz2Freq <font id="function_arguments">(f_Hz : REAL)</font> <font id="function_return">return FREQ</font>
- kHz2Freq <font id="function_arguments">(f_kHz : REAL)</font> <font id="function_return">return FREQ</font>
- MHz2Freq <font id="function_arguments">(f_MHz : REAL)</font> <font id="function_return">return FREQ</font>
- GHz2Freq <font id="function_arguments">(f_GHz : REAL)</font> <font id="function_return">return FREQ</font>
- to_real <font id="function_arguments">(t : time;			scale : time)</font> <font id="function_return">return REAL</font>
- to_real <font id="function_arguments">(f : FREQ;			scale : FREQ)</font> <font id="function_return">return REAL</font>
- to_real <font id="function_arguments">(br : BAUD;			scale : BAUD)</font> <font id="function_return">return REAL</font>
- to_real <font id="function_arguments">(mem : MEMORY;	scale : MEMORY)</font> <font id="function_return">return REAL</font>
- to_int <font id="function_arguments">(t : time;			scale : time;		RoundingStyle : T_ROUNDING_STYLE := ROUND_TO_NEAREST)</font> <font id="function_return">return integer</font>
- to_int <font id="function_arguments">(f : FREQ;			scale : FREQ;		RoundingStyle : T_ROUNDING_STYLE := ROUND_TO_NEAREST)</font> <font id="function_return">return integer</font>
- to_int <font id="function_arguments">(br : BAUD;		scale : BAUD;		RoundingStyle : T_ROUNDING_STYLE := ROUND_TO_NEAREST)</font> <font id="function_return">return integer</font>
- to_int <font id="function_arguments">(mem : MEMORY;	scale : MEMORY;	RoundingStyle : T_ROUNDING_STYLE := ROUND_UP)</font> <font id="function_return">return integer</font>
- TimingToCycles <font id="function_arguments">(Timing : time; Clock_Period			: time; RoundingStyle : T_ROUNDING_STYLE := ROUND_UP)</font> <font id="function_return">return natural</font>
- TimingToCycles <font id="function_arguments">(Timing : time; Clock_Frequency	: FREQ; RoundingStyle : T_ROUNDING_STYLE := ROUND_UP)</font> <font id="function_return">return natural</font>
- CyclesToDelay <font id="function_arguments">(Cycles : natural; Clock_Period			: time)</font> <font id="function_return">return time</font>
- CyclesToDelay <font id="function_arguments">(Cycles : natural; Clock_Frequency	: FREQ)</font> <font id="function_return">return time</font>
- to_string <font id="function_arguments">(t : time; precision : natural)</font> <font id="function_return">return string</font>
- to_string <font id="function_arguments">(f : FREQ; precision : natural)</font> <font id="function_return">return string</font>
- to_string <font id="function_arguments">(br : BAUD; precision : natural)</font> <font id="function_return">return string</font>
- to_string <font id="function_arguments">(mem : MEMORY; precision : natural)</font> <font id="function_return">return string</font>
