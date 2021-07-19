# Package: GigEthPkg

- **File**: GigEthPkg.vhd
## Constants

| Name                         | Type             | Value                                                                                                                                                                       | Description                                                 |
| ---------------------------- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| PAUSE_512BITS_C              | positive         |  64                                                                                                                                                                         | For 1GbE: 64 clock cycles for 512 bits = one pause "quanta" |
| GIG_ETH_AN_ADV_CONFIG_INIT_C | slv(15 downto 0) |  x"0021"                                                                                                                                                                    | Refer to PG047                                              |
| GIG_ETH_CONFIG_INIT_C        | GigEthConfigType |  (       softRst    => '0',<br><span style="padding-left:20px">       coreConfig => "00000",<br><span style="padding-left:20px">       macConfig  => ETH_MAC_CONFIG_INIT_C) |                                                             |
## Types

| Name             | Type | Description |
| ---------------- | ---- | ----------- |
| GigEthConfigType |      |             |
| GigEthStatusType |      |             |
