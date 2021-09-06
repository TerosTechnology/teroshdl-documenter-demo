# Entity: AxisToJtag

- **File**: AxisToJtag.vhd
## Diagram

![Diagram](AxisToJtag.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Title      : JTAG Support
-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: AXI stream to JTAG
-----------------------------------------------------------------------------
 This file is part of 'SLAC Firmware Standard Library'.
 It is subject to the license terms in the LICENSE.txt file found in the
 top-level directory of this distribution and at:
    https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
 No part of 'SLAC Firmware Standard Library', including this file,
 may be copied, modified, propagated, or distributed except according to
 the terms contained in the LICENSE.txt file.
-----------------------------------------------------------------------------
 Axi Stream to JTAG Protocol

 This module implements a simple protocol for encoding XVC transactions over
 an AXI stream. Part of this is support for unreliable transport protocols
 (by means of a memory buffer and transaction IDs).
 Once the protocol header is processed the stream is delegated to the
 AxisToJtagCore module.

 INCOMING STREAM

 The incoming Stream consists of consecutive words of AXIS_WIDTH_G bytes,
 must be framed with 'TLAST' and is expected to have the following format :

    Header Word [, Payload ]

 The header word is defined as

   [31:30]  Protocol Version -- currently "00"
   [29:28]  Command
   [27:00]  Command-specific parameter(s)

 Note that if the core is configured for a stream width (AXIS_WIDTH_G) > 4
 then the header is padded up to the desired width, i.e., the paylod must
 be word-aligned.

 Each command word is answered with a reply word on the outgoing stream
 (see below).

 The following commands are currently defined:

      "00"  QUERY: request basic features such as word length, memory depth.

            Payload: NONE, i.e., TLAST should be asserted with this command.

      "01"  JTAG: shift jtag vectors. The vectors are shipped in the payload.
            The parameter bits for this command are defined as follows:

            [27:20] Transaction ID; this is used when the core is configured
                    with MEM_DEPTH_G > 0 in order to support a non-reliable
                    transport.
            [19:00] JTAG vector length (in bits). The payload must provide
                    2*ceil( length / AXIS_WIDTH_G ) words of TMS/TDI vector
                    data. I.e., the length refers to the length of a single
                    TMS or TDI vector.
                    !!!!!!!
                     NOTE: the number in [19:00] encodes the actual number
                           minus 1. E.g., a value of 0 transmits one TMS
                           and one TDI bit. Two payload words are expected
                           in this example.
                    !!!!!!!

            Payload: sequence of words from the TMS and TDI bit-vectors:

                    TMS_WORD, TDI_WORD, TMS_WORD, TDI_WORD, ...

                    Note that the user must format the stream accordingly
                    and therefore must be aware of the stream width. This
                    parameter is returned by the QUERY command.

                    If the number of bits supplied does not fill the last
                    word then the relevant bits must be lsb/right-aligned
                    in the last word.

                    TLAST must be asserted during the transmission of the
                    last TDI/payload word.

 OUTGOING STREAM

 The outgoing stream consists of consecutive words of AXIS_WIDTH_G bytes
 and is framed with 'TLAST'. Each reply has the following format:

    Header Word [, Payload ]

 The header word is defined as

   [31:30]  Protocol Version; if the user supplies an unsupported protocol
            version in the request header then the reply contains an error
            code (see below) and the protocol version in the reply is set
            to the supported version.

   [29:28]  Command -- the request command is returned unless an error occurred;
            in case of an error the command bits in the reply are:

            "10"  ERROR: An error was detected. The 8 least-significant bits
                  [7:0] contain an error code:
                  1: bad protocol version; the protocol version in the reply
                     is set to the supported version.
                  2: bad/unsupported command code
                  3: truncated input stream (TLAST detected before the
                     first TDI word was received). Note that a premature
                     TLAST which is detected after the first TDI word
                     does NOT flag an error but yields a truncated reply
                     (less TDO words than requested by the number of bits).

            "00"  QUERY: the response to a QUERY command encodes information
                  in the command-specific bits:

                 [ 3: 0] AXIS_WIDTH_G - 1. I.e., this field encodes the
                         word size (minus one) used by the core. This information
                         is important for formatting the stream.
                 [19: 4] MEM_DEPTH_G. Indicates how much memory (if any) was
                         configured in words.
                 [27:20] TCK period. Encoded as

                                          200Mhz     1
                            round{ log10( ------- ) --- 256 }
                                           Ttck      4

                        With the special value 0 representing 'unknown'.


            "01"  JTAG: the response to a JTAG command is a sequence of
                  TDO words which form the TDO bit vector. The vector
                  stored in little-endian format (first bit of the vector
                  is the LSB of the first TDO word).
                  If the number of JTAG bits does not fill the last TDO
                  word completely then the relevant bits are right-
                  aligned.

 RELIABILITY SUPPORT

 If the transport mechanism contains unreliable segments with a potential for
 data loss then a simple retry mechanism is not suitable because JTAG operations
 are not necessarily idempotent.
 The core can be configured to use internal memory (MEM_DEPTH_C > 0) in which
 case it stores the last JTAG TDO response in memory.
 When the next JTAG command arrives the core inspects the 'transaction ID' field
 of the command and if it is identical with the ID submitted along with the previous
 transaction then the core detects a retried operation and does not actually execute
 it again on JTAG but plays back the stored TDO response to the requestor.
## Generics

| Generic name | Type                      | Value  | Description                                                                                                                                                                                                                                                                                 |
| ------------ | ------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TPD_G        | time                      | 1 ns   |                                                                                                                                                                                                                                                                                             |
| AXIS_FREQ_G  | real                      | 0.0    | Clock frequency in Hz. This information is used for computing the JTAG clock frequency which is sent as part of a QUERY reply. If unset (=0.0) then this will cause the XVC server (software) to always return the requested (and not the true) TCK frequency in the XVC 'settck' command.  |
| AXIS_WIDTH_G | positive range 4 to 16    | 4      | Width in bytes of the TDATA; this module does not support TKEEP nor resizing the I/O streams.                                                                                                                                                                                               |
| CLK_DIV2_G   | positive                  | 4      | Half period of TCK in axisClk cycles. I.e., for a given TCK frequency set CLK_DIV2_G = round( AXIS_FREQ_G / TCK_FREQ / 2 );                                                                                                                                                                 |
| MEM_DEPTH_G  | natural  range 0 to 65535 | 4      | Depth of buffer memory (in units of words of width AXIS_WIDTH_G) Setting to zero disables memory.                                                                                                                                                                                           |
| MEM_STYLE_G  | string                    | "auto" | Memory type inference (Vivado) - use 'auto', 'block' or 'distributed'                                                                                                                                                                                                                       |
## Ports

| Port name | Direction | Type                | Description |
| --------- | --------- | ------------------- | ----------- |
| axisClk   | in        | sl                  |             |
| axisRst   | in        | sl                  |             |
| mAxisReq  | in        | AxiStreamMasterType |             |
| sAxisReq  | out       | AxiStreamSlaveType  |             |
| mAxisTdo  | out       | AxiStreamMasterType |             |
| sAxisTdo  | in        | AxiStreamSlaveType  |             |
| tck       | out       | sl                  | JTAG        |
| tdi       | out       | sl                  |             |
| tms       | out       | sl                  |             |
| tdo       | in        | sl                  |             |
## Signals

| Name   | Type                          | Description           |
| ------ | ----------------------------- | --------------------- |
| r      | RegType                       |                       |
| rin    | RegType                       |                       |
| s      | CombSigType                   |                       |
| bufMem | MemType                       |  buffer memory        |
| memOut | slv(WORD_SIZE_C - 1 downto 0) |  memory readout port  |
## Constants

| Name            | Type                   | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Description                    |
| --------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| WORD_SIZE_C     | positive               |  8*AXIS_WIDTH_G                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                |
| ADDR_ZERO_C     | AddrType               |  (others => '0')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                |
| LOCL_OSTRM_PORT | natural                |  0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |  Stream selector port indices  |
| JTAG_OSTRM_PORT | natural                |  1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                |
| TCK_FREQ_REF_C  | real                   |  2.0E+8                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                |
| TCK_FREQ_C      | real                   |  ite( AXIS_FREQ_G = 0.0,<br><span style="padding-left:20px"> TCK_FREQ_REF_C,<br><span style="padding-left:20px"> AXIS_FREQ_G/(2.0*real(CLK_DIV2_G)) )                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                |
| TCK_LOG_RAT_C   | real                   |  ieee.math_real.log10( TCK_FREQ_REF_C / TCK_FREQ_C )                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                |
| TCK_BITS_C      | natural range 0 to 255 |  natural( ieee.math_real.round( TCK_LOG_RAT_C * 256.0/4.0 ) )                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                |
| REG_INIT_C      | RegType                |  (       state       => IDLE_S,<br><span style="padding-left:20px">       nstate      => IDLE_S,<br><span style="padding-left:20px">       replyData   => AXI_STREAM_MASTER_INIT_C,<br><span style="padding-left:20px">       tLastSeen   => '0',<br><span style="padding-left:20px">       ackInput    => '0',<br><span style="padding-left:20px">       passTdo     => '0',<br><span style="padding-left:20px">       passTdi     => '0',<br><span style="padding-left:20px">       ridx        => ADDR_ZERO_C,<br><span style="padding-left:20px">       widx        => ADDR_ZERO_C,<br><span style="padding-left:20px">       memValid    => false,<br><span style="padding-left:20px">       xid         => (others => '0')    ) |                                |
## Types

| Name        | Type                                                                                                                                                                                                                                                                  | Description                                                                                |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| MemType     |                                                                                                                                                                                                                                                                       |                                                                                            |
| StateType   | (IDLE_S,<br><span style="padding-left:20px"> SEND_REP_S,<br><span style="padding-left:20px"> WAIT_STARTED_S,<br><span style="padding-left:20px"> WAIT_HDR_READY_S,<br><span style="padding-left:20px"> WAIT_STOPPED_S,<br><span style="padding-left:20px"> REPLAY_S)  |  one guard bit                                                                             |
| RegType     |                                                                                                                                                                                                                                                                       |  State Record                                                                              |
| CombSigType |                                                                                                                                                                                                                                                                       |  group signals so it's easier not to forget one  in the combinatorial sensitivity list...  |
## Functions
- xidIsNew <font id="function_arguments">( data       : in slv;<br><span style="padding-left:20px"> xid        : in XidType;<br><span style="padding-left:20px"> memValid   : in boolean ) </font> <font id="function_return">return boolean </font>
- checkLen <font id="function_arguments">( data      : in slv ) </font> <font id="function_return">return boolean </font>
- setQueryData <font id="function_arguments">( wordLength : in natural range 4 to    16;<br><span style="padding-left:20px"> memDepth   : in natural range 0 to 65535;<br><span style="padding-left:20px"> data : inout slv ) </font> <font id="function_return">return ()</font>
- sendHeaderNow <font id="function_arguments">( v          : inout RegType ) </font> <font id="function_return">return ()</font>
## Processes
- P_MUX_TDI: ( r, mAxisReq, s )
**Description**
 Control flow of the input stream to the AxisToJtagCore.  We stop the flow while inspecting the header or during  playback from memory (when we discard the input stream) 
- P_TKEEP: ( s )
**Description**
 output stream; splice in TKEEP 
- P_COMB: ( r, mAxisReq, sAxisTdo, s, memOut )
- P_SEQ: ( axisClk )
## Instantiations

- U_MUX: surf.AxiStreamSelector
**Description**
 A stream multiplexer; depending on 'sel' either Ib(0) or Ib(1)
 is routed to Ob.
 We use this to splice locally generated info (reply header and
 memory playback data) into the output stream.

- U_JTAG: surf.AxisToJtagCore
**Description**
 The core which does all the JTAG work (while this module deals with
 the protocol and housekeeping.

