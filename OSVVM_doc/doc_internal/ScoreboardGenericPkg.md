# Package: ScoreboardGenericPkg

- **File**: ScoreboardGenericPkg.vhd
## Types

| Name                   | Type                                                                                                             | Description               |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------- | ------------------------- |
| ScoreboardReportType   | (REPORT_ERROR,<br><span style="padding-left:20px"> REPORT_ALL,<br><span style="padding-left:20px"> REPORT_NONE)  | replaced by affirmations  |
| ScoreboardIdType       |                                                                                                                  |                           |
| ScoreboardIdArrayType  | array (integer range <>) of ScoreboardIdType                                                                     |                           |
| ScoreboardIdMatrixType | array (integer range <>,<br><span style="padding-left:20px"> integer range <>) of ScoreboardIdType               |                           |
| ScoreBoardPType        |                                                                                                                  |                           |
## Functions
- Push <font id="function_arguments">( constant ID     : in  ScoreboardIDType ;<br><span style="padding-left:20px"> constant Item   : in  ExpectedType ) </font> <font id="function_return">return ()</font>
**Description**
Push items into the scoreboard/FIFOSimple Scoreboard, no tag
- Push <font id="function_arguments">( constant ID     : in  ScoreboardIDType ;<br><span style="padding-left:20px"> constant Tag    : in  string ;<br><span style="padding-left:20px"> constant Item   : in  ExpectedType ) </font> <font id="function_return">return ()</font>
**Description**
Simple Tagged Scoreboard
- Check <font id="function_arguments">( constant ID           : in  ScoreboardIDType ;<br><span style="padding-left:20px"> constant ActualData   : in ActualType ) </font> <font id="function_return">return ()</font>
**Description**
Check received item with item in the scoreboard/FIFOSimple Scoreboard, no tag
- Check <font id="function_arguments">( constant ID           : in  ScoreboardIDType ;<br><span style="padding-left:20px"> constant Tag          : in  string ;<br><span style="padding-left:20px"> constant ActualData   : in  ActualType ) </font> <font id="function_return">return ()</font>
**Description**
Simple Tagged Scoreboard
- Pop <font id="function_arguments">( constant ID     : in  ScoreboardIDType ;<br><span style="padding-left:20px"> variable Item   : out  ExpectedType ) </font> <font id="function_return">return ()</font>
**Description**
Pop the top item (FIFO) from the scoreboard/FIFOSimple Scoreboard, no tag
- Pop <font id="function_arguments">( constant ID     : in  ScoreboardIDType ;<br><span style="padding-left:20px"> constant Tag    : in  string ;<br><span style="padding-left:20px"> variable Item   : out  ExpectedType ) </font> <font id="function_return">return ()</font>
**Description**
Simple Tagged Scoreboard
- Peek <font id="function_arguments">( constant ID     : in  ScoreboardIDType ;<br><span style="padding-left:20px"> constant Tag    : in  string ;<br><span style="padding-left:20px"> variable Item   : out ExpectedType ) </font> <font id="function_return">return ()</font>
**Description**
Peek at the top item (FIFO) from the scoreboard/FIFOSimple Tagged Scoreboard
- Peek <font id="function_arguments">( constant ID     : in  ScoreboardIDType ;<br><span style="padding-left:20px"> variable Item   : out  ExpectedType ) </font> <font id="function_return">return ()</font>
**Description**
Simple Scoreboard, no tag
- SetAlertLogID <font id="function_arguments">( constant ID              : in  ScoreboardIDType ;<br><span style="padding-left:20px"> constant Name            : in  string ;<br><span style="padding-left:20px"> constant ParentID        : in  AlertLogIDType := ALERTLOG_BASE_ID ;<br><span style="padding-left:20px"> constant CreateHierarchy : in  Boolean := TRUE ) </font> <font id="function_return">return ()</font>
**Description**
SetAlertLogID - associate an AlertLogID with a scoreboard to allow integrated error reporting
- SetAlertLogID <font id="function_arguments">( constant ID     : in  ScoreboardIDType ;<br><span style="padding-left:20px"> constant A      : AlertLogIDType ) </font> <font id="function_return">return ()</font>
**Description**
Use when an AlertLogID is used by multiple items (Model or other Scoreboards).  See also AlertLogPkg.GetAlertLogID
- Flush <font id="function_arguments">( constant ID          : in  ScoreboardIDType ;<br><span style="padding-left:20px"> constant ItemNumber  :  in  integer ) </font> <font id="function_return">return ()</font>
**Description**
Flush - Remove elements in the scoreboard upto and including the one with ItemNumberSee Find to identify an ItemNumber of a particular value and tag (if applicable)Simple Scoreboards
- Flush <font id="function_arguments">( constant ID          : in  ScoreboardIDType ;<br><span style="padding-left:20px"> constant Tag         :  in  string ;<br><span style="padding-left:20px"> constant ItemNumber  :  in  integer ) </font> <font id="function_return">return ()</font>
**Description**
Tagged Scoreboards - only removes items that also match the tag
- Deallocate <font id="function_arguments">( constant ID     : in  ScoreboardIDType ) </font> <font id="function_return">return ()</font>
**Description**
Generally these are not required.  When a simulation ends and another simulation is started, a simulator will release all allocated items.  
- Initialize <font id="function_arguments">( constant ID     : in  ScoreboardIDType ) </font> <font id="function_return">return ()</font>
**Description**
Deletes all allocated items
- CheckFinish <font id="function_arguments">( ID                 : ScoreboardIDType ;<br><span style="padding-left:20px"> FinishCheckCount   : integer ;<br><span style="padding-left:20px"> FinishEmpty        : boolean ) </font> <font id="function_return">return ()</font>
- SetReportMode <font id="function_arguments">( constant ID           : in  ScoreboardIDType ;<br><span style="padding-left:20px"> constant ReportModeIn : in  ScoreboardReportType ) </font> <font id="function_return">return ()</font>
**Description**
SetReportMode  Not AlertFlow    REPORT_ALL:     Replaced by AlertLogPkg.SetLogEnable(PASSED, TRUE)    REPORT_ERROR:   Replaced by AlertLogPkg.SetLogEnable(PASSED, FALSE)    REPORT_NONE:    Deprecated, do not use.AlertFlow:          REPORT_ALL:     Replaced by AlertLogPkg.SetLogEnable(AlertLogID, PASSED, TRUE)    REPORT_ERROR:   Replaced by AlertLogPkg.SetLogEnable(AlertLogID, PASSED, FALSE)    REPORT_NONE:    Replaced by AlertLogPkg.SetAlertEnable(AlertLogID, ERROR, FALSE)
