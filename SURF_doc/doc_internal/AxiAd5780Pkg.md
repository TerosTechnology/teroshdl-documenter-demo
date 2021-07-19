# Package: AxiAd5780Pkg

- **File**: AxiAd5780Pkg.vhd
## Constants

| Name                     | Type                | Value                                                                                                                                                                                                                                                                                                                                                                          | Description |
| ------------------------ | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| AXI_AD5780_IN_INIT_C     | AxiAd5780InType     |  (dacSdo => '1')                                                                                                                                                                                                                                                                                                                                                               |             |
| AXI_AD5780_OUT_INIT_C    | AxiAd5780OutType    |  (       '1',<br><span style="padding-left:20px">       '1',<br><span style="padding-left:20px">       '1',<br><span style="padding-left:20px">       '1',<br><span style="padding-left:20px">       '1',<br><span style="padding-left:20px">       '1')                                                                                                                       |             |
| AXI_AD5780_STATUS_INIT_C | AxiAd5780StatusType |  (       '0',<br><span style="padding-left:20px">       (others => '0'))                                                                                                                                                                                                                                                                                                       |             |
| AXI_AD5780_CONFIG_INIT_C | AxiAd5780ConfigType |  (       (others => '1'),<br><span style="padding-left:20px">       '1',<br><span style="padding-left:20px">       '0',<br><span style="padding-left:20px">       '0',<br><span style="padding-left:20px">       '0',<br><span style="padding-left:20px">       '1',<br><span style="padding-left:20px">       '0',<br><span style="padding-left:20px">       (others => '0')) |             |
## Types

| Name                    | Type                                                                                             | Description |
| ----------------------- | ------------------------------------------------------------------------------------------------ | ----------- |
| AxiAd5780InType         |                                                                                                  |             |
| AxiAd5780InArray        | array (natural range <>) of AxiAd5780InType                                                      |             |
| AxiAd5780InVectorArray  | array (integer range<>,<br><span style="padding-left:20px"> integer range<>)of AxiAd5780InType   |             |
| AxiAd5780OutType        |                                                                                                  |             |
| AxiAd5780OutArray       | array (natural range <>) of AxiAd5780OutType                                                     |             |
| AxiAd5780OutVectorArray | array (integer range<>,<br><span style="padding-left:20px"> integer range<>)of AxiAd5780OutType  |             |
| AxiAd5780StatusType     |                                                                                                  |             |
| AxiAd5780ConfigType     |                                                                                                  |             |
