# Entity: misc_bit_lz
## Diagram
![Diagram](misc_bit_lz.svg "Diagram")
## Description
EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Description:
 An LZ77-based bit stream compressor.
 Output Format
 1 | Literal
   A literal bit string of length COUNT_BITS+OFFSET_BITS.
 0 | <Count:COUNT_BITS> | <Offset:OFFSET_BITS>
   Repetition starting at <Offset> in history buffer of length
   <Count>+COUNT_BITS+OFFSET_BITS where <Count> < 2^COUNT_BITS-1.
   Unless <Count> = 2^COUNT_BITS-2, this repetition is
   followed by a trailing non-matching, i.e. inverted, bit.
   The most recent bit just preceding the repetition is considered to be at
   offset zero(0). Older bits are at higher offsets accordingly. The
   reported length of the repetition may actually be greater than the
   offset. In this case, the repetition is reoccuring in itself. The
   reconstruction must then be performed in several steps.
 0 | <1:COUNT_BITS> | <Offset:OFFSET_BITS>
   This marks the end of the message. The <Offset> field alters the
   semantics of the immediately preceding message:
   a)If the preceding message was a repetition, <Offset> specifies the value
     of the trailing bit explicitly in its rightmost bit. The implicit
     trailing non-matching bit is overridden.
   b)If the preceding message was a literal, <Offset> is a non-positive
     number d given in its one's complement representation. The value
     ~d specifies the number of bits,  which this literal repeated of the
     preceding output. These bits must be deleted from the reconstructed
     stream.
 Parameter Constraints
  COUNT_BITS <= OFFSET_BITS < 2**COUNT_BITS - COUNT_BITS
=============================================================================
Authors:     Thomas B. Preusser <thomas.preusser@utexas.edu>
=============================================================================
References:
  Original Study
     Kai-Uwe Irrgang <kai-uwe.irrgang@b-tu.de>
     PhD Thesis: "Modellierung von On-Chip-Trace-Architekturen
                  fuer eingebettete Systeme"
  Papers
     Kai-Uwe Irrgang and Thomas B. Preusser and Rainer G. Spallek:
     "An LZ77-Style Bit-Level Compression for Trace Data Compaction",
     International Conference on Field Programmable Logic and
     Applications (FPL 2015), Sep, 2015.
     Kai-Uwe Irrgang and Thomas B. Preusser and Rainer G. Spallek:
     "Kompression von Tracedaten auf der Basis eines auf Bitebene
      arbeitenden LZ77-Woerterbuchansatzes",
     Fehlertolerante und energieeffiziente eingebettete Systeme:
     Methoden und Anwendungen (FEES 2015), Oct, 2015.
=============================================================================
## Generics
| Generic name   | Type     | Value | Description                      |
| -------------- | -------- | ----- | -------------------------------- |
| COUNT_BITS     | positive |       |                                  |
| OFFSET_BITS    | positive |       |                                  |
| OUTPUT_REGS    | boolean  | true  | Register all outputs             |
| OPTIMIZE_SPEED | boolean  | true  | Favor achievable clock over size |
## Ports
| Port name | Direction | Type                                              | Description                                          |
| --------- | --------- | ------------------------------------------------- | ---------------------------------------------------- |
| clk       | in        | std_logic                                         | Global Control                                       |
| rst       | in        | std_logic                                         |                                                      |
| din       | in        | std_logic                                         | Data Input                                           |
| put       | in        | std_logic                                         |                                                      |
| flush     | in        | std_logic                                         | end of message,                                      |
| odat      | out       | std_logic_vector(COUNT_BITS+OFFSET_BITS downto 0) | to be asserted after last associated putData Output  |
| ostb      | out       | std_logic                                         |                                                      |
## Signals
| Name       | Type                                      | Description                |
| ---------- | ----------------------------------------- | -------------------------- |
| History    | std_logic_vector(HISTORY_SIZE   downto 0) | History and Match Buffers  |
| Match      | std_logic_vector(HISTORY_SIZE-1 downto 0) |                            |
| Count      | signed(COUNT_BITS downto 0)               |                            |
| Offset     | unsigned(OFFSET_BITS-1 downto 0)          |                            |
| Term       | std_logic                                 |                            |
| Offset_nxt | unsigned(Offset'range)                    |                            |
| ov         | X01                                       | Counter Overflow           |
| valid      | X01                                       | Still some Match available |
| data       | std_logic_vector(odat'range)              | Outputs                    |
| push       | std_logic                                 |                            |
## Constants
| Name         | Type     | Value                     | Description |
| ------------ | -------- | ------------------------- | ----------- |
| HISTORY_SIZE | positive |  2**OFFSET_BITS           |             |
| LITERAL_LEN  | positive |  COUNT_BITS + OFFSET_BITS |             |
## Processes
- unnamed: _( clk )_
Registers

**Description**
Registers

