# Package: Ad9249Pkg

- **File**: Ad9249Pkg.vhd
## Constants

| Name              | Type                | Value                                                                                                                                                                                                                                                                                                                                                                                                                                       | Description |
| ----------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| AD9249_AXIS_CFG_G | AxiStreamConfigType |  (       TSTRB_EN_C    => false,<br><span style="padding-left:20px">       TDATA_BYTES_C => 2,<br><span style="padding-left:20px">       TDEST_BITS_C  => 0,<br><span style="padding-left:20px">       TID_BITS_C    => 0,<br><span style="padding-left:20px">       TKEEP_MODE_C  => TKEEP_FIXED_C,<br><span style="padding-left:20px">       TUSER_BITS_C  => 0,<br><span style="padding-left:20px">       TUSER_MODE_C  => TUSER_NONE_C) |             |
## Types

| Name                   | Type                                               | Description |
| ---------------------- | -------------------------------------------------- | ----------- |
| Ad9249SerialGroupType  |                                                    |             |
| Ad9249SerialGroupArray | array (natural range <>) of Ad9249SerialGroupType  |             |
