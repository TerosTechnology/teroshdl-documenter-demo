# Package: ansi_pkg
## Constants
| Name      | Type          | Value                                              | Description |
| --------- | ------------- | -------------------------------------------------- | ----------- |
| no_colors | ansi_colors_t |  (fg => no_color, bg => no_color, style => normal) |             |
## Types
| Name          | Type                                                                                                                                                                                                                                                                       | Description |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| ansi_color_t  | (     no_color,      black,     red,     green,     yellow,     blue,     magenta,     cyan,     white,       Non standard foregrounds     lightblack,     lightred,     lightgreen,     lightyellow,     lightblue,     lightmagenta,     lightcyan,     lightwhite     ) |             |
| ansi_style_t  | (     dim,     normal,     bright     )                                                                                                                                                                                                                                    |             |
| ansi_colors_t |                                                                                                                                                                                                                                                                            |             |
## Functions
- disable_colors <font id="function_arguments">()</font> <font id="function_return">return ()</font>
- enable_colors <font id="function_arguments">()</font> <font id="function_return">return ()</font>
- ansi_color_demo <font id="function_arguments">()</font> <font id="function_return">return ()</font>
