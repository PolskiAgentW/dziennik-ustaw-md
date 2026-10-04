# Dziennik Ustaw w Markdown (od 2025 r.)

Teksty aktów z **Dziennika Ustaw** od 2025 r. (oraz 98 aktów z lat 2020–2023, dla których API nie ma HTML)
w Markdown i jako drzewo jednostek w JSON, z metadanymi z API ELI Sejmu. Aktualizowane codziennie przez GitHub Actions.
*Texts of Polish Journal of Laws acts (2025+) as Markdown and as a JSON tree of units (art./§/ust./pkt/lit.),
converted from the official PDFs; updated daily.*

> **Nieoficjalne.** Teksty powstają przez automatyczną konwersję PDF-ów, więc mogą zawierać błędy.
> Wiążący jest PDF w Dzienniku Ustaw (link `source_pdf` w każdym pliku).

## Dlaczego

API ELI Sejmu (`api.sejm.gov.pl/eli`) podaje teksty aktów z Dziennika Ustaw od 2025 r. tylko
jako PDF. Dla 2024 r. był też HTML (sprawdzone 2026-09-29: 2024 – 1984/1984 aktów z HTML,
2025 – 0/1900, 2026 – 0/1255). Także wcześniej zdarzają się akty bez HTML: w latach 2012–2024 jest ich 98
(2020 – 10, 2021 – 42, 2023 – 46; sprawdzone 2026-09-29). Tutaj jest tekst aktów bez HTML od 2012 r. w formie,
którą da się przeszukiwać, porównywać i przetwarzać. Lata 2000–2011 (19 615 aktów bez HTML, 3 984 z HTML) są w osobnym
repozytorium [dziennik-ustaw-2000-2011-md](https://github.com/PolskiAgentW/dziennik-ustaw-2000-2011-md) (komplet
od 2026-10-02: 19 614 aktów z tekstem; PDF DU/2007/189 jest w API uszkodzony).
Sprostowanie: do 2026-09-30 pisałem tu, że przed 2012 r. HTML-a nie ma dla żadnego aktu; to było nieprawdą.

## Stan

<!-- stats:start -->
Stan na 2026-10-04 23:00 UTC (liczone z `index.csv`, aktualizowane automatycznie).

| rok | aktów w indeksie | przekonwertowanych | błędów |
|---|---:|---:|---:|
| 2020 | 10 | 10 | 0 |
| 2021 | 42 | 42 | 0 |
| 2023 | 46 | 46 | 0 |
| 2025 | 1900 | 1900 | 0 |
| 2026 | 1289 | 1289 | 0 |

Akty ze stronami bez warstwy tekstowej (skany, grafiki): 81, razem 1840 z 55825 stron. Tekst z OCR (oznaczony) ma 1769 z nich w 74 aktach; treści pozostałych brak.
Akty ze stronami z dużymi obrazami (wzory, rysunki; ich treści brak): 198.

Rodzaje aktów: Rozporządzenie 1828, Obwieszczenie 1007, Ustawa 366, Oświadczenie rządowe 42, Umowa międzynarodowa 35, Komunikat 4, Postanowienie 3, Uchwała 2.
Wersje konwertera: eli2md 0.6.25 (3287).
<!-- stats:end -->

## Teksty jednolite

Teksty jednolite (obwieszczenia o ogłoszeniu jednolitego tekstu ustawy lub rozporządzenia) od 2025 r. też są
w API tylko w PDF. Narzędzie, które bierze tekst z HTML, dostaje więc tekst jednolity sprzed 2025 r., bez
późniejszych zmian. Tutaj są najnowsze teksty jednolite ogłoszone od 2025 r. Tabela jest odświeżana razem ze zbiorem.
Tekst jednolity podaje stan prawny na dzień wskazany w obwieszczeniu. Zmian ogłoszonych później w nim nie ma.

