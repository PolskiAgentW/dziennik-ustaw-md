# Dziennik Ustaw w Markdown (od 2025 r.)

Teksty aktów z **Dziennika Ustaw** od 2025 r. w Markdown i jako drzewo jednostek w JSON, z metadanymi
z API ELI Sejmu. Aktualizowane codziennie przez GitHub Actions.
*Texts of Polish Journal of Laws acts (2025+) as Markdown and as a JSON tree of units (art./§/ust./pkt/lit.),
converted from the official PDFs; updated daily.*

> **Nieoficjalne.** Teksty powstają przez automatyczną konwersję PDF-ów, więc mogą zawierać błędy.
> Wiążący jest PDF w Dzienniku Ustaw (link `source_pdf` w każdym pliku).

## Dlaczego

API ELI Sejmu (`api.sejm.gov.pl/eli`) podaje teksty aktów z Dziennika Ustaw od 2025 r. tylko
jako PDF. Dla 2024 r. był też HTML (sprawdzone 2026-09-29: 2024 – 1984/1984 aktów z HTML,
2025 – 0/1900, 2026 – 0/1255). Tutaj jest tekst tych aktów w formie, którą da się przeszukiwać,
porównywać i przetwarzać.

## Stan

<!-- stats:start -->
Stan na 2026-09-29 15:43 UTC (liczone z `index.csv`, aktualizowane automatycznie).

| rok | aktów w indeksie | przekonwertowanych | błędów |
|---|---:|---:|---:|
| 2025 | 1900 | 1900 | 0 |
| 2026 | 1268 | 1268 | 0 |

Akty ze stronami bez warstwy tekstowej (skany, grafiki): 62, razem 1734 z 53356 stron. Tekst z OCR (oznaczony) ma 1640 z nich w 52 aktach; treści pozostałych brak.
Akty ze stronami z dużymi obrazami (wzory, rysunki; ich treści brak): 195.

Rodzaje aktów: Rozporządzenie 1735, Obwieszczenie 989, Ustawa 360, Oświadczenie rządowe 41, Umowa międzynarodowa 34, Komunikat 4, Postanowienie 3, Uchwała 2.
Wersje konwertera: eli2md 0.5.3 (3106), eli2md 0.6.0 (62).
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
które mają i PDF, i oficjalny HTML. Na odłożonej próbie 46 aktów (wersja 0.5.3, której używa ten zbiór,
ocena jednorazowa):
- słowa treści głównej: recall 0.998, precision 0.984;
- drzewo jednostek (art., §, ust., pkt, lit.): w treści głównej 1256 z 1256 jednostek z właściwą ścieżką
  we właściwym miejscu i żadnej fałszywej; w załącznikach recall 0.998, precision 0.994;
- nagłówki artykułów/paragrafów w treści głównej: 145 ze 148, bez fałszywych (3 brakujące to jeden akt,
  poprawiony po teście, więc ta liczba nie jest niezależna).

Przypisy i tabele wypadają słabiej (tabele są spłaszczone do akapitów, wiersz po wierszu). Szczegóły,
słabe miejsca i poprzednie wyniki są w README eli2md.

Zmiana 2026-09-29 wieczorem (eli2md 0.5.2 → 0.5.3, wszystkie akty przekonwertowane od nowa, dodany JSON).
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

Akty normatywne i ich urzędowe projekty nie są przedmiotem prawa autorskiego (art. 4 pkt 2 ustawy
o prawie autorskim i prawach pokrewnych). Pozostała zawartość (indeks, skrypty): CC0 1.0.

Błędy konwersji zgłaszaj w Issues. Najlepiej podaj pozycję aktu i fragment.
