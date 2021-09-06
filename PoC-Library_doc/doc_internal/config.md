# Package: config_private

- **File**: config.vhdl
## Types

| Name                         | Type                                              | Description                                  |
| ---------------------------- | ------------------------------------------------- | -------------------------------------------- |
| T_BOARD_UART_DESC            |                                                   |  Data structures to describe UART / RS232    |
| T_BOARD_ETHERNET_DESC        |                                                   |  Data structures to describe Ethernet        |
| T_BOARD_ETHERNET_DESC_VECTOR | array(natural range <>) of T_BOARD_ETHERNET_DESC  |                                              |
| T_BOARD_INFO                 |                                                   |  Data structures to describe a board layout  |
| T_BOARD_INFO_VECTOR          | array (natural range <>) of T_BOARD_INFO          |                                              |
## Functions
- conf <font id="function_arguments">(str : string) </font> <font id="function_return">return T_BOARD_CONFIG_STRING </font>
