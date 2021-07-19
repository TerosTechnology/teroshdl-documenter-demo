# Package: SsiCmdMasterPkg

- **File**: SsiCmdMasterPkg.vhd
## Constants

| Name                  | Type             | Value                                                                                                                                                                | Description |
| --------------------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| SSI_CMD_MASTER_INIT_C | SsiCmdMasterType |  (       valid   => '0',<br><span style="padding-left:20px">       opCode  => (others => '0'),<br><span style="padding-left:20px">       context => (others => '0')) |             |
## Types

| Name              | Type                                          | Description |
| ----------------- | --------------------------------------------- | ----------- |
| SsiCmdMasterType  |                                               |             |
| SsiCmdMasterArray | array (natural range <>) of SsiCmdMasterType  |             |
