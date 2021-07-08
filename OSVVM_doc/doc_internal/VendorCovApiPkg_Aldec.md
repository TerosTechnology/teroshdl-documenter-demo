# Package: VendorCovApiPkg

## Types

| Name                    | Type                                              | Description                                                        |
| ----------------------- | ------------------------------------------------- | ------------------------------------------------------------------ |
| VendorCovRangeType      |                                                   | Types for how coverage bins are represented.  Matches OSVVM types. |
| VendorCovRangeArrayType | array ( integer range <> ) of VendorCovRangeType  |                                                                    |
## Functions
- VendorCovSetName <font id="function_arguments">( obj: VendorCovHandleType;<br><span style="padding-left:20px"> name: string ) </font> <font id="function_return">return ()</font>
**Description**
 Sets/Updates the name of the Coverage Model. Should not be called until the data structure is created by VendorCovPointCreate or VendorCovCrossCreate. Replaces name that was set by VendorCovPointCreate or VendorCovCrossCreate.
- VendorCovBinAdd <font id="function_arguments">( obj: VendorCovHandleType;<br><span style="padding-left:20px"> bins: VendorCovRangeArrayType;<br><span style="padding-left:20px"> Action: integer;<br><span style="padding-left:20px"> atleast: integer;<br><span style="padding-left:20px"> name: string ) </font> <font id="function_return">return ()</font>
**Description**
 Add a bin or set of bins to either a Point/Item or Cross Functional Coverage Model Checking for sizing that is different from original sizing already done in OSVVM CoveragePkg It is important to maintain an index that corresponds to the order the bins were entered as that is used when coverage is recorded.
- VendorCovBinInc <font id="function_arguments">( obj: VendorCovHandleType;<br><span style="padding-left:20px"> index: integer ) </font> <font id="function_return">return ()</font>
**Description**
 Increment the coverage of bin identified by index number. Index ranges from 1 to Number of Bins. Index corresponds to the order the bins were entered (starting from 1)
