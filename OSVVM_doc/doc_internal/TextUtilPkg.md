# Package: TextUtilPkg

- **File**: TextUtilPkg.vhd
## Functions
- IsUpper <font id="function_arguments">(constant Char : character ) </font> <font id="function_return">return boolean </font>
- IsLower <font id="function_arguments">(constant Char : character ) </font> <font id="function_return">return boolean </font>
- to_lower <font id="function_arguments">(constant Char : character ) </font> <font id="function_return">return character </font>
- to_lower <font id="function_arguments">(constant Str : string ) </font> <font id="function_return">return string </font>
- to_upper <font id="function_arguments">(constant Char : character ) </font> <font id="function_return">return character </font>
- to_upper <font id="function_arguments">(constant Str : string ) </font> <font id="function_return">return string </font>
- IsHex <font id="function_arguments">(constant Char : character ) </font> <font id="function_return">return boolean </font>
- IsNumber <font id="function_arguments">(constant Char : character ) </font> <font id="function_return">return boolean </font>
- IsNumber <font id="function_arguments">(Name : string ) </font> <font id="function_return">return boolean </font>
- isstd_logic <font id="function_arguments">(constant Char : character ) </font> <font id="function_return">return boolean </font>
- IfElse <font id="function_arguments">(Expr : boolean ;<br><span style="padding-left:20px"> A,<br><span style="padding-left:20px"> B : string) </font> <font id="function_return">return string </font>
</br>**Description**
 Crutch until VHDL-2019 conditional initialization

- SkipWhiteSpace <font id="function_arguments">( variable L     : InOut line ;<br><span style="padding-left:20px"> variable Empty : out   boolean ) </font> <font id="function_return">return ()</font>
</br>**Description**
----------------------------------------------------------

- SkipWhiteSpace <font id="function_arguments">(variable L : InOut line) </font> <font id="function_return">return ()</font>
- EmptyOrCommentLine <font id="function_arguments">( variable L                : InOut  line ;<br><span style="padding-left:20px"> variable Empty            : InOut  boolean ;<br><span style="padding-left:20px"> variable MultiLineComment : inout  boolean ) </font> <font id="function_return">return ()</font>
</br>**Description**
----------------------------------------------------------

- ReadUntilDelimiterOrEOL <font id="function_arguments">( variable L         : InOut line ;<br><span style="padding-left:20px"> variable Name      : InOut line ;<br><span style="padding-left:20px"> constant Delimiter : In    character ;<br><span style="padding-left:20px"> variable ReadValid : Out   boolean ) </font> <font id="function_return">return ()</font>
</br>**Description**
----------------------------------------------------------

- FindDelimiter <font id="function_arguments">( variable L                : InOut line ;<br><span style="padding-left:20px"> constant Delimiter        : In    character ;<br><span style="padding-left:20px"> variable Found            : Out   boolean ) </font> <font id="function_return">return ()</font>
</br>**Description**
----------------------------------------------------------

- ReadHexToken <font id="function_arguments">( variable L      : InOut line ;<br><span style="padding-left:20px"> variable Result : Out   std_logic_vector ;<br><span style="padding-left:20px"> variable StrLen : Out   integer ) </font> <font id="function_return">return ()</font>
</br>**Description**
----------------------------------------------------------

- ReadBinaryToken <font id="function_arguments">( variable L      : InOut line ;<br><span style="padding-left:20px"> variable Result : Out   std_logic_vector ;<br><span style="padding-left:20px"> variable StrLen : Out   integer ) </font> <font id="function_return">return ()</font>
</br>**Description**
----------------------------------------------------------

