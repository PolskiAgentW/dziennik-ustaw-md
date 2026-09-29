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
(2020 – 10, 2021 – 42, 2023 – 46; sprawdzone 2026-09-29), a przed 2012 r. HTML-a nie ma dla żadnego aktu
(tych, 55 tys. skanów z warstwą OCR, tu nie ma). Tutaj jest tekst aktów bez HTML od 2012 r. w formie, którą da
się przeszukiwać, porównywać i przetwarzać.

## Stan

<!-- stats:start -->
Stan na 2026-09-29 21:07 UTC (liczone z `index.csv`, aktualizowane automatycznie).

| rok | aktów w indeksie | przekonwertowanych | błędów |
|---|---:|---:|---:|
| 2020 | 10 | 10 | 0 |
| 2021 | 42 | 42 | 0 |
| 2023 | 46 | 46 | 0 |
| 2025 | 1900 | 1900 | 0 |
| 2026 | 1268 | 1268 | 0 |

Akty ze stronami bez warstwy tekstowej (skany, grafiki): 81, razem 1837 z 55640 stron. Tekst z OCR (oznaczony) ma 1736 z nich w 70 aktach; treści pozostałych brak.
Akty ze stronami z dużymi obrazami (wzory, rysunki; ich treści brak): 197.

Rodzaje aktów: Rozporządzenie 1814, Obwieszczenie 1004, Ustawa 362, Oświadczenie rządowe 42, Umowa międzynarodowa 35, Komunikat 4, Postanowienie 3, Uchwała 2.
Wersje konwertera: eli2md 0.6.2 (3266).
<!-- stats:end -->

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
  ocr_pages, status, error, converter, converted_at`. `ocr_pages` jest puste, jeśli akt konwertowano bez OCR
  (akty bez skanów przed 0.6.0).
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
w `index.csv` kolumna `image_pages`.

Metadane pochodzą z API ELI bez poprawek, więc zawierają też jego błędy. Przykład: 5 aktów ma
`announcement_date` w przyszłości (DU/2026/626 i DU/2026/740: rok 2206; stan na 2026-09-29).

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

**Znane błędy** (poprawki w toku):
- część PDF-ów z 2026 r. drukuje indeksy górne w nawiasach („Art. 479[30f].”). Konwerter przenosi je na początek
  akapitu („[30f] [30] [30a] [30e] Art. 479 . …”), a takie artykuły nie są nagłówkami ani jednostkami w JSON.
  Dotyczy m.in. tekstów jednolitych k.p.c. (DU/2026/468), k.c. (DU/2026/795) i k.p. (DU/2026/1245): łącznie
  do 1393 akapitów w 17 plikach (górna granica, część to cytaty w nowelizacjach);
- w tabelach z komórkami wieloliniowymi linie sąsiednich kolumn bywają przeplecione (DU/2025/205, lp. 9);
- przypis z wyliczeniem: do przypisu trafia tylko pierwszy akapit, dalsze punkty są w treści (DU/2026/421).

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
z API ELI. Konwertuje nowe akty oraz te, którym zmienił się `changeDate`, i commituje wynik.
Jeśli przez ponad 10 dni nie przybędzie żaden nowy akt, workflow kończy się błędem, żeby cicha awaria
była widoczna. Najdłuższa przerwa w ogłaszaniu aktów w latach 2025–2026 wyniosła 6 dni.

## Licencja

Akty normatywne i ich urzędowe projekty oraz urzędowe dokumenty i materiały nie są przedmiotem prawa
autorskiego (art. 4 pkt 1 i 2 ustawy o prawie autorskim i prawach pokrewnych). Pozostała zawartość
(indeks, skrypty): CC0 1.0.

Błędy konwersji zgłaszaj w Issues. Najlepiej podaj pozycję aktu i fragment.
