---
language:
- pl
license: cc0-1.0
pretty_name: Dziennik Ustaw od 2025 r. w Markdown/JSON
size_categories:
- 1K<n<10K
tags:
- legal
- law
- poland
configs:
- config_name: default
  data_files:
  - split: train
    path: data/*.parquet
---

# Dziennik Ustaw od 2025 r. — teksty aktów w Markdown/JSON

Nieoficjalne teksty wszystkich aktów z Dziennika Ustaw ogłoszonych od 2025 r. (oraz 98 aktów z lat 2020–2023,
które w API nie mają HTML), przekonwertowane z urzędowych PDF-ów otwartym konwerterem
[eli2md](https://github.com/PolskiAgentW/eli2md). Odświeżane codziennie.

*Unofficial plain-text (Markdown) and structured (JSON tree of articles/paragraphs/points) versions of all acts
published in the Polish Journal of Laws (Dziennik Ustaw) since 2025. The Sejm ELI API serves these acts only as PDF.
Converted automatically; the PDF is the binding text. Updated daily.*

**Dlaczego:** API ELI Sejmu udostępnia teksty aktów z Dziennika Ustaw od 2025 r. tylko jako PDF (HTML jest dla
lat 2012–2024). Szczegóły i sprawdzenie: [repozytorium na GitHubie](https://github.com/PolskiAgentW/dziennik-ustaw-md).

**Teksty jednolite** (obwieszczenia o ogłoszeniu jednolitego tekstu) od 2025 r. też są tylko w PDF, np. najnowsze
teksty jednolite Kodeksu cywilnego (DU/2026/795), Kodeksu pracy (DU/2026/1245) i Kodeksu postępowania cywilnego
(DU/2026/468). Najnowszy tekst jednolity każdego aktu:
[TEKSTY_JEDNOLITE.md](https://github.com/PolskiAgentW/dziennik-ustaw-md/blob/main/TEKSTY_JEDNOLITE.md).
Na 12 tekstach jednolitych, które mają też HTML, 5903 z 5929 artykułów ma te same słowa co HTML
([pomiar](https://github.com/PolskiAgentW/eli2md/blob/main/eval/tj_articles_0.6.17.md)).

<!-- zbiory:start -->
**Wszystkie zbiory** (ten sam format plików, konwerter [eli2md](https://github.com/PolskiAgentW/eli2md)). Akty, które API ELI
podaje w HTML (np. większość Dziennika Ustaw 2012–2024), nie są tu powielane.

| lata | Dziennik Ustaw | Monitor Polski |
|---|---|---|
| od 2012 | [GitHub](https://github.com/PolskiAgentW/dziennik-ustaw-md) · [HF](https://huggingface.co/datasets/PolskiAgentW/dziennik-ustaw-md): od 2025 r. wszystkie, wcześniej 98 aktów bez HTML; codziennie | [GitHub](https://github.com/PolskiAgentW/monitor-polski-md) · [HF](https://huggingface.co/datasets/PolskiAgentW/monitor-polski-md): wszystkie z PDF (API nie ma HTML); codziennie |
| 2000–2011 | [GitHub](https://github.com/PolskiAgentW/dziennik-ustaw-2000-2011-md) · [HF](https://huggingface.co/datasets/PolskiAgentW/dziennik-ustaw-2000-2011-md): akty bez HTML w API | [GitHub](https://github.com/PolskiAgentW/monitor-polski-2000-2011-md) · [HF](https://huggingface.co/datasets/PolskiAgentW/monitor-polski-2000-2011-md): wszystkie z PDF |
| 1990–1999 | [GitHub](https://github.com/PolskiAgentW/dziennik-ustaw-1990-1999-md) · [HF](https://huggingface.co/datasets/PolskiAgentW/dziennik-ustaw-1990-1999-md): akty bez HTML w API (OCR skanów) | brak |

Kolumny są we wszystkich zbiorach te same, więc lata można wczytać razem (nadal bez aktów, które API ELI podaje w HTML):

```python
from datasets import load_dataset

du = load_dataset("parquet", split="train", data_files=[
    "hf://datasets/PolskiAgentW/dziennik-ustaw-1990-1999-md/data/*.parquet",
    "hf://datasets/PolskiAgentW/dziennik-ustaw-2000-2011-md/data/*.parquet",
    "hf://datasets/PolskiAgentW/dziennik-ustaw-md/data/*.parquet",
])  # 30 018 aktów (2026-10-05); Monitor Polski: monitor-polski-2000-2011-md + monitor-polski-md
```
<!-- zbiory:end -->

## Użycie

```python
from datasets import load_dataset
import json

ds = load_dataset("PolskiAgentW/dziennik-ustaw-md", split="train")
act = ds.filter(lambda r: r["eli"] == "DU/2025/900")[0]
print(act["markdown"][:500])
tree = json.loads(act["tree"])  # drzewo jednostek: art., §, ust., pkt, lit.
```

## Kolumny

Jeden wiersz = jeden akt.
- `eli` (np. `DU/2025/900`), `year`, `pos`, `type`, `title`, `display_address`, `announcement_date`, `promulgation`,
  `entry_into_force`, `legal_status`, `keywords`, `change_date`, `source_pdf`, `pdf_sha256`: metadane z API ELI
  (bez poprawek, więc z jego błędami; `legal_status` — stan w chwili konwersji);
- `pages`, `words`, `no_text_pages`, `image_pages`, `ocr_pages`, `image_ocr_pages`: strony PDF, słowa wyniku,
  strony bez warstwy tekstowej (skany), strony z dużymi obrazami (ich treści brak), strony odczytane przez OCR,
  strony, na których OCR odczytał obraz tekstu (s. 1 umów międzynarodowych, od eli2md 0.6.4);
- `markdown`: tekst aktu (`##### Art. N.`, akapity, `## Załącznik …`, przypisy `[^n]`; tekst z OCR jako cytaty `> …`
  z notką przed stroną);
- `tree`: ten sam akt jako drzewo jednostek w JSON (tekst; opis formatu w
  [README eli2md](https://github.com/PolskiAgentW/eli2md#json-drzewo-jednostek-od-053));
- `converter`, `converted_at`: wersja eli2md i czas konwersji.

## Jakość

Zmierzona na aktach z 2024 r., które mają i PDF, i oficjalny HTML: na odłożonej próbie 46 aktów słowa treści
głównej — recall 0.998, precision 0.984; drzewo jednostek w treści głównej — 1256 z 1256 jednostek na właściwym
miejscu. Losowa kontrola wzrokowa danych 2025–2026 (35 stron): 28 stron bez błędu, 6 z błędem konwertera
(kolejność tekstu, tabele, przypisy), słowa nie giną. Tabele są spłaszczone do akapitów. Szczegóły, znane błędy
i historia zmian: [README na GitHubie](https://github.com/PolskiAgentW/dziennik-ustaw-md#jak-powstaje-i-jak-dobre-jest).

**To nie jest urzędowy tekst.** Wiążący jest PDF w Dzienniku Ustaw (`source_pdf`). Błędy konwersji zgłaszaj
w [Issues na GitHubie](https://github.com/PolskiAgentW/dziennik-ustaw-md/issues).

## Źródło i licencja

Źródło: [API ELI Sejmu](https://api.sejm.gov.pl/eli/acts/DU). Ten sam zbiór jako pliki `.md`/`.json`:
[github.com/PolskiAgentW/dziennik-ustaw-md](https://github.com/PolskiAgentW/dziennik-ustaw-md).
Akty normatywne nie są przedmiotem prawa autorskiego (art. 4 pkt 1 ustawy o prawie autorskim i prawach
pokrewnych); pozostała zawartość: CC0 1.0.
