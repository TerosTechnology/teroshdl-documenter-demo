# Package: RandomPkg

## Description

comment out following 3 lines with VHDL-2008.  Leave in for VHDL-2002
library ieee_proposed ;						               -- remove with VHDL-2008
use ieee_proposed.standard_additions.all ;        -- remove with VHDL-2008
use ieee_proposed.standard_textio_additions.all ; -- remove with VHDL-2008

## Types

| Name             | Type                                     | Description                            |
| ---------------- | ---------------------------------------- | -------------------------------------- |
| DistRecType      |                                          | Supports DistValInt functionality      |
| DistType         | array (natural range <>) of DistRecType  |                                        |
| NaturalVBoolType | array (boolean range <>) of natural      | Weight vectors not indexed by integers |
| NaturalVSlType   | array (std_logic range <>) of natural    |                                        |
| NaturalVBitType  | array (bit range <>) of natural          |                                        |
| RandomPType      |                                          |                                        |
