# Package: axi_pkg

- **File**: axi_pkg.vhd
## Constants

| Name                  | Type             | Value                 | Description |
| --------------------- | ---------------- | --------------------- | ----------- |
| axi_resp_okay         | axi_resp_t       |  "00"                 |             |
| axi_resp_exokay       | axi_resp_t       |  "01"                 |             |
| axi_resp_slverr       | axi_resp_t       |  "10"                 |             |
| axi_resp_decerr       | axi_resp_t       |  "11"                 |             |
| axi_burst_type_fixed  | axi_burst_type_t |  "00"                 |             |
| axi_burst_type_incr   | axi_burst_type_t |  "01"                 |             |
| axi_burst_type_wrap   | axi_burst_type_t |  "10"                 |             |
| max_axi4_burst_length | natural          |  2**axi4_len_t'length |             |
