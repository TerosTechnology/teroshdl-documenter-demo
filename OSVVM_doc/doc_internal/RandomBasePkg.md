# Package: RandomBasePkg
## Description
comment out following 2 lines with VHDL-2008.  Leave in for VHDL-2002 
library ieee_proposed ;						          -- remove with VHDL-2008
use ieee_proposed.standard_additions.all ;   -- remove with VHDL-2008

## Types
| Name           | Type | Description |
| -------------- | ---- | ----------- |
| RandomSeedType |      |             |
## Functions
- Uniform <font id="function_arguments">(Result : out real ;  Seed : inout RandomSeedType)</font> <font id="function_return">return ()</font>
- to_string <font id="function_arguments">(A : RandomSeedType)</font> <font id="function_return">return string</font>
**Description**
IO for RandomSeedType.  If use subtype, then create aliases herein a similar fashion VHDL-2008 std_logic_textio.Not required by RandomPkg
- write <font id="function_arguments">(variable L: inout line ; A : RandomSeedType )</font> <font id="function_return">return ()</font>
- read <font id="function_arguments">(variable L: inout line ; A : out RandomSeedType ; good : out boolean )</font> <font id="function_return">return ()</font>
- read <font id="function_arguments">(variable L: inout line ; A : out RandomSeedType )</font> <font id="function_return">return ()</font>
