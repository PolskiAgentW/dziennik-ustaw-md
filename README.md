# Dziennik Ustaw w Markdown (od 2025 r.)

Teksty aktów z **Dziennika Ustaw** od 2025 r. (oraz 98 aktów z lat 2020–2023, dla których API nie ma HTML,
i teksty jednolite ustaw z lat 2012–2024)
w Markdown i jako drzewo jednostek w JSON, z metadanymi z API ELI Sejmu. Aktualizowane codziennie przez GitHub Actions.
*Texts of Polish Journal of Laws acts (2025+) as Markdown and as a JSON tree of units (art./§/ust./pkt/lit.),
converted from the official PDFs; updated daily.*

> **Nieoficjalne.** Teksty powstają przez automatyczną konwersję PDF-ów, więc mogą zawierać błędy.
> Wiążący jest PDF w Dzienniku Ustaw (link `source_pdf` w każdym pliku).

<!-- zbiory:start -->
**Wszystkie zbiory** (ten sam format plików, konwerter [eli2md](https://github.com/PolskiAgentW/eli2md)). Akty, które API ELI
podaje w HTML (np. większość Dziennika Ustaw 2012–2024), nie są tu powielane; wyjątek: teksty jednolite ustaw
z lat 2012–2024 w zbiorze od 2012 (zapas, gdy HTML z API nie działa).

| lata | Dziennik Ustaw | Monitor Polski |
|---|---|---|
| od 2012 | [GitHub](https://github.com/PolskiAgentW/dziennik-ustaw-md) · [HF](https://huggingface.co/datasets/PolskiAgentW/dziennik-ustaw-md): od 2025 r. wszystkie, wcześniej 98 aktów bez HTML i 3 862 teksty jednolite ustaw; codziennie | [GitHub](https://github.com/PolskiAgentW/monitor-polski-md) · [HF](https://huggingface.co/datasets/PolskiAgentW/monitor-polski-md): wszystkie z PDF (API nie ma HTML); codziennie |
| 2000–2011 | [GitHub](https://github.com/PolskiAgentW/dziennik-ustaw-2000-2011-md) · [HF](https://huggingface.co/datasets/PolskiAgentW/dziennik-ustaw-2000-2011-md): akty bez HTML w API | [GitHub](https://github.com/PolskiAgentW/monitor-polski-2000-2011-md) · [HF](https://huggingface.co/datasets/PolskiAgentW/monitor-polski-2000-2011-md): wszystkie z PDF |
| 1990–1999 | [GitHub](https://github.com/PolskiAgentW/dziennik-ustaw-1990-1999-md) · [HF](https://huggingface.co/datasets/PolskiAgentW/dziennik-ustaw-1990-1999-md): akty bez HTML w API (OCR skanów) | brak |
| 1918–1989 | [GitHub](https://github.com/PolskiAgentW/dziennik-ustaw-1918-1989-md) · [HF](https://huggingface.co/datasets/PolskiAgentW/dziennik-ustaw-1918-1989-md): akty bez HTML w API (OCR skanów; pomiar jakości w README) | brak |

Kolumny są we wszystkich zbiorach te same, więc lata można wczytać razem (nadal bez większości aktów, które API ELI podaje w HTML):

```python
from datasets import load_dataset

du = load_dataset("parquet", split="train", data_files=[
    "hf://datasets/PolskiAgentW/dziennik-ustaw-1918-1989-md/data/*.parquet",
    "hf://datasets/PolskiAgentW/dziennik-ustaw-1990-1999-md/data/*.parquet",
    "hf://datasets/PolskiAgentW/dziennik-ustaw-2000-2011-md/data/*.parquet",
    "hf://datasets/PolskiAgentW/dziennik-ustaw-md/data/*.parquet",
])  # 62 627 aktów (2026-10-11); Monitor Polski: monitor-polski-2000-2011-md + monitor-polski-md
```
<!-- zbiory:end -->

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
Stan na 2026-10-26 01:12 UTC (liczone z `index.csv`, aktualizowane automatycznie).

| rok | aktów w indeksie | przekonwertowanych | błędów |
|---|---:|---:|---:|
| 2012 | 67 | 67 | 0 |
| 2013 | 110 | 110 | 0 |
| 2014 | 142 | 142 | 0 |
| 2015 | 208 | 208 | 0 |
| 2016 | 316 | 316 | 0 |
| 2017 | 336 | 336 | 0 |
| 2018 | 382 | 382 | 0 |
| 2019 | 404 | 404 | 0 |
| 2020 | 411 | 411 | 0 |
| 2021 | 368 | 368 | 0 |
| 2022 | 391 | 391 | 0 |
| 2023 | 433 | 433 | 0 |
| 2024 | 392 | 392 | 0 |
| 2025 | 1900 | 1900 | 0 |
| 2026 | 1390 | 1390 | 0 |

Akty ze stronami bez warstwy tekstowej (skany, grafiki): 94, razem 1917 z 204758 stron. Tekst z OCR (oznaczony) ma 1832 z nich w 86 aktach; treści pozostałych brak.
Akty ze stronami z dużymi obrazami (wzory, rysunki; ich treści brak): 252.

Rodzaje aktów: Obwieszczenie 4904, Rozporządzenie 1875, Ustawa 379, Oświadczenie rządowe 45, Umowa międzynarodowa 37, Komunikat 4, Postanowienie 3, Uchwała 2, Traktat 1.
Wersje konwertera: eli2md 0.6.52 (3394), eli2md 0.6.25 (2111), eli2md 0.6.53 (691), eli2md 0.6.56 (369), eli2md 0.6.61 (307), eli2md 0.6.59 (209), eli2md 0.6.60 (88), eli2md 0.6.57 (34), eli2md 0.6.58 (29), eli2md 0.6.25.2 (10), eli2md 0.6.54 (6), eli2md 0.6.67 (2).
<!-- stats:end -->

## Teksty jednolite

Teksty jednolite (obwieszczenia o ogłoszeniu jednolitego tekstu ustawy lub rozporządzenia) od 2025 r. też są
w API tylko w PDF. Narzędzie, które bierze tekst z HTML, dostaje więc tekst jednolity sprzed 2025 r., bez
późniejszych zmian. Tutaj są najnowsze teksty jednolite ogłoszone od 2025 r. Tabela jest odświeżana razem ze zbiorem.
Tekst jednolity podaje stan prawny na dzień wskazany w obwieszczeniu. Zmian ogłoszonych później w nim nie ma.

Artykuły z PDF zgadzają się z HTML: na 12 tekstach jednolitych, które mają oba formaty (m.in. KC, KP, KPC, KK),
w plikach tego zbioru 5912 z 5929 artykułów ma te same słowa (pomiar 2026-10-24: `.github/tj_articles_published.py`;
przy eli2md 0.6.17 było 5903: [pomiar](https://github.com/PolskiAgentW/eli2md/blob/main/eval/tj_articles_0.6.17.md)).
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
| Kodeks karny | [Dz.U. 2026 poz. 1342](DU/2026/DU-2026-1342.md) | 2026-10-16 | [Dz.U. 2025 poz. 383](DU/2025/DU-2025-383.md) |
| Kodeks karny skarbowy | [Dz.U. 2025 poz. 633](DU/2025/DU-2025-633.md) | 2025-05-15 | – |
| Kodeks karny wykonawczy | [Dz.U. 2026 poz. 1307](DU/2026/DU-2026-1307.md) | 2026-10-08 | [Dz.U. 2025 poz. 911](DU/2025/DU-2025-911.md) |
| Kodeks postępowania administracyjnego | [Dz.U. 2025 poz. 1691](DU/2025/DU-2025-1691.md) | 2025-12-03 | – |
| Kodeks postępowania cywilnego | [Dz.U. 2026 poz. 468](DU/2026/DU-2026-468.md) | 2026-04-07 | – |
| Kodeks postępowania karnego | [Dz.U. 2026 poz. 490](DU/2026/DU-2026-490.md) | 2026-04-09 | [Dz.U. 2025 poz. 46](DU/2025/DU-2025-46.md) |
| Kodeks postępowania w sprawach o wykroczenia | [Dz.U. 2026 poz. 1336](DU/2026/DU-2026-1336.md) | 2026-10-15 | [Dz.U. 2025 poz. 860](DU/2025/DU-2025-860.md) |
| Kodeks pracy | [Dz.U. 2026 poz. 1245](DU/2026/DU-2026-1245.md) | 2026-09-24 | [Dz.U. 2025 poz. 277](DU/2025/DU-2025-277.md) |
| Kodeks rodzinny i opiekuńczy | [Dz.U. 2026 poz. 236](DU/2026/DU-2026-236.md) | 2026-02-27 | – |
| Kodeks wyborczy | [Dz.U. 2026 poz. 1261](DU/2026/DU-2026-1261.md) | 2026-09-28 | [Dz.U. 2025 poz. 365](DU/2025/DU-2025-365.md) |
| Kodeks wykroczeń | [Dz.U. 2026 poz. 1372](DU/2026/DU-2026-1372.md) | 2026-10-21 | [Dz.U. 2025 poz. 734](DU/2025/DU-2025-734.md) |
| Ordynacja podatkowa | [Dz.U. 2026 poz. 622](DU/2026/DU-2026-622.md) | 2026-05-11 | [Dz.U. 2025 poz. 111](DU/2025/DU-2025-111.md) |

Wszystkie akty z tekstem jednolitym ogłoszonym od 2025 r. (910): [TEKSTY_JEDNOLITE.md](TEKSTY_JEDNOLITE.md).
<!-- tj:end -->

### Teksty jednolite ustaw z lat 2012–2024

Zbiór ma też 3 862 obwieszczenia o ogłoszeniu jednolitego tekstu ustawy z lat 2012–2024 (wybranych po tytule:
„jednolitego tekstu ustawy”), choć API ELI podaje je również w HTML. To zapas na wypadek, gdy HTML z API nie działa:
2026-10-10 `text.html` zwracał HTTP 500 dla wszystkich sprawdzonych aktów (397 z 397, 22:20–22:28 CEST), a `text.pdf`
i metadane działały ([zgłoszenie](https://github.com/PolskiAgentW/dziennik-ustaw-md/issues/1)). 2026-10-11 od 00:37 CEST
`text.html` znów działał (te same 397 aktów: 397 z 397 HTTP 200, 00:38–00:55 CEST). Pliki są pod tymi
samymi adresami co reszta zbioru: `DU/<rok>/DU-<rok>-<pozycja>.md` i `.json`. W `.json` tekst jednolity jest
w `annexes[0].body` (nagłówek `annexes[0].heading` zaczyna się od „Załącznik do obwieszczenia”; w `body` jest tylko
krótkie obwieszczenie), załączniki do ustawy w kolejnych `annexes`, a przypisy w `footnotes`, wspólnych dla całego aktu.
Wyjątki (2 z 3 862): w DU/2013/1442 tekst jednolity jest w `body`, po podpisie obwieszczenia, a w DU/2018/2321
w `annexes[3]` (przed nim są cytowane w obwieszczeniu załączniki ustawy zmieniającej). Nagłówek `annexes[0]` ma inną
pisownię w źródle w DU/2018/280 („Załącznik do obwieszczania”) i DU/2015/295 („Załącznik obwieszczenia”).

Te akty przekonwertowałem lokalnie eli2md 0.6.52 (wersja 0.6.50 nie rozpoznawała nagłówka tekstu jednolitego
w PDF z lat 2012–2014 i rozbijała słowa z literą w innym foncie: „si ę”, a wersja 0.6.51 słowa z miękkim dywizem:
„przysługuj ą cego”; opis w README eli2md). 2026-10-16 i 2026-10-17 część przeliczyłem nowszymi wersjami (6 aktów eli2md 0.6.58, 247 aktów eli2md 0.6.59;
opis w „Zmiana 2026-10-16” i „Zmiana 2026-10-17” niżej). Codzienna aktualizacja nie przelicza tekstu aktów, które
mają HTML, więc gdy API zmieni treść któregoś z nich, tutaj ta zmiana nie dotrze (metadane tak, od 2026-10-13).

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
- indeks dolny z literą lub kropką ginął: „kategorii T , T , T” zamiast „T1b, T2b, T3b” (DU/2025/1490 art. 54);
  od eli2md 0.6.53 (2026-10-11) „kategorii T1b, T2b, T3b, T4.1b, T4.2b, T4.3b i T₅”.

Zmiana 2026-10-24 (eli2md 0.6.61, 306 aktów): oznaczenie litery albo punktu z odnośnikiem na początku wiersza doklejało
się do poprzedniego akapitu: „…z zastrzeżeniem ust. 4f, d)[^22] przychodów ze zbycia…” (DU/2026/554, początek strony 42
PDF). Od eli2md 0.6.61 takie oznaczenie zaczyna nową jednostkę. Codzienna aktualizacja używa eli2md 0.6.61. Sprawdzone
A/B 0.6.60 → 0.6.61: wszystkie 377 ustaw z lat 2025–2026 w zbiorze, pliki .md i .json bez zmian.
Takie oznaczenie w środku akapitu (np. „…, d)[^22] …”) miało 307 tekstów jednolitych (477 miejsc). 306 z nich przeliczyłem
ponownie z tych samych PDF (sha256 jak w `index.csv`). W 295 słowa są te same co poprzednio. W 11 znaki są te same,
a zmieniają się wyrazy: indeksy dolne wracają do symboli we wzorach („Lw jn” → „Lwjn”, „M hw” → „Mhw” w DU/2025/100)
i rozdzielone wyrazy się łączą („r ozporządzenia” → „rozporządzenia”, DU/2025/1555). Po przeliczeniu takich miejsc
jest 16 w 3 aktach: DU/2025/1251 (9; w PDF wiersz zaczyna się od oznaczenia, przyczyny nie znam), DU/2020/1905 (1;
w PDF dwie etykiety „a)57)” i „a)58)”) i DU/2025/97 (6). DU/2025/97 nie przeliczałem, bo 0.6.61 zapisuje w nim odnośnik
„d)[^141]” jako zwykły tekst „d)¹⁴¹⁾”. Pomiar artykułów 12 tekstów jednolitych (wyżej) po przeliczeniu: dalej 5912 z 5929.

Zmiana 2026-10-26 (drzewo JSON, kod drzewa eli2md 0.6.70, 1 akt; opis w README eli2md, wpis 0.6.70): nagłówek z liczebnikiem
słownym pisanym małymi literami, stojący jako osobny akapit („Część pierwsza”, „Część druga”), jest w `.json` węzłem
`heading`. Wcześniej trafiał jako tekst do jednostki przed nim (DU/2025/903). `.md` się nie zmienił, więc pole `converter` (w `.md`, `.json` i `index.csv`) zostaje wersją, w której powstał `.md`. Liczba jednostek i słowa w drzewie bez zmian.
Codzienna aktualizacja używa od dziś eli2md 0.6.70 (wcześniej 0.6.67–0.6.69; zmiany 0.6.68 i 0.6.69 dotyczą tylko stron
czytanych przez OCR). Drzewa wszystkich aktów zbioru zbudowane z tych samych `.md` przez 0.6.69 i 0.6.70 różnią się tylko w tym akcie.

Zmiana 2026-10-25 (eli2md 0.6.67, 2 akty; opis w README eli2md, wpis 0.6.67): ostatnia pozycja rocznika ma w winiecie
gwiazdkę przy numerze pozycji, a pod kreską na s. 1 przypis „*) Ostatnia pozycja w 2025 r.”. To przypis winiety, ale stał na
końcu tekstu aktu i w ostatniej jednostce drzewa (DU/2025/1900: art. 93). Przeliczyłem ponownie oba takie akty tego zbioru
(DU/2021/2507 z eli2md 0.6.25, DU/2025/1900 z 0.6.53): ubywa tylko słów przypisu, nic nie przybywa. Codzienna
aktualizacja używa od dziś eli2md 0.6.67: na 40 losowych aktach z lat 2012–2026 (20 DU, 20 MP) daje te same pliki co
0.6.61 i 0.6.66 (poza numerem wersji).

Zmiana 2026-10-17 (eli2md 0.6.60, 23 akty): indeks dolny symbolu zapisanego kursywną wielką literą trafiał na sąsiedni
wiersz, często do środka wyrazu przeniesionego w PDF, a symbol zostawał bez indeksu: „WbP – … na realizację prot−1 gramów
rządowych” (DU/2025/337), „DEF – … przedłożonego Sejn−2 mowi” (DU/2025/1483), „publikod waną” (DU/2026/68). Teraz
„WbPt−1 – … na realizację programów rządowych”, „DEFn−2 – … przedłożonego Sejmowi”. Przeliczyłem 23 akty, w których
eli2md 0.6.60 daje inny wynik niż 0.6.59: 19 tekstów jednolitych z lat 2025–2026 (DU/2025/214, 337, 439, 450, 498, 610,
870, 901, 1273, 1483, DU/2026/68, 156, 599, 619, 650, 807, 1242, 1252, 1293) i 4 ustawy (DU/2025/159, 303, 759, 1301).
Sprawdzone A/B 0.6.59 → 0.6.60: wszystkie 491 tekstów jednolitych z lat 2025–2026, 369 ustaw bez tekstu HTML w API
(lista z 12.10) i 2 nowsze ustawy, 500 losowych aktów DU. W porównaniu z opublikowanymi plikami liczba jednostek jest ta sama, 22 akty nie tracą
żadnego znaku, a DU/2025/159 traci tylko „-” złączonego wyrazu „bezpieczeń-stwa”. Cyfry indeksu są teraz indeksem dolnym
(„P 2024” → „P₂₀₂₄”, DU/2025/759, DU/2026/807). W próbie zmieniło się też 6 tekstów jednolitych z lat 2012–2024
(DU/2014/1695, DU/2018/150, 2190, DU/2021/1930, DU/2023/725, DU/2024/1361). Tych nie przeliczałem, bo mają tekst HTML
w API. Pozostałych tekstów jednolitych z tych lat nie sprawdzałem. Codzienna aktualizacja używa eli2md 0.6.60.

Zmiana 2026-10-17 (eli2md 0.6.59, 247 aktów): 247 tekstów jednolitych z lat 2012–2024 przeliczyłem ponownie
(eli2md 0.6.52 → 0.6.59). To te, w których 0.6.59 daje inny wynik niż 0.6.52; w pozostałych 3 608 tekstach jednolitych
z tych lat wynik jest taki sam. Przykłady zmian: indeksy dolne i górne wracają do wyrazu, do którego należą:
„(SO )” → „(SO₂)”, „L … Aeq” → „LAeq” (DU/2013/1107, 1232), DU/2017/569 art. 31 ust. 2
„według wzoru: ( ) D K = W R + O - W - K” (indeksy w przypisie 14) → „( ) D KO(i - 1) = Ws Rk(i - 1) + Ok(i - 1) -
Wdk(i - 1) - KOZW(i - 1)”, DU/2020/1077 „NH , PM , PM … 3 10 2,5” → „NH₃, PM₁₀, PM2,5”. Pomiar (znaki tekstu bez odstępów,
znaczników Markdown i odsyłaczy, indeksy jak zwykłe cyfry i litery): 227 aktów bez utraty znaków, 20 traci tylko „-”;
w 19 to wyraz przeniesiony w PDF, którego części rozdzielał indeks, teraz złączony, a w DU/2020/1077 złe złączenie
„błę- … z” → „błęz” w tabeli, w której kolejność kolumn jest zła w obu wersjach. W 9 aktach jednostek jest więcej, bo
sklejone jednostki są rozdzielone (np. „Art. 19.” w DU/2020/23 jako nagłówek). Codzienna aktualizacja używa eli2md 0.6.59;
przed wydaniem A/B 0.6.58 → 0.6.59 na 4579 aktach tego zbioru zmienił tylko DU/2017/569 (opis w README eli2md).

Zmiana 2026-10-16 (eli2md 0.6.58, 7 aktów): artykuł złożony w PDF ciasno pod nagłówkiem rozdziału był w tekście tego
nagłówka, np. DU/2025/960: „Rozdział 1 Zmiany w przepisach Art. 480–524. (pominięte)”, DU/2020/105: „Rozdział 21
Nadzór nad działalnością funduszy emerytalnych Art. 199. (uchylony) Art. 200. 1. (uchylony) 2. …”. Teraz te artykuły
są osobnymi jednostkami w `.md` i w drzewie `.json`. Dotyczy DU/2020/105, 110, 276, 2052, DU/2021/1990, DU/2022/2378
i DU/2025/960 (A/B 0.6.57 → 0.6.58: tekst bez zmian, opis w README eli2md). Sześć z nich to teksty jednolite z lat
2020–2022, dotąd z eli2md 0.6.52; w pięciu tekst jest taki sam jak w opublikowanym pliku. W DU/2020/110 dochodzi poprawka
indeksów dolnych z 0.6.53: „kategorii T , T , T , C, R, 4.1 4.2 5” → „kategorii T4.1, T4.2, T₅, C, R”, „O = p + …” →
„On = pj + …”. Od tej zmiany codzienna aktualizacja używa eli2md 0.6.58.

Zmiana 2026-10-13 (eli2md 0.6.57, 6 aktów): tytuł bez tego, co API ELI dopisuje po tabulatorze (np. DU/2023/544:
„…Prawosławnego⇥2023-03-23⇥Pobierz dokument D2023000054401.pdf”, DU/2025/1028: „…służby⇥2025”). Dotyczy `title`
we front matter, linii `# tytuł`, `title` w `.json` i w `index.csv` w DU/2023/544, DU/2025/471, 959, 1028, DU/2026/202
i 564; tekst bez zmian (A/B 0.6.56 → 0.6.57). Od tej zmiany codzienna aktualizacja używa eli2md 0.6.57. Tego samego dnia
metadane 4 tekstów jednolitych (DU/2019/1079, DU/2021/994, DU/2022/470, DU/2024/1251) uzgodnione z API (słowa
kluczowe w 3, `change_date` w 4), bez przeliczania tekstu. Teksty jednolite z lat 2012–2024 mają w API także HTML,
więc codzienna aktualizacja ich nie przelicza; od tego dnia uzgadnia z API tylko ich metadane (MAINTENANCE.md).

Zmiana 2026-10-13 (eli2md 0.6.56, 267 aktów): podpis pod aktem. W tych aktach podpis był zwykłym akapitem `.md`,
a w `.json` tekstem ostatniej jednostki (w 257, np. dzieckiem § 43 w DU/2026/1316) albo tekstem na najwyższym poziomie.
Konwerter nie rozpoznawał podpisu z przecinkiem w nazwie urzędu („Minister Rodziny, Pracy i Polityki Społecznej: …”),
z „z up.” przed nazwiskiem, z długą nazwą urzędu ani kontrasygnaty Prezesa Rady Ministrów pod podpisem Prezydenta
(opis w README eli2md, wpisy 0.6.55 i 0.6.56). Teraz podpis jest kursywą i węzłem `signature`: 256 aktów ma pierwszy
taki węzeł, 11 dostaje kontrasygnatę. Wcześniej te pliki były z eli2md 0.6.25 (261), 0.6.25.2 (2) i 0.6.54 (4).
Poza podpisem tekst zmienia się w 21 z nich i są to zmiany konwertera od 0.6.25: złączone przeniesienia
(„ratowniczo- gaśniczego” → „ratowniczo-gaśniczego”, DU/2026/872), rozbite słowa („w obec” → „wobec”, DU/2026/456),
indeksy dolne („K , K , K , K” → „K₁, K₂, K₃, K₄”, DU/2025/1874), odstępy przed przypisem i nawiasem. Inne znaki
mają tylko DU/2025/1874 (indeksy) i DU/2026/8 (tekst obróconej tabeli, nieczytelny także wcześniej). Liczba jednostek
(art., §, ust., pkt) jest ta sama we wszystkich 267. Od tej zmiany codzienna aktualizacja używa eli2md 0.6.56
(wcześniej 0.6.54).

Zmiana 2026-10-13 (eli2md 0.6.56, kolejne 120 aktów): nagłówek `.md` z metadanymi sprzed ich zmiany w API ELI.
Przeliczenie wszystkich aktów 2026-10-05 (i ustaw oraz tekstów jednolitych 2026-10-11) korzystało z lokalnej kopii
metadanych i PDF pobranej wcześniej, więc akty, które API zmieniło w międzyczasie, dostały stare dane, a codzienna
aktualizacja ich nie ruszała (`index.csv` miał już nowy `change_date`). W tych 120 i w 267 opisanych wyżej nagłówek miał
starą datę ogłoszenia albo promulgacji w 32 aktach — wszystkie to daty, które API poprawiło po zgłoszeniu rozbieżności
z drukiem (np. DU/2025/1099: 2028-08-04 → 2025-08-04) — a stary status w 9. W 17 aktach (np. DU/2025/1099, DU/2026/135)
w zbiorze był też tekst z PDF sprzed jego wymiany w API; teraz `pdf_sha256` w `index.csv` to PDF z API.
Wcześniej te 120 plików było z eli2md 0.6.25 (23), 0.6.25.2 (19), 0.6.53 (68) i 0.6.54 (10). Treść zmienia się w 6:
indeksy dolne (DU/2025/1761, DU/2026/649), odstęp przed gwiazdką odnośnika (DU/2025/1727), „„ OPIEKUN” → „„OPIEKUN”
(DU/2025/81), a w wykropkowanym formularzu DU/2025/697 „3. 4.” → „34..” (ten fragment był zniekształcony także
wcześniej; jedna jednostka mniej). W pozostałych 114 zmienia się tylko nagłówek i pole `converter`.

Zmiana 2026-10-12 (eli2md 0.6.54, 1 akt): w DU/2025/179 drzewo w JSON miało przy art. 1 pkt 29 lit. d nagłówek
„Część VII” i ust. 1–7 na najwyższym poziomie. To wiersze tabeli, którą ustawa dodaje bez cudzysłowu, a pkt 30 art. 1
wisiał pod „ust. 7”. Teraz nagłówek i wiersze są tekstem lit. d, a art. 1 ma pkt 1–30. Markdown i słowa bez zmian.
W żadnym innym akcie tego zbioru drzewo się nie zmienia (A/B drzewa 0.6.53 → 0.6.54 na wszystkich plikach .md).

Zmiana 2026-10-11 (eli2md 0.6.53, 479 tekstów jednolitych ustaw z lat 2025–2026, ta sama lista co w porównaniach
w README eli2md): przeliczone z tych samych PDF; wcześniej eli2md 0.6.25 i 0.6.25.2. Tekst zmienia się w 41. W 32 zostają
te same znaki, zmieniają się odstępy. W 9 cyfry indeksów są teraz zapisane jako ₀₁₂… przy swoim symbolu, a przeniesienia
rozdzielone indeksem są scalone: „kategorii T , T , T , T , T , T i T” → „kategorii T1b, T2b, T3b, T4.1b, T4.2b, T4.3b
i T₅” (DU/2025/1490), „CO 20 MW¹⁾²” → „CO₂ 20 MW¹⁾” (DU/2025/1685), „Ener- 2025 getyki” → „Energetyki” (DU/2025/610).
W jednym spłaszczonym wzorze cyfra trafia w złe miejsce: „0,0036∙(1−t )∙∑ … CO 2” → „0,0036∙(1−tCO )∙∑ … EJ =²”
(DU/2025/610; wzory i tak trzeba czytać z PDF). Liczba jednostek (art., ust., pkt, §) jest ta sama we wszystkich 479.
W pozostałych 438 zmienia się tylko pole `converter`.

Zmiana 2026-10-11 (eli2md 0.6.53, 369 ustaw, czyli wszystkie akty typu Ustawa w `index.csv`): przeliczone z tych
samych PDF; wcześniej tekst z eli2md 0.6.25 i 0.6.25.2. Tekst zmienia się w 13 z nich. W 11 zostają te same znaki,
a zmieniają się tylko odstępy, głównie przy indeksach dolnych: „WYD n‒1” → „WYDn‒1” (DU/2025/39), „(NO x )” → „(NOx)”
(DU/2026/1157). W 2 indeksy z cyfr są teraz zapisane jako ₀₁₂… na wierszu swojego symbolu, a przeniesienie
rozdzielone indeksem jest scalone: „PZM AU” → „PZMAU”, „zakon- AG traktowane” → „zakontraktowane” (DU/2025/159),
„E =e ec +e₁ +e p” → „E =eec +e₁ +ep”, „gosposca darce” → „gospodarce” (DU/2025/303). Liczba jednostek (art., ust.,
pkt, §) jest ta sama we wszystkich 369, żaden akt nie zgubił tekstu. W pozostałych 356 zmienia się tylko pole
`converter`. Od tej zmiany codzienna aktualizacja używa eli2md 0.6.53 (wcześniej 0.6.52).

Zmiana 2026-10-11 (eli2md 0.6.52): dodane 3 862 teksty jednolite ustaw z lat 2012–2024, które API ELI ma też w HTML
(opis w sekcji „Teksty jednolite ustaw z lat 2012–2024”). Pozostałe akty bez zmian.

Zmiana 2026-10-10 (drzewo JSON, kod drzewa eli2md 0.6.50, 85 aktów; opis w README eli2md, wpis 0.6.50): nagłówki z
liczebnikiem słownym („DZIAŁ PIĄTY”, „CZĘŚĆ PIERWSZA”), z numerem rzymskim z wielką literą („DZIAŁ IVA”) albo z
odnośnikiem po numerze („Rozdział 5a[^28]”) są w `.json` węzłami `heading`. Wcześniej trafiały jako tekst do artykułu,
paragrafu albo punktu przed nimi. Nowych nagłówków: 261, żaden nie zniknął. `.md` się nie zmienił, więc pole
`converter` (w `.md`, `.json` i `index.csv`) zostaje wersją, w której powstał `.md`. Liczba jednostek bez zmian, słowa
w drzewach: zgubione 0. Pozostałe akty bez zmian (porównanie drzew wszystkich aktów zbioru). Wątpliwe: w tabeli
załącznika DU/2026/956 „Część I” i „Część II” są teraz nagłówkami, choć to wiersze tabeli (tekst ten sam, zmienia się
tylko typ węzła).

Od 2026-10-10 codzienna aktualizacja używa eli2md 0.6.50 (wcześniej 0.6.25.2). Sprawdzenie przed zmianą: 100
najnowszych aktów DU przeliczonych wersją 0.6.50 z tych samych PDF ma ten sam `.md` i `.json` co w zbiorze (poza
polem `converter`).

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
