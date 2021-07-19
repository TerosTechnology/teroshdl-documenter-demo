# Package: UdpDebugBridgePkg

- **File**: UdpDebugBridgePkg.vhd
## Description

Configuration constants (used for generics) for AxisJtagDebugBridge
Instantiating two variants (stub and real implementation) of the
module could be elegantly done with vhdl configurations but alas
there are is flaky (seems to work fine but subordinate IP dcp is
not used/linked into main dcp when I use configurations) support
(still in 2017.3) in vivado.
Therefore we define a package with relevant constants to reduce
redundant boilerplate at least a little bit...

## Constants

| Name             | Type                     | Value                                                                    | Description                                             |
| ---------------- | ------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------- |
| XVC_MEM_SIZE_C   | natural                  |  1450/2                                                                  | non-jumbo MTU; mem must hold max. reply = max request/2 |
| XVC_TCLK_FREQ_C  | real                     |  15.0E+6                                                                 |                                                         |
| XVC_ACLK_FREQ_C  | real                     |  156.25E+6                                                               |                                                         |
| XVC_TCLK_DIV2_C  | positive                 |  positive( ieee.math_real.round( XVC_ACLK_FREQ_C/XVC_TCLK_FREQ_C/2.0 ) ) |                                                         |
| XVC_AXIS_WIDTH_C | positive range 4 to 16   |  EMAC_AXIS_CONFIG_C.TDATA_BYTES_C                                        |                                                         |
| XVC_MEM_DEPTH_C  | natural range 0 to 65535 |   XVC_MEM_SIZE_C/XVC_AXIS_WIDTH_C                                        |                                                         |
| XVC_MEM_STYLE_C  | string                   |  "auto"                                                                  |                                                         |
