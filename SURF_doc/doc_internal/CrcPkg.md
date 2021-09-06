# Package: CrcPkg

- **File**: CrcPkg.vhd
## Functions
- crcByteLookup <font id="function_arguments">(inByte : slv;<br><span style="padding-left:20px"> constant poly : slv) </font> <font id="function_return">return slv </font>
- crcLfsrShift <font id="function_arguments">(lfsr : slv;<br><span style="padding-left:20px"> constant poly : slv;<br><span style="padding-left:20px"> input : sl) </font> <font id="function_return">return slv </font>
- crc32Parallel1Byte <font id="function_arguments">(crcCur : slv(31 downto 0);<br><span style="padding-left:20px"> data : slv(7 downto 0)) </font> <font id="function_return">return slv </font>
</br>**Description**
Specific CRC32 parallel implementations with the standard polynomial: 0x04C11DB7

- crc32Parallel2Byte <font id="function_arguments">(crcCur : slv(31 downto 0);<br><span style="padding-left:20px"> data : slv(15 downto 0)) </font> <font id="function_return">return slv </font>
- crc32Parallel3Byte <font id="function_arguments">(crcCur : slv(31 downto 0);<br><span style="padding-left:20px"> data : slv(23 downto 0)) </font> <font id="function_return">return slv </font>
- crc32Parallel4Byte <font id="function_arguments">(crcCur : slv(31 downto 0);<br><span style="padding-left:20px"> data : slv(31 downto 0)) </font> <font id="function_return">return slv </font>
- crc32Parallel5Byte <font id="function_arguments">(crcCur : slv(31 downto 0);<br><span style="padding-left:20px"> data : slv(39 downto 0)) </font> <font id="function_return">return slv </font>
- crc32Parallel6Byte <font id="function_arguments">(crcCur : slv(31 downto 0);<br><span style="padding-left:20px"> data : slv(47 downto 0)) </font> <font id="function_return">return slv </font>
- crc32Parallel7Byte <font id="function_arguments">(crcCur : slv(31 downto 0);<br><span style="padding-left:20px"> data : slv(55 downto 0)) </font> <font id="function_return">return slv </font>
- crc32Parallel8Byte <font id="function_arguments">(crcCur : slv(31 downto 0);<br><span style="padding-left:20px"> data : slv(63 downto 0)) </font> <font id="function_return">return slv </font>
