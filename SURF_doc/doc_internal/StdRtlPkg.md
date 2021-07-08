# Package: StdRtlPkg

## Constants

| Name                     | Type             | Value                                                                                                                                                                                           | Description |
| ------------------------ | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| IN_SIMULATION_C          | boolean          |  false -- pragma translate_off    or true                                                                                                                                                       |             |
| IN_SYNTHESIS_C           | boolean          |  not(IN_SIMULATION_C)                                                                                                                                                                           |             |
| BUILD_INFO_DEFAULT_C     | BuildInfoRetType |  (       buildString =>  (others => (others => '0')),<br><span style="padding-left:20px">       fwVersion => X"00000000",<br><span style="padding-left:20px">       gitHash => (others => '0')) |             |
| BUILD_INFO_DEFAULT_SLV_C | BuildInfoType    |  (others => '0')                                                                                                                                                                                |             |
## Types

| Name                | Type                                                                                               | Description                                                            |
| ------------------- | -------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| IntegerArray        | array (natural range <>) of integer                                                                |                                                                        |
| NaturalArray        | array (natural range <>) of natural                                                                |                                                                        |
| PositiveArray       | array (natural range <>) of positive                                                               |                                                                        |
| RealArray           | array (natural range <>) of real                                                                   |                                                                        |
| TimeArray           | array (natural range <>) of time                                                                   |                                                                        |
| BooleanArray        | array (natural range <>) of boolean                                                                |                                                                        |
| IntegerVectorArray  | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of integer            |                                                                        |
| NaturalVectorArray  | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of natural            |                                                                        |
| PositiveVectorArray | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of positive           |                                                                        |
| RealVectorArray     | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of real               |                                                                        |
| TimeVectorArray     | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of time               |                                                                        |
| BooleanVectorArray  | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of boolean            |                                                                        |
| frequency           |                                                                                                    | Some synthesis tools wont accept unit typespragma translate_off        |
| Slv256Array         | array (natural range <>) of slv(255 downto 0)                                                      | pragma translate_onAdd more slv array sizes here as they become needed |
| Slv255Array         | array (natural range <>) of slv(254 downto 0)                                                      |                                                                        |
| Slv254Array         | array (natural range <>) of slv(253 downto 0)                                                      |                                                                        |
| Slv253Array         | array (natural range <>) of slv(252 downto 0)                                                      |                                                                        |
| Slv252Array         | array (natural range <>) of slv(251 downto 0)                                                      |                                                                        |
| Slv251Array         | array (natural range <>) of slv(250 downto 0)                                                      |                                                                        |
| Slv250Array         | array (natural range <>) of slv(249 downto 0)                                                      |                                                                        |
| Slv249Array         | array (natural range <>) of slv(248 downto 0)                                                      |                                                                        |
| Slv248Array         | array (natural range <>) of slv(247 downto 0)                                                      |                                                                        |
| Slv247Array         | array (natural range <>) of slv(246 downto 0)                                                      |                                                                        |
| Slv246Array         | array (natural range <>) of slv(245 downto 0)                                                      |                                                                        |
| Slv245Array         | array (natural range <>) of slv(244 downto 0)                                                      |                                                                        |
| Slv244Array         | array (natural range <>) of slv(243 downto 0)                                                      |                                                                        |
| Slv243Array         | array (natural range <>) of slv(242 downto 0)                                                      |                                                                        |
| Slv242Array         | array (natural range <>) of slv(241 downto 0)                                                      |                                                                        |
| Slv241Array         | array (natural range <>) of slv(240 downto 0)                                                      |                                                                        |
| Slv240Array         | array (natural range <>) of slv(239 downto 0)                                                      |                                                                        |
| Slv239Array         | array (natural range <>) of slv(238 downto 0)                                                      |                                                                        |
| Slv238Array         | array (natural range <>) of slv(237 downto 0)                                                      |                                                                        |
| Slv237Array         | array (natural range <>) of slv(236 downto 0)                                                      |                                                                        |
| Slv236Array         | array (natural range <>) of slv(235 downto 0)                                                      |                                                                        |
| Slv235Array         | array (natural range <>) of slv(234 downto 0)                                                      |                                                                        |
| Slv234Array         | array (natural range <>) of slv(233 downto 0)                                                      |                                                                        |
| Slv233Array         | array (natural range <>) of slv(232 downto 0)                                                      |                                                                        |
| Slv232Array         | array (natural range <>) of slv(231 downto 0)                                                      |                                                                        |
| Slv231Array         | array (natural range <>) of slv(230 downto 0)                                                      |                                                                        |
| Slv230Array         | array (natural range <>) of slv(229 downto 0)                                                      |                                                                        |
| Slv229Array         | array (natural range <>) of slv(228 downto 0)                                                      |                                                                        |
| Slv228Array         | array (natural range <>) of slv(227 downto 0)                                                      |                                                                        |
| Slv227Array         | array (natural range <>) of slv(226 downto 0)                                                      |                                                                        |
| Slv226Array         | array (natural range <>) of slv(225 downto 0)                                                      |                                                                        |
| Slv225Array         | array (natural range <>) of slv(224 downto 0)                                                      |                                                                        |
| Slv224Array         | array (natural range <>) of slv(223 downto 0)                                                      |                                                                        |
| Slv223Array         | array (natural range <>) of slv(222 downto 0)                                                      |                                                                        |
| Slv222Array         | array (natural range <>) of slv(221 downto 0)                                                      |                                                                        |
| Slv221Array         | array (natural range <>) of slv(220 downto 0)                                                      |                                                                        |
| Slv220Array         | array (natural range <>) of slv(219 downto 0)                                                      |                                                                        |
| Slv219Array         | array (natural range <>) of slv(218 downto 0)                                                      |                                                                        |
| Slv218Array         | array (natural range <>) of slv(217 downto 0)                                                      |                                                                        |
| Slv217Array         | array (natural range <>) of slv(216 downto 0)                                                      |                                                                        |
| Slv216Array         | array (natural range <>) of slv(215 downto 0)                                                      |                                                                        |
| Slv215Array         | array (natural range <>) of slv(214 downto 0)                                                      |                                                                        |
| Slv214Array         | array (natural range <>) of slv(213 downto 0)                                                      |                                                                        |
| Slv213Array         | array (natural range <>) of slv(212 downto 0)                                                      |                                                                        |
| Slv212Array         | array (natural range <>) of slv(211 downto 0)                                                      |                                                                        |
| Slv211Array         | array (natural range <>) of slv(210 downto 0)                                                      |                                                                        |
| Slv210Array         | array (natural range <>) of slv(209 downto 0)                                                      |                                                                        |
| Slv209Array         | array (natural range <>) of slv(208 downto 0)                                                      |                                                                        |
| Slv208Array         | array (natural range <>) of slv(207 downto 0)                                                      |                                                                        |
| Slv207Array         | array (natural range <>) of slv(206 downto 0)                                                      |                                                                        |
| Slv206Array         | array (natural range <>) of slv(205 downto 0)                                                      |                                                                        |
| Slv205Array         | array (natural range <>) of slv(204 downto 0)                                                      |                                                                        |
| Slv204Array         | array (natural range <>) of slv(203 downto 0)                                                      |                                                                        |
| Slv203Array         | array (natural range <>) of slv(202 downto 0)                                                      |                                                                        |
| Slv202Array         | array (natural range <>) of slv(201 downto 0)                                                      |                                                                        |
| Slv201Array         | array (natural range <>) of slv(200 downto 0)                                                      |                                                                        |
| Slv200Array         | array (natural range <>) of slv(199 downto 0)                                                      |                                                                        |
| Slv199Array         | array (natural range <>) of slv(198 downto 0)                                                      |                                                                        |
| Slv198Array         | array (natural range <>) of slv(197 downto 0)                                                      |                                                                        |
| Slv197Array         | array (natural range <>) of slv(196 downto 0)                                                      |                                                                        |
| Slv196Array         | array (natural range <>) of slv(195 downto 0)                                                      |                                                                        |
| Slv195Array         | array (natural range <>) of slv(194 downto 0)                                                      |                                                                        |
| Slv194Array         | array (natural range <>) of slv(193 downto 0)                                                      |                                                                        |
| Slv193Array         | array (natural range <>) of slv(192 downto 0)                                                      |                                                                        |
| Slv192Array         | array (natural range <>) of slv(191 downto 0)                                                      |                                                                        |
| Slv191Array         | array (natural range <>) of slv(190 downto 0)                                                      |                                                                        |
| Slv190Array         | array (natural range <>) of slv(189 downto 0)                                                      |                                                                        |
| Slv189Array         | array (natural range <>) of slv(188 downto 0)                                                      |                                                                        |
| Slv188Array         | array (natural range <>) of slv(187 downto 0)                                                      |                                                                        |
| Slv187Array         | array (natural range <>) of slv(186 downto 0)                                                      |                                                                        |
| Slv186Array         | array (natural range <>) of slv(185 downto 0)                                                      |                                                                        |
| Slv185Array         | array (natural range <>) of slv(184 downto 0)                                                      |                                                                        |
| Slv184Array         | array (natural range <>) of slv(183 downto 0)                                                      |                                                                        |
| Slv183Array         | array (natural range <>) of slv(182 downto 0)                                                      |                                                                        |
| Slv182Array         | array (natural range <>) of slv(181 downto 0)                                                      |                                                                        |
| Slv181Array         | array (natural range <>) of slv(180 downto 0)                                                      |                                                                        |
| Slv180Array         | array (natural range <>) of slv(179 downto 0)                                                      |                                                                        |
| Slv179Array         | array (natural range <>) of slv(178 downto 0)                                                      |                                                                        |
| Slv178Array         | array (natural range <>) of slv(177 downto 0)                                                      |                                                                        |
| Slv177Array         | array (natural range <>) of slv(176 downto 0)                                                      |                                                                        |
| Slv176Array         | array (natural range <>) of slv(175 downto 0)                                                      |                                                                        |
| Slv175Array         | array (natural range <>) of slv(174 downto 0)                                                      |                                                                        |
| Slv174Array         | array (natural range <>) of slv(173 downto 0)                                                      |                                                                        |
| Slv173Array         | array (natural range <>) of slv(172 downto 0)                                                      |                                                                        |
| Slv172Array         | array (natural range <>) of slv(171 downto 0)                                                      |                                                                        |
| Slv171Array         | array (natural range <>) of slv(170 downto 0)                                                      |                                                                        |
| Slv170Array         | array (natural range <>) of slv(169 downto 0)                                                      |                                                                        |
| Slv169Array         | array (natural range <>) of slv(168 downto 0)                                                      |                                                                        |
| Slv168Array         | array (natural range <>) of slv(167 downto 0)                                                      |                                                                        |
| Slv167Array         | array (natural range <>) of slv(166 downto 0)                                                      |                                                                        |
| Slv166Array         | array (natural range <>) of slv(165 downto 0)                                                      |                                                                        |
| Slv165Array         | array (natural range <>) of slv(164 downto 0)                                                      |                                                                        |
| Slv164Array         | array (natural range <>) of slv(163 downto 0)                                                      |                                                                        |
| Slv163Array         | array (natural range <>) of slv(162 downto 0)                                                      |                                                                        |
| Slv162Array         | array (natural range <>) of slv(161 downto 0)                                                      |                                                                        |
| Slv161Array         | array (natural range <>) of slv(160 downto 0)                                                      |                                                                        |
| Slv160Array         | array (natural range <>) of slv(159 downto 0)                                                      |                                                                        |
| Slv159Array         | array (natural range <>) of slv(158 downto 0)                                                      |                                                                        |
| Slv158Array         | array (natural range <>) of slv(157 downto 0)                                                      |                                                                        |
| Slv157Array         | array (natural range <>) of slv(156 downto 0)                                                      |                                                                        |
| Slv156Array         | array (natural range <>) of slv(155 downto 0)                                                      |                                                                        |
| Slv155Array         | array (natural range <>) of slv(154 downto 0)                                                      |                                                                        |
| Slv154Array         | array (natural range <>) of slv(153 downto 0)                                                      |                                                                        |
| Slv153Array         | array (natural range <>) of slv(152 downto 0)                                                      |                                                                        |
| Slv152Array         | array (natural range <>) of slv(151 downto 0)                                                      |                                                                        |
| Slv151Array         | array (natural range <>) of slv(150 downto 0)                                                      |                                                                        |
| Slv150Array         | array (natural range <>) of slv(149 downto 0)                                                      |                                                                        |
| Slv149Array         | array (natural range <>) of slv(148 downto 0)                                                      |                                                                        |
| Slv148Array         | array (natural range <>) of slv(147 downto 0)                                                      |                                                                        |
| Slv147Array         | array (natural range <>) of slv(146 downto 0)                                                      |                                                                        |
| Slv146Array         | array (natural range <>) of slv(145 downto 0)                                                      |                                                                        |
| Slv145Array         | array (natural range <>) of slv(144 downto 0)                                                      |                                                                        |
| Slv144Array         | array (natural range <>) of slv(143 downto 0)                                                      |                                                                        |
| Slv143Array         | array (natural range <>) of slv(142 downto 0)                                                      |                                                                        |
| Slv142Array         | array (natural range <>) of slv(141 downto 0)                                                      |                                                                        |
| Slv141Array         | array (natural range <>) of slv(140 downto 0)                                                      |                                                                        |
| Slv140Array         | array (natural range <>) of slv(139 downto 0)                                                      |                                                                        |
| Slv139Array         | array (natural range <>) of slv(138 downto 0)                                                      |                                                                        |
| Slv138Array         | array (natural range <>) of slv(137 downto 0)                                                      |                                                                        |
| Slv137Array         | array (natural range <>) of slv(136 downto 0)                                                      |                                                                        |
| Slv136Array         | array (natural range <>) of slv(135 downto 0)                                                      |                                                                        |
| Slv135Array         | array (natural range <>) of slv(134 downto 0)                                                      |                                                                        |
| Slv134Array         | array (natural range <>) of slv(133 downto 0)                                                      |                                                                        |
| Slv133Array         | array (natural range <>) of slv(132 downto 0)                                                      |                                                                        |
| Slv132Array         | array (natural range <>) of slv(131 downto 0)                                                      |                                                                        |
| Slv131Array         | array (natural range <>) of slv(130 downto 0)                                                      |                                                                        |
| Slv130Array         | array (natural range <>) of slv(129 downto 0)                                                      |                                                                        |
| Slv129Array         | array (natural range <>) of slv(128 downto 0)                                                      |                                                                        |
| Slv128Array         | array (natural range <>) of slv(127 downto 0)                                                      |                                                                        |
| Slv127Array         | array (natural range <>) of slv(126 downto 0)                                                      |                                                                        |
| Slv126Array         | array (natural range <>) of slv(125 downto 0)                                                      |                                                                        |
| Slv125Array         | array (natural range <>) of slv(124 downto 0)                                                      |                                                                        |
| Slv124Array         | array (natural range <>) of slv(123 downto 0)                                                      |                                                                        |
| Slv123Array         | array (natural range <>) of slv(122 downto 0)                                                      |                                                                        |
| Slv122Array         | array (natural range <>) of slv(121 downto 0)                                                      |                                                                        |
| Slv121Array         | array (natural range <>) of slv(120 downto 0)                                                      |                                                                        |
| Slv120Array         | array (natural range <>) of slv(119 downto 0)                                                      |                                                                        |
| Slv119Array         | array (natural range <>) of slv(118 downto 0)                                                      |                                                                        |
| Slv118Array         | array (natural range <>) of slv(117 downto 0)                                                      |                                                                        |
| Slv117Array         | array (natural range <>) of slv(116 downto 0)                                                      |                                                                        |
| Slv116Array         | array (natural range <>) of slv(115 downto 0)                                                      |                                                                        |
| Slv115Array         | array (natural range <>) of slv(114 downto 0)                                                      |                                                                        |
| Slv114Array         | array (natural range <>) of slv(113 downto 0)                                                      |                                                                        |
| Slv113Array         | array (natural range <>) of slv(112 downto 0)                                                      |                                                                        |
| Slv112Array         | array (natural range <>) of slv(111 downto 0)                                                      |                                                                        |
| Slv111Array         | array (natural range <>) of slv(110 downto 0)                                                      |                                                                        |
| Slv110Array         | array (natural range <>) of slv(109 downto 0)                                                      |                                                                        |
| Slv109Array         | array (natural range <>) of slv(108 downto 0)                                                      |                                                                        |
| Slv108Array         | array (natural range <>) of slv(107 downto 0)                                                      |                                                                        |
| Slv107Array         | array (natural range <>) of slv(106 downto 0)                                                      |                                                                        |
| Slv106Array         | array (natural range <>) of slv(105 downto 0)                                                      |                                                                        |
| Slv105Array         | array (natural range <>) of slv(104 downto 0)                                                      |                                                                        |
| Slv104Array         | array (natural range <>) of slv(103 downto 0)                                                      |                                                                        |
| Slv103Array         | array (natural range <>) of slv(102 downto 0)                                                      |                                                                        |
| Slv102Array         | array (natural range <>) of slv(101 downto 0)                                                      |                                                                        |
| Slv101Array         | array (natural range <>) of slv(100 downto 0)                                                      |                                                                        |
| Slv100Array         | array (natural range <>) of slv(99 downto 0)                                                       |                                                                        |
| Slv99Array          | array (natural range <>) of slv(98 downto 0)                                                       |                                                                        |
| Slv98Array          | array (natural range <>) of slv(97 downto 0)                                                       |                                                                        |
| Slv97Array          | array (natural range <>) of slv(96 downto 0)                                                       |                                                                        |
| Slv96Array          | array (natural range <>) of slv(95 downto 0)                                                       |                                                                        |
| Slv95Array          | array (natural range <>) of slv(94 downto 0)                                                       |                                                                        |
| Slv94Array          | array (natural range <>) of slv(93 downto 0)                                                       |                                                                        |
| Slv93Array          | array (natural range <>) of slv(92 downto 0)                                                       |                                                                        |
| Slv92Array          | array (natural range <>) of slv(91 downto 0)                                                       |                                                                        |
| Slv91Array          | array (natural range <>) of slv(90 downto 0)                                                       |                                                                        |
| Slv90Array          | array (natural range <>) of slv(89 downto 0)                                                       |                                                                        |
| Slv89Array          | array (natural range <>) of slv(88 downto 0)                                                       |                                                                        |
| Slv88Array          | array (natural range <>) of slv(87 downto 0)                                                       |                                                                        |
| Slv87Array          | array (natural range <>) of slv(86 downto 0)                                                       |                                                                        |
| Slv86Array          | array (natural range <>) of slv(85 downto 0)                                                       |                                                                        |
| Slv85Array          | array (natural range <>) of slv(84 downto 0)                                                       |                                                                        |
| Slv84Array          | array (natural range <>) of slv(83 downto 0)                                                       |                                                                        |
| Slv83Array          | array (natural range <>) of slv(82 downto 0)                                                       |                                                                        |
| Slv82Array          | array (natural range <>) of slv(81 downto 0)                                                       |                                                                        |
| Slv81Array          | array (natural range <>) of slv(80 downto 0)                                                       |                                                                        |
| Slv80Array          | array (natural range <>) of slv(79 downto 0)                                                       |                                                                        |
| Slv79Array          | array (natural range <>) of slv(78 downto 0)                                                       |                                                                        |
| Slv78Array          | array (natural range <>) of slv(77 downto 0)                                                       |                                                                        |
| Slv77Array          | array (natural range <>) of slv(76 downto 0)                                                       |                                                                        |
| Slv76Array          | array (natural range <>) of slv(75 downto 0)                                                       |                                                                        |
| Slv75Array          | array (natural range <>) of slv(74 downto 0)                                                       |                                                                        |
| Slv74Array          | array (natural range <>) of slv(73 downto 0)                                                       |                                                                        |
| Slv73Array          | array (natural range <>) of slv(72 downto 0)                                                       |                                                                        |
| Slv72Array          | array (natural range <>) of slv(71 downto 0)                                                       |                                                                        |
| Slv71Array          | array (natural range <>) of slv(70 downto 0)                                                       |                                                                        |
| Slv70Array          | array (natural range <>) of slv(69 downto 0)                                                       |                                                                        |
| Slv69Array          | array (natural range <>) of slv(68 downto 0)                                                       |                                                                        |
| Slv68Array          | array (natural range <>) of slv(67 downto 0)                                                       |                                                                        |
| Slv67Array          | array (natural range <>) of slv(66 downto 0)                                                       |                                                                        |
| Slv66Array          | array (natural range <>) of slv(65 downto 0)                                                       |                                                                        |
| Slv65Array          | array (natural range <>) of slv(64 downto 0)                                                       |                                                                        |
| Slv64Array          | array (natural range <>) of slv(63 downto 0)                                                       |                                                                        |
| Slv63Array          | array (natural range <>) of slv(62 downto 0)                                                       |                                                                        |
| Slv62Array          | array (natural range <>) of slv(61 downto 0)                                                       |                                                                        |
| Slv61Array          | array (natural range <>) of slv(60 downto 0)                                                       |                                                                        |
| Slv60Array          | array (natural range <>) of slv(59 downto 0)                                                       |                                                                        |
| Slv59Array          | array (natural range <>) of slv(58 downto 0)                                                       |                                                                        |
| Slv58Array          | array (natural range <>) of slv(57 downto 0)                                                       |                                                                        |
| Slv57Array          | array (natural range <>) of slv(56 downto 0)                                                       |                                                                        |
| Slv56Array          | array (natural range <>) of slv(55 downto 0)                                                       |                                                                        |
| Slv55Array          | array (natural range <>) of slv(54 downto 0)                                                       |                                                                        |
| Slv54Array          | array (natural range <>) of slv(53 downto 0)                                                       |                                                                        |
| Slv53Array          | array (natural range <>) of slv(52 downto 0)                                                       |                                                                        |
| Slv52Array          | array (natural range <>) of slv(51 downto 0)                                                       |                                                                        |
| Slv51Array          | array (natural range <>) of slv(50 downto 0)                                                       |                                                                        |
| Slv50Array          | array (natural range <>) of slv(49 downto 0)                                                       |                                                                        |
| Slv49Array          | array (natural range <>) of slv(48 downto 0)                                                       |                                                                        |
| Slv48Array          | array (natural range <>) of slv(47 downto 0)                                                       |                                                                        |
| Slv47Array          | array (natural range <>) of slv(46 downto 0)                                                       |                                                                        |
| Slv46Array          | array (natural range <>) of slv(45 downto 0)                                                       |                                                                        |
| Slv45Array          | array (natural range <>) of slv(44 downto 0)                                                       |                                                                        |
| Slv44Array          | array (natural range <>) of slv(43 downto 0)                                                       |                                                                        |
| Slv43Array          | array (natural range <>) of slv(42 downto 0)                                                       |                                                                        |
| Slv42Array          | array (natural range <>) of slv(41 downto 0)                                                       |                                                                        |
| Slv41Array          | array (natural range <>) of slv(40 downto 0)                                                       |                                                                        |
| Slv40Array          | array (natural range <>) of slv(39 downto 0)                                                       |                                                                        |
| Slv39Array          | array (natural range <>) of slv(38 downto 0)                                                       |                                                                        |
| Slv38Array          | array (natural range <>) of slv(37 downto 0)                                                       |                                                                        |
| Slv37Array          | array (natural range <>) of slv(36 downto 0)                                                       |                                                                        |
| Slv36Array          | array (natural range <>) of slv(35 downto 0)                                                       |                                                                        |
| Slv35Array          | array (natural range <>) of slv(34 downto 0)                                                       |                                                                        |
| Slv34Array          | array (natural range <>) of slv(33 downto 0)                                                       |                                                                        |
| Slv33Array          | array (natural range <>) of slv(32 downto 0)                                                       |                                                                        |
| Slv32Array          | array (natural range <>) of slv(31 downto 0)                                                       |                                                                        |
| Slv31Array          | array (natural range <>) of slv(30 downto 0)                                                       |                                                                        |
| Slv30Array          | array (natural range <>) of slv(29 downto 0)                                                       |                                                                        |
| Slv29Array          | array (natural range <>) of slv(28 downto 0)                                                       |                                                                        |
| Slv28Array          | array (natural range <>) of slv(27 downto 0)                                                       |                                                                        |
| Slv27Array          | array (natural range <>) of slv(26 downto 0)                                                       |                                                                        |
| Slv26Array          | array (natural range <>) of slv(25 downto 0)                                                       |                                                                        |
| Slv25Array          | array (natural range <>) of slv(24 downto 0)                                                       |                                                                        |
| Slv24Array          | array (natural range <>) of slv(23 downto 0)                                                       |                                                                        |
| Slv23Array          | array (natural range <>) of slv(22 downto 0)                                                       |                                                                        |
| Slv22Array          | array (natural range <>) of slv(21 downto 0)                                                       |                                                                        |
| Slv21Array          | array (natural range <>) of slv(20 downto 0)                                                       |                                                                        |
| Slv20Array          | array (natural range <>) of slv(19 downto 0)                                                       |                                                                        |
| Slv19Array          | array (natural range <>) of slv(18 downto 0)                                                       |                                                                        |
| Slv18Array          | array (natural range <>) of slv(17 downto 0)                                                       |                                                                        |
| Slv17Array          | array (natural range <>) of slv(16 downto 0)                                                       |                                                                        |
| Slv16Array          | array (natural range <>) of slv(15 downto 0)                                                       |                                                                        |
| Slv15Array          | array (natural range <>) of slv(14 downto 0)                                                       |                                                                        |
| Slv14Array          | array (natural range <>) of slv(13 downto 0)                                                       |                                                                        |
| Slv13Array          | array (natural range <>) of slv(12 downto 0)                                                       |                                                                        |
| Slv12Array          | array (natural range <>) of slv(11 downto 0)                                                       |                                                                        |
| Slv11Array          | array (natural range <>) of slv(10 downto 0)                                                       |                                                                        |
| Slv10Array          | array (natural range <>) of slv(9 downto 0)                                                        |                                                                        |
| Slv9Array           | array (natural range <>) of slv(8 downto 0)                                                        |                                                                        |
| Slv8Array           | array (natural range <>) of slv(7 downto 0)                                                        |                                                                        |
| Slv7Array           | array (natural range <>) of slv(6 downto 0)                                                        |                                                                        |
| Slv6Array           | array (natural range <>) of slv(5 downto 0)                                                        |                                                                        |
| Slv5Array           | array (natural range <>) of slv(4 downto 0)                                                        |                                                                        |
| Slv4Array           | array (natural range <>) of slv(3 downto 0)                                                        |                                                                        |
| Slv3Array           | array (natural range <>) of slv(2 downto 0)                                                        |                                                                        |
| Slv2Array           | array (natural range <>) of slv(1 downto 0)                                                        |                                                                        |
| Slv1Array           | array (natural range <>) of slv(0 downto 0)                                                        |                                                                        |
| Slv256VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(255 downto 0)  | Add more slv vector array sizes here as they become needed             |
| Slv255VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(254 downto 0)  |                                                                        |
| Slv254VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(253 downto 0)  |                                                                        |
| Slv253VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(252 downto 0)  |                                                                        |
| Slv252VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(251 downto 0)  |                                                                        |
| Slv251VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(250 downto 0)  |                                                                        |
| Slv250VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(249 downto 0)  |                                                                        |
| Slv249VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(248 downto 0)  |                                                                        |
| Slv248VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(247 downto 0)  |                                                                        |
| Slv247VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(246 downto 0)  |                                                                        |
| Slv246VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(245 downto 0)  |                                                                        |
| Slv245VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(244 downto 0)  |                                                                        |
| Slv244VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(243 downto 0)  |                                                                        |
| Slv243VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(242 downto 0)  |                                                                        |
| Slv242VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(241 downto 0)  |                                                                        |
| Slv241VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(240 downto 0)  |                                                                        |
| Slv240VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(239 downto 0)  |                                                                        |
| Slv239VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(238 downto 0)  |                                                                        |
| Slv238VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(237 downto 0)  |                                                                        |
| Slv237VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(236 downto 0)  |                                                                        |
| Slv236VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(235 downto 0)  |                                                                        |
| Slv235VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(234 downto 0)  |                                                                        |
| Slv234VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(233 downto 0)  |                                                                        |
| Slv233VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(232 downto 0)  |                                                                        |
| Slv232VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(231 downto 0)  |                                                                        |
| Slv231VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(230 downto 0)  |                                                                        |
| Slv230VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(229 downto 0)  |                                                                        |
| Slv229VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(228 downto 0)  |                                                                        |
| Slv228VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(227 downto 0)  |                                                                        |
| Slv227VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(226 downto 0)  |                                                                        |
| Slv226VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(225 downto 0)  |                                                                        |
| Slv225VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(224 downto 0)  |                                                                        |
| Slv224VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(223 downto 0)  |                                                                        |
| Slv223VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(222 downto 0)  |                                                                        |
| Slv222VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(221 downto 0)  |                                                                        |
| Slv221VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(220 downto 0)  |                                                                        |
| Slv220VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(219 downto 0)  |                                                                        |
| Slv219VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(218 downto 0)  |                                                                        |
| Slv218VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(217 downto 0)  |                                                                        |
| Slv217VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(216 downto 0)  |                                                                        |
| Slv216VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(215 downto 0)  |                                                                        |
| Slv215VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(214 downto 0)  |                                                                        |
| Slv214VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(213 downto 0)  |                                                                        |
| Slv213VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(212 downto 0)  |                                                                        |
| Slv212VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(211 downto 0)  |                                                                        |
| Slv211VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(210 downto 0)  |                                                                        |
| Slv210VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(209 downto 0)  |                                                                        |
| Slv209VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(208 downto 0)  |                                                                        |
| Slv208VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(207 downto 0)  |                                                                        |
| Slv207VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(206 downto 0)  |                                                                        |
| Slv206VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(205 downto 0)  |                                                                        |
| Slv205VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(204 downto 0)  |                                                                        |
| Slv204VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(203 downto 0)  |                                                                        |
| Slv203VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(202 downto 0)  |                                                                        |
| Slv202VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(201 downto 0)  |                                                                        |
| Slv201VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(200 downto 0)  |                                                                        |
| Slv200VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(199 downto 0)  |                                                                        |
| Slv199VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(198 downto 0)  |                                                                        |
| Slv198VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(197 downto 0)  |                                                                        |
| Slv197VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(196 downto 0)  |                                                                        |
| Slv196VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(195 downto 0)  |                                                                        |
| Slv195VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(194 downto 0)  |                                                                        |
| Slv194VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(193 downto 0)  |                                                                        |
| Slv193VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(192 downto 0)  |                                                                        |
| Slv192VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(191 downto 0)  |                                                                        |
| Slv191VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(190 downto 0)  |                                                                        |
| Slv190VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(189 downto 0)  |                                                                        |
| Slv189VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(188 downto 0)  |                                                                        |
| Slv188VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(187 downto 0)  |                                                                        |
| Slv187VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(186 downto 0)  |                                                                        |
| Slv186VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(185 downto 0)  |                                                                        |
| Slv185VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(184 downto 0)  |                                                                        |
| Slv184VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(183 downto 0)  |                                                                        |
| Slv183VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(182 downto 0)  |                                                                        |
| Slv182VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(181 downto 0)  |                                                                        |
| Slv181VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(180 downto 0)  |                                                                        |
| Slv180VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(179 downto 0)  |                                                                        |
| Slv179VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(178 downto 0)  |                                                                        |
| Slv178VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(177 downto 0)  |                                                                        |
| Slv177VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(176 downto 0)  |                                                                        |
| Slv176VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(175 downto 0)  |                                                                        |
| Slv175VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(174 downto 0)  |                                                                        |
| Slv174VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(173 downto 0)  |                                                                        |
| Slv173VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(172 downto 0)  |                                                                        |
| Slv172VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(171 downto 0)  |                                                                        |
| Slv171VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(170 downto 0)  |                                                                        |
| Slv170VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(169 downto 0)  |                                                                        |
| Slv169VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(168 downto 0)  |                                                                        |
| Slv168VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(167 downto 0)  |                                                                        |
| Slv167VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(166 downto 0)  |                                                                        |
| Slv166VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(165 downto 0)  |                                                                        |
| Slv165VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(164 downto 0)  |                                                                        |
| Slv164VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(163 downto 0)  |                                                                        |
| Slv163VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(162 downto 0)  |                                                                        |
| Slv162VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(161 downto 0)  |                                                                        |
| Slv161VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(160 downto 0)  |                                                                        |
| Slv160VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(159 downto 0)  |                                                                        |
| Slv159VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(158 downto 0)  |                                                                        |
| Slv158VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(157 downto 0)  |                                                                        |
| Slv157VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(156 downto 0)  |                                                                        |
| Slv156VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(155 downto 0)  |                                                                        |
| Slv155VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(154 downto 0)  |                                                                        |
| Slv154VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(153 downto 0)  |                                                                        |
| Slv153VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(152 downto 0)  |                                                                        |
| Slv152VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(151 downto 0)  |                                                                        |
| Slv151VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(150 downto 0)  |                                                                        |
| Slv150VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(149 downto 0)  |                                                                        |
| Slv149VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(148 downto 0)  |                                                                        |
| Slv148VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(147 downto 0)  |                                                                        |
| Slv147VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(146 downto 0)  |                                                                        |
| Slv146VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(145 downto 0)  |                                                                        |
| Slv145VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(144 downto 0)  |                                                                        |
| Slv144VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(143 downto 0)  |                                                                        |
| Slv143VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(142 downto 0)  |                                                                        |
| Slv142VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(141 downto 0)  |                                                                        |
| Slv141VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(140 downto 0)  |                                                                        |
| Slv140VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(139 downto 0)  |                                                                        |
| Slv139VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(138 downto 0)  |                                                                        |
| Slv138VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(137 downto 0)  |                                                                        |
| Slv137VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(136 downto 0)  |                                                                        |
| Slv136VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(135 downto 0)  |                                                                        |
| Slv135VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(134 downto 0)  |                                                                        |
| Slv134VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(133 downto 0)  |                                                                        |
| Slv133VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(132 downto 0)  |                                                                        |
| Slv132VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(131 downto 0)  |                                                                        |
| Slv131VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(130 downto 0)  |                                                                        |
| Slv130VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(129 downto 0)  |                                                                        |
| Slv129VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(128 downto 0)  |                                                                        |
| Slv128VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(127 downto 0)  |                                                                        |
| Slv127VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(126 downto 0)  |                                                                        |
| Slv126VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(125 downto 0)  |                                                                        |
| Slv125VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(124 downto 0)  |                                                                        |
| Slv124VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(123 downto 0)  |                                                                        |
| Slv123VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(122 downto 0)  |                                                                        |
| Slv122VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(121 downto 0)  |                                                                        |
| Slv121VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(120 downto 0)  |                                                                        |
| Slv120VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(119 downto 0)  |                                                                        |
| Slv119VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(118 downto 0)  |                                                                        |
| Slv118VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(117 downto 0)  |                                                                        |
| Slv117VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(116 downto 0)  |                                                                        |
| Slv116VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(115 downto 0)  |                                                                        |
| Slv115VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(114 downto 0)  |                                                                        |
| Slv114VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(113 downto 0)  |                                                                        |
| Slv113VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(112 downto 0)  |                                                                        |
| Slv112VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(111 downto 0)  |                                                                        |
| Slv111VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(110 downto 0)  |                                                                        |
| Slv110VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(109 downto 0)  |                                                                        |
| Slv109VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(108 downto 0)  |                                                                        |
| Slv108VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(107 downto 0)  |                                                                        |
| Slv107VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(106 downto 0)  |                                                                        |
| Slv106VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(105 downto 0)  |                                                                        |
| Slv105VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(104 downto 0)  |                                                                        |
| Slv104VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(103 downto 0)  |                                                                        |
| Slv103VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(102 downto 0)  |                                                                        |
| Slv102VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(101 downto 0)  |                                                                        |
| Slv101VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(100 downto 0)  |                                                                        |
| Slv100VectorArray   | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(99 downto 0)   |                                                                        |
| Slv99VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(98 downto 0)   |                                                                        |
| Slv98VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(97 downto 0)   |                                                                        |
| Slv97VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(96 downto 0)   |                                                                        |
| Slv96VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(95 downto 0)   |                                                                        |
| Slv95VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(94 downto 0)   |                                                                        |
| Slv94VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(93 downto 0)   |                                                                        |
| Slv93VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(92 downto 0)   |                                                                        |
| Slv92VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(91 downto 0)   |                                                                        |
| Slv91VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(90 downto 0)   |                                                                        |
| Slv90VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(89 downto 0)   |                                                                        |
| Slv89VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(88 downto 0)   |                                                                        |
| Slv88VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(87 downto 0)   |                                                                        |
| Slv87VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(86 downto 0)   |                                                                        |
| Slv86VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(85 downto 0)   |                                                                        |
| Slv85VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(84 downto 0)   |                                                                        |
| Slv84VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(83 downto 0)   |                                                                        |
| Slv83VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(82 downto 0)   |                                                                        |
| Slv82VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(81 downto 0)   |                                                                        |
| Slv81VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(80 downto 0)   |                                                                        |
| Slv80VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(79 downto 0)   |                                                                        |
| Slv79VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(78 downto 0)   |                                                                        |
| Slv78VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(77 downto 0)   |                                                                        |
| Slv77VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(76 downto 0)   |                                                                        |
| Slv76VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(75 downto 0)   |                                                                        |
| Slv75VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(74 downto 0)   |                                                                        |
| Slv74VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(73 downto 0)   |                                                                        |
| Slv73VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(72 downto 0)   |                                                                        |
| Slv72VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(71 downto 0)   |                                                                        |
| Slv71VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(70 downto 0)   |                                                                        |
| Slv70VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(69 downto 0)   |                                                                        |
| Slv69VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(68 downto 0)   |                                                                        |
| Slv68VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(67 downto 0)   |                                                                        |
| Slv67VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(66 downto 0)   |                                                                        |
| Slv66VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(65 downto 0)   |                                                                        |
| Slv65VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(64 downto 0)   |                                                                        |
| Slv64VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(63 downto 0)   |                                                                        |
| Slv63VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(62 downto 0)   |                                                                        |
| Slv62VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(61 downto 0)   |                                                                        |
| Slv61VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(60 downto 0)   |                                                                        |
| Slv60VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(59 downto 0)   |                                                                        |
| Slv59VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(58 downto 0)   |                                                                        |
| Slv58VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(57 downto 0)   |                                                                        |
| Slv57VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(56 downto 0)   |                                                                        |
| Slv56VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(55 downto 0)   |                                                                        |
| Slv55VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(54 downto 0)   |                                                                        |
| Slv54VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(53 downto 0)   |                                                                        |
| Slv53VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(52 downto 0)   |                                                                        |
| Slv52VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(51 downto 0)   |                                                                        |
| Slv51VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(50 downto 0)   |                                                                        |
| Slv50VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(49 downto 0)   |                                                                        |
| Slv49VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(48 downto 0)   |                                                                        |
| Slv48VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(47 downto 0)   |                                                                        |
| Slv47VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(46 downto 0)   |                                                                        |
| Slv46VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(45 downto 0)   |                                                                        |
| Slv45VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(44 downto 0)   |                                                                        |
| Slv44VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(43 downto 0)   |                                                                        |
| Slv43VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(42 downto 0)   |                                                                        |
| Slv42VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(41 downto 0)   |                                                                        |
| Slv41VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(40 downto 0)   |                                                                        |
| Slv40VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(39 downto 0)   |                                                                        |
| Slv39VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(38 downto 0)   |                                                                        |
| Slv38VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(37 downto 0)   |                                                                        |
| Slv37VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(36 downto 0)   |                                                                        |
| Slv36VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(35 downto 0)   |                                                                        |
| Slv35VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(34 downto 0)   |                                                                        |
| Slv34VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(33 downto 0)   |                                                                        |
| Slv33VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(32 downto 0)   |                                                                        |
| Slv32VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(31 downto 0)   |                                                                        |
| Slv31VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(30 downto 0)   |                                                                        |
| Slv30VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(29 downto 0)   |                                                                        |
| Slv29VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(28 downto 0)   |                                                                        |
| Slv28VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(27 downto 0)   |                                                                        |
| Slv27VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(26 downto 0)   |                                                                        |
| Slv26VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(25 downto 0)   |                                                                        |
| Slv25VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(24 downto 0)   |                                                                        |
| Slv24VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(23 downto 0)   |                                                                        |
| Slv23VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(22 downto 0)   |                                                                        |
| Slv22VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(21 downto 0)   |                                                                        |
| Slv21VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(20 downto 0)   |                                                                        |
| Slv20VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(19 downto 0)   |                                                                        |
| Slv19VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(18 downto 0)   |                                                                        |
| Slv18VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(17 downto 0)   |                                                                        |
| Slv17VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(16 downto 0)   |                                                                        |
| Slv16VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(15 downto 0)   |                                                                        |
| Slv15VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(14 downto 0)   |                                                                        |
| Slv14VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(13 downto 0)   |                                                                        |
| Slv13VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(12 downto 0)   |                                                                        |
| Slv12VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(11 downto 0)   |                                                                        |
| Slv11VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(10 downto 0)   |                                                                        |
| Slv10VectorArray    | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(9 downto 0)    |                                                                        |
| Slv9VectorArray     | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(8 downto 0)    |                                                                        |
| Slv8VectorArray     | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(7 downto 0)    |                                                                        |
| Slv7VectorArray     | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(6 downto 0)    |                                                                        |
| Slv6VectorArray     | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(5 downto 0)    |                                                                        |
| Slv5VectorArray     | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(4 downto 0)    |                                                                        |
| Slv4VectorArray     | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(3 downto 0)    |                                                                        |
| Slv3VectorArray     | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(2 downto 0)    |                                                                        |
| Slv2VectorArray     | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(1 downto 0)    |                                                                        |
| Slv1VectorArray     | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of slv(0 downto 0)    |                                                                        |
| SlVectorArray       | array (natural range<>,<br><span style="padding-left:20px"> natural range<>) of sl                 |                                                                        |
| BuildInfoRetType    |                                                                                                    |                                                                        |
## Functions
- slvAll <font id="function_arguments">(size  : positive;<br><span style="padding-left:20px"> value : sl) </font> <font id="function_return">return slv </font>
**Description**
Create an arbitrary sized slv with all bits set high or low
- slvZero <font id="function_arguments">(size : positive) </font> <font id="function_return">return slv </font>
- slvOne <font id="function_arguments">(size  : positive) </font> <font id="function_return">return slv </font>
- isPowerOf2 <font id="function_arguments">(number       : natural) </font> <font id="function_return">return boolean </font>
**Description**
Very useful functions
- isPowerOf2 <font id="function_arguments">(vector       : slv) </font> <font id="function_return">return boolean </font>
- log2 <font id="function_arguments">(constant number    : integer) </font> <font id="function_return">return natural </font>
- logB <font id="function_arguments">(base : natural;<br><span style="padding-left:20px"> number : natural) </font> <font id="function_return">return natural </font>
- bitSize <font id="function_arguments">(constant number : natural) </font> <font id="function_return">return positive </font>
- bitReverse <font id="function_arguments">(a            : slv) </font> <font id="function_return">return slv </font>
- wordCount <font id="function_arguments">(number : positive;<br><span style="padding-left:20px"> wordSize : positive := 8) </font> <font id="function_return">return natural </font>
- endianSwap <font id="function_arguments">(vector : slv) </font> <font id="function_return">return slv </font>
- list <font id="function_arguments">(constant start,<br><span style="padding-left:20px"> size,<br><span style="padding-left:20px"> step : integer) </font> <font id="function_return">return IntegerArray </font>
**Description**
Similar to python's range() function
- decode <font id="function_arguments">(v    : slv) </font> <font id="function_return">return slv </font>
**Description**
Simple decoder and mux functions
- genmux <font id="function_arguments">(s,<br><span style="padding-left:20px"> v : slv) </font> <font id="function_return">return sl </font>
- toBoolean <font id="function_arguments">(logic : sl) </font> <font id="function_return">return boolean </font>
**Description**
This should be unnecessary in VHDL 2008
- toSl <font id="function_arguments">(bool       : boolean) </font> <font id="function_return">return sl </font>
- toString <font id="function_arguments">(bool   : boolean) </font> <font id="function_return">return string </font>
- toBoolean <font id="function_arguments">(str   : string) </font> <font id="function_return">return boolean </font>
- toSlv <font id="function_arguments">(bools      : BooleanArray) </font> <font id="function_return">return slv </font>
- toBooleanArray <font id="function_arguments">(vec : slv) </font> <font id="function_return">return BooleanArray </font>
- uOr <font id="function_arguments">(vec  : slv) </font> <font id="function_return">return sl </font>
**Description**
Unary reduction operators, also unnecessary in VHDL 2008
- uAnd <font id="function_arguments">(vec : slv) </font> <font id="function_return">return sl </font>
- uXor <font id="function_arguments">(vec : slv) </font> <font id="function_return">return sl </font>
- allBits <font id="function_arguments">(vec : slv;<br><span style="padding-left:20px"> test : sl) </font> <font id="function_return">return boolean </font>
**Description**
Test if all bits in a vector are set to a given logic value
- noBits <font id="function_arguments">(vec  : slv;<br><span style="padding-left:20px"> test : sl) </font> <font id="function_return">return boolean </font>
- evenParity <font id="function_arguments">(vec : slv) </font> <font id="function_return">return sl </font>
**Description**
These just use uXor to calculate parityOutput is parity bit value needed to achieve that parity given vec.
- oddParity <font id="function_arguments">(vec  : slv) </font> <font id="function_return">return sl </font>
- onesCountU <font id="function_arguments">(vec : slv) </font> <font id="function_return">return unsigned </font>
**Description**
Functions for counting the number of '1' in a slv bus
- onesCount <font id="function_arguments">(vec : slv) </font> <font id="function_return">return slv </font>
- grayEncode <font id="function_arguments">(vec : unsigned) </font> <font id="function_return">return unsigned </font>
**Description**
Gray Code functions
- grayEncode <font id="function_arguments">(vec : slv) </font> <font id="function_return">return slv </font>
- grayDecode <font id="function_arguments">(vec : unsigned) </font> <font id="function_return">return unsigned </font>
- grayDecode <font id="function_arguments">(vec : slv) </font> <font id="function_return">return slv </font>
- lfsrShift <font id="function_arguments">(lfsr : slv;<br><span style="padding-left:20px"> constant taps : NaturalArray;<br><span style="padding-left:20px"> input : sl := '0') </font> <font id="function_return">return slv </font>
**Description**
Linear Feedback Shift Register function
- maximum <font id="function_arguments">(left,<br><span style="padding-left:20px"> right : integer) </font> <font id="function_return">return integer </font>
- maximum <font id="function_arguments">(a : IntegerArray) </font> <font id="function_return">return integer </font>
- minimum <font id="function_arguments">(left,<br><span style="padding-left:20px"> right : integer) </font> <font id="function_return">return integer </font>
- minimum <font id="function_arguments">(a : IntegerArray) </font> <font id="function_return">return integer </font>
- sort <font id="function_arguments">(a : IntegerArray) </font> <font id="function_return">return IntegerArray </font>
- median <font id="function_arguments">(a : IntegerArray) </font> <font id="function_return">return integer </font>
- ite <font id="function_arguments">(i : boolean;<br><span style="padding-left:20px"> t : boolean;<br><span style="padding-left:20px"> e : boolean) </font> <font id="function_return">return boolean </font>
**Description**
One line if-then-else functions. Useful for assigning constants based on generics.
- ite <font id="function_arguments">(i : boolean;<br><span style="padding-left:20px"> t : sl;<br><span style="padding-left:20px"> e : sl) </font> <font id="function_return">return sl </font>
- ite <font id="function_arguments">(i : boolean;<br><span style="padding-left:20px"> t : slv;<br><span style="padding-left:20px"> e : slv) </font> <font id="function_return">return slv </font>
- ite <font id="function_arguments">(i : boolean;<br><span style="padding-left:20px"> t : bit;<br><span style="padding-left:20px"> e : bit) </font> <font id="function_return">return bit </font>
- ite <font id="function_arguments">(i : boolean;<br><span style="padding-left:20px"> t : bit_vector;<br><span style="padding-left:20px"> e : bit_vector) </font> <font id="function_return">return bit_vector </font>
- ite <font id="function_arguments">(i : boolean;<br><span style="padding-left:20px"> t : character;<br><span style="padding-left:20px"> e : character) </font> <font id="function_return">return character </font>
- ite <font id="function_arguments">(i : boolean;<br><span style="padding-left:20px"> t : string;<br><span style="padding-left:20px"> e : string) </font> <font id="function_return">return string </font>
- ite <font id="function_arguments">(i : boolean;<br><span style="padding-left:20px"> t : integer;<br><span style="padding-left:20px"> e : integer) </font> <font id="function_return">return integer </font>
- ite <font id="function_arguments">(i : boolean;<br><span style="padding-left:20px"> t : real;<br><span style="padding-left:20px"> e : real) </font> <font id="function_return">return real </font>
- ite <font id="function_arguments">(i : boolean;<br><span style="padding-left:20px"> t : time;<br><span style="padding-left:20px"> e : time) </font> <font id="function_return">return time </font>
- toSlv <font id="function_arguments">(ARG : integer;<br><span style="padding-left:20px"> SIZE : integer) </font> <font id="function_return">return slv </font>
**Description**
conv_std_logic_vector functions
- adcConversion <font id="function_arguments">(ain : real;<br><span style="padding-left:20px"> low : real;<br><span style="padding-left:20px"> high : real;<br><span style="padding-left:20px"> bits : positive;<br><span style="padding-left:20px"> twosComp : boolean) </font> <font id="function_return">return slv </font>
- getTimeRatio <font id="function_arguments">(T1,<br><span style="padding-left:20px"> T2 : time) </font> <font id="function_return">return natural </font>
- getTimeRatio <font id="function_arguments">(T1,<br><span style="padding-left:20px"> T2 : real) </font> <font id="function_return">return natural </font>
- assignSlv <font id="function_arguments">(i : inout integer;<br><span style="padding-left:20px"> vector : inout slv;<br><span style="padding-left:20px"> value  : in    slv) </font> <font id="function_return">return ()</font>
- assignSlv <font id="function_arguments">(i : inout integer;<br><span style="padding-left:20px"> vector : inout slv;<br><span style="padding-left:20px"> value  : in    sl) </font> <font id="function_return">return ()</font>
- assignRecord <font id="function_arguments">(i : inout integer;<br><span style="padding-left:20px"> vector : in    slv;<br><span style="padding-left:20px"> value  : inout slv) </font> <font id="function_return">return ()</font>
- assignRecord <font id="function_arguments">(i : inout integer;<br><span style="padding-left:20px"> vector : in    slv;<br><span style="padding-left:20px"> value  : inout sl) </font> <font id="function_return">return ()</font>
- resize <font id="function_arguments">(vec : slv;<br><span style="padding-left:20px"> newSize : integer;<br><span style="padding-left:20px"> pad : sl := '0') </font> <font id="function_return">return slv </font>
**Description**
Resize vector types, either by trimming or padding upper indicies
- resize <font id="function_arguments">(str : string;<br><span style="padding-left:20px"> newSize : integer;<br><span style="padding-left:20px"> pad : character := nul) </font> <font id="function_return">return string </font>
- StdMatch <font id="function_arguments">(L,<br><span style="padding-left:20px"> R: std_ulogic) </font> <font id="function_return">return boolean </font>
**Description**
Match Functions
- StdMatch <font id="function_arguments">(L,<br><span style="padding-left:20px"> R: unsigned) </font> <font id="function_return">return boolean </font>
- StdMatch <font id="function_arguments">(L,<br><span style="padding-left:20px"> R: signed) </font> <font id="function_return">return boolean </font>
- StdMatch <font id="function_arguments">(L,<br><span style="padding-left:20px"> R: slv) </font> <font id="function_return">return boolean </font>
- toTime <font id="function_arguments">(f : frequency) </font> <font id="function_return">return time </font>
- muxSlVectorArray <font id="function_arguments">(vec : SlVectorArray;<br><span style="padding-left:20px"> addr : natural;<br><span style="padding-left:20px"> allowOutOfRange : boolean := false) </font> <font id="function_return">return slv </font>
**Description**
Mux a SlVectorArray into an SLV
- toBuildInfo <font id="function_arguments">(din : slv) </font> <font id="function_return">return BuildInfoRetType </font>
- toSlv <font id="function_arguments">(      din : BuildInfoRetType) </font> <font id="function_return">return BuildInfoType </font>