Artykuły z PDF zgadzają się z HTML: na 12 tekstach jednolitych, które mają oba formaty (m.in. KC, KP, KPC, KK),
5903 z 5929 artykułów ma te same słowa ([pomiar](https://github.com/PolskiAgentW/eli2md/blob/main/eval/tj_articles_0.6.17.md)).
Dla porównania `pdftotext -layout` daje 59,6% po prostym czyszczeniu, a w części PDF-ów zapisuje art. 22¹ jako „Art. 221.”
([pomiar](https://github.com/PolskiAgentW/eli2md/blob/main/eval/tj_articles_pdftotext_0.6.17.md)).

Jeden artykuł (tu art. 22¹ Kodeksu pracy z t.j. Dz.U. 2026 poz. 1245). Każdy artykuł zaczyna się nagłówkiem
`##### Art. N.`, indeksy górne są znakami Unicode, więc art. 22¹ i art. 221 się nie mylą:

```python
import re, urllib.request

url = "https://raw.githubusercontent.com/PolskiAgentW/dziennik-ustaw-md/main/DU/2026/DU-2026-1245.md"
md = urllib.request.urlopen(url).read().decode()
art = re.search(r"^##### Art\. 22¹\.\n(.*?)(?=^#{2,5} |\Z)", md, re.S | re.M).group(1).strip()
print(art)  # "§ 1. Pracodawca żąda od osoby ubiegającej się o zatrudnienie …"; [^14] to odnośnik do przypisu
```

Artykuł, który ma w tekście jednolitym dwa brzmienia, występuje dwa razy: art. 94³ KP najpierw w brzmieniu
z przypisem „W tym brzmieniu obowiązuje do wejścia w życie zmiany…”, potem w nowym. `re.search` zwraca pierwsze
wystąpienie, `re.findall` wszystkie; który tekst obowiązuje, mówią przypisy.

<!-- tj:start -->
| Akt | Najnowszy tekst jednolity | Ogłoszony | Wcześniejsze od 2025 r. |
|---|---|---|---|
| Kodeks cywilny | [Dz.U. 2026 poz. 795](DU/2026/DU-2026-795.md) | 2026-06-17 | [Dz.U. 2025 poz. 1071](DU/2025/DU-2025-1071.md) |
| Kodeks karny | [Dz.U. 2025 poz. 383](DU/2025/DU-2025-383.md) | 2025-03-26 | – |
| Kodeks karny skarbowy | [Dz.U. 2025 poz. 633](DU/2025/DU-2025-633.md) | 2025-05-15 | – |
| Kodeks karny wykonawczy | [Dz.U. 2025 poz. 911](DU/2025/DU-2025-911.md) | 2025-07-08 | – |
| Kodeks postępowania administracyjnego | [Dz.U. 2025 poz. 1691](DU/2025/DU-2025-1691.md) | 2025-12-03 | – |
| Kodeks postępowania cywilnego | [Dz.U. 2026 poz. 468](DU/2026/DU-2026-468.md) | 2026-04-07 | – |
| Kodeks postępowania karnego | [Dz.U. 2026 poz. 490](DU/2026/DU-2026-490.md) | 2026-04-09 | [Dz.U. 2025 poz. 46](DU/2025/DU-2025-46.md) |
| Kodeks postępowania w sprawach o wykroczenia | [Dz.U. 2025 poz. 860](DU/2025/DU-2025-860.md) | 2025-06-30 | – |
| Kodeks pracy | [Dz.U. 2026 poz. 1245](DU/2026/DU-2026-1245.md) | 2026-09-24 | [Dz.U. 2025 poz. 277](DU/2025/DU-2025-277.md) |
| Kodeks rodzinny i opiekuńczy | [Dz.U. 2026 poz. 236](DU/2026/DU-2026-236.md) | 2026-02-27 | – |
| Kodeks wyborczy | [Dz.U. 2026 poz. 1261](DU/2026/DU-2026-1261.md) | 2026-09-28 | [Dz.U. 2025 poz. 365](DU/2025/DU-2025-365.md) |
| Kodeks wykroczeń | [Dz.U. 2025 poz. 734](DU/2025/DU-2025-734.md) | 2025-06-04 | – |
| Ordynacja podatkowa | [Dz.U. 2026 poz. 622](DU/2026/DU-2026-622.md) | 2026-05-11 | [Dz.U. 2025 poz. 111](DU/2025/DU-2025-111.md) |

Wszystkie akty z tekstem jednolitym ogłoszonym od 2025 r. (890): [TEKSTY_JEDNOLITE.md](TEKSTY_JEDNOLITE.md).
<!-- tj:end -->

## Zawartość

- `DU/<rok>/DU-<rok>-<pozycja>.md`: jeden akt. Front matter YAML z metadanymi ELI
  (klucze zgodne z [legalize-pl](https://github.com/legalize-dev/legalize-pl) tam, gdzie znaczą to
  samo), potem tekst: `##### Art. N.` (albo `##### § N.`), akapity, `## Załącznik …`, przypisy `[^n]`.
  Ust., pkt i lit. zaczynają akapit. Cytowane przepisy (nowelizacje) nie są nagłówkami.
  Indeksy jako znaki Unicode: `Art. 41¹.`, `m²`, `P₂O₅`.
- `DU/<rok>/DU-<rok>-<pozycja>.json`: ten sam akt jako drzewo jednostek (od 2026-09-29, eli2md 0.5.3).
  Węzły `art`, `par` (§), `ust`, `pkt`, `lit`, `tir` mają numer, ścieżkę (`art_5/ust_2/pkt_3`), tekst i dzieci;
  akapity bez numeru to węzły `text`, przepisy cytowane w nowelizacjach to `text` z `"quoted": true`
  pod jednostką, która je zawiera. Osobne drzewo dla każdego załącznika, przypisy w `footnotes`.
  Opis i przykład: [README eli2md](https://github.com/PolskiAgentW/eli2md#json-drzewo-jednostek-od-053).
- `index.csv`: jeden wiersz na akt, także nieudany: `eli, year, pos, type, title,
  announcement_date, promulgation, change_date, pdf_sha256, pages, words, no_text_pages, image_pages,
  ocr_pages, image_ocr_pages, status, error, converter, converted_at`. `ocr_pages` jest puste, jeśli akt
  konwertowano bez OCR (akty bez skanów przed 0.6.0); `image_ocr_pages` (od 0.6.4) to liczba stron, na których
  OCR odczytał obraz tekstu (niżej).
- Cały zbiór w jednym pliku: [`dziennik-ustaw-md.jsonl.gz`](https://github.com/PolskiAgentW/dziennik-ustaw-md/releases/download/dane/dziennik-ustaw-md.jsonl.gz)
  (JSON Lines, jeden akt w wierszu: kolumny `index.csv`, `meta` = front matter, `markdown` = tekst bez front
  matter, `tree` = drzewo z pliku `.json`). Odświeżany codziennie po aktualizacji (workflow „Eksport”).
  Przykład: `pandas.read_json("dziennik-ustaw-md.jsonl.gz", lines=True)`.
- Ten sam zbiór na Hugging Face (Parquet, drzewo jako tekst JSON): [huggingface.co/datasets/PolskiAgentW/dziennik-ustaw-md](https://huggingface.co/datasets/PolskiAgentW/dziennik-ustaw-md),
  `datasets.load_dataset("PolskiAgentW/dziennik-ustaw-md")`. Odświeżany razem z plikiem JSON Lines.

Część stron w PDF-ach nie ma warstwy tekstowej: to skany (głównie teksty umów międzynarodowych, po polsku
i w językach obcych) albo grafiki. Od 2026-09-29 (eli2md 0.6.0) takie strony czyta OCR (tesseract).
**Tekst z OCR jest oznaczony**: przed każdą stroną stoi notka `> [Strona 5 PDF nie ma warstwy tekstowej.
Tekst poniżej odczytał OCR …]`, a każdy akapit OCR jest cytatem blokowym (`> …`); w JSON to węzły `ocr`, nigdy
jednostki. We front matter jest pole `pages_ocr`, w `index.csv` kolumna `ocr_pages`. OCR myli się częściej niż
warstwa tekstowa PDF, zwłaszcza w liczbach i tabelach. Zmierzone na stronach cyfrowych (górna granica, prawdziwe
skany są gorsze): recall słów 0.97–0.98, słów z cyframi 0.88–0.91, tabel ok. 0.83. Strony, z których OCR nie daje
czytelnego tekstu (mapy, rysunki, podpisy), mają nadal tylko notkę `> [Strony … PDF nie mają warstwy tekstowej …]`.

Na innych stronach obok tekstu są duże obrazy (wzory formularzy, rysunki, mapy). **Ich treści tu nie ma.**
W tekście jest notka `> [Na stronie 7 PDF jest obraz …]`, we front matter pole `pages_with_images`,
w `index.csv` kolumna `image_pages`. Wyjątek od 0.6.4: gdy obraz jest skanem tekstu ciągłego (s. 1 umów
międzynarodowych: preambuła i pierwsze artykuły), tekst odczytuje OCR. Stoi wtedy pod notką `> [Na stronie 1 PDF
jest obraz tekstu (skan). Tekst poniżej odczytał z obrazu OCR …]` jako cytaty `> …`; we front matter pole
`pages_images_ocr`, w `index.csv` kolumna `image_ocr_pages`. Tak jest w 19 umowach (24 strony). Reguła jest
ostrożna: w 2025–2026 z 43 umów, których s. 1 jest obrazem, tekst dostaje 25 (DU i M.P. razem); tytuły
w krótkich liniach zostają z notką.

Metadane pochodzą z API ELI bez poprawek, więc zawierają też jego błędy. Przykład: 5 aktów miało
`announcement_date` późniejszą niż data z tytułu (DU/2025/1099, DU/2025/1122, DU/2026/1141: rok 2028;
DU/2026/626, DU/2026/740: rok 2206; stan na 2026-09-30). API poprawiło te daty 2026-10-01 (`change_date`),
zbiór ma już nowe wartości. 2026-10-02 API zmieniło kolejne daty aktów DU i M.P. z lat 2012–2026, które różniły się od PDF;
w tym zbiorze 20 (`announcement_date` lub `promulgation_date`), nowe wartości są tu od aktualizacji 2026-10-03.
18 z nich jest teraz zgodnych z PDF. W 2 umowach międzynarodowych (DU/2026/189, DU/2026/684) API podaje inną
datę niż tytuł; według ISAP przy umowach to data ratyfikacji.

## Jak powstaje i jak dobre jest

Konwerter: [eli2md](https://github.com/PolskiAgentW/eli2md). Jakość zmierzyłem na aktach z 2024 r.,
które mają i PDF, i oficjalny HTML. Na odłożonej próbie 46 aktów (wersja 0.5.3; kolejne wersje 0.6.x mierzone na
nowych próbach dają w treści głównej te same lub lepsze wyniki, szczegóły w README eli2md; ocena jednorazowa):
- słowa treści głównej: recall 0.998, precision 0.984;
- drzewo jednostek (art., §, ust., pkt, lit.): w treści głównej 1256 z 1256 jednostek z właściwą ścieżką
  we właściwym miejscu i żadnej fałszywej; w załącznikach recall 0.998, precision 0.994;
- nagłówki artykułów/paragrafów w treści głównej: 145 ze 148, bez fałszywych (3 brakujące to jeden akt,
  poprawiony po teście, więc ta liczba nie jest niezależna).

Przypisy i tabele wypadają słabiej (tabele są spłaszczone do akapitów, wiersz po wierszu). Szczegóły,
słabe miejsca i poprzednie wyniki są w README eli2md.

**Losowa kontrola wzrokowa danych 2025–2026** (2026-09-29, eli2md 0.6.2): 20 losowych aktów, 35 stron (strona 1
i jedna losowa), strona PDF obok wyniku. Bez żadnego błędu: 28 stron. Błąd konwertera: 6 stron, w tym 4 istotne
(kolejność tekstu przy indeksach w nawiasach, przypis z wyliczeniem, dwie tabele z przeplecionymi komórkami)
i 2 drobne; na 1 stronie tylko błędna data przepisana z API. Na żadnej stronie nie zginęło słowo. Próba jest mała
(przedział 95% dla odsetka stron z błędem: 7–34%) i nadreprezentuje strony tytułowe; tabel były w niej tylko
2 strony. Raport: [eval/visual_audit_2025_2026_v0.6.2.md](https://github.com/PolskiAgentW/eli2md/blob/main/eval/visual_audit_2025_2026_v0.6.2.md).

**Porównanie tekstów jednolitych z poprzednim tekstem jednolitym w HTML** (2026-10-04). Dla 381 ustaw najnowszy
tekst jednolity w zbiorze porównałem artykuł po artykule z wcześniejszym tekstem jednolitym tej samej ustawy, który
API ELI ma w HTML. Artykuł, którego nie zmieniła żadna nowelizacja, powinien mieć ten sam tekst. Z 50 823 artykułów
w obu tekstach 43 531 (85,7%) jest identycznych (bez białych znaków). 7 292 różniące się porównałem z warstwą tekstową
PDF tego samego tekstu jednolitego: 7 006 się z nią zgadza (różnica to zmiana prawa, nie błąd konwersji), 286 jest do
oceny. Wśród nich: 92 różnice do 3 znaków (kolejność etykiet, dzielenie wyrazów), 61 linii zakresu „Art. 22–28.
(pominięte)” doklejonych do poprzedniego artykułu, 47 przypisów z etykietą „I)” / „a)” wpisanych w treść ostatniego
artykułu, 35 wzorów, 8 zgubionych indeksów dolnych z literą, 4 nagłówki działu w treści artykułu, 4 artykuły z literą
„ł” bez własnego nagłówka, 35 innych (głównie wzory i tabele, nie wszystkie obejrzane). Metoda nie widzi błędów
w artykułach dodanych później (1 182) ani błędów wspólnych z warstwą tekstową PDF. Raport i skrypty:
[eval/tj_survey_2026-10-04.md](https://github.com/PolskiAgentW/eli2md/blob/main/eval/tj_survey_2026-10-04.md).

**Znane błędy**:
- wzory z Worda są spłaszczone do jednej linii i trzeba je czytać z PDF. W 4 aktach (DU/2025/454, 459, 1743, 1744)
  mapa znaków czcionki wzorów jest w PDF błędna, więc wzory są nieczytelne;
- w tabelach z komórkami wieloliniowymi linie sąsiednich kolumn bywają przeplecione (DU/2025/205, lp. 9);
- przypis z wyliczeniem: do przypisu trafia tylko pierwszy akapit, dalsze punkty są w treści (DU/2026/421).
- przypis z etykietą rzymską w zwykłym druku („I) Odnośnik dodany przez…”) dokleja się do poprzedniego przypisu;
- indeks dolny z literą lub kropką ginie: „kategorii T , T , T” zamiast „T1b, T2b, T3b” (DU/2025/1490 art. 54).

Zmiana 2026-10-05 w nocy (eli2md 0.6.25, wszystkie akty od nowa; wcześniej większość była z 0.6.7). Zmienione 386
z 3287 plików, w 355 z nich te same słowa (zmieniają się tylko nagłówki, przypisy i podział akapitów): więcej nagłówków
jednostek w 316 plikach, więcej przypisów w 73, w żadnym mniej. Słowa: −1694 / +1662 na 11,5 mln w zmienionych plikach,
w 31 plikach, z tego 25 to akty z OCR (1601 z 1694 usuniętych słów; strony odczytane od nowa tesseractem 5.5.0 zamiast
5.3.4 na serwerze GitHuba); żaden plik nie
stracił więcej niż 2% słów. Poprawione m.in.: przypisy z etykietą „I)” / „a)” na końcu aktu są przypisami, a odnośnik
„z późn. zm.a)” to `[^a]` (DU/2025/1131 art. 279, DU/2023/1206); linia „Art. 14–26a. (pominięte)” jest nagłówkiem
(DU/2025/1584); art. 106ł ma własny nagłówek (DU/2025/633). Przed przeliczeniem na dwóch odłożonych próbach aktów
z HTML (70 z 2024 r. i 60 z 2012–2023) tekst 0.6.25 i 0.6.7 był taki sam co do słowa
([pomiar](https://github.com/PolskiAgentW/eli2md/blob/main/eval/heldout/README.md)). Od 2026-10-05 workflow
aktualizacji używa eli2md 0.6.25.

Zmiana 2026-10-01 wieczorem (eli2md 0.6.22, 42 akty, w których OCR nie dał tekstu z części stron). Strona skanu,
z której OCR nie odczytał użytecznego tekstu, jest czytana drugi raz z podaną rozdzielczością obrazu (wcześniej tesseract
jej nie dostawał i na stronach z tabelami gubił odstępy między słowami). Strony odczytane wcześniej czyta się jak przedtem.
W tych 42 aktach: strony z tekstem z OCR 570 → 602, słowa 766 359 → 769 299; w 8 aktach OCR odczytał teraz wszystkie
strony bez warstwy tekstowej. W 2 aktach (DU/2025/54, DU/2025/898) jest o 1 stronę z OCR mniej: to strony z mapą, z których
OCR daje głównie szum z napisów na mapie, a serwer GitHuba odczytuje je inaczej niż konwersja lokalna (przyczyny nie znam).
01.10 przez ok. 15 min (commit fa1dc461) była tu wersja 0.6.21, która część dobrze czytanych stron odrzucała; zastąpiona.

Zmiana 2026-09-30 około 10:00 (eli2md 0.6.7, wszystkie akty od nowa). Tekst zmienił się w 369 z 3266 plików:
- objaśnienia wydrukowane w treści (pod tabelami i formularzami w załącznikach, przypisy cytowane przez nowelizacje:
  „¹⁾ Niniejsza ustawa wdraża…”) mają znaczniki `¹⁾` jak w druku, a nie `[^n]`. Wcześniej prowadziły do przypisu aktu
  o tym samym numerze (DU/2025/1016: „Arsen[^1]” w tabeli → przypis o ministrze kierującym działem). 251 aktów;
- przypis z wyliczeniem („Niniejsza ustawa:” + „1) wdraża…” + „2) służy…”) jest w całości przypisem, punkty są jego
  akapitami z wcięciem. Wcześniej trafiały na koniec pliku jako treść, a w JSON jako jednostki `pkt` po podpisie
  (DU/2026/421). 165 aktów.
Selfcheck (te same akty, ta sama miara): odsetek słów PDF obecnych w wyniku wzrósł w 247 plikach (cyfry `¹⁾` są
słowami PDF), spadł w 2 (najwięcej o 0,0008).

Zmiana 2026-09-30 przed południem (eli2md 0.6.5, wszystkie akty od nowa). Tekst i drzewo JSON zmieniły się w 133
z 3266 plików: przypisy ze stron, na których kreska przypisów jest wysoko (np. strona z samymi przypisami
w obwieszczeniu tekstu jednolitego) albo jest narysowana linią, są teraz definicjami `[^n]:` na końcu pliku, a nie
akapitami treści (np. DU/2025/1016). Selfcheck bez zmian w każdym z tych plików (słowa są te same).

Zmiana 2026-09-30 rano (eli2md 0.6.4, wszystkie akty od nowa). Tekst zmienił się w 40 plikach, drzewo JSON
w 68:
- s. 1 umów międzynarodowych: tekst z obrazu przez OCR (opis wyżej), 19 aktów;
- wzory z Worda (Cambria Math) bez podwojonych liter („k” zamiast „kk”), mniej ukrytego tekstu z wklejonych PDF-ów
  (np. zakryte pierwotne nagłówki załączników w DU/2026/667; sprawdzone na renderze strony);
- JSON: numerowane wiersze tabel i formularzy (wykazy współrzędnych, karty akwenów, wiersze tabel zmienianych
  bez cudzysłowu) są tekstem, nie jednostkami ust./pkt.
Sprawdzenie (selfcheck, te same akty, ta sama miara): odsetek słów PDF obecnych w wyniku wzrósł w 16 plikach,
spadł w 5 — w obejrzanych (DU/2026/40, DU/2026/667) dlatego, że wynik nie zawiera już ukrytego tekstu, który
miara po stronie PDF nadal liczy. Na odłożonej próbie 35 aktów z 2024 r. wyniki 0.6.4 i 0.6.3 są identyczne.

Zmiana 2026-09-30 w nocy (eli2md 0.6.3, wszystkie akty od nowa). Tekst zmienił się w 352 z 3266 plików
(w pozostałych tylko pole `converter`):
- indeksy przy numerach jednostek, drukowane w części PDF-ów z 2026 r. w nawiasach („Art. 479[30f].”), a wcześniej
  jako małe „1a” (Art. 22 1a), są teraz znakami górnymi: `Art. 479³⁰ᶠ.`, `Art. 22¹ᵃ.` (tak samo `num` i `path`
  w JSON). Wcześniej takie artykuły nie były nagłówkami ani jednostkami w JSON. Nagłówków art./§ w całym zbiorze
  jest 92 626 (było 91 151); w k.p.c. (DU/2026/468) 2015 nagłówków artykułów (było 1169);
- wzory i tekst w czcionkach z błędnymi metrykami (Cambria) nie są już brane za tekst ukryty (np. DU/2026/1236);
- na stronach obróconych (tabele w poziomie) nie giną litery drobnego druku; w ciasnych tabelach pozycje
  „2)”, „b)” zaczynają nowy akapit.
Sprawdzenie (eval/selfcheck.py z eli2md, ta sama miara dla obu wersji, na 352 zmienionych plikach): odsetek słów
PDF obecnych w wyniku wzrósł w 154 plikach i spadł w 14 (najwięcej o 0,0002). Szczegóły w README eli2md.

Zmiana 2026-09-29 późnym wieczorem (eli2md 0.6.2, wszystkie akty od nowa):
- akapity: część aktów jest składana z większym odstępem między liniami (ok. 0,6 rozmiaru czcionki), a konwerter
  robił wtedy z każdej linii osobny akapit. Tekst zmienił się w 182 plikach (w pozostałych tylko pole `converter`);
  akapitów w nich było 272 723, jest 214 537. Na odłożonej próbie z 2024 r. (41 aktów) fałszywe podziały
  w załącznikach: precision 0.953 → 0.989, bez utraty prawdziwych podziałów (recall 0.997 w obu wersjach);
- JSON: „Rozdział 2. Tytuł” w jednej linii jest nagłówkiem, a sekcje załącznika „I.”, „II.”, … zamykają jednostki
  poprzedniej sekcji (wcześniej np. lista „1) …” z sekcji III wisiała pod ust. 6 z sekcji II). Zmienione drzewo
  w 313 plikach JSON, w 74 inne ścieżki jednostek; węzłów `heading` 940 → 2093;
- dane z Monitora Polskiego (2025–2026, ten sam konwerter) są w osobnym repozytorium:
  [monitor-polski-md](https://github.com/PolskiAgentW/monitor-polski-md);
- poprawiona podstawa prawna w sekcji Licencja (art. 4 pkt 1, wcześniej błędnie pkt 2).

Zmiana 2026-09-29 wieczorem (eli2md 0.6.1, wszystkie akty od nowa):
- przypisy: numeracja zaczyna się od nowa w załącznikach i formularzach, a etykiety w Markdown się powtarzały
  (466 plików), przez co odnośniki wskazywały zły przypis, a w JSON część przypisów ginęła. Teraz kolejne
  przypisy o tym samym numerze mają etykiety `[^1_2]`, `[^1_3]`…;
- strony, na których większość znaków nie ma kodów Unicode (formularze; w tekście było „(cid:3)(cid:346)…”,
  27 plików), są traktowane jak strony bez czytelnej warstwy tekstowej i czytane przez OCR;
- akapit zaczynający się od `>` albo `#` (np. `> 90 dni` w tabeli) jest poprzedzony `\`;
- dołączone 98 aktów z lat 2020–2023, dla których API nie ma HTML (selfcheck: mediana odsetka słów PDF
  obecnych w wyniku 0.972, odwrotnie 0.989 — jak w aktach 2025–2026);
- znany problem: na ok. 11 stronach w kilku aktach (np. DU/2025/1249 s. 104–107) większość znaków nie ma kodów
  Unicode, a OCR nie dał czytelnego tekstu, więc jest tylko notka; w poprzedniej wersji była tam część słów.
  Od 0.6.2 taka strona zachowuje czytelną część warstwy tekstowej (bez nieczytelnych znaków, z notką), o ile
  jakaś jest: w DU/2025/1249 wróciła s. 104, a s. 105–107 nadal mają tylko notkę (w całym zbiorze stron bez
  czytelnej warstwy tekstowej: 1848 → 1837).

Zmiana 2026-09-29 po południu (eli2md 0.5.2 → 0.5.3, wszystkie akty przekonwertowane od nowa, dodany JSON).
Policzone na całym zbiorze przed i po:
- pliki, w których ust./pkt/lit. były sklejone w jeden akapit („…: a) …; b) …”): 347 → 176
  (wystąpień 11 066 → 2 691). Część rozporządzeń jest składana z bardzo małym odstępem między jednostkami;
- wyraz przeniesiony na dywizie („rolno- -środowiskowy” zamiast „rolno-środowiskowy”): 421 plików → 3;
- akapitów dłuższych niż 2000 znaków: 1434 → 915;
- tekst z dołu tabel brany za przypisy (obramowanie tabeli podobne do kreski nad przypisami): poprawione;
- § w treści głównej bez nagłówka, bo załącznik zawierał akapit „Art. 42 ust. 1 …”: poprawione.

Zmiana 2026-09-29 rano (eli2md 0.4.0 → 0.5.2): wcześniej cyfry w indeksie górnym były błędnie zamieniane
na odnośniki do przypisów (`Art. 59[^2]` zamiast `Art. 59²`, `m[^2]` zamiast `m²`; w 0.4.0 dotyczyło to
co najmniej 410 i 220 plików), a cytowane artykuły nowelizacji dostawały nagłówki `#####`.

Aktualizacja: codziennie o 04:23 UTC workflow `.github/workflows/update.yml` pobiera listę aktów
z API ELI. GitHub potrafi opóźnić taki start o kilka godzin, więc jeśli do 10:17 UTC nie było
udanej aktualizacji, workflow rusza drugi raz. Konwertuje nowe akty oraz te, którym zmienił się `changeDate`, i commituje wynik.
Jeśli przez ponad 10 dni nie przybędzie żaden nowy akt, workflow kończy się błędem, żeby cicha awaria
była widoczna. Najdłuższa przerwa w ogłaszaniu aktów w latach 2025–2026 wyniosła 6 dni.

## Licencja

Akty normatywne i ich urzędowe projekty oraz urzędowe dokumenty i materiały nie są przedmiotem prawa
autorskiego (art. 4 pkt 1 i 2 ustawy o prawie autorskim i prawach pokrewnych). Pozostała zawartość
(indeks, skrypty): CC0 1.0.

Błędy konwersji zgłaszaj w Issues. Najlepiej podaj pozycję aktu i fragment.
