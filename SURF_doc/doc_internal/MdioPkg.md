# Package: MdioPkg

## Constants

| Name            | Type            | Value                                                                                                                                                                                                                                                               | Description |
| --------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| MDIO_CMD_INIT_C | MdioCommandType |        (          rdNotWr => '1',<br><span style="padding-left:20px">          phyAddr => (others => '0'),<br><span style="padding-left:20px">          regAddr => (others => '0'),<br><span style="padding-left:20px">          dataOut => (others => '1')       ) |             |
## Types

| Name             | Type                                      | Description                                                                                                                                                                                                 |
| ---------------- | ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MdioCommandType  |                                           | A command to be submitted to the MdioCore.Use the 'mdioReadCommand()/mdioWriteCommand() conveniencefunctions to initialize/create a MdioCommandType object.                                                 |
| MdioInstType     |                                           | An mdio instruction. This record is intended tobe used as an element in a MdioProgramArray whichis a list of MdioCommandTypes amended with a 'last'bit. The 'last' bit marks the last command of asequence. |
| MdioProgramArray | array (natural range <>) of MdioInstType  | PROGRAMS_C is then used as the MDIO_PROG_G generic (MdioSeqCore) andthe indices 'SEQ_1_START_C', 'SEQ_2_START_C' etc. are used toinitiate processing of the respective sequences.                           |
## Functions
- mdioReadCommand <font id="function_arguments">( phyAddr : in natural;<br><span style="padding-left:20px"> regAddr : in natural ) </font> <font id="function_return">return MdioCommandType </font>
**Description**
create a READ command
- mdioWriteCommand <font id="function_arguments">( phyAddr : in natural;<br><span style="padding-left:20px"> regAddr : in natural;<br><span style="padding-left:20px"> dataOut : in slv(15 downto 0) ) </font> <font id="function_return">return MdioCommandType </font>
**Description**
create a WRITE command
- mdioReadInst <font id="function_arguments">( phyAddr : in natural;<br><span style="padding-left:20px"> regAddr : in natural;<br><span style="padding-left:20px"> theLast : in boolean := false ) </font> <font id="function_return">return MdioInstType </font>
**Description**
create/initialize a READ instruction. 'theLast' mustbe set to 'true' if this instruction is the last oneof a sequence.
- mdioWriteInst <font id="function_arguments">( phyAddr : in natural;<br><span style="padding-left:20px"> regAddr : in natural;<br><span style="padding-left:20px"> dataOut : in slv(15 downto 0);<br><span style="padding-left:20px"> theLast : in boolean := false ) </font> <font id="function_return">return MdioInstType </font>
**Description**
create/initialize a WRITE instruction. 'theLast' mustbe set to 'true' if this instruction is the last oneof a sequence.
- mdioProgNumReadTransactions <font id="function_arguments">( prog : in MdioProgramArray ) </font> <font id="function_return">return natural </font>
**Description**
calculate the number of read transactions in a sequence
