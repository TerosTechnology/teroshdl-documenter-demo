# Entity: ad_perfect_shuffle

## Diagram

![Diagram](ad_perfect_shuffle.svg "Diagram")
## Description

***************************************************************************
 ***************************************************************************
 Copyright 2018 (c) Analog Devices, Inc. All rights reserved.
 Each core or library found in this collection may have its own licensing terms.
 The user should keep this in in mind while exploring these cores.
 Redistribution and use in source and binary forms,
 with or without modification of this file, are permitted under the terms of either
  (at the option of the user):
   1. The GNU General Public License version 2 as published by the
      Free Software Foundation, which can be found in the top level directory, or at:
 https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html
 OR
   2.  An ADI specific BSD license as noted in the top level directory, or on-line at:
 https://github.com/analogdevicesinc/hdl/blob/dev/LICENSE
 ***************************************************************************
 ***************************************************************************
 
## Generics

| Generic name    | Type | Value | Description |
| --------------- | ---- | ----- | ----------- |
| NUM_GROUPS      |      | 2     |             |
| WORDS_PER_GROUP |      | 2     |             |
| WORD_WIDTH      |      | 8     |             |
## Ports

| Port name | Direction | Type                                        | Description |
| --------- | --------- | ------------------------------------------- | ----------- |
| data_in   | input     | [NUM_GROUPS*WORDS_PER_GROUP*WORD_WIDTH-1:0] |             |
| data_out  | output    | [NUM_GROUPS*WORDS_PER_GROUP*WORD_WIDTH-1:0] |             |
