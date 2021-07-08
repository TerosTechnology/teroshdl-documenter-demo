# Package: AxiLtc2270Pkg

## Constants

| Name                         | Type                   | Value                                                                                                                                                                                                                                                                                                    | Description |
| ---------------------------- | ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| AXI_LTC2270_IN_INIT_C        | AxiLtc2270InType       |  (       '1',<br><span style="padding-left:20px">       '0',<br><span style="padding-left:20px">       (others => (others => '1')),<br><span style="padding-left:20px">       (others => (others => '0')),<br><span style="padding-left:20px">       '1',<br><span style="padding-left:20px">       '0') |             |
| AXI_LTC2270_IN_OUT_INIT_C    | AxiLtc2270InOutType    |  (sdo => 'Z')                                                                                                                                                                                                                                                                                            |             |
| AXI_LTC2270_OUT_INIT_C       | AxiLtc2270OutType      |  (       '0',<br><span style="padding-left:20px">       '0',<br><span style="padding-left:20px">       '0',<br><span style="padding-left:20px">       '0',<br><span style="padding-left:20px">       '1',<br><span style="padding-left:20px">       '0')                                                 |             |
| AXI_LTC2270_DELAY_IN_INIT_C  | AxiLtc2270DelayInType  |  (       '0',<br><span style="padding-left:20px">       '0',<br><span style="padding-left:20px">       (others => (others => (others => '0'))))                                                                                                                                                          |             |
| AXI_LTC2270_DELAY_OUT_INIT_C | AxiLtc2270DelayOutType |  (       '0',<br><span style="padding-left:20px">       (others => (others => (others => '0'))))                                                                                                                                                                                                         |             |
| AXI_LTC2270_CONFIG_INIT_C    | AxiLtc2270ConfigType   |  (       (others => '0'),<br><span style="padding-left:20px">       AXI_LTC2270_DELAY_IN_INIT_C)                                                                                                                                                                                                         |             |
| AXI_LTC2270_STATUS_INIT_C    | AxiLtc2270StatusType   |  (       (others => '0'),<br><span style="padding-left:20px">       (others => x"0000"),<br><span style="padding-left:20px">       AXI_LTC2270_DELAY_OUT_INIT_C)                                                                                                                                         |             |
## Types

| Name                   | Type                                             | Description |
| ---------------------- | ------------------------------------------------ | ----------- |
| AxiLtc2270InType       |                                                  |             |
| AxiLtc2270InArray      | array (natural range <>) of AxiLtc2270InType     |             |
| AxiLtc2270InOutType    |                                                  |             |
| AxiLtc2270InOutArray   | array (natural range <>) of AxiLtc2270InOutType  |             |
| AxiLtc2270OutType      |                                                  |             |
| AxiLtc2270OutArray     | array (natural range <>) of AxiLtc2270OutType    |             |
| AxiLtc2270DelayInType  |                                                  |             |
| AxiLtc2270DelayOutType |                                                  |             |
| AxiLtc2270ConfigType   |                                                  |             |
| AxiLtc2270StatusType   |                                                  |             |
