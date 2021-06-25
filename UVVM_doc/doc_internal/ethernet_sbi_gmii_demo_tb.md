# Entity: ethernet_sbi_gmii_demo_tb
## Diagram
![Diagram](ethernet_sbi_gmii_demo_tb.svg "Diagram")
## Constants
| Name                | Type                  | Value                 | Description |
| ------------------- | --------------------- | --------------------- | ----------- |
| C_CLK_PERIOD        | time                  |  8 ns                 |             |
| C_SCOPE             | string                |  C_TB_SCOPE_DEFAULT   |             |
| C_VVC_ETH_SBI       | natural               |  1                    |             |
| C_VVC_SBI           | natural               |  1                    |             |
| C_VVC_ETH_GMII      | natural               |  2                    |             |
| C_VVC_GMII          | natural               |  2                    |             |
| C_ETH_SBI_MAC_ADDR  | unsigned(47 downto 0) |  x"00_00_00_00_00_01" |             |
| C_ETH_GMII_MAC_ADDR | unsigned(47 downto 0) |  x"00_00_00_00_00_02" |             |
## Processes
- p_main: _(  )_

## Instantiations
- i_ti_uvvm_engine: uvvm_vvc_framework.ti_uvvm_engine
- i_test_harness: bitvis_vip_ethernet.ethernet_sbi_gmii_demo_th
