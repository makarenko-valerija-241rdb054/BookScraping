# SCP skrapētājs
Šis ir RTU DITEF IT studentes Valerijas Makarenko noslēguma projekta darbs stūdiju priekšmetā "Datu struktūras un algoritmi". Šī darba galvenais uzdevums ir mājaslapas pārlukošanas automatizācija, konkrētāk, noteikto tās elementu atrašana un manipulācijas ar tām. "Skrāpējāma" mājaslapa, "SCP Foundation Wiki", ir īpatnēja jauno cilvēku interneta kultūras daļa, un es ceru uz jūsu vienaldzību pret dažiem tās savādākiem aspektiem un fokusu uz tiem aspektiem, kas ir aktuāli šim darbam - tas ir, tās HTML elementi un struktūra.

## Projekta konteksts
SCP projekts ir viens no lielākājiem pasaulē "fanu daiļliteratūras" (fanfiction) projektiem, kurā piedalās tukstošiem cilvēku no visas pasaules. Oficiāla projekta vietne izskatās pēc noslēpumainās organizācijas
(The SCP Foundation) mājaslapas - organizācijas, kuras mērķis ir notvērt un klasificēt dažādas pasaulē sastopamas "anomālijas". Katrai "anomālijai" mājaslapā ir sava tīmekļa lapa (lai arī tekstam katrā no tām ir noteiktais formāts, tās visas ir taisījuši parasti lietotāji, tāpat kā parastajā Vikipēdijā), un šīs tīmekļa lapas ir sakārtotas deviņos katalogos, kas arī ir HTML lapas.
It visus nozīmīgus datus par "anomālijām" (klasifikācijas kodu, raksturojošo vārdu) var nolasīt no kataloga lapām, bet vienu no harakteristikām (bīstamības klase)
iespējams nolasīt tikai no pašai "anomālijai" vēltītās HTML lapas, kas prasa papildu tīmekļa pārlūkošanu.
Visām lapām SCP projekta mājaslapā ir diezgan vienkārša HTML struktūra, un no tā, ka viss projekts
ir parastu tīmekļa lietotāju iniciatīva, var izsēcināt, ka serveris, kas apkalpo šo mājaslapu, iespējams, nav ļoti izturīgs pret lielu pieprasījumu skaitu.

## Projekta apraksts
Mana projekta vai programmas mērķis bija uzrakstīt programmu, kas veic tīmekļa skrāpēšanu uz SCP projekta mājaslapas, tas ir, viena no tās anomāliju katalogiem (kataloga numuru specificē lietotājs), un izgūst
noteiktu skaitu "anomāliju, tas ir, saglaba tās kā Node klases objektus ar trīm vērtībām: code - klasifikācijas kods, name - raksturojošais vārds, danger -
bīstamības klase. Node klases objekti tiks sakārtoti Linked List klases objektā (abas klases ir definētas manuāli). Pēc Linked List saglabāšanas, ar to būs iespējams veikt vairākas darbības: izvadīt konkrētu
"anomāliju" pēc indeksa (print n), izvadīt visas saglabātas "anomālijas" (print all) un izveidot Excel failu, kas glabās anomālijas ar lietotāja specificēto bīstamības klasi (excel euclid/keter/thaumiel). Šīs komandas varēs pildīt manis realizētajā elementārajā komandu terminalī.

## Apkopojums par projektu
Izmantotas bibliotēkas: requests, bs4, re, openpyxl, time
Manuāli definēta datu struktūra: Linked List

## Kas ir .devcontainer?
devcontainer ir artifakts no šī projekta izstrādes procesa. Sākotnēji mana vēlme bija šo uzdevumu veikt ar Selenium bibliotēku, nevis arhaiski ar requests un regex, bet es sastapos ar to, ka Selenium nepilnīgi strādā GitHub Codespaces vidē. Pilnīgi godīgi, es vērsos pie mākslīgā intelekta, lai rastu atbildi uz to, kā palaist Selenium GitHub-ā, un .devcontainer fails bija viņa piedāvātais risinājums. Beigu beigās arī ar šo failu Selenium nestrādāja, bet es realizēju savu tagādējo projektu, šim failam esot repozitorijā, un man ir bažas par to, kas notiks, ja es viņu nodzēsīšu. Zvēru, ka Selenium un vairāki teorētiskie jautājumi par bibliotēkām ir vienīgais, ar ko man palīdzēja MI - par to var pārliecināties, izvērtējot mana koda kvalitāti, kas dažādos momentos ir šausmīga.

## Projekta nepilnības
Tika uzstādīts diezgan ilgs laika buferis (2s) starp katra objekta skrāpēšanu, lai neizjauktu, iespējams, vāju serveri, tāpēc izgūt visus 999 objektus, kas mēdz būt vienā katalogā, nebūtu praktikāli. Metods, kādā
notiek pārslēgšanās starp tīmekļa lapām, ir diezgan arhaisks, jo projekta autora datora nav pietiekami daudz atmiņas, lai instalētu Visual Studio, un projekts bija jārealizē GitHub Codespaces.
