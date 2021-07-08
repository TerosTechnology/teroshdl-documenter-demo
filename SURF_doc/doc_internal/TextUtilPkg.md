# Package: TextUtilPkg

## Functions
- print <font id="function_arguments">(text : string) </font> <font id="function_return">return ()</font>
- print <font id="function_arguments">(active : boolean;<br><span style="padding-left:20px"> text : string) </font> <font id="function_return">return ()</font>
**Description**
prints the message when activeuseful for debug switches
- chr <font id="function_arguments">(sl : std_logic) </font> <font id="function_return">return character </font>
**Description**
converts std_logic into a character
- str <font id="function_arguments">(sl : std_logic) </font> <font id="function_return">return string </font>
**Description**
converts std_logic into a string (1 to 1)
- str <font id="function_arguments">(slv : std_logic_vector) </font> <font id="function_return">return string </font>
**Description**
converts std_logic_vector into a string (binary base)
- str <font id="function_arguments">(b : boolean) </font> <font id="function_return">return string </font>
**Description**
converts boolean into a string
- chr <font id="function_arguments">(int : integer) </font> <font id="function_return">return character </font>
**Description**
converts an integer into a single character(can also be used for hex conversion and other bases)
- int <font id="function_arguments">(c : character) </font> <font id="function_return">return integer </font>
**Description**
Converts a character into an integer
- str <font id="function_arguments">(int : integer;<br><span style="padding-left:20px"> base : integer) </font> <font id="function_return">return string </font>
**Description**
converts integer into string using specified base
- int <font id="function_arguments">(s : string;<br><span style="padding-left:20px"> base : integer) </font> <font id="function_return">return integer </font>
**Description**
converts a string with specified base into an integer
- str <font id="function_arguments">(int : integer) </font> <font id="function_return">return string </font>
**Description**
converts integer to string, using base 10
- str <font id="function_arguments">(tim : time) </font> <font id="function_return">return string </font>
**Description**
converts a time to a string
- hstr <font id="function_arguments">(slv : std_logic_vector) </font> <font id="function_return">return string </font>
**Description**
convert std_logic_vector into a string in hex format
- toUpper <font id="function_arguments">(c : character) </font> <font id="function_return">return character </font>
**Description**
convert a character to upper case
- toLower <font id="function_arguments">(c : character) </font> <font id="function_return">return character </font>
**Description**
convert a character to lower case
- toUpper <font id="function_arguments">(s : string) </font> <font id="function_return">return string </font>
**Description**
convert a string to upper case
- toLower <font id="function_arguments">(s : string) </font> <font id="function_return">return string </font>
**Description**
convert a string to lower case
- isWhitespace <font id="function_arguments">(c : character) </font> <font id="function_return">return boolean </font>
**Description**
checks if whitespace (JFF)
- strip <font id="function_arguments">(s : string) </font> <font id="function_return">return string </font>
**Description**
remove leading whitespace (JFF)
- firstString <font id="function_arguments">(s : string) </font> <font id="function_return">return string </font>
**Description**
return first nonwhitespace substring (JFF)
- chomp <font id="function_arguments">(variable s : inout string;<br><span style="padding-left:20px"> variable shead : out string) </font> <font id="function_return">return ()</font>
**Description**
finds the first non-whitespace substring in a string and (JFF)returns both the substring and the original with the substring removed
- toSl <font id="function_arguments">(c : character) </font> <font id="function_return">return std_logic </font>
**Description**
converts a character into std_logic
- toSlv <font id="function_arguments">(s : string) </font> <font id="function_return">return std_logic_vector </font>
**Description**
converts a string into std_logic_vector
- strRead <font id="function_arguments">(file in_file :     text;<br><span style="padding-left:20px"> res_string   : out string) </font> <font id="function_return">return ()</font>
**Description**
read variable length string from input file
- print <font id="function_arguments">(file out_file :    text;<br><span style="padding-left:20px"> new_string    : in string) </font> <font id="function_return">return ()</font>
**Description**
print string to a file and start new line
- print <font id="function_arguments">(file out_file :    text;<br><span style="padding-left:20px"> char          : in character) </font> <font id="function_return">return ()</font>
**Description**
print character to a file and start new line
