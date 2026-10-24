"""Articles of the 12 consolidated texts from eli2md eval/tj_articles.py, measured on the .md files of THIS repo
(not on a fresh conversion): words of each top-level article vs the official ELI HTML.

    ELI2MD=/path/to/eli2md python .github/tj_articles_published.py [--out FILE]

Needs a checkout of https://github.com/PolskiAgentW/eli2md (eval/tj_articles.py downloads text.pdf and text.html
of the 12 acts from the ELI API into ~/cache/eli; the PDF is not converted here).
"""
import os
import pathlib
import sys

ELI2MD = pathlib.Path(os.environ["ELI2MD"])
sys.path[:0] = [str(ELI2MD / "eval"), str(ELI2MD)]
import tj_articles as t  # noqa: E402

DATA = pathlib.Path(__file__).resolve().parents[1] / "DU"
t.__version__ = "dziennik-ustaw-md-files"
t.convert = lambda pdf: pdf
t.to_markdown = lambda pdf: (lambda d: (DATA / d.parent.name / f"DU-{d.parent.name}-{d.name}.md").read_text(
    encoding="utf-8"))(pathlib.Path(pdf).parent)
t.main()
