# Package: physical

- **File**: physical.vhdl
## Constants

| Name                               | Type    | Value | Description                                                                     |
| ---------------------------------- | ------- | ----- | ------------------------------------------------------------------------------- |
| C_PHYSICAL_REPORT_TIMING_DEVIATION | boolean |  TRUE |  if true: TimingToCycles reports difference between expected and actual result  |
## Types

| Name      | Type                               | Description         |
| --------- | ---------------------------------- | ------------------- |
| FREQ      |                                    |                     |
| BAUD      |                                    |                     |
| MEMORY    |                                    |                     |
| T_TIMEVEC | array(natural range <>) of time    |  vector data types  |
| T_FREQVEC | array(natural range <>) of FREQ    |                     |
| T_BAUDVEC | array(natural range <>) of BAUD    |                     |
| T_MEMVEC  | array(natural range <>) of MEMORY  |                     |
## Functions
- to_time <font id="function_arguments">(f : FREQ) </font> <font id="function_return">return time </font>
</br>**Description**
 conversion functions

- to_freq <font id="function_arguments">(p : time) </font> <font id="function_return">return FREQ </font>
- to_freq <font id="function_arguments">(br : BAUD) </font> <font id="function_return">return FREQ </font>
- to_baud <font id="function_arguments">(str : string) </font> <font id="function_return">return BAUD </font>
- div <font id="function_arguments">(a : time;<br><span style="padding-left:20px"> b : time) </font> <font id="function_return">return real </font>
</br>**Description**
 inter-type arithmetic

- div <font id="function_arguments">(a : FREQ;<br><span style="padding-left:20px"> b : FREQ) </font> <font id="function_return">return real </font>
- ite <font id="function_arguments">(cond : boolean;<br><span style="padding-left:20px"> value1 : time;<br><span style="padding-left:20px">	value2 : time) </font> <font id="function_return">return time </font>
</br>**Description**
 if-then-else

- ite <font id="function_arguments">(cond : boolean;<br><span style="padding-left:20px"> value1 : FREQ;<br><span style="padding-left:20px">	value2 : FREQ) </font> <font id="function_return">return FREQ </font>
- ite <font id="function_arguments">(cond : boolean;<br><span style="padding-left:20px"> value1 : BAUD;<br><span style="padding-left:20px">	value2 : BAUD) </font> <font id="function_return">return BAUD </font>
- ite <font id="function_arguments">(cond : boolean;<br><span style="padding-left:20px"> value1 : MEMORY;<br><span style="padding-left:20px">	value2 : MEMORY) </font> <font id="function_return">return MEMORY </font>
- tmin <font id="function_arguments">(arg1 : time;<br><span style="padding-left:20px"> arg2 : time) </font> <font id="function_return">return time </font>
</br>**Description**
 Calculates: min(arg1, arg2) for times
- fmin <font id="function_arguments">(arg1 : FREQ;<br><span style="padding-left:20px"> arg2 : FREQ) </font> <font id="function_return">return FREQ </font>
</br>**Description**
 Calculates: min(arg1, arg2) for frequencies
- bmin <font id="function_arguments">(arg1 : BAUD;<br><span style="padding-left:20px"> arg2 : BAUD) </font> <font id="function_return">return BAUD </font>
</br>**Description**
 Calculates: min(arg1, arg2) for symbols per second
- mmin <font id="function_arguments">(arg1 : MEMORY;<br><span style="padding-left:20px"> arg2 : MEMORY) </font> <font id="function_return">return MEMORY </font>
</br>**Description**
 Calculates: min(arg1, arg2) for memory
- tmax <font id="function_arguments">(arg1 : time;<br><span style="padding-left:20px"> arg2 : time) </font> <font id="function_return">return time </font>
</br>**Description**
 Calculates: max(arg1, arg2) for times
- fmax <font id="function_arguments">(arg1 : FREQ;<br><span style="padding-left:20px"> arg2 : FREQ) </font> <font id="function_return">return FREQ </font>
</br>**Description**
 Calculates: max(arg1, arg2) for frequencies
- bmax <font id="function_arguments">(arg1 : BAUD;<br><span style="padding-left:20px"> arg2 : BAUD) </font> <font id="function_return">return BAUD </font>
</br>**Description**
 Calculates: max(arg1, arg2) for symbols per second
- mmax <font id="function_arguments">(arg1 : MEMORY;<br><span style="padding-left:20px"> arg2 : MEMORY) </font> <font id="function_return">return MEMORY </font>
</br>**Description**
 Calculates: max(arg1, arg2) for memory
