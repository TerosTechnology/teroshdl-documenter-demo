# Package: AxiRssiPkg

- **File**: AxiRssiPkg.vhd
## Constants

| Name              | Type          | Value                                                                                                                                                                                                                                                                                      | Description |
| ----------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| RSSI_AXI_CONFIG_C | AxiConfigType |  (       ADDR_WIDTH_C => 13,<br><span style="padding-left:20px">               -- 2^13 = 8kB buffer       DATA_BYTES_C => 8,<br><span style="padding-left:20px">                -- 8 bytes = 64-bits       ID_BITS_C    => 2,<br><span style="padding-left:20px">       LEN_BITS_C   => 7) |             |
## Functions
- GetRssiCsum <font id="function_arguments">(              -- 2 clock cycle latency calculation init     : in    sl;<br><span style="padding-left:20px"> header   : in    slv(63 downto 0);<br><span style="padding-left:20px"> accumReg : in    slv(20 downto 0);<br><span style="padding-left:20px"> accumVar : inout slv(20 downto 0);<br><span style="padding-left:20px"> chksumOk : inout sl;<br><span style="padding-left:20px"> checksum : inout slv(15 downto 0)) </font> <font id="function_return">return ()</font>
**Description**
Up to 1kB bursting
