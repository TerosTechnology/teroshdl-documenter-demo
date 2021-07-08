# Package: arith

## Types

| Name      | Type                                                                                                                                      | Description |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| tArch     | (AAM,<br><span style="padding-left:20px"> CAI,<br><span style="padding-left:20px"> CCA,<br><span style="padding-left:20px"> PAI)          |             |
| tBlocking | (DFLT,<br><span style="padding-left:20px"> FIX,<br><span style="padding-left:20px"> ASC,<br><span style="padding-left:20px"> DESC)        |             |
| tSkipping | (PLAIN,<br><span style="padding-left:20px"> CCC,<br><span style="padding-left:20px"> PPN_KS,<br><span style="padding-left:20px"> PPN_BK)  |             |
## Functions
- arith_div_latency <font id="function_arguments">(a_bits,<br><span style="padding-left:20px"> rapow : positive) </font> <font id="function_return">return positive </font>
**Description**
This function computes the latency of the sequential divider, both for thepipelined and the regular sequential implementation. The returned valuespecifies the number of cycles it takes after asserting start for theresult to become ready.
