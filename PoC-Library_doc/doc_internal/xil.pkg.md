# Package: xil

- **File**: xil.pkg.vhdl
## Constants

| Name                       | Type                 | Value                                                                                                                                                                                                                                                                  | Description            |
| -------------------------- | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| C_XIL_DRP_BUS_IN_EMPTY     | T_XIL_DRP_BUS_IN     |  ( 		Clock			=> '0',<br><span style="padding-left:20px"> 		Enable		=> '0',<br><span style="padding-left:20px"> 		ReadWrite => '0',<br><span style="padding-left:20px"> 		Address		=> (others => '0'),<br><span style="padding-left:20px"> 		Data			=> (others => '0')) |                        |
| C_XIL_DRP_BUS_OUT_EMPTY    | T_XIL_DRP_BUS_OUT    |  ( 		Ack				=> '0',<br><span style="padding-left:20px"> 		Data			=> (others => '0'))                                                                                                                                                                                   |                        |
| C_XIL_DRP_MAX_CONFIG_COUNT | positive             |  8                                                                                                                                                                                                                                                                     |  define array indices  |
| C_XIL_DRP_CONFIG_EMPTY     | T_XIL_DRP_CONFIG     |  ( 		Address =>	(others => '0'),<br><span style="padding-left:20px"> 		Data =>			(others => '0'),<br><span style="padding-left:20px"> 		Mask =>			(others => '0') 	)                                                                                                   |                        |
| C_XIL_DRP_CONFIG_SET_EMPTY | T_XIL_DRP_CONFIG_SET |  ( 		Configs		=> (others => C_XIL_DRP_CONFIG_EMPTY),<br><span style="padding-left:20px"> 		LastIndex	=> 0 	)                                                                                                                                                           |                        |
## Types

| Name                           | Type                                                 | Description |
| ------------------------------ | ---------------------------------------------------- | ----------- |
| T_XIL_CHIPSCOPE_CONTROL_VECTOR | array (natural range <>) of T_XIL_CHIPSCOPE_CONTROL  |             |
| T_XIL_DRP_ADDRESS_VECTOR       | array (natural range <>) of T_XIL_DRP_ADDRESS        |             |
| T_XIL_DRP_DATA_VECTOR          | array (natural range <>) of T_XIL_DRP_DATA           |             |
| T_XIL_DRP_BUS_IN               |                                                      |             |
| T_XIL_DRP_BUS_OUT              |                                                      |             |
| T_XIL_DRP_CONFIG               |                                                      |             |
| T_XIL_DRP_CONFIG_VECTOR        | array (natural range <>) of T_XIL_DRP_CONFIG         |             |
| T_XIL_DRP_CONFIG_SET           |                                                      |             |
| T_XIL_DRP_CONFIG_ROM           | array (natural range <>) of T_XIL_DRP_CONFIG_SET     |             |
