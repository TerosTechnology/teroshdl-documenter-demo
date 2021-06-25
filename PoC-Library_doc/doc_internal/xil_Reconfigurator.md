# Entity: xil_Reconfigurator
## Diagram
![Diagram](xil_Reconfigurator.svg "Diagram")
## Generics
| Generic name | Type                 | Value                                      | Description |
| ------------ | -------------------- | ------------------------------------------ | ----------- |
| DEBUG        | boolean              | FALSE                                      |             |
| CLOCK_FREQ   | FREQ                 | 100 MHz                                    |             |
| CONFIG_ROM   | T_XIL_DRP_CONFIG_ROM | (0 downto 0 => C_XIL_DRP_CONFIG_SET_EMPTY) |             |
## Ports
| Port name    | Direction | Type                                                         | Description |
| ------------ | --------- | ------------------------------------------------------------ | ----------- |
| Clock        | in        | std_logic                                                    |             |
| Reset        | in        | std_logic                                                    |             |
| Reconfig     | in        | std_logic                                                    |             |
| ReconfigDone | out       | std_logic                                                    |             |
| ConfigSelect | in        | std_logic_vector(log2ceilnz(CONFIG_ROM'length) - 1 downto 0) |             |
| DRP_en       | out       | std_logic                                                    |             |
| DRP_Address  | out       | T_XIL_DRP_ADDRESS                                            |             |
| DRP_we       | out       | std_logic                                                    |             |
| DRP_DataIn   | in        | T_XIL_DRP_DATA                                               |             |
| DRP_DataOut  | out       | T_XIL_DRP_DATA                                               |             |
| DRP_Ack      | in        | std_logic                                                    |             |
## Signals
| Name               | Type                                    | Description |
| ------------------ | --------------------------------------- | ----------- |
| State              | T_STATE                                 |             |
| NextState          | T_STATE                                 |             |
| DataBuffer_en      | std_logic                               |             |
| DataBuffer_d       | T_XIL_DRP_DATA                          |             |
| ROM_Entry          | T_XIL_DRP_CONFIG                        |             |
| ROM_LastConfigWord | std_logic                               |             |
| ConfigSelect_d     | std_logic_vector(ConfigSelect'range)    |             |
| ConfigIndex_rst    | std_logic                               |             |
| ConfigIndex_en     | std_logic                               |             |
| ConfigIndex_us     | unsigned(CONFIGINDEX_BITS - 1 downto 0) |             |
## Constants
| Name             | Type     | Value                          | Description |
| ---------------- | -------- | ------------------------------ | ----------- |
| CONFIGINDEX_BITS | positive |  log2ceilnz(CONFIG_ROM'length) |             |
## Types
| Name    | Type                                                                                      | Description |
| ------- | ----------------------------------------------------------------------------------------- | ----------- |
| T_STATE | ( 		ST_IDLE, 		ST_READ_BEGIN,	ST_READ_WAIT, 		ST_WRITE_BEGIN,	ST_WRITE_WAIT, 		ST_DONE 	) |             |
## Processes
- unnamed: _( Clock )_

- unnamed: _( Clock )_

- unnamed: _( Clock )_

- unnamed: _( State, Reconfig, ROM_LastConfigWord, DRP_Ack )_

