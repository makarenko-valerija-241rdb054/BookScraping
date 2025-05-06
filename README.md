# SCP skrapētājs
Šis ir mans (Valerija Makarenko, 1. grupa, 241RDB054) nobeiguma projekts studiju priekšmetā Datu struktūras un algoritmi, un, pildot šo projektu, visparējais uzdevums bija izveidot programmu, kas atvieglotu/
automatizētu kādu ikdienas darbu. Es negrāsos teikt, ka SCP projekta tīmekļa vietnes pētīšana ir mans ikdienas darbs, tomēr sanāca tā, ka tā bija vienīgā vietne, kurai man bez problēmām izdevas pielietot savas
tīmekļa skrapēšanas prasmes, tāpēc, lai arī tas ne pilnībā atbilst uzdevuma prasībām, es ceru, ka tā ir derīga projekta ideja.

## Projekta konteksts
SCP projekts ir viens no lielākājiem pasaulē "fanu daiļliteratūras" (fanfiction) projektiem, kurā piedalās tukstošiem cilvēku no visas pasaules. Oficiāla projekta vietne izskatās kā noslēpumainās organizācijas
(The SCP Foundation) - organizācijas, kuras mērķis ir notvērt un klasificēt dažādas pasaulē sastopamas anomālijas. Katrai anomālijai mājaslapā ir sava tīmekļa lapa (katru no šīm HTML lapām ir rakstījis vai pārtulkojis
aizrautīgs neprofesionāls rakstnieks), un šīs tīmekļa lapas ir sakārtotas deviņos katalogos, kas arī ir HTML lapas. Visām lapām SCP projekta mājaslapā ir diezgan vienkārša HTML struktūra, un no tā, ka viss projekts
ir parastu tīmekļa lietotāju iniciatīva, varētu izsēcināt, ka serveris, kas apkalpo šo mājaslapu, iespējams, nav ļoti izturīgs pret lielu pieprasījumu skaitu.

## Projekta apraksts
Mana projekta vai programmas mērķis bija uzrakstīt programmu, kas veic tīmekļa skrāpēšanu uz SCP projekta mājaslapas, tas ir, viena no tās anomāliju katalogiem (kataloga numuru specificē lietotājs), un izgūst
noteiktu skaitu anomāliju jeb SCP vienību, tas ir, saglaba tās kā Node klases objektus ar trīm vērtībām: code - unikāls kods, kas piemīt katrai SCP anomālijai, name - anomālijas nosaukums, danger -
bīstamības klase, kas arī piemīt katram SCP objektam. code un name var nolasīt jau no kataloga HTML lapas, bet, lai izgūtu bīstamības klasi, ir nepieciešams atvērt vēl vienu lapu - anomālijas lapu - un nolasīt
danger to turienes. Node klases objekti tiks sakārtoti Linked List klases objektā (abas klases ir definētas manuāli). Pēc Linked List saglabāšanas, ar to būs iespējams veikt vairākas darbības: izvadīt konkrētu
anomāliju pēc indeksa, izvadīt visas saglabātas anomālijas un izveidot Excel failu, kas glabās anomālijas ar lietotāja specificēto bīstamības klasi. Šīs komandas varēs pildīt uzprogrametajā elementārajā komandu 
terminalī.

## Apkopojums par projektu
Izmantotas bibliotēkas: requests, bs4, re, openpyxl, time
Manuāli definēta datu struktūra: Linked List

## Projekta nepilnības
Tika uzstādīts diezgan ilgs laika buferis (2s) starp katra objekta skrāpēšanu, lai neizjauktu, iespējams, vāju serveri, tāpēc izgūt visus 999 objektus, kas mēdz būt vienā katalogā, nebūtu praktikāli. Metods, kādā
notiek pārslēgšanās starp tīmekļa lapām, ir diezgan arhaisks, jo projekta autora datora nav pietiekami daudz atmiņas, lai instalētu Visual Studio, un projekts bija jārealizē GitHub Codespaces.
