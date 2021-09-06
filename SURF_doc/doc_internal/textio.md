# Package: Textio

- **File**: textio.vhdl
## Types

| Name | Type                                               | Description                                                                                                                                                                                                        |
| ---- | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Line |                                                    |                                                                                                                                                                                                                    |
| text |                                                    |   A file of variable-length ASCII records.   Note: in order to work correctly, the TEXT file type must be declared in   the Textio package of library Std.  Otherwise, a file of string has a   non-ASCII format.  |
| side | (right,<br><span style="padding-left:20px"> left)  |  For justifying ouput data within fields.                                                                                                                                                                          |
## Functions
- Justify <font id="function_arguments">(Value: String;<br><span style="padding-left:20px"> Justified : Side := Right;<br><span style="padding-left:20px"> Field: Width := 0 ) </font> <font id="function_return">return String </font>
</br>**Description**
 For specifying widths of output fields.
 standard text files
START-V08

- readline <font id="function_arguments">(variable f: in text;<br><span style="padding-left:20px"> l: inout line) </font> <font id="function_return">return ()</font>
</br>**Description**
V87
- readline <font id="function_arguments">(file f: text;<br><span style="padding-left:20px"> l: inout line) </font> <font id="function_return">return ()</font>
</br>**Description**
!V87
- read <font id="function_arguments">(l: inout line;<br><span style="padding-left:20px"> value: out bit;<br><span style="padding-left:20px"> good: out boolean) </font> <font id="function_return">return ()</font>
</br>**Description**
  For READ procedures:
  In this implementation, any L is accepted (ie, there is no constraints
  on direction, or left bound).  Therefore, even variable of type LINE
  not initialized by READLINE are accepted.  Strictly speaking, this is
  not required by LRM, nor prevented.  However, other implementations may
  fail at parsing such Strings.

  Also, in case of error (GOOD is false), this implementation do not
  modify L (as specified by the LRM) nor VALUE.

  For READ procedures without a GOOD argument, an assertion fails in case
  of error.

  In case of overflow (ie, if the number is out of the bounds of the type),
  the procedure will fail with an execution error.
  FIXME: this should not occur for a bad String.

- read <font id="function_arguments">(l: inout line;<br><span style="padding-left:20px"> value: out bit) </font> <font id="function_return">return ()</font>
- read <font id="function_arguments">(l: inout line;<br><span style="padding-left:20px"> value: out bit_vector;<br><span style="padding-left:20px"> good: out boolean) </font> <font id="function_return">return ()</font>
- read <font id="function_arguments">(l: inout line;<br><span style="padding-left:20px"> value: out bit_vector) </font> <font id="function_return">return ()</font>
- read <font id="function_arguments">(l: inout line;<br><span style="padding-left:20px"> value: out boolean;<br><span style="padding-left:20px"> good: out boolean) </font> <font id="function_return">return ()</font>
- read <font id="function_arguments">(l: inout line;<br><span style="padding-left:20px"> value: out boolean) </font> <font id="function_return">return ()</font>
- read <font id="function_arguments">(l: inout line;<br><span style="padding-left:20px"> value: out character;<br><span style="padding-left:20px"> good: out boolean) </font> <font id="function_return">return ()</font>
- read <font id="function_arguments">(l: inout line;<br><span style="padding-left:20px"> value: out character) </font> <font id="function_return">return ()</font>
- read <font id="function_arguments">(l: inout line;<br><span style="padding-left:20px"> value: out integer;<br><span style="padding-left:20px"> good: out boolean) </font> <font id="function_return">return ()</font>
- read <font id="function_arguments">(l: inout line;<br><span style="padding-left:20px"> value: out integer) </font> <font id="function_return">return ()</font>
- read <font id="function_arguments">(l: inout line;<br><span style="padding-left:20px"> value: out real;<br><span style="padding-left:20px"> good: out boolean) </font> <font id="function_return">return ()</font>
- read <font id="function_arguments">(l: inout line;<br><span style="padding-left:20px"> value: out real) </font> <font id="function_return">return ()</font>
- read <font id="function_arguments">(l: inout line;<br><span style="padding-left:20px"> value: out String;<br><span style="padding-left:20px"> good: out boolean) </font> <font id="function_return">return ()</font>
- read <font id="function_arguments">(l: inout line;<br><span style="padding-left:20px"> value: out String) </font> <font id="function_return">return ()</font>
- read <font id="function_arguments">(l: inout line;<br><span style="padding-left:20px"> value: out time;<br><span style="padding-left:20px"> good: out boolean) </font> <font id="function_return">return ()</font>
</br>**Description**
  This implementation requires no space after the unit identifier,
  ie "7.5 nsv" is parsed as 7.5 ns.
  The unit identifier can be in lower case, upper case or mixed case.

