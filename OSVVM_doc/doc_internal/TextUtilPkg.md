# Package: TextUtilPkg
## Functions
- IsUpper <font id="function_arguments">(constant Char : character )</font> <font id="function_return">return boolean</font>
- IsLower <font id="function_arguments">(constant Char : character )</font> <font id="function_return">return boolean</font>
- to_lower <font id="function_arguments">(constant Char : character )</font> <font id="function_return">return character</font>
- to_lower <font id="function_arguments">(constant Str : string )</font> <font id="function_return">return string</font>
- to_upper <font id="function_arguments">(constant Char : character )</font> <font id="function_return">return character</font>
- to_upper <font id="function_arguments">(constant Str : string )</font> <font id="function_return">return string</font>
- IsHex <font id="function_arguments">(constant Char : character )</font> <font id="function_return">return boolean</font>
- IsNumber <font id="function_arguments">(constant Char : character )</font> <font id="function_return">return boolean</font>
- IsNumber <font id="function_arguments">(Name : string )</font> <font id="function_return">return boolean</font>
- isstd_logic <font id="function_arguments">(constant Char : character )</font> <font id="function_return">return boolean</font>
- IfElse <font id="function_arguments">(Expr : boolean ; A, B : string)</font> <font id="function_return">return string</font>
**Description**
Crutch until VHDL-2019 conditional initialization
- SkipWhiteSpace <font id="function_arguments">(  
    variable L     : InOut line ;
    variable Empty : out   boolean
  )</font> <font id="function_return">return ()</font>
- SkipWhiteSpace <font id="function_arguments">(variable L : InOut line)</font> <font id="function_return">return ()</font>
- EmptyOrCommentLine <font id="function_arguments">(  
    variable L                : InOut  line ;
    variable Empty            : InOut  boolean ;
    variable MultiLineComment : inout  boolean 
  )</font> <font id="function_return">return ()</font>
- ReadUntilDelimiterOrEOL <font id="function_arguments">(  
    variable L         : InOut line ; 
    variable Name      : InOut line ; 
    constant Delimiter : In    character ;
    variable ReadValid : Out   boolean 
  )</font> <font id="function_return">return ()</font>
- FindDelimiter <font id="function_arguments">(  
    variable L                : InOut line ; 
    constant Delimiter        : In    character ;
    variable Found            : Out   boolean 
  )</font> <font id="function_return">return ()</font>
- ReadHexToken <font id="function_arguments">(   Reads Upto Result'length values, less is ok.
   Does not skip white space
  
    variable L      : InOut line ;
    variable Result : Out   std_logic_vector ;
    variable StrLen : Out   integer 
  )</font> <font id="function_return">return ()</font>
- ReadBinaryToken <font id="function_arguments">(   Reads Upto Result'length values, less is ok.
   Does not skip white space
  
    variable L      : InOut line ;
    variable Result : Out   std_logic_vector ;
    variable StrLen : Out   integer 
  )</font> <font id="function_return">return ()</font>
