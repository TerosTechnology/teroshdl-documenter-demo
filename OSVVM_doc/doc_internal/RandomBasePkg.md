# Package: RandomBasePkg

- **File**: RandomBasePkg.vhd
## Description

 comment out following 2 lines with VHDL-2008.  Leave in for VHDL-2002 
 library ieee_proposed ;						          -- remove with VHDL-2008
 use ieee_proposed.standard_additions.all ;   -- remove with VHDL-2008

## Constants

| Name                     | Type                             | Value              | Description |
| ------------------------ | -------------------------------- | ------------------ | ----------- |
| OSVVM_RANDOM_ALERTLOG_ID | AlertLogIDType                   |  OSVVM_ALERTLOG_ID |             |
| NULL_INTV                | integer_vector (NULL_RANGE_TYPE) |  (others => 0)     |             |
## Types

| Name           | Type                                                                                                                                                                                                                                          | Description                                                                                                            |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| RandomSeedType |                                                                                                                                                                                                                                               | ---------------------------------------------------------------  RandomSeedType - Abstract the type for randomization  |
| RandomDistType | (NONE,<br><span style="padding-left:20px"> UNIFORM,<br><span style="padding-left:20px"> FAVOR_SMALL,<br><span style="padding-left:20px"> FAVOR_BIG,<br><span style="padding-left:20px"> NORMAL,<br><span style="padding-left:20px"> POISSON)  | --------------------------------------------------------------- - Distribution Types and read/write procedures         |
| RandomParmType |                                                                                                                                                                                                                                               |                                                                                                                        |
## Functions
- Uniform <font id="function_arguments">(Result : out real ;<br><span style="padding-left:20px">  Seed : inout RandomSeedType) </font> <font id="function_return">return ()</font>
**Description**
---------------------------------------------------------------
 Uniform
   Generate a random number with a Uniform distribution
   Required by RandomPkg.  All randomization is derived from here.
   Value produced must be either: 
     0 <= Value < 1  or  0 < Value < 1

   Current version uses ieee.math_real.Uniform
   This abstraction allows higher precision version 
   of a uniform distribution to be used provided


- to_string <font id="function_arguments">(A : RandomSeedType) </font> <font id="function_return">return string </font>
**Description**
---------------------------------------------------------------
- RandomSeedType IO

- write <font id="function_arguments">(variable L: inout line ;<br><span style="padding-left:20px"> A : RandomSeedType ) </font> <font id="function_return">return ()</font>
- read <font id="function_arguments">(variable L: inout line ;<br><span style="padding-left:20px"> A : out RandomSeedType ;<br><span style="padding-left:20px"> good : out boolean ) </font> <font id="function_return">return ()</font>
- read <font id="function_arguments">(variable L: inout line ;<br><span style="padding-left:20px"> A : out RandomSeedType ) </font> <font id="function_return">return ()</font>
- to_string <font id="function_arguments">(A : RandomDistType) </font> <font id="function_return">return string </font>
**Description**
---------------------------------------------------------------
 RandomParm IO

- write <font id="function_arguments">(variable L : inout line ;<br><span style="padding-left:20px"> A : RandomDistType ) </font> <font id="function_return">return ()</font>
- read <font id="function_arguments">(variable L : inout line ;<br><span style="padding-left:20px"> A : out RandomDistType ;<br><span style="padding-left:20px"> good : out boolean ) </font> <font id="function_return">return ()</font>
- read <font id="function_arguments">(variable L : inout line ;<br><span style="padding-left:20px"> A : out RandomDistType ) </font> <font id="function_return">return ()</font>
- to_string <font id="function_arguments">(A : RandomParmType) </font> <font id="function_return">return string </font>
- write <font id="function_arguments">(variable L : inout line ;<br><span style="padding-left:20px"> A : RandomParmType ) </font> <font id="function_return">return ()</font>
- read <font id="function_arguments">(variable L : inout line ;<br><span style="padding-left:20px"> A : out RandomParmType ;<br><span style="padding-left:20px"> good : out boolean ) </font> <font id="function_return">return ()</font>
- read <font id="function_arguments">(variable L : inout line ;<br><span style="padding-left:20px"> A : out RandomParmType ) </font> <font id="function_return">return ()</font>
- Scale <font id="function_arguments">(A,<br><span style="padding-left:20px"> Min,<br><span style="padding-left:20px"> Max : real) </font> <font id="function_return">return real </font>
**Description**
---------------------------------------------------------------
-  Randomization Support
-    Scale                - Scale a value to be within a given range
-    FavorSmall, FavorBig - Distribution Support
-    RemoveExclude 

- Scale <font id="function_arguments">(A : real ;<br><span style="padding-left:20px"> Min,<br><span style="padding-left:20px"> Max : integer) </font> <font id="function_return">return integer </font>
- FavorSmall <font id="function_arguments">(A : real) </font> <font id="function_return">return real </font>
- FavorBig <font id="function_arguments">(A : real) </font> <font id="function_return">return real </font>
- to_time_vector <font id="function_arguments">(A : integer_vector ;<br><span style="padding-left:20px"> Unit : time) </font> <font id="function_return">return time_vector </font>
- to_integer_vector <font id="function_arguments">(A : time_vector ;<br><span style="padding-left:20px"> Unit : time) </font> <font id="function_return">return integer_vector </font>
- RemoveExclude <font id="function_arguments">(A,<br><span style="padding-left:20px"> Exclude : integer_vector ;<br><span style="padding-left:20px"> variable NewA : out integer_vector ;<br><span style="padding-left:20px"> variable NewALength : inout natural ) </font> <font id="function_return">return ()</font>
- inside <font id="function_arguments">(A : real ;<br><span style="padding-left:20px"> Exclude : real_vector) </font> <font id="function_return">return boolean </font>
- RemoveExclude <font id="function_arguments">(A,<br><span style="padding-left:20px"> Exclude : real_vector ;<br><span style="padding-left:20px"> variable NewA : out real_vector ;<br><span style="padding-left:20px"> variable NewALength : inout natural ) </font> <font id="function_return">return ()</font>
- inside <font id="function_arguments">(A : time ;<br><span style="padding-left:20px"> Exclude : time_vector) </font> <font id="function_return">return boolean </font>
- RemoveExclude <font id="function_arguments">(A,<br><span style="padding-left:20px"> Exclude : time_vector ;<br><span style="padding-left:20px"> variable NewA : out time_vector ;<br><span style="padding-left:20px"> variable NewALength : inout natural ) </font> <font id="function_return">return ()</font>
