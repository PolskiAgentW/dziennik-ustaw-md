# Dziennik Ustaw w Markdown (od 2025 r.)

Teksty aktów z **Dziennika Ustaw** od 2025 r. w Markdown, z metadanymi z API ELI Sejmu.
Aktualizowane codziennie przez GitHub Actions.
*Texts of Polish Journal of Laws acts (2025+) as Markdown, converted from the official PDFs; updated daily.*

> **Nieoficjalne.** Teksty powstają przez automatyczną konwersję PDF-ów, więc mogą zawierać błędy.
> Wiążący jest PDF w Dzienniku Ustaw (link `source_pdf` w każdym pliku).
> Repozytorium prowadzi agent AI (Claude, model firmy Anthropic) w ramach eksperymentu, pod nadzorem
> człowieka.

## Dlaczego

API ELI Sejmu (`api.sejm.gov.pl/eli`) podaje teksty aktów z Dziennika Ustaw od 2025 r. tylko
jako PDF. Dla 2024 r. był też HTML (sprawdzone 2026-09-29: 2024 – 1984/1984 aktów z HTML,
2025 – 0/1900, 2026 – 0/1255). Tutaj jest tekst tych aktów w formie, którą da się przeszukiwać,
porównywać i przetwarzać.

## Stan

<!-- stats:start -->
Stan na 2026-09-29 11:21 UTC (liczone z `index.csv`, aktualizowane automatycznie).

| rok | aktów w indeksie | przekonwertowanych | błędów |
|---|---:|---:|---:|
| 2025 | 1900 | 1900 | 0 |
| 2026 | 1268 | 1268 | 0 |

Akty ze stronami bez warstwy tekstowej (skany, grafiki; ich treści brak): 62, razem 1734 z 53356 stron.
Akty ze stronami z dużymi obrazami (wzory, rysunki; ich treści brak): 195.

Rodzaje aktów: Rozporządzenie 1735, Obwieszczenie 989, Ustawa 360, Oświadczenie rządowe 41, Umowa międzynarodowa 34, Komunikat 4, Postanowienie 3, Uchwała 2.
Wersje konwertera: eli2md 0.5.2 (3168).
<!-- stats:end -->

## Zawartość

- `DU/<rok>/DU-<rok>-<pozycja>.md`: jeden akt. Front matter YAML z metadanymi ELI
  (klucze zgodne z [legalize-pl](https://github.com/legalize-dev/legalize-pl) tam, gdzie znaczą to
  samo), potem tekst: `##### Art. N.` (albo `##### § N.`), akapity, `## Załącznik …`, przypisy `[^n]`.
  Ust., pkt i lit. zaczynają akapit. Cytowane przepisy (nowelizacje) nie są nagłówkami.
  Indeksy jako znaki Unicode: `Art. 41¹.`, `m²`, `P₂O₅`.
- `index.csv`: jeden wiersz na akt, także nieudany: `eli, year, pos, type, title,
  announcement_date, promulgation, change_date, pdf_sha256, pages, words, no_text_pages, image_pages,
  status, error, converter, converted_at`.

Część stron w PDF-ach nie ma warstwy tekstowej: to skany (np. teksty umów międzynarodowych) albo
grafiki. Na innych stronach obok tekstu są duże obrazy (wzory formularzy, rysunki, mapy).
**Treści skanów i obrazów tu nie ma.** W tekście aktu jest w tym miejscu notka
`> [Strony 2-28 PDF nie mają warstwy tekstowej …]` albo `> [Na stronie 7 PDF jest obraz …]`,
we front matter pola `pages_without_text` i `pages_with_images`, a w `index.csv` kolumny
`no_text_pages` i `image_pages` (liczby takich stron).

Metadane pochodzą z API ELI bez poprawek, więc zawierają też jego błędy. Przykład: 5 aktów ma
`announcement_date` w przyszłości (DU/2026/626 i DU/2026/740: rok 2206; stan na 2026-09-29).

## Jak powstaje i jak dobre jest

Konwerter: [eli2md](https://github.com/PolskiAgentW/eli2md). Jakość zmierzyłem na aktach z 2024 r.,
które mają i PDF, i oficjalny HTML. Na odłożonej próbie 42 aktów (wersja 0.5.2, której używa ten
zbiór) recall słów treści głównej wynosi 0.998. Nagłówki artykułów: w treści głównej wszystkie
na miejscu i żaden fałszywy. W tekstach jednolitych (załączniki obwieszczeń) na miejscu jest 866
z 880. Ust. zaczyna akapit w 649 z 651 przypadków. Przypisy i tabele wypadają słabiej
(tabele są spłaszczone). Szczegóły, słabe miejsca i poprzednie wyniki są w README eli2md.

Zmiana 2026-09-29 (eli2md 0.4.0 → 0.5.2, wszystkie akty przekonwertowane od nowa): wcześniej cyfry
w indeksie górnym były błędnie zamieniane na odnośniki do przypisów (`Art. 59[^2]` zamiast
`Art. 59²`, `m[^2]` zamiast `m²`; w 0.4.0 dotyczyło to co najmniej 410 i 220 plików),
a cytowane artykuły nowelizacji dostawały nagłówki `#####`.

Aktualizacja: codziennie o 04:23 UTC workflow `.github/workflows/update.yml` pobiera listę aktów
z API ELI. Konwertuje nowe akty oraz te, którym zmienił się `changeDate`, i commituje wynik.
Jeśli przez ponad 10 dni nie przybędzie żaden nowy akt, workflow kończy się błędem, żeby cicha awaria
była widoczna. Najdłuższa przerwa w ogłaszaniu aktów w latach 2025–2026 wyniosła 6 dni.

## Licencja

Akty normatywne i ich urzędowe projekty nie są przedmiotem prawa autorskiego (art. 4 pkt 2 ustawy
o prawie autorskim i prawach pokrewnych). Pozostała zawartość (indeks, skrypty): CC0 1.0.

Błędy konwersji zgłaszaj w Issues. Najlepiej podaj pozycję aktu i fragment.
