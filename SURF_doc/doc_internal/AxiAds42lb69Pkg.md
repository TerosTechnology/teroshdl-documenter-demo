# Package: AxiAds42lb69Pkg

## Constants

| Name                           | Type                     | Value                                                                                                                                                                                                                                                                | Description |
| ------------------------------ | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| AXI_ADS42LB69_DELAY_IN_INIT_C  | AxiAds42lb69DelayInType  |  (       load => (others =>(others => '0')),<br><span style="padding-left:20px">       rst  => '0',<br><span style="padding-left:20px">       data => (others => '0'))                                                                                               |             |
| AXI_ADS42LB69_DELAY_OUT_INIT_C | AxiAds42lb69DelayOutType |  (       rdy  => '0',<br><span style="padding-left:20px">       data => (others => (others => (others => '0'))))                                                                                                                                                     |             |
| AXI_ADS42LB69_CONFIG_INIT_C    | AxiAds42lb69ConfigType   |  (       dmode   => (others => '0'),<br><span style="padding-left:20px">       invert  => (others => '0'),<br><span style="padding-left:20px">       convert => (others => '0'),<br><span style="padding-left:20px">       delayIn => AXI_ADS42LB69_DELAY_IN_INIT_C) |             |
| AXI_ADS42LB69_STATUS_INIT_C    | AxiAds42lb69StatusType   |  (       adcValid => (others => '0'),<br><span style="padding-left:20px">       adcData  => (others => x"0000"),<br><span style="padding-left:20px">       delayOut => AXI_ADS42LB69_DELAY_OUT_INIT_C)                                                               |             |
## Types

| Name                     | Type                                             | Description |
| ------------------------ | ------------------------------------------------ | ----------- |
| AxiAds42lb69InType       |                                                  |             |
| AxiAds42lb69InArray      | array (natural range <>) of AxiAds42lb69InType   |             |
| AxiAds42lb69OutType      |                                                  |             |
| AxiAds42lb69OutArray     | array (natural range <>) of AxiAds42lb69OutType  |             |
| AxiAds42lb69DelayInType  |                                                  |             |
| AxiAds42lb69DelayOutType |                                                  |             |
| AxiAds42lb69ConfigType   |                                                  |             |
| AxiAds42lb69StatusType   |                                                  |             |
