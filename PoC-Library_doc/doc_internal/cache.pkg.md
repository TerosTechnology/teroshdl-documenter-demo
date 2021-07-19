# Package: cache

- **File**: cache.pkg.vhdl
## Types

| Name           | Type                                                                                                                              | Description |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| T_CACHE_RESULT | (CACHE_RESULT_NONE,<br><span style="padding-left:20px"> CACHE_RESULT_HIT,<br><span style="padding-left:20px"> CACHE_RESULT_MISS)  |             |
## Functions
- to_Cache_Result <font id="function_arguments">(CacheHit : std_logic;<br><span style="padding-left:20px"> CacheMiss : std_logic) </font> <font id="function_return">return T_CACHE_RESULT </font>