- tmin <font id="function_arguments">(vec : T_TIMEVEC) </font> <font id="function_return">return time </font>
</br>**Description**
 Calculates: min(vec) for a time vector
- fmin <font id="function_arguments">(vec : T_FREQVEC) </font> <font id="function_return">return FREQ </font>
</br>**Description**
 Calculates: min(vec) for a frequency vector
- bmin <font id="function_arguments">(vec : T_BAUDVEC) </font> <font id="function_return">return BAUD </font>
</br>**Description**
 Calculates: min(vec) for a baud vector
- mmin <font id="function_arguments">(vec : T_MEMVEC) </font> <font id="function_return">return MEMORY </font>
</br>**Description**
 Calculates: min(vec) for a memory vector
- tmax <font id="function_arguments">(vec : T_TIMEVEC) </font> <font id="function_return">return time </font>
</br>**Description**
 Calculates: max(vec) for a time vector
- fmax <font id="function_arguments">(vec : T_FREQVEC) </font> <font id="function_return">return FREQ </font>
</br>**Description**
 Calculates: max(vec) for a frequency vector
- bmax <font id="function_arguments">(vec : T_BAUDVEC) </font> <font id="function_return">return BAUD </font>
</br>**Description**
 Calculates: max(vec) for a baud vector
- mmax <font id="function_arguments">(vec : T_MEMVEC) </font> <font id="function_return">return MEMORY </font>
</br>**Description**
 Calculates: max(vec) for a memory vector
- tsum <font id="function_arguments">(vec : T_TIMEVEC) </font> <font id="function_return">return time </font>
</br>**Description**
 Calculates: sum(vec) for a time vector
- fsum <font id="function_arguments">(vec : T_FREQVEC) </font> <font id="function_return">return FREQ </font>
</br>**Description**
 Calculates: sum(vec) for a frequency vector
- bsum <font id="function_arguments">(vec : T_BAUDVEC) </font> <font id="function_return">return BAUD </font>
</br>**Description**
 Calculates: sum(vec) for a baud vector
- msum <font id="function_arguments">(vec : T_MEMVEC) </font> <font id="function_return">return MEMORY </font>
</br>**Description**
 Calculates: sum(vec) for a memory vector
- fs2Time <font id="function_arguments">(t_fs : integer) </font> <font id="function_return">return time </font>
</br>**Description**
 convert standard types (NATURAL, REAL) to time (TIME)

- ps2Time <font id="function_arguments">(t_ps : integer) </font> <font id="function_return">return time </font>
- ns2Time <font id="function_arguments">(t_ns : integer) </font> <font id="function_return">return time </font>
- us2Time <font id="function_arguments">(t_us : integer) </font> <font id="function_return">return time </font>
- ms2Time <font id="function_arguments">(t_ms : integer) </font> <font id="function_return">return time </font>
- sec2Time <font id="function_arguments">(t_sec : integer) </font> <font id="function_return">return time </font>
- fs2Time <font id="function_arguments">(t_fs : REAL) </font> <font id="function_return">return time </font>
- ps2Time <font id="function_arguments">(t_ps : REAL) </font> <font id="function_return">return time </font>
- ns2Time <font id="function_arguments">(t_ns : REAL) </font> <font id="function_return">return time </font>
- us2Time <font id="function_arguments">(t_us : REAL) </font> <font id="function_return">return time </font>
- ms2Time <font id="function_arguments">(t_ms : REAL) </font> <font id="function_return">return time </font>
- sec2Time <font id="function_arguments">(t_sec : REAL) </font> <font id="function_return">return time </font>
- Hz2Time <font id="function_arguments">(f_Hz : natural) </font> <font id="function_return">return time </font>
</br>**Description**
 convert standard types (NATURAL, REAL) to period (TIME)

- kHz2Time <font id="function_arguments">(f_kHz : natural) </font> <font id="function_return">return time </font>
- MHz2Time <font id="function_arguments">(f_MHz : natural) </font> <font id="function_return">return time </font>
- GHz2Time <font id="function_arguments">(f_GHz : natural) </font> <font id="function_return">return time </font>
- Hz2Time <font id="function_arguments">(f_Hz : REAL) </font> <font id="function_return">return time </font>
- kHz2Time <font id="function_arguments">(f_kHz : REAL) </font> <font id="function_return">return time </font>
- MHz2Time <font id="function_arguments">(f_MHz : REAL) </font> <font id="function_return">return time </font>
- GHz2Time <font id="function_arguments">(f_GHz : REAL) </font> <font id="function_return">return time </font>
- Hz2Freq <font id="function_arguments">(f_Hz : natural) </font> <font id="function_return">return FREQ </font>
</br>**Description**
 convert standard types (NATURAL, REAL) to frequency (FREQ)

