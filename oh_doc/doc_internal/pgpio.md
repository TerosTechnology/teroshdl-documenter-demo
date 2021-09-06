# Entity: pgpio

- **File**: pgpio.v
## Diagram

![Diagram](pgpio.svg "Diagram")
## Description

 Implements GPIO pins from the PS/EMIO
 Works with 7010 (24 pins) or 7020 (48 pins) and
 either single-ended or differential IO

## Generics

| Generic name | Type | Value | Description       |
| ------------ | ---- | ----- | ----------------- |
| NGPIO        |      | 24    |  12 or 24         |
| NPS          |      | 64    |  signals for PS   |
| DIFF         |      | 0     |  0= single ended  |
## Ports

| Port name | Direction | Type        | Description       |
| --------- | --------- | ----------- | ----------------- |
| gpio_p    | inout     | [NGPIO-1:0] |  1= differential  |
| gpio_n    | inout     | [NGPIO-1:0] |                   |
| ps_gpio_i | output    | [NPS-1:0]   |                   |
| ps_gpio_o | input     | [NPS-1:0]   |                   |
| ps_gpio_t | input     | [NPS-1:0]   |                   |
