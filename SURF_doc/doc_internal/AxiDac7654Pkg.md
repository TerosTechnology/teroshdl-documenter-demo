# Package: AxiDac7654Pkg

## Constants

| Name                       | Type                 | Value                                                                                                                                                                                                                                                                                                    | Description |
| -------------------------- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| AXI_DAC7654_IN_INIT_C      | AxiDac7654InType     |  (       sdo => '0')                                                                                                                                                                                                                                                                                     |             |
| AXI_DAC7654_OUT_INIT_C     | AxiDac7654OutType    |  (       cs   => '1',<br><span style="padding-left:20px">       sck  => '1',<br><span style="padding-left:20px">       sdi  => '0',<br><span style="padding-left:20px">       load => '1',<br><span style="padding-left:20px">       ldac => '0',<br><span style="padding-left:20px">       rst  => '0') |             |
| AXI_DAC7654_SPI_IN_INIT_C  | AxiDac7654SpiInType  |  (       req  => '1',<br><span style="padding-left:20px">       data => (others => x"8000"))                                                                                                                                                                                                             |             |
| AXI_DAC7654_SPI_OUT_INIT_C | AxiDac7654SpiOutType |  (       ack => '0')                                                                                                                                                                                                                                                                                     |             |
| AXI_DAC7654_STATUS_INIT_C  | AxiDac7654StatusType |  (       spi => AXI_DAC7654_SPI_OUT_INIT_C)                                                                                                                                                                                                                                                              |             |
| AXI_DAC7654_CONFIG_INIT_C  | AxiDac7654ConfigType |  (       spi => AXI_DAC7654_SPI_IN_INIT_C)                                                                                                                                                                                                                                                               |             |
## Types

| Name                     | Type                                                                                              | Description |
| ------------------------ | ------------------------------------------------------------------------------------------------- | ----------- |
| AxiDac7654InType         |                                                                                                   |             |
| AxiDac7654InArray        | array (natural range <>) of AxiDac7654InType                                                      |             |
| AxiDac7654InVectorArray  | array (integer range<>,<br><span style="padding-left:20px"> integer range<>)of AxiDac7654InType   |             |
| AxiDac7654OutType        |                                                                                                   |             |
| AxiDac7654OutArray       | array (natural range <>) of AxiDac7654OutType                                                     |             |
| AxiDac7654OutVectorArray | array (integer range<>,<br><span style="padding-left:20px"> integer range<>)of AxiDac7654OutType  |             |
| AxiDac7654SpiInType      |                                                                                                   |             |
| AxiDac7654SpiOutType     |                                                                                                   |             |
| AxiDac7654StatusType     |                                                                                                   |             |
| AxiDac7654ConfigType     |                                                                                                   |             |
