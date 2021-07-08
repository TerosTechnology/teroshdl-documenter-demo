# Package: local_adaptations_pkg

## Constants

| Name                       | Type              | Value                                                                                                                                                                                                                                                                                                                                                                                                                         | Description                                   |
| -------------------------- | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| C_CSV_FILE_MAX_LINE_LENGTH | positive          |  256                                                                                                                                                                                                                                                                                                                                                                                                                          |                                               |
| C_CSV_DELIMITER            | character         |  ',<br><span style="padding-left:20px">'                                                                                                                                                                                                                                                                                                                                                                                      | Delimiter when reading and writing CSV files. |
| C_SPEC_COV_CONFIG_DEFAULT  | t_spec_cov_config |  (         missing_req_label_severity  => TB_WARNING,<br><span style="padding-left:20px">         csv_delimiter               => C_CSV_DELIMITER,<br><span style="padding-left:20px">         max_requirements            => 1000,<br><span style="padding-left:20px">         max_testcases_per_req       => 20,<br><span style="padding-left:20px">         csv_max_line_length         => C_CSV_FILE_MAX_LINE_LENGTH     ) |                                               |
## Types

| Name              | Type | Description |
| ----------------- | ---- | ----------- |
| t_spec_cov_config |      |             |
