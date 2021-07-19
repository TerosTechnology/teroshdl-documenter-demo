# Package: AxiXcf128Pkg

- **File**: AxiXcf128Pkg.vhd
## Constants

| Name                     | Type                | Value                                                                                                                                                                                                                                                                                                                           | Description |
| ------------------------ | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| AXI_XCF128_IN_OUT_INIT_C | AxiXcf128InOutType  |  (       data => (others => 'Z'))                                                                                                                                                                                                                                                                                               |             |
| AXI_XCF128_OUT_INIT_C    | AxiXcf128OutType    |  (       '1',<br><span style="padding-left:20px">       '1',<br><span style="padding-left:20px">       '1',<br><span style="padding-left:20px">       '1',<br><span style="padding-left:20px">       (others => '1'))                                                                                                           |             |
| AXI_XCF128_STATUS_INIT_C | AxiXcf128StatusType |  (       data => (others => '1'))                                                                                                                                                                                                                                                                                               |             |
| AXI_XCF128_CONFIG_INIT_C | AxiXcf128ConfigType |  (       '1',<br><span style="padding-left:20px">       '1',<br><span style="padding-left:20px">       '1',<br><span style="padding-left:20px">       '0',<br><span style="padding-left:20px">       (others => '1'),<br><span style="padding-left:20px">       '1',<br><span style="padding-left:20px">       (others => '1')) |             |
## Types

| Name                      | Type                                                                                               | Description |
| ------------------------- | -------------------------------------------------------------------------------------------------- | ----------- |
| AxiXcf128InOutType        |                                                                                                    |             |
| AxiXcf128InOutArray       | array (natural range <>) of AxiXcf128InOutType                                                     |             |
| AxiXcf128InOutVectorArray | array (integer range<>,<br><span style="padding-left:20px"> integer range<>)of AxiXcf128InOutType  |             |
| AxiXcf128OutType          |                                                                                                    |             |
| AxiXcf128OutArray         | array (natural range <>) of AxiXcf128OutType                                                       |             |
| AxiXcf128OutVectorArray   | array (integer range<>,<br><span style="padding-left:20px"> integer range<>)of AxiXcf128OutType    |             |
| AxiXcf128StatusType       |                                                                                                    |             |
| AxiXcf128ConfigType       |                                                                                                    |             |
