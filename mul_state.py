import re

def calculate_enabled_multiplications(text):
    enabled = True
    total = 0
    position = 0
    
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    do_pattern = r'do\(\)'
    dont_pattern = r'don\'t\(\)'
    
    mul_matches = [(m.group(1), m.group(2), m.start()) for m in re.finditer(mul_pattern, text)]
    do_matches = [m.start() for m in re.finditer(do_pattern, text)]
    dont_matches = [m.start() for m in re.finditer(dont_pattern, text)]
    
    state_changes = [(pos, True) for pos in do_matches] + [(pos, False) for pos in dont_matches]
    state_changes.sort()
    
    current_state_index = 0
    
    for num1, num2, mul_pos in mul_matches:
        while current_state_index < len(state_changes) and state_changes[current_state_index][0] < mul_pos:
            enabled = state_changes[current_state_index][1]
            current_state_index += 1
        
        if enabled:
            total += int(num1) * int(num2)
    
    return total

input_data = """what(){mul(697,542)/>why(479,94)mul(995,893)why()]%?:]select()%}mul(408,907),{from()$&&/mul(893,282)[#%@(who()what()!~mul(313,566)@@how()$mul(964,183)]how()where():?what()>%mul(743,40)*']~+/!mul(241,491)<{]<)]from()how()'from()don't()&where()%how(216,229)how()where()!mul(35,991)when()why(610,462)> select(594,57)$}&^mul(699,136)}]?who()when(){mul(970,603) ?mul(200,732)/[:select()(mul(967,199)+select(),/!how()when()mul(521,824)#;]:+&->)}mul(473,278):$&mul(347,457)}&*why()~ when()mul(324,773)-$ mul(460,152)#-;~,when()@mul(331,186)%don't()]-mul(197,390)how()mul(774,494)/from()))how()),mul(758,549) >why()mul(485,656)where()~-mul(938,190)&mul(326,51) mul(304,567)mul(165,576)+'-]when()'+why()/mul(906,352)from(618,898)where() how()#~mul(508,347)what()when()/&^why()why()</mul(793,679)why()-}who()from(){*where(),$don't()*#+{<mul(38,430){^}why()~%from(318,733):~<mul(611,673):-#/%why()~#how()mul(339,558)<why()*:&when()[/mul(716,978)?from()@&^/&'>mul(847,535)~ #)from()what()$)/do()//)where()what();where(200,117)how();+mul(242,61)?:-?mul(371,193)%%mul(173,850)*from()why()# ,#)mul(566,907)&don't()/how()&mul(412,399)}^why()from()mul(905,46)^from(169,718)!(when()mul(920,500)*don't()who()how()what()}why()-]who()who()(mul(927,865)@select()mul(371,913)mul(254,979)-select()mul(614,684)$;,{mul(841,422)!when()^mul(292,172)/]what(),&]mul(668,298)what() mul(788,698))&mul(241,230),*mul(513,152)}*:[/mul(762,255)*/mul(199,330)how()')^mul(716,272)}#-select(196,254)-&how()*mul(181,411)@){]#%:,mul(830,669):-[>!select()who()mul(490,309):mul(597,806)who()mul(911,931)when()]<mul(877,212)+(;?~;mul(242,138)from()?(select()how()$mul(624,989)[mul(232,970)select(480,963)select()'&(>:mul(749,304)select()$who()*&$:!}mul(499,106)why()select())when(453,833)~%^don't()who()<]]>}{(mul(666,746)@&where(){do()from());why()where()#mul(436,226); what()^from()~when()*mul(333,877)&[mul(849,387)mul(846,509)$mul(690,845)where()what()-~where())mul(120,516+'[;where()- mul(671,693)]who()#/mul(151,226)'what()mul(662,390)when():don't()how()mul(586,859){who()+}*?select()*}[mul(162,392)##who()!don't()^from();select(183,354)+@#+how()mul(235,965);<['*@*&mul(836,254)#who()^,{~*&from(912,964)mul(81,63)('who()+]who()who(616,562)&[don't()-%select()>why()&:*mul(148,501)<'?don't()/'%$when()+#mul(565,716)how(551,943)~>':)mul(812,235)(who()@what()do()mul(933,530)mul(516+when(95,848):what()/~mul(685,485)why(){[<^,from()-why():mul(372,990)^mul(780,194)~(when()-$> mul(158,500)where(213,721)where()-+mul(783,720)]select()mul(830,674)-*,;^)mul(542,769)<>;@;mul(340,494)~,mul(972,343)-*{<}*why()'&@mul(995,93)}/}^&mul(632,3)~mul(151,607)'~who()~+ why()select(970,692)mul(253,471)what()}select(450,660){mul(186,635)!'from():>;@+mul(109,407)mul(231,530)who()'mul(721,360)(#{what()?mul(764,403) mul(974>mul(700,804)>:>select(108,396)-where()where()~#from()mul(618,688),<?*who()@[&(mul(862,757)?^mul(448,304)who()who())'(~when(887,857)what()+mul(761,362)@mul(937,417)when(949,74)who();why(669,288),where()%select()mul(31,324)'who()mul(910,432<<@when(148,213)^+from()who()>?*mul(786,325)'<select(){mul(216,115)mul(553,306)/what(944,865)%*?where(669,409){don't():who()/)mul(247,444)*->]who()-([mul(312select()do()from()@%mul(647,88)+!mul(920,442)where(){$mul(876,103)select()select()&<-~';#mul(658,434)
what(203,778)-)]mul(25,629)why()^$~)?why()mul(207,846)(from(560,549)select()&-]?>what()mul(782,867}(^}^mul(48,779)<$where()how(396,689)mul(623,278)}select(34,689)when(),how()%({;$mul(494,74)*from()when()mul(35,522):> &&when()mul(328?}mul(186,822)]when()how())why()mul(775,741){->%mul(812'{~;mul(202,822)-mul(282,383)what()from(340,89){mul(729,896),^-what(313,84)mul(172,196#mul(447,361)why()&*?<!mul:how()#{*->/who()(+mul(395,872)#^^{@,-mul(394,873from()%mul(988,272)(%select()!~mul(101,388)what(),how()how()$#how()*mul(551,577)%what()mul(191,793)''don't()mul(744,26)!select(){'>,mul(140,452)mul(887,632)#>}{;@^+-mul(835,39) how()+/-}*},@mul(66,401)what();why()]] %+&do(),when();:who()[select():mul(474,260)who(),{,)}why()%who()mul(126,874)}where(746,668)>mul(60,400)~#select()select()@:mul-@*%when(134,304)?how()mul(18,684)what())'&/ ,{^mul(770,406){{@*  {who()who()-mul(312,245)/>{when()why()from()^&mul(936,201)&from()-#$(mul(970,306){%from(193,334)mul(770,300)how()don't()mul(17,145)(%mul(204,15)]#!mul(592,786)+?what()*^mul(903,387);}($mul(977,422)where(136,281)mul(412,540)select()@&,mul(331,930)where()!;%why())!mul(647,169):!mul(624,260)>,^^!where()#+mul(364,706) why()[when()(?from(361,489)~?/mul(572,99){mul(162,620)select()#?'$)mul(963,810)(<'^mul(381,182)mul(154,418)(mul(307,576){;select()mul(872,424)[,{&){&/mul(542,342)&*(when()+#<mul(71,788)!!what())'mul(208,451)?mul(876,225)<(what()'mul(97,553)who();$ &&#%why()]mul(932,42)# >/>mul(29,665)$don't()?where()mul(903,998)%?select()])#;mul(660,171)who() why()>what(), <mul(34]}%where(36,389)mul(769,195)]how()'#mul(780,304)-?!' what()how()mul(86,199)-{>mul(956,616);,$,}mul(982,695)-:where()why()mul(585,888)why()where()]!&{mul(422,906)select()where(721,370)<mul(397,873)why()where():mul(354,754);)mul(815,211)mul(343,66)<who(501,465)#how()who() (mul(672,904)]%where(579,405)why()how()({what()#;mul(855,294(#}mul(681,259))mul(832,942)where()who()+&+mul(484,780)(%when()where()mul(343,393)-' select()mul(356,496)who()%;why()!where()when())why()mul(925,579)]#when()why()^why()@/how(286,462)mul(702,403)-,%;?&^mul(673,873)(mul(147,896){}<<what(),do()when():&{$;!}why()~mul(70,323)}why(178,679)what())#'^,^]mul(153,346)mul(738,463)select()from()[#?:-;$<mul(993,379)mul(305,729)?>mul(673,348)from() mulwhen()~don't()',@&+]]where()$ mul(813,553)+'who()-where()select(){{,:mul(535,550)how();&;what(992,219)mul(564,279 mul(551,875)?how(920,226)(+;+?;^mul(383,579)?##%{ [*mul(576,484)>:}<,+when()do()>who()&#how())]what()mul(272,737)-/,who():;#+~]mul(580,211) :from()[&/what()}mul(893,368){*&+mul(393,508)}-!^when(962,123)]@/mul(184,205)when()]]when()'who()mul(249,915)when()from()-@/ how()~mul(495,101))<(}+%,:?,mul(356,636when()(why()^]]mul(662,103)#mul(118,597)mul(968,629):why()@]mul(676,360)select(),'select()-<mul(678,598)mul(341,306)what()@^who()%why(){/$mul(527,202)$-mul(666,372)[]'+,[what()from())mul(732,488)*)mul(817,225who(){^select()from()select(),mul(913,885):]#@(;when()select()&when()mul(337,865)select()what()-mul(798,769)(([mul(132,976);*where()when()from()*(,mul(90,998) )  )from())what()?do()why()!what()<who()mul(720,893)[$from()from()%($who()mul(361,619)%mul(773,817)~/,/*mul(262,292)^$mul(543,488:select()from()~$mul(9,28)>,mul(579,23)@why()@$:what()mul(370,656)
from()'/,what()/<,%how()mul(748,154)>[select();,who()>select():'mul(663,830)%@(mul(417,364)-why()'mul(947,551);!/)!++mul(385,221),>%#mul(410,27)}from(669,909)&who()~:'<)how()mul(203,50)why():$who()from()^{^(mul(425,96)why())from()#*&[}mul(657,805)why(){$&mul(764,125)what()select()mul(118:%;do()where()@why()@{'mul(3,361),/mul(9,725)who()from()'from()}>@*!mul(258,517)@! !}[mul(734,173),>~mul(567,929)>^$%}?mul(458,106),-mul(904,99)#where():!mul(304,344)('] )mul(474,433){]why(552,617)[*>*[?mul(292,452)@/when():mul(671,8)what();mul/*&mul(157,964)):+$^:select()mul(577:@(mul(481,28)mul(120,742):+&@mul(932,682)don't()#~,]{mul(584,430)don't()!who()]]/$when():mul(447,144);)~#mul{select(899,436)}:when()mul(18,3)$'why()/ <mul(803,2) '$when()(-mul(498,989)when()>select()*(~from(848,249) mul(402,212#(when()what(526,893)(when()who()!select(855,813)mul(267,568)?when()~?mul(790,400)how();:%mul(565,976)*}how()what()>+from()from()#don't()><mul(117,353)+<>what(465,504)+,+/@^mul(702,607)/%mul(775,709)from()what()$(where()^what()why()when()}mul(728,176)&$~mul(732,727)^'&mul(999,652)']~mul(780,700)-~&{-{<*select()when()mul(729,462) mul(105,648)@;,?^#!how(963,469))mul(906,654)&]who()from()&mul(881,852)how(),how()where()where()@(<(from()mul(822,522)mul(874,978)mul(233,399)select()from()>/;where()when()^[why()mul(474,473)where(896,324)^mul(638,197)}how())-{>how()why()}>mul(611,521)mul(364,693)why(),-&where()+># how()mul(53,996)/<[where(204,56)<-;}~(mul(547,235)+where()~%why()'select()mul(407?%%]/how()~>^mul(749,65)mul(171,190 why()%+?when()when()&how()]<mul(696,733)mul(101,606)from()where() mul(606,572)/>!@<+%don't():-@{who()#mul(104,125)when()>{<-%mul(627,539)when()]how()-select()]mul(983,406)+where()]-when()when()mul(537,478)from()#~)how()mul(305,547)/&?)%+who(){do()^who()why()+*select()@#^mul*+!mul(324,352)*{why()select()when()where()how()++@mul(758,823)>from()(how()mul(155,143)how()$[] +-mul(220,494)<#<mul(24,76)(>how():&@what()mul(996,77)],<}^where()%mul(153,549)/$&}[[#):!mul(974,546)!where()mul(406,100)mul(684,435)<when()/)!what()/&;>mul(36,14)*,$@~,don't()<{@*&mul(302,244)mul(934,996)}-when(),;where()->mul(184,150)<~/!){mul(457,435)/select()mul(692,366)mul(294,439)(*where()who()why(124,291)$how():don't())mul(238,489)[;(^&/}select()>@mul(199,347)<why()-mul(101when()%'mul(676,397)who()what(){#mul(850,573)mul(534,475)-'&;mul(558,350)mul(545,931)who(688,232);where()'%mul(870,756)+^-+mul(365,269,select()(mul(458,213)(]-, mul(72,716)>(<(#mul(135,803),what()where() !):!mul(119,226)-)],who()mul(443,526))how();where()mul(652,762)from()$)'$^[!mul(915,54)%'what()where()who()mul(685,223)^how()$]/'mul(660,757))mul(401,390)!) ;what()what()@{:mulselect()#( ?where()[+when()mul(677,473)~@:select()]*mul(368,274)#%{where()mul(387,806)!@why()select()''+mul(673,924)}?<where()>%mul(544,205)%? when()+mul(990,513)@'&:(]mul(115,860)?-<*>how()mul(452,49)>mul(672,248)why()~where()^+[mul(15,506)>}don't()}~,~when()<what()mul(284,616)how()/what()select()}(select()>mul(732,173)mul(26,691):where() where()who();when()}mul(483,470)+/ select()mul(693,863^/&mul(999,441)what()&select()?, ?<mul(463,840)mul(429,885:{]mul(317,971)from() : mul(797,491)why()),why()>*why()when() *mul(114,59*[>{-{#!/usr/bin/perlwhy()mul(247,67)?what()when()%what()@'{+mul(453,52)
where()mul(231,244)>>/where()mul(216,829)who(){%mul(552,537)when()]$mul(185,377);}>where()::why()mul(300,903)]#!mul(61,613)/mul(106,584)^,'?; &'select()~mul(145,411))?what()+&how():&mul(139,18)/where()< ,from()+&don't()#% ,*mul(158,236)^,(what()!?mul(861,544)]:who()how()-*how(),mul(103,378)+):what(712,256)-+$:from()(mul(172,254);?;how(){{}@mul(812,458)how()(,:)))~mul(256,397)#]from() >?where()[~mul(132,458)/<[mul(441,730),&+mul(410,879)@@select()@$from(424,812)-mul(80,361);(select()$!:?mul(3,489)(mul(692,445)-?:[;/@mul(630,252)-<:~how()%:mul(755,275);}<who(97,679)]mul(528,294)^/when()where(){!+select()why()mul(540,523)/+>why()*]who()$'what()mul(404,857))}when()}:mul(795,571)}?'<how()~mul(158,220)mul(763,816);#&+select()do()(mul(872,912)from()mul(459,72)mul(185,530)@@#mul(114,891)[mul(746,254)]who()@}  where()select()? mul(232,873)'@mul(365,668))where()'mul(511,416) ^+}[]select()!mul(914,595){>?what()&>who(709,757),[mul(85,479)[^ /mul(12,677)mulwho()<mul(280,994)where()]};-mul(881,791;'%#]select()mul(882,540)/[how()^mul(830,639){@;[~mul(278,495'?^(}mul(45,101)mul(242,987)@mul(534,500)what()$]{:,!%-'mul(130,566)@@%~mul(305,194)from()!;,]<)$mul(386,814)%)when()^^[select()};mul(248,686)what()(}what(){^do()]-'mul(738,398)when()-]%mul(263,840)(when()*~)^)mul(814,32),,<^&>;@]why()mul(507,433)how()%;{mul(703,269)@'from()&}mul(195,324%where()mul(333,588)who(210,905)@{how()-why()don't()',~^who()mul(976,376) ;mul(617,616)+don't()~how()^/},#&how()~mul(464,668)>(%$from()>what()mul(330,462)don't(),$]~mul(47,160)select()'-<}^what()mul(813,866)@mul(932,649)from()how()when(){]^^$where()mul(298,181)  ^ '!*:mul(395,824);>>@->!%mul(169,544)when()what(165,141)]$',>?$mul(677,950)+<#[select(680,459)mul(104,437)how(){mul(238,478))+#:(~where()~mul(990,466)<~#mul(67,165)where(103,910)@(when()^*~,when()'mul(820,708)]}&when()?%#/mul(489,883)[{ {<select()mul(369,476)$<&&mul(171,711)?!!@)mul(118,212)>^where()mul(278,843[mul(865,505)+'why())mul(545,55)(:{+<mul(279,179)'#mul(396,191)}when())#[%mul(117,91)]~,~-mul(581,752)[$<-'mul(765,81)why()$}from()/{'mul(37,389){# #mul(249{[when(785,173)mul(249,933)<how()?mul(110,134) mul(799,655),mul(295,401)mul(703,330)@&}):^ %mul(457,121)((mul'select()-{]&%/mul(236,202)$[)select()!}>mul(248,445)?mul(391,995>#-,*%^ mul(354,732)!/mul(619who()^*[,~[~>$why()mul(723,806)who()from()[why()?$>&mul(721,363)>what()how()]^+mul(301,140)^~:~who()mul(469,571)~mulwhy()from()+'<'don't()&<where()~;,><~mul(219,408))^mul(215,767)-]mul(519,445)mul(907,35)what()-!^why()what()-how()select()mul(742,645)mul(213,651)&+when()mul(942,859)^*from()mul(871,479)<^mul(88,805)mul(397,727-([*select()what()what()select()$/+mul(24,343),@from()mul(594,62)+<mul(61,432)@!(~how(),:] mul(353,968)?how()$&+mul(591,184)#{);[who(982,47)%mul(95,398) +>['from()<mul(198,998)?;,*]]>#mul(807,849)~%+*}mul(552,461)]from()@!@#select()who()^~don't()?;]mul(201,836)&+&>mul(741,810)
mul(695,640)[mul(908,779)+/mul(78,761)[+?};*{mul(105,818) [from()-mul(451,768)what()]!what()from()what()when()~^mul(619,244)[from();,&from()where()from()^?mul(899,374)when()#^:/mul(541,467)/mul(692,925)why()how()what()>/:<mul(532,861)[?select()%mul>^mul(463,858)<why()#)?<^from()-mul<do()'<from()%<what()$&mul(510select()how()select(370,782)when()what()-[:mul(150,223)where()!mul(999,372)<;}*mul(43,815)when(642,18)^({who()&}*mul(200,902select()^[( ^who()mul(547,387)what(632,584)<mul(464,280)!+~mul(337,538)from(858,497)from()mul(116,978)@select(),mul(174,116)~(,;]when()mul(177,316)mul(313,712)!who()^:,mul(288,39))(+[;%%do()$)@-:<(mul(404,923))),do()!)/-$'@mul(662,630)?(what()why()when()mul(825,112)~*!,mul(631,707)/why()<^@,do()^-what();:}why()from()*when()mul(637,832)<?where()why()^how()+'mul(583,659)%} mul(251,47)<?mul(271,563)*{mul#+<'mul(690,953):[)>how()where()^:[~mul(31,347)?<})*>!/mul(627,404)do(),?^$when() mul(24,930)mul(873,35)select()what()where()/don't()&& [mul(248,460)&where()from(45,338)*?mul(16,424)'}mul(9,674)<}select()$@mul(985[mul(441,498)]<who() ]mul(725,72)>what()@'/{mul(626,540)[;/%,mul(764,748)mul(867,602)why()who()what()mul(885,438)who() ]-{'~/>mul(668,937)&(mul(973,416)when()<why()mul(581,734why()<do()'[#(/;;select()how()}mul(333,76) }(who()]?what()mul(790,234){mul(761,575)who() ;!#@]where()mul(404,574);mul(307,239)mul(37;!/from()%who()mul(578,186)mul(399,705)%$select(237,775)from() what()&)where()mul(834,844))where()-<where() >mul(647,557)~<select()^:[],from()where(864,206)mul(550,551)'mul(763,930)what()^{-how():mul(579,304))how()!*@mul(126,394)mul(123,990)[mul(363,828)& @'when()mul(66,810)mul(238,58)?mul(615,798)who()@*~&~]mul(450,877)}/*do()>how() {+?@mul(485,856)how()select()when()/select()mul(33,198){!mul(382,685))why()!*mul(711,362)<*what()mul(645,252)from(479,19)where()who()mul(561,165)?>$*?:mul:#mul(877,920)#:-mul(440,17)how()>![,@+]mul(151,701)}^[$*mul(353,641){^$+>~%{;}mul(39,274)*mul(657,123)how()*where(){mul(346,442)mul(790,227)?when()>when()(!%mul(60,33)&/$where()}$-<:{mul(930,295)%from()how()@$from();who();mul(494,10 #mul(700,474){^mul(552,224)~'how()select()%}mul(5,285)mul(833,131?%>/from()mul(457,368)^'>%>mul(233,98)[' <^mul(312,497)mul(933,575)who(){mul(859,323)-mul(484,721){where(445,310)),>}!;,?mul +)*:%?mul(122,560)what()select():+mul(749,209)mul(478,283)&#mul(67,742)@^mul(494,481)&%from()':!/&:why()mul(768,612)where(),:]$mul(512,595)mul(658,426)what()+>)where()%&mul(213,517)+<where()!)mul(665,992)$where()>+what())what():who()mul(891,196)@when()why()mul(46,798)@)select()[how()mul+from()select()mul(128,259)when()/select()when()-*):}mul(115,723)select()@where() mul(235,95)mul(507,424)why()] !mul(680,738)/<mul(634,100)mul(569,333)where()%]why()];[$mul(185,17)^}%><&$)>mul(349%]how()mul(719,909)when()%*mul(27,357)mul(734,373)/{>%;[$!mul(733<what()]<mul(233,784)mul(252,863) mul(741,457)when()>)why()&mul(938,12)
from()#,why()~& ;#:mul(731,521)*how()} do()mul(399,167)from()mul(71,499)how()from()%!who():;mul(730,287)why()mul(422,401)select();@+[-mul(742,851)< ^$why()mul(153,315)+%mul(206,613): ,from()[~select()mul(971,155)[%*:&{mul(239,834)'#:{'~$;mul(224; mul(163,711)$$/!select()^%do()&where()>@*from()select(719,23)#:<mul(859,6){where()why()mul(611,142)[>,how()>from()mul(874,522)'what()!from()*select()mul(950,277),<@-!*mul(35,822)>)~*mul(934,771) #mul(752,754)how()-from()+who());]:<mul(110,865)from()why()@)*where()when()mul(804,930)-mul(948,779),# when(907,369)mul(650,833)<&-(!^^+mul(986,368)}~'{!mul(549,524)[->where()/select(297,243)!%+mul(603,67)#]}what()mul(486,614)mul(761,335)! %:[;from()^when()mul(162,639)(({;%) mul(410,831)mul(74,9) [),}!!+?&mul(365,386)?do()&from()who(486,875)why()mul(545,922)*mul(333,104)where()do()~$^who(),[;mul(357,374)$}what()/from()^when()}/mul(828,346)mul(128,556))*{:from()@mul(277,303)#[^-%]how() /mul(817,849):mul(477,520)&$what()}<{]#]^mul(263,446):%when()-&how()from()[&>mul(307,210)<mul(779,78)*how()select(447,622)mul(624,455)++&&what()@*#mul(898,875),];/when()mul(463,295)who()select()why()&who()why(795,44)>]!+mul(293,549){when()~mul(478,825)&what()')%mul(233,939)%]>;>}]mul(680,156);}~mul(66,418)when()/]'? select()mul(506,752) ?select()select()%,}mul(685,266)(from()mul(354,792)~+;when()~#where(){mul(745,146)mul(926,660)%mul(721,86)~?&#?mul(964,815){when()-why()mul(333,175)mul(490,526)when()^mul(370,894)>&who()'^mul(686,63)~[?!%'select(){mul(543,91)@#mul(43,96)where()mul(278,584)~%)where()%mul(163,853)&#when()'mul(561,872)#when()where()'~don't()mul(896,297)<'>@mul(919,548) who()how()?@+when()]%(mul(691,41)$;+]&who()-**mul(272,776)}what()#why() what()who() when();mul(824,393)-@ %[^,why()do()/mul(891,874)$'<<?select()mul(843,864):%/!what()who()/{%mul(262,169)&:[mul(189,651)how()[from():,{?mul(453,774)(+how()]~-{:(&do()mul(600,585)/#don't()%*']]%-:)mul(538,508)where(508,481)how()where()*what(767,256)/mul(254,549),}@^?'/:^mul(664,632)$ ;:when()where()what(655,337)%;~mul(343,605)where()don't()from()%{what()mul(967,749)mul(982,465)!who(),mul(320,945)mul(769,926)/-)<]who() mul(26,66){who()]{}!mul(122,617):$[??when(),-why()select()mul(125,904)select()::[*mul(420,593)?&&*select()}where()@mul(810,984)'mul(789,703);$mul(228,679)?>!&@** )mul(437,39):]'mul(255,961)!what()!mul(22,237)~mul(287,360)select()how()what()}^mul(153,348){when()&)}{/{mul(8,764)how()@}mul(231,703)why()>%~!when() ^mul(418,457)select()how():?who()$when()when()mul(957,951){'where()'mul(6,320)~mul(168,639)^!mul(715,855)~select()^mul(44,209)&mul(767,449)mul(503,357)<mul(821,550)+<;from():%how()mul(76,386)}<how()@/when()mul(753,291)]how()&)from()?&what()&why()mul(956,734)mul(206,478)!how()how()>^where(),]select();mul(571,436)]-select()select()&"""
result = calculate_enabled_multiplications(input_data)
print(f"Sum of enabled multiplications: {result}")