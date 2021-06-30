# Package: RandomPkg

## Description

comment out following 3 lines with VHDL-2008.  Leave in for VHDL-2002
library ieee_proposed ;						               -- remove with VHDL-2008
use ieee_proposed.standard_additions.all ;        -- remove with VHDL-2008
use ieee_proposed.standard_textio_additions.all ; -- remove with VHDL-2008

## Constants

| Name      | Type                             | Value          | Description |
| --------- | -------------------------------- | -------------- | ----------- |
| NULL_INTV | integer_vector (NULL_RANGE_TYPE) |  (others => 0) |             |
## Types

| Name             | Type                                                      | Description                                                                                |
| ---------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| DistRecType      |                                                           | Supports DistValInt functionality                                                          |
| DistType         |                                                           |                                                                                            |
| NaturalVBoolType |                                                           | Weight vectors not indexed by integers                                                     |
| NaturalVSlType   |                                                           |                                                                                            |
| NaturalVBitType  |                                                           |                                                                                            |
| RandomDistType   | (NONE, UNIFORM, FAVOR_SMALL, FAVOR_BIG, NORMAL, POISSON)  | Parameters for randomizationRandomDistType specifies the distribution to use for randomize |
| RandomParmType   |                                                           |                                                                                            |
| RandomPType      |                                                           |                                                                                            |
## Functions
- to_string <font id="function_arguments">(A : RandomDistType) </font> <font id="function_return">return string </font>
**Description**
RandomParm IO
- write <font id="function_arguments">(variable L : inout line ; A : RandomDistType ) </font> <font id="function_return">return ()</font>
- read <font id="function_arguments">(variable L : inout line ; A : out RandomDistType ; good : out boolean ) </font> <font id="function_return">return ()</font>
- read <font id="function_arguments">(variable L : inout line ; A : out RandomDistType ) </font> <font id="function_return">return ()</font>
- to_string <font id="function_arguments">(A : RandomParmType) </font> <font id="function_return">return string </font>
- write <font id="function_arguments">(variable L : inout line ; A : RandomParmType ) </font> <font id="function_return">return ()</font>
- read <font id="function_arguments">(variable L : inout line ; A : out RandomParmType ; good : out boolean ) </font> <font id="function_return">return ()</font>
- read <font id="function_arguments">(variable L : inout line ; A : out RandomParmType ) </font> <font id="function_return">return ()</font>
