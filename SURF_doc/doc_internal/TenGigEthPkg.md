# Package: TenGigEthPkg

## Constants

| Name                      | Type            | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Description |
| ------------------------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| TEN_GIG_ETH_CONFIG_INIT_C | TenGigEthConfig |  (       softRst      => '0',<br><span style="padding-left:20px">       macConfig    => ETH_MAC_CONFIG_INIT_C,<br><span style="padding-left:20px">       pma_pmd_type => "111",<br><span style="padding-left:20px">            --111 = 10GBASE-SR (Wavelength:850 nm & OM3:300m)       pma_loopback => '0',<br><span style="padding-left:20px">       pma_reset    => '0',<br><span style="padding-left:20px">       pcs_loopback => '0',<br><span style="padding-left:20px">       pcs_reset    => '0') |             |
## Types

| Name            | Type | Description |
| --------------- | ---- | ----------- |
| TenGigEthConfig |      |             |
| TenGigEthStatus |      |             |
