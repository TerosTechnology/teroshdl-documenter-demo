# Package: axil_pkg
## Constants
| Name                | Type             | Value                                                                                                                                                                                                                                                                                                      | Description |
| ------------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| axil_addr_m2s_init  | axil_addr_m2s_t  |  (valid => '0',                                                     addr => (others => '0'))                                                                                                                                                                                                               |             |
| axil_addr_s2m_init  | axil_addr_s2m_t  |  (ready => '0')                                                                                                                                                                                                                                                                                            |             |
| axil_read_m2s_init  | axil_read_m2s_t  |  (ready => '0')                                                                                                                                                                                                                                                                                            |             |
| axil_read_s2m_init  | axil_read_s2m_t  |  (valid => '0',                                                     data => (others => '0'),                                                     resp => (others => '0'))                                                                                                                                  |             |
| axil_write_m2s_init | axil_write_m2s_t |  (valid => '0',                                                       data => (others => '0'),                                                       strb => (others => '0'))                                                                                                                              |             |
| axil_write_s2m_init | axil_write_s2m_t |  (ready => '0')                                                                                                                                                                                                                                                                                            |             |
| axil_wresp_m2s_init | axil_wresp_m2s_t |  (ready => '0')                                                                                                                                                                                                                                                                                            |             |
| axil_wresp_s2m_init | axil_wresp_s2m_t |  (valid => '0',                                                       resp => (others => '0'))                                                                                                                                                                                                             |             |
| axil_m2s_init       | axil_m2s_t       |  (ar => axil_addr_m2s_init,                                           aw => axil_addr_m2s_init,                                           r => axil_read_m2s_init,                                           w => axil_write_m2s_init,                                           b => axil_wresp_m2s_init) |             |
| axil_s2m_init       | axil_s2m_t       |  (ar => axil_addr_s2m_init,                                           aw => axil_addr_s2m_init,                                           r => axil_read_s2m_init,                                           w => axil_write_s2m_init,                                           b => axil_wresp_s2m_init) |             |
## Types
| Name             | Type | Description |
| ---------------- | ---- | ----------- |
| axil_addr_m2s_t  |      |             |
| axil_addr_s2m_t  |      |             |
| axil_read_m2s_t  |      |             |
| axil_read_s2m_t  |      |             |
| axil_write_m2s_t |      |             |
| axil_write_s2m_t |      |             |
| axil_wresp_m2s_t |      |             |
| axil_wresp_s2m_t |      |             |
| axil_m2s_t       |      |             |
| axil_s2m_t       |      |             |
