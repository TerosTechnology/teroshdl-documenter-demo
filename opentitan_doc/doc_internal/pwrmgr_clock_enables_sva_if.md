# Package: pwrmgr_pkg

- **File**: pwrmgr_clock_enables_sva_if.sv
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 This has some assertions that check that the output clock enables correspond
 to the control CSR when transitioning into or out of the active state. In
 addition, the usb clock can change anytime when in the active state.
 The synchronized control CSR bits.
 The output enables.


