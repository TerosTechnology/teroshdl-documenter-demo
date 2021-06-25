# Package: local_adaptations_pkg
## Constants
| Name                       | Type              | Value                                                                                                                                                                                                                                                                         | Description |
| -------------------------- | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| C_CSV_FILE_MAX_LINE_LENGTH | positive          |  256                                                                                                                                                                                                                                                                          |             |
| C_CSV_DELIMITER            | character         |  ','                                                                                                                                                                                                                                                                          |             |
| C_SPEC_COV_CONFIG_DEFAULT  | t_spec_cov_config |  (         missing_req_label_severity  => TB_WARNING,         csv_delimiter               => C_CSV_DELIMITER,         max_requirements            => 1000,         max_testcases_per_req       => 20,         csv_max_line_length         => C_CSV_FILE_MAX_LINE_LENGTH     ) |             |
## Types
| Name              | Type | Description |
| ----------------- | ---- | ----------- |
| t_spec_cov_config |      |             |
