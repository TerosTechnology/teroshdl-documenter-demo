# Package: Code8b10bPkg

## Constants

| Name     | Type            | Value       | Description         |
| -------- | --------------- | ----------- | ------------------- |
| K_28_0_C | slv(7 downto 0) |  "00011100" | K28.0, 0x1C         |
| K_28_1_C | slv(7 downto 0) |  "00111100" | K28.1, 0x3C (Comma) |
| K_28_2_C | slv(7 downto 0) |  "01011100" | K28.2, 0x5C         |
| K_28_3_C | slv(7 downto 0) |  "01111100" | K28.3, 0x7C         |
| K_28_4_C | slv(7 downto 0) |  "10011100" | K28.4, 0x9C         |
| K_28_5_C | slv(7 downto 0) |  "10111100" | K28.5, 0xBC (Comma) |
| K_28_6_C | slv(7 downto 0) |  "11011100" | K28.6, 0xDC         |
| K_28_7_C | slv(7 downto 0) |  "11111100" | K28.7, 0xFC (Comma) |
| K_23_7_C | slv(7 downto 0) |  "11110111" | K23.7, 0xF7         |
| K_27_7_C | slv(7 downto 0) |  "11111011" | K27.7, 0xFB         |
| K_29_7_C | slv(7 downto 0) |  "11111101" | K29.7, 0xFD         |
| K_30_7_C | slv(7 downto 0) |  "11111110" | K30.7, 0xFE         |
| D_10_2_C | slv(7 downto 0) |  "01001010" | D10.2, 0x4A         |
| D_21_5_C | slv(7 downto 0) |  "10110101" | D21.5, 0xB5         |
## Functions
- encode8b10b <font id="function_arguments">( dataIn  : in  slv(7 downto 0);<br><span style="padding-left:20px"> dataKIn : in  sl;<br><span style="padding-left:20px"> dispIn  : in  sl;<br><span style="padding-left:20px"> dataOut : out slv(9 downto 0);<br><span style="padding-left:20px"> dispOut : out sl) </font> <font id="function_return">return ()</font>
- decode8b10b <font id="function_arguments">( dataIn   : in  slv(9 downto 0);<br><span style="padding-left:20px"> dispIn   : in  sl;<br><span style="padding-left:20px"> dataOut  : out slv(7 downto 0);<br><span style="padding-left:20px"> dataKOut : out sl;<br><span style="padding-left:20px"> dispOut  : out sl;<br><span style="padding-left:20px"> codeErr  : out sl;<br><span style="padding-left:20px"> dispErr  : out sl) </font> <font id="function_return">return ()</font>
