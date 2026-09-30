"""Rewrite the stats section of README.md from index.csv."""
import csv
import re
import datetime as dt
from collections import Counter, defaultdict
from pathlib import Path

rows = list(csv.DictReader(open("index.csv", encoding="utf-8")))
ok = [r for r in rows if r["status"] == "ok"]
years = sorted({r["year"] for r in rows})
lines = [f"Stan na {dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M} UTC "
         f"(liczone z `index.csv`, aktualizowane automatycznie).", "",
         "| rok | aktów w indeksie | przekonwertowanych | błędów |", "|---|---:|---:|---:|"]
for y in years:
    ry = [r for r in rows if r["year"] == y]
    lines.append(f"| {y} | {len(ry)} | {sum(r['status'] == 'ok' for r in ry)} | "
                 f"{sum(r['status'] != 'ok' for r in ry)} |")
nt = [r for r in ok if int(r.get("no_text_pages") or 0) > 0]
ocr = [r for r in ok if int(r.get("ocr_pages") or 0) > 0]
lines += ["", f"Akty ze stronami bez warstwy tekstowej (skany, grafiki): {len(nt)}, "
              f"razem {sum(int(r['no_text_pages']) for r in nt)} z {sum(int(r['pages'] or 0) for r in ok)} stron. "
              f"Tekst z OCR (oznaczony) ma {sum(int(r['ocr_pages']) for r in ocr)} z nich w {len(ocr)} aktach; "
              f"treści pozostałych brak.",
          f"Akty ze stronami z dużymi obrazami (wzory, rysunki; ich treści brak): "
          f"{sum(int(r.get('image_pages') or 0) > 0 for r in ok)}."]
types = Counter(r["type"] for r in ok)
lines += ["", "Rodzaje aktów: " + ", ".join(f"{t} {n}" for t, n in types.most_common()) + "."]
conv = Counter(r["converter"] for r in ok)
lines += ["Wersje konwertera: " + ", ".join(f"{c} ({n})" for c, n in conv.most_common()) + "."]
readme = Path("README.md").read_text(encoding="utf-8")
a, b = "<!-- stats:start -->", "<!-- stats:end -->"
i, j = readme.index(a) + len(a), readme.index(b)
Path("README.md").write_text(readme[:i] + "\n" + "\n".join(lines) + "\n" + readme[j:], encoding="utf-8")

# Consolidated texts (obwieszczenia "w sprawie ogłoszenia jednolitego tekstu ..."), newest per act, 2025+ only:
# older ones mostly have HTML in the API and are not here, so "newest here" would not be the newest one.
tj = defaultdict(list)
for r in ok:
    m = re.search(r"jednolitego tekstu (.+?)\.?$", r["title"])
    if m and int(r["year"]) >= 2025:
        tj[re.sub(r"\s+[-–—]\s+", " – ", m.group(1).strip())].append(r)
for v in tj.values():
    v.sort(key=lambda r: (r["promulgation"], int(r["year"]), int(r["pos"])), reverse=True)


def link(r: dict, rel: str = "") -> str:
    return f"[Dz.U. {r['year']} poz. {r['pos']}]({rel}DU/{r['year']}/DU-{r['year']}-{r['pos']}.md)"


codes = sorted(n for n in tj if re.match(r"ustawy – (Kodeks|Ordynacja podatkowa)", n))
tab = ["| Akt | Najnowszy tekst jednolity | Ogłoszony | Wcześniejsze od 2025 r. |", "|---|---|---|---|"]
for n in codes:
    v = tj[n]
    tab.append(f"| {n[len('ustawy – '):]} | {link(v[0])} | {v[0]['promulgation']} | "
               f"{', '.join(link(r) for r in v[1:]) or '–'} |")
tab += ["", f"Wszystkie akty z tekstem jednolitym ogłoszonym od 2025 r. ({len(tj)}): "
            f"[TEKSTY_JEDNOLITE.md](TEKSTY_JEDNOLITE.md)."]
readme = Path("README.md").read_text(encoding="utf-8")
a, b = "<!-- tj:start -->", "<!-- tj:end -->"
if a in readme:
    i, j = readme.index(a) + len(a), readme.index(b)
    Path("README.md").write_text(readme[:i] + "\n" + "\n".join(tab) + "\n" + readme[j:], encoding="utf-8")
full = ["# Teksty jednolite ogłoszone od 2025 r.", "",
        "Najnowszy tekst jednolity każdego aktu w tym zbiorze (z pliku `index.csv`, odświeżane automatycznie). "
        "Nazwa aktu pochodzi z tytułu obwieszczenia. Tekst jednolity podaje stan prawny na dzień wskazany "
        "w obwieszczeniu; zmian ogłoszonych później w nim nie ma. Teksty nieoficjalne, wiążący jest PDF.", ""]
for kind, head in (("ustawy", "Ustawy"), ("rozporządzenia", "Rozporządzenia")):
    names = sorted((n for n in tj if n.startswith(kind + " ")), key=lambda n: n.lower())
    full += [f"## {head} ({len(names)})", "", "| Akt | Najnowszy | Ogłoszony | Wcześniejsze od 2025 r. |", "|---|---|---|---|"]
    for n in names:
        v = tj[n]
        full.append(f"| {n[len(kind) + 1:].replace('|', '/')} | {link(v[0])} | {v[0]['promulgation']} | "
                    f"{', '.join(link(r) for r in v[1:]) or '–'} |")
    full.append("")
Path("TEKSTY_JEDNOLITE.md").write_text("\n".join(full), encoding="utf-8")
