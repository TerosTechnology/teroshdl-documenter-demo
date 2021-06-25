# Package: xil
## Constants
| Name                       | Type                 | Value                                                                                                                  | Description          |
| -------------------------- | -------------------- | ---------------------------------------------------------------------------------------------------------------------- | -------------------- |
| C_XIL_DRP_BUS_IN_EMPTY     | T_XIL_DRP_BUS_IN     |  ( 		Clock			=> '0', 		Enable		=> '0', 		ReadWrite => '0', 		Address		=> (others => '0'), 		Data			=> (others => '0')) |                      |
| C_XIL_DRP_BUS_OUT_EMPTY    | T_XIL_DRP_BUS_OUT    |  ( 		Ack				=> '0', 		Data			=> (others => '0'))                                                                       |                      |
| C_XIL_DRP_MAX_CONFIG_COUNT | positive             |  8                                                                                                                     | define array indices |
| C_XIL_DRP_CONFIG_EMPTY     | T_XIL_DRP_CONFIG     |  ( 		Address =>	(others => '0'), 		Data =>			(others => '0'), 		Mask =>			(others => '0') 	)                           |                      |
| C_XIL_DRP_CONFIG_SET_EMPTY | T_XIL_DRP_CONFIG_SET |  ( 		Configs		=> (others => C_XIL_DRP_CONFIG_EMPTY), 		LastIndex	=> 0 	)                                               |                      |
## Types
| Name                           | Type | Description |
| ------------------------------ | ---- | ----------- |
| T_XIL_CHIPSCOPE_CONTROL_VECTOR |      |             |
| T_XIL_DRP_ADDRESS_VECTOR       |      |             |
| T_XIL_DRP_DATA_VECTOR          |      |             |
| T_XIL_DRP_BUS_IN               |      |             |
| T_XIL_DRP_BUS_OUT              |      |             |
| T_XIL_DRP_CONFIG               |      |             |
| T_XIL_DRP_CONFIG_VECTOR        |      |             |
| T_XIL_DRP_CONFIG_SET           |      |             |
| T_XIL_DRP_CONFIG_ROM           |      |             |