- read <font id="function_arguments">(l: inout line;<br><span style="padding-left:20px"> value: out time) </font> <font id="function_return">return ()</font>
- Sread <font id="function_arguments">(L : inout Line;<br><span style="padding-left:20px"> Value : out String;<br><span style="padding-left:20px"> Strlen : out Natural) </font> <font id="function_return">return ()</font>
</br>**Description**
START-V08

- Oread <font id="function_arguments">(L : inout Line;<br><span style="padding-left:20px"> Value : out Bit_Vector;<br><span style="padding-left:20px"> Good : out Boolean) </font> <font id="function_return">return ()</font>
- Oread <font id="function_arguments">(L : inout Line;<br><span style="padding-left:20px"> Value : out Bit_Vector) </font> <font id="function_return">return ()</font>
- Hread <font id="function_arguments">(L : inout Line;<br><span style="padding-left:20px"> Value : out Bit_Vector;<br><span style="padding-left:20px"> Good : out Boolean) </font> <font id="function_return">return ()</font>
- Hread <font id="function_arguments">(L : inout Line;<br><span style="padding-left:20px"> Value : out Bit_Vector) </font> <font id="function_return">return ()</font>
- writeline <font id="function_arguments">(variable f: out text;<br><span style="padding-left:20px"> l: inout line) </font> <font id="function_return">return ()</font>
</br>**Description**
V87
- writeline <font id="function_arguments">(file f: text;<br><span style="padding-left:20px"> l: inout line) </font> <font id="function_return">return ()</font>
</br>**Description**
!V87
- Tee <font id="function_arguments">(file f : Text;<br><span style="padding-left:20px"> L : inout LINE) </font> <font id="function_return">return ()</font>
</br>**Description**
START-V08

- write <font id="function_arguments">(l: inout line;<br><span style="padding-left:20px"> value: in bit;<br><span style="padding-left:20px"> justified: in side := right;<br><span style="padding-left:20px"> field: in width := 0) </font> <font id="function_return">return ()</font>
</br>**Description**
END-V08
  This implementation accept any value for all the types.

- write <font id="function_arguments">(l: inout line;<br><span style="padding-left:20px"> value: in bit_vector;<br><span style="padding-left:20px"> justified: in side := right;<br><span style="padding-left:20px"> field: in width := 0) </font> <font id="function_return">return ()</font>
- write <font id="function_arguments">(l: inout line;<br><span style="padding-left:20px"> value: in boolean;<br><span style="padding-left:20px"> justified: in side := right;<br><span style="padding-left:20px"> field: in width := 0) </font> <font id="function_return">return ()</font>
- write <font id="function_arguments">(l: inout line;<br><span style="padding-left:20px"> value: in character;<br><span style="padding-left:20px"> justified: in side := right;<br><span style="padding-left:20px"> field: in width := 0) </font> <font id="function_return">return ()</font>
- write <font id="function_arguments">(l: inout line;<br><span style="padding-left:20px"> value: in integer;<br><span style="padding-left:20px"> justified: in side := right;<br><span style="padding-left:20px"> field: in width := 0) </font> <font id="function_return">return ()</font>
- write <font id="function_arguments">(L: inout line;<br><span style="padding-left:20px"> value: in real;<br><span style="padding-left:20px"> justified: in side := right;<br><span style="padding-left:20px"> field: in width := 0;<br><span style="padding-left:20px"> digits: in natural := 0) </font> <font id="function_return">return ()</font>
- write <font id="function_arguments">(l: inout line;<br><span style="padding-left:20px"> value: in String;<br><span style="padding-left:20px"> justified: in side := right;<br><span style="padding-left:20px"> field: in width := 0) </font> <font id="function_return">return ()</font>
- write <font id="function_arguments">(l: inout line;<br><span style="padding-left:20px"> value : in time;<br><span style="padding-left:20px"> justified: in side := right;<br><span style="padding-left:20px"> field: in width := 0;<br><span style="padding-left:20px"> unit : in TIME := ns) </font> <font id="function_return">return ()</font>
</br>**Description**
  UNIT must be a unit name declared in std.standard.  Of course, no rules
  in the core VHDL language prevent you from using a value that is not a
  unit (eg: 10 ns or even 5 fs).
  An assertion error message is generated in this case, and question mark
  (?) is written at the place of the unit name.

- Owrite <font id="function_arguments">(L : inout line;<br><span style="padding-left:20px"> value : in Bit_Vector;<br><span style="padding-left:20px"> Justified : in Side := Right;<br><span style="padding-left:20px"> Field : in Width := 0) </font> <font id="function_return">return ()</font>
- Hwrite <font id="function_arguments">(L : inout line;<br><span style="padding-left:20px"> value : in Bit_Vector;<br><span style="padding-left:20px"> Justified : in Side := Right;<br><span style="padding-left:20px"> Field : in Width := 0) </font> <font id="function_return">return ()</font>