- kHz2Freq <font id="function_arguments">(f_kHz : natural) </font> <font id="function_return">return FREQ </font>
- MHz2Freq <font id="function_arguments">(f_MHz : natural) </font> <font id="function_return">return FREQ </font>
- GHz2Freq <font id="function_arguments">(f_GHz : natural) </font> <font id="function_return">return FREQ </font>
- Hz2Freq <font id="function_arguments">(f_Hz : REAL) </font> <font id="function_return">return FREQ </font>
- kHz2Freq <font id="function_arguments">(f_kHz : REAL) </font> <font id="function_return">return FREQ </font>
- MHz2Freq <font id="function_arguments">(f_MHz : REAL) </font> <font id="function_return">return FREQ </font>
- GHz2Freq <font id="function_arguments">(f_GHz : REAL) </font> <font id="function_return">return FREQ </font>
- to_real <font id="function_arguments">(t : time;<br><span style="padding-left:20px">			scale : time) </font> <font id="function_return">return REAL </font>
</br>**Description**
 convert physical types to standard type (REAL)

- to_real <font id="function_arguments">(f : FREQ;<br><span style="padding-left:20px">			scale : FREQ) </font> <font id="function_return">return REAL </font>
- to_real <font id="function_arguments">(br : BAUD;<br><span style="padding-left:20px">			scale : BAUD) </font> <font id="function_return">return REAL </font>
- to_real <font id="function_arguments">(mem : MEMORY;<br><span style="padding-left:20px">	scale : MEMORY) </font> <font id="function_return">return REAL </font>
- to_int <font id="function_arguments">(t : time;<br><span style="padding-left:20px">			scale : time;<br><span style="padding-left:20px">		RoundingStyle : T_ROUNDING_STYLE := ROUND_TO_NEAREST) </font> <font id="function_return">return integer </font>
</br>**Description**
 convert physical types to standard type (INTEGER)

- to_int <font id="function_arguments">(f : FREQ;<br><span style="padding-left:20px">			scale : FREQ;<br><span style="padding-left:20px">		RoundingStyle : T_ROUNDING_STYLE := ROUND_TO_NEAREST) </font> <font id="function_return">return integer </font>
- to_int <font id="function_arguments">(br : BAUD;<br><span style="padding-left:20px">		scale : BAUD;<br><span style="padding-left:20px">		RoundingStyle : T_ROUNDING_STYLE := ROUND_TO_NEAREST) </font> <font id="function_return">return integer </font>
- to_int <font id="function_arguments">(mem : MEMORY;<br><span style="padding-left:20px">	scale : MEMORY;<br><span style="padding-left:20px">	RoundingStyle : T_ROUNDING_STYLE := ROUND_UP) </font> <font id="function_return">return integer </font>
- TimingToCycles <font id="function_arguments">(Timing : time;<br><span style="padding-left:20px"> Clock_Period			: time;<br><span style="padding-left:20px"> RoundingStyle : T_ROUNDING_STYLE := ROUND_UP) </font> <font id="function_return">return natural </font>
</br>**Description**
 calculate needed counter cycles to achieve a given 1. timing/delay and 2. frequency/period

- TimingToCycles <font id="function_arguments">(Timing : time;<br><span style="padding-left:20px"> Clock_Frequency	: FREQ;<br><span style="padding-left:20px"> RoundingStyle : T_ROUNDING_STYLE := ROUND_UP) </font> <font id="function_return">return natural </font>
- CyclesToDelay <font id="function_arguments">(Cycles : natural;<br><span style="padding-left:20px"> Clock_Period			: time) </font> <font id="function_return">return time </font>
- CyclesToDelay <font id="function_arguments">(Cycles : natural;<br><span style="padding-left:20px"> Clock_Frequency	: FREQ) </font> <font id="function_return">return time </font>
- to_string <font id="function_arguments">(t : time;<br><span style="padding-left:20px"> precision : natural) </font> <font id="function_return">return string </font>
</br>**Description**
 convert and format physical types to STRING

- to_string <font id="function_arguments">(f : FREQ;<br><span style="padding-left:20px"> precision : natural) </font> <font id="function_return">return string </font>
- to_string <font id="function_arguments">(br : BAUD;<br><span style="padding-left:20px"> precision : natural) </font> <font id="function_return">return string </font>
- to_string <font id="function_arguments">(mem : MEMORY;<br><span style="padding-left:20px"> precision : natural) </font> <font id="function_return">return string </font>
