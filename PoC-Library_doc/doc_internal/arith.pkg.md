# Package: arith
## Types
| Name      | Type                         | Description |
| --------- | ---------------------------- | ----------- |
| tArch     | (AAM, CAI, CCA, PAI)         |             |
| tBlocking | (DFLT, FIX, ASC, DESC)       |             |
| tSkipping | (PLAIN, CCC, PPN_KS, PPN_BK) |             |
## Functions
- arith_div_latency <font id="function_arguments">(a_bits, rapow : positive)</font> <font id="function_return">return positive</font>
**Description**
This function computes the latency of the sequential divider, both for thepipelined and the regular sequential implementation. The returned valuespecifies the number of cycles it takes after asserting start for theresult to become ready.
